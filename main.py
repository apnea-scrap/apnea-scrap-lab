from pathlib import Path
import os
import re
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
import yaml


def define_env(env):
    docs_dir = Path(env.project_dir) / "docs"

    def read_meta(path: Path) -> dict:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if match:
            return yaml.safe_load(match.group(1)) or {}
        return {}

    @env.macro
    def yt(id, title="", ratio="56.25%"):
        title = title or "YouTube video"
        return f'''<div style="position:relative;padding-top:{ratio};">
  <iframe src="https://www.youtube-nocookie.com/embed/{id}" title="{title}" loading="lazy" allowfullscreen
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"></iframe>
</div>'''

    def _format_decimal(value, places=3) -> str:
        quantised = Decimal(str(value)).quantize(Decimal(f"1.{'0' * places}"), rounding=ROUND_HALF_UP)
        text = format(quantised.normalize(), "f")
        if "." in text:
            text = text.rstrip("0").rstrip(".")
        return text

    def _format_currency(amount: Decimal, currency: str) -> str:
        currency = (currency or "").upper()
        symbols = {
            "GBP": "£",
            "USD": "$",
            "EUR": "€",
        }
        quantised = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        symbol = symbols.get(currency)
        if symbol:
            return f"{symbol}{quantised}"
        if currency:
            return f"{currency} {quantised}"
        return str(quantised)

    def _format_quantity_display(quantity, unit):
        quantity_decimal: Decimal | None = None
        if quantity is not None:
            try:
                quantity_decimal = Decimal(str(quantity))
                quantity_text = _format_decimal(quantity_decimal)
            except Exception:
                quantity_decimal = None
                quantity_text = str(quantity)
            if unit:
                quantity_text = f"{quantity_text} {unit}"
        else:
            quantity_text = unit or ""
        return quantity_text, quantity_decimal

    def _bill_of_material_items(meta_source: Path) -> list[dict]:
        meta = read_meta(meta_source)
        items = meta.get("bill_of_materials", []) or []
        results: list[dict] = []

        for item in items:
            material_path = item.get("material")
            name = item.get("name")

            if not material_path and not name:
                raise ValueError(
                    f"Bill of materials item in {meta_source} must define either 'material' or 'name'."
                )

            description = item.get("description")
            notes = item.get("notes")
            quantity_field = item.get("quantity")
            explicit_unit = item.get("unit")
            quantity_amount = None
            quantity_display_override = None

            if isinstance(quantity_field, dict):
                quantity_amount = quantity_field.get("amount")
                quantity_display_override = quantity_field.get("display")
                explicit_unit = quantity_field.get("unit", explicit_unit)
            else:
                quantity_amount = quantity_field

            material_meta: dict | None = None
            material_page_rel: Path | None = None
            title = name

            if material_path:
                material_page = Path(material_path)
                if material_page.is_absolute():
                    material_page = material_page.relative_to(docs_dir)
                if material_page.suffix != ".md":
                    material_page = material_page.with_suffix(".md")
                material_page_rel = material_page
                material_meta = read_meta(docs_dir / material_page)
                title = title or material_meta.get("title")

            if not title and material_page_rel is not None:
                title = material_page_rel.stem.replace("-", " ").title()
            title = title or ""

            unit_cost_field = item.get("unit_cost")
            unit_cost_label: str | None = None
            if isinstance(unit_cost_field, dict):
                unit_cost = unit_cost_field.copy()
            elif isinstance(unit_cost_field, str):
                unit_cost = {}
                unit_cost_label = unit_cost_field.strip() or None
            else:
                unit_cost = {}

            unit_cost_amount = unit_cost.get("amount")
            unit_cost_currency = unit_cost.get("currency")
            unit_cost_per = unit_cost.get("per")
            if unit_cost_label is None:
                label_value = unit_cost.get("label")
                if isinstance(label_value, str):
                    unit_cost_label = label_value.strip() or None

            direct_region = item.get("region")
            direct_supplier = item.get("supplier")
            direct_date = item.get("date")

            purchase_hint_raw = item.get("purchase")

            if material_path and (
                purchase_hint_raw
                or direct_region is not None
                or direct_supplier is not None
                or direct_date is not None
            ):
                raise ValueError(
                    "Bill of materials entries that reference a material must not define purchase hints; "
                    "set quantity.unit to match the desired purchase instead."
                )

            purchase_hint = purchase_hint_raw or {}

            region_hint = purchase_hint.get("region") or direct_region
            supplier_hint = purchase_hint.get("supplier") or direct_supplier
            date_hint = purchase_hint.get("date") or direct_date
            unit_hint = purchase_hint.get("unit")

            if material_path and explicit_unit:
                unit_hint = explicit_unit

            material_info = material_meta or {}
            material_purchases = material_info.get("material", {}).get("purchases", [])
            selected_purchase = _select_material_purchase(
                material_purchases,
                region=region_hint,
                supplier=supplier_hint,
                date=date_hint,
                unit=unit_hint,
            )

            purchase_unit: str | None = None
            if selected_purchase:
                purchase_price = selected_purchase.get("price") or {}
                if unit_cost_amount is None and purchase_price.get("amount") is not None:
                    unit_cost_amount = purchase_price.get("amount")
                if not unit_cost_currency and purchase_price.get("currency"):
                    unit_cost_currency = purchase_price.get("currency")
                purchase_unit = selected_purchase.get("unit")
                if not unit_cost_per and purchase_unit:
                    per_value = str(purchase_unit)
                    unit_cost_per = per_value[4:] if per_value.lower().startswith("per ") else per_value

            if not purchase_unit:
                for candidate in material_purchases:
                    candidate_unit = candidate.get("unit")
                    if candidate_unit:
                        purchase_unit = candidate_unit
                        break

            resolved_unit = explicit_unit or purchase_unit
            quantity_display, quantity_decimal = _format_quantity_display(quantity_amount, resolved_unit)
            if quantity_display_override:
                quantity_display = str(quantity_display_override)

            unit_cost_decimal: Decimal | None = None
            if unit_cost_amount is not None:
                try:
                    unit_cost_decimal = Decimal(str(unit_cost_amount))
                except Exception:
                    unit_cost_decimal = None

            line_total_decimal: Decimal | None = None
            if unit_cost_decimal is not None and unit_cost_currency and quantity_decimal is not None:
                line_total_decimal = quantity_decimal * unit_cost_decimal

            results.append(
                {
                    "material_page": material_page_rel,
                    "title": title,
                    "description": description,
                    "notes": notes,
                    "quantity_display": quantity_display,
                    "quantity_decimal": quantity_decimal,
                    "unit": resolved_unit,
                    "unit_cost_currency": unit_cost_currency,
                    "unit_cost_decimal": unit_cost_decimal,
                    "unit_cost_amount": unit_cost_amount,
                    "unit_cost_per": unit_cost_per,
                    "unit_cost_label": unit_cost_label,
                    "line_total_decimal": line_total_decimal,
                }
            )

        return results

    def _bill_of_material_totals(items: list[dict]) -> list[tuple[str, Decimal]]:
        totals: dict[str, Decimal] = {}
        for item in items:
            currency = item.get("unit_cost_currency")
            line_total = item.get("line_total_decimal")
            if not currency or line_total is None:
                continue
            currency_code = str(currency).upper()
            totals.setdefault(currency_code, Decimal("0"))
            totals[currency_code] += line_total
        return sorted(totals.items(), key=lambda entry: entry[0])

    @env.macro
    def versions_table(path: str | None = None) -> str:
        rel_dir = Path(path) if path else Path(env.page.file.src_path).parent
        base = docs_dir / rel_dir

        def build_nav_lookup():
            nav_lookup: dict[str, str] = {}

            def visit(items):
                for item in items:
                    if isinstance(item, dict):
                        for title, value in item.items():
                            if isinstance(value, str):
                                key = str(Path(value)).replace("\\", "/")
                                nav_lookup[key] = title
                            elif isinstance(value, list):
                                visit(value)
                            else:
                                visit([value])
                    elif isinstance(item, list):
                        visit(item)

            visit(env.conf.get("nav", []))
            return nav_lookup

        nav_titles = build_nav_lookup()
        rows = []
        for file in sorted(base.glob("**/*.md")):
            if file.name == "index.md":
                continue
            meta = read_meta(file)
            rel_path = file.relative_to(base)
            full_rel_path = rel_dir / rel_path
            nav_key = full_rel_path.as_posix()
            link_text = nav_titles.get(nav_key, " ".join(rel_path.with_suffix("").parts).replace("-", " "))
            link = f"[{link_text}]({rel_path.as_posix()})"
            bom_items = _bill_of_material_items(file)
            bom_totals = _bill_of_material_totals(bom_items)
            if bom_totals:
                cost = [
                    {"amount": total_amount, "currency": currency}
                    for currency, total_amount in bom_totals
                ]
            else:
                cost = meta.get("estimated_cost")
            impl = meta.get("time_to_implement")
            wait = meta.get("waiting_time")
            status = meta.get("status", "")
            if status:
                status_class = status.lower().replace(" ", "-")
                status_text = status.title()
                status_html = f'<span class="status-badge status-{status_class}">{status_text}</span>'
            else:
                status_html = ""

            def format_cost(value):
                if value is None:
                    return ""
                if isinstance(value, list):
                    formatted = [format_cost(item) for item in value]
                    return "; ".join(filter(None, formatted))
                if isinstance(value, dict):
                    amount = value.get("amount")
                    currency = value.get("currency")
                    region = value.get("region")
                    note = value.get("note")

                    parts: list[str] = []
                    if currency and amount is not None:
                        try:
                            parts.append(_format_currency(Decimal(str(amount)), currency))
                        except Exception:
                            parts.append(f"{str(currency).upper()} {amount}")
                    elif amount is not None:
                        parts.append(str(amount))
                    elif currency:
                        parts.append(str(currency).upper())

                    details = [detail for detail in [region, note] if detail]
                    if details:
                        parts.append(f"({' — '.join(details)})")

                    return " ".join(parts).strip()

                return str(value)

            cost_display = format_cost(cost)
            rows.append(
                (
                    nav_key,
                    link,
                    status_html,
                    cost_display,
                    f"{impl}h" if impl is not None else "",
                    f"{wait}h" if wait is not None else "",
                )
            )

        if not rows:
            return "No versions documented yet."

        header = "| Version | Status | Estimated Cost | Implementation Time (h) | Waiting Time (h) |"
        separator = "|---|---|---|---|---|"
        lines = [header, separator]
        for _, link, status, cost, impl, wait in sorted(rows, key=lambda row: row[0], reverse=True):
            lines.append(f"| {link} | {status} | {cost} | {impl} | {wait} |")
        return "\n".join(lines)

    def _format_date(value: str | None) -> str | None:
        if not value:
            return None
        for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
            try:
                parsed = datetime.strptime(value, fmt)
            except ValueError:
                continue
            if fmt == "%Y":
                return parsed.strftime("%Y")
            return parsed.strftime("%b %Y")
        return value

    def _parse_date(value: str | None) -> datetime | None:
        if not value:
            return None
        for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
        return None

    def _normalise(value: str | None) -> str:
        return (value or "").strip().lower()

    def _select_material_purchase(
        purchases: list[dict],
        *,
        region: str | None = None,
        supplier: str | None = None,
        date: str | None = None,
        unit: str | None = None,
    ) -> dict | None:
        if not purchases:
            return None

        candidates = purchases

        if region:
            region_matches = [p for p in candidates if _normalise(p.get("region")) == _normalise(region)]
            candidates = region_matches or candidates

        if supplier:
            supplier_matches = [p for p in candidates if _normalise(p.get("supplier")) == _normalise(supplier)]
            candidates = supplier_matches or candidates

        if date:
            date_matches = [p for p in candidates if str(p.get("date")) == str(date)]
            candidates = date_matches or candidates

        if unit:
            unit_matches = [p for p in candidates if _normalise(p.get("unit")) == _normalise(unit)]
            candidates = unit_matches or candidates

        def sort_key(purchase: dict):
            parsed = _parse_date(purchase.get("date"))
            return (parsed or datetime.min, purchase.get("supplier") or "")

        return sorted(candidates, key=sort_key, reverse=True)[0]

    @env.macro
    def render_bill_of_materials(path: str | None = None) -> str:
        page_rel = Path(env.page.file.src_path)
        meta_source = Path(path) if path else Path(env.page.file.abs_src_path)
        items = _bill_of_material_items(meta_source)

        if not items:
            return "No bill of materials recorded yet."

        page_dir_abs = docs_dir / page_rel.parent

        table_lines = [
            "| Material | Quantity | Unit Cost | Line Cost |",
            "| --- | --- | --- | --- |",
        ]

        for item in items:
            material_cell = ""
            material_page_rel: Path | None = item.get("material_page")
            title = item.get("title") or ""

            if material_page_rel is not None:
                material_abs = docs_dir / material_page_rel
                rel_path = os.path.relpath(material_abs, start=page_dir_abs)
                material_cell = f"[{title}]({rel_path.replace(os.sep, '/')})" if title else f"[{material_page_rel.stem}]({rel_path.replace(os.sep, '/')})"
            elif title:
                material_cell = title

            description = item.get("description")
            notes = item.get("notes")
            if description:
                suffix = description if notes else description
                material_cell = f"{material_cell}<br><small>{suffix}</small>" if material_cell else suffix

            if notes:
                note_html = notes if str(notes).startswith("<") else notes
                if material_cell:
                    material_cell += f"<br><small>{note_html}</small>"
                else:
                    material_cell = f"<small>{note_html}</small>"

            quantity_cell = item.get("quantity_display") or ""

            unit_cost_cell = ""
            unit_cost_currency = item.get("unit_cost_currency")
            unit_cost_decimal = item.get("unit_cost_decimal")
            unit_cost_amount = item.get("unit_cost_amount")
            unit_cost_per = item.get("unit_cost_per")
            unit_cost_label = item.get("unit_cost_label")

            if unit_cost_decimal is not None and unit_cost_currency:
                unit_cost_cell = _format_currency(unit_cost_decimal, unit_cost_currency)
            elif unit_cost_amount is not None and unit_cost_currency:
                unit_cost_cell = f"{unit_cost_currency} {unit_cost_amount}"
            elif unit_cost_decimal is not None:
                unit_cost_cell = _format_decimal(unit_cost_decimal)
            elif unit_cost_amount is not None:
                unit_cost_cell = str(unit_cost_amount)
            elif unit_cost_currency:
                unit_cost_cell = unit_cost_currency

            if unit_cost_per:
                per_value = str(unit_cost_per)
                if per_value.lower().startswith("per "):
                    unit_cost_cell = f"{unit_cost_cell} {per_value}".strip()
                else:
                    suffix = f"per {per_value}" if unit_cost_cell else f"per {per_value}"
                    unit_cost_cell = f"{unit_cost_cell} {suffix}".strip()

            if unit_cost_label:
                unit_cost_cell = unit_cost_label if not unit_cost_cell else f"{unit_cost_cell} — {unit_cost_label}"

            line_cost_cell = ""
            line_total_decimal = item.get("line_total_decimal")
            if line_total_decimal is not None and unit_cost_currency:
                line_cost_cell = _format_currency(line_total_decimal, unit_cost_currency)

            table_lines.append(
                f"| {material_cell} | {quantity_cell} | {unit_cost_cell} | {line_cost_cell} |"
            )

        totals = _bill_of_material_totals(items)
        for currency, amount in totals:
            table_lines.append(
                f"| **Total** |  |  | **{_format_currency(amount, currency)}** |"
            )

        return "\n".join(table_lines)

    @env.macro
    def render_material_purchases(path: str | None = None, heading_level: int = 3) -> str:
        page_path = Path(path) if path else Path(env.page.file.abs_src_path)
        meta = read_meta(page_path)
        material_block = meta.get("material") or {}
        purchases = material_block.get("purchases") or []

        if not purchases:
            return "No purchase history recorded yet."

        grouped: dict[str, list[dict]] = {}
        for purchase in purchases:
            region = purchase.get("region") or "Unspecified region"
            grouped.setdefault(region, []).append(purchase)

        heading_prefix = "#" * max(heading_level, 1)
        sections: list[str] = []

        def display_region(region_key: str) -> str:
            mapping = {
                "uk": "United Kingdom",
                "us": "United States",
                "eu": "European Union",
            }
            normalised = region_key.strip().lower()
            return mapping.get(normalised, region_key)

        for region_key in sorted(grouped.keys(), key=lambda value: value.lower()):
            sections.append(f"{heading_prefix} {display_region(region_key)}")
            sections.append("| Date | Supplier | Unit price | Notes |")
            sections.append("| --- | --- | --- | --- |")

            region_purchases = sorted(
                grouped[region_key],
                key=lambda purchase: (_parse_date(purchase.get("date")) or datetime.min, purchase.get("supplier") or ""),
                reverse=True,
            )

            for purchase in region_purchases:
                display_date = _format_date(purchase.get("date")) or ""
                supplier = purchase.get("supplier") or ""
                url = purchase.get("url")
                supplier_cell = f"[{supplier}]({url})" if supplier and url else supplier

                price_block = purchase.get("price") or {}
                price_amount = price_block.get("amount")
                price_currency = price_block.get("currency")
                if price_amount is not None and price_currency:
                    try:
                        price_value = _format_currency(Decimal(str(price_amount)), price_currency)
                    except Exception:
                        price_value = f"{price_currency} {price_amount}"
                elif price_amount is not None:
                    price_value = str(price_amount)
                elif price_currency:
                    price_value = price_currency
                else:
                    price_value = ""

                purchase_unit = purchase.get("unit")
                if purchase_unit:
                    unit_text = str(purchase_unit)
                    if unit_text.lower().startswith("per "):
                        price_value = f"{price_value} {unit_text}" if price_value else unit_text
                    else:
                        price_value = f"{price_value} per {unit_text}" if price_value else f"per {unit_text}"

                notes = purchase.get("notes") or ""
                sections.append(f"| {display_date} | {supplier_cell} | {price_value} | {notes} |")

            sections.append("")

        return "\n".join(sections).strip()

    @env.macro
    def status_banner(status: str | None = None) -> str:
        meta = read_meta(Path(env.page.file.abs_src_path))
        status = status or meta.get("status")
        if not status:
            return ""
        status_class = status.lower().replace(" ", "-")
        return f'<div class="status-banner status-{status_class}">{status.title()}</div>'

    @env.macro
    def parent_child_title():
        page = env.variables.get("page")
        parent = getattr(page, "parent", None)
        parent_title = getattr(parent, "title", "") if parent else ""
        return f"{parent_title} - {page.title}" if parent_title else page.title

    @env.macro
    def flex_predictor_embed():
        return (
            '<link rel="stylesheet" href="https://flex.apneascrap.com/fin-bending.css">\n'
            '<div id="fin-bending-app"></div>\n'
            '<script src="https://flex.apneascrap.com/fin-bending-core.js"></script>\n'
            '<script src="https://flex.apneascrap.com/fin-bending-render.js"></script>'
        )
