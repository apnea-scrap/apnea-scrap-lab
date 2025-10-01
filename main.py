from pathlib import Path
import os
import re
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from html import escape
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

    def _format_total_display(currency: str, low_total: Decimal, high_total: Decimal) -> str:
        if low_total == high_total:
            return _format_currency(low_total, currency)
        return f"{_format_currency(low_total, currency)} - {_format_currency(high_total, currency)}"

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

    def _resolve_usage_type(entry: dict, material_meta: dict | None) -> dict[str, str]:
        raw_value = entry.get("usage_type")
        source_value = raw_value

        if source_value is None and material_meta:
            costing_block = (material_meta.get("material") or {}).get("costing") or {}
            source_value = costing_block.get("usage_type")

        normalised = _normalise(str(source_value) if source_value is not None else None)

        if not normalised:
            return {"key": "consumable", "display": "Consumable", "modifier": "consumable"}

        if normalised == "consumable":
            return {"key": normalised, "display": "Consumable", "modifier": "consumable"}

        if normalised == "reusable":
            return {"key": normalised, "display": "Reusable", "modifier": "reusable"}

        display_text = str(source_value).strip() if source_value is not None else ""
        if not display_text:
            display_text = normalised.replace("-", " ").title()

        return {"key": normalised, "display": display_text, "modifier": "custom"}

    def _tools_required(meta_source: Path) -> list[dict]:
        meta = read_meta(meta_source)
        raw_tools = meta.get("tools_required")

        if not raw_tools:
            return []

        if not isinstance(raw_tools, (list, tuple)):
            raw_tools = [raw_tools]

        tools: list[dict] = []

        for entry in raw_tools:
            if isinstance(entry, dict):
                name = (
                    entry.get("name")
                    or entry.get("label")
                    or entry.get("title")
                    or entry.get("tool")
                )
                name = str(name).strip() if name is not None else ""

                purpose = entry.get("purpose")
                if purpose is None:
                    purpose = entry.get("description") or entry.get("details")
                purpose = str(purpose).strip() if purpose is not None else ""

                if not name:
                    raise ValueError(
                        "Tools in front matter must define a 'name' field."
                    )
                if not purpose:
                    raise ValueError(
                        f"Tool '{name}' in {meta_source} must define a 'purpose' field."
                    )

                notes_field = entry.get("notes") or entry.get("note")
                notes = str(notes_field).strip() if notes_field is not None else ""

                link_field = entry.get("link") or entry.get("url")
                link = str(link_field).strip() if link_field else ""

                tools.append(
                    {
                        "name": name,
                        "purpose": purpose,
                        "notes": notes,
                        "link": link,
                    }
                )
            elif entry is None:
                continue
            else:
                raise ValueError(
                    f"Tools in {meta_source} must be dictionaries with name and purpose."
                )

        return tools

    def _resolve_project_techniques(meta_source: Path) -> list[dict]:
        meta = read_meta(meta_source)
        raw_entries = meta.get("techniques") or meta.get("technique_references")

        if not raw_entries:
            return []

        if not isinstance(raw_entries, (list, tuple)):
            raise ValueError(
                "Techniques listed in front matter must be provided as a list."
            )

        resolved: list[dict] = []

        for index, entry in enumerate(raw_entries):
            if isinstance(entry, str):
                entry = {"path": entry}

            if not isinstance(entry, dict):
                raise ValueError(
                    "Each technique entry must be a dictionary or path string."
                )

            path_value = (
                entry.get("path")
                or entry.get("page")
                or entry.get("source")
                or entry.get("ref")
            )

            if not path_value:
                raise ValueError(
                    "Technique entries must define a 'path' (or 'page'/'source') field."
                )

            technique_path = Path(path_value)

            if not technique_path.is_absolute():
                if str(technique_path).startswith("docs/") or str(technique_path).startswith("docs\\"):
                    technique_path = Path(env.project_dir) / technique_path
                else:
                    technique_path = docs_dir / technique_path

            if not technique_path.exists():
                raise FileNotFoundError(
                    f"Technique file '{path_value}' referenced in {meta_source} does not exist."
                )

            display_title = entry.get("title") or entry.get("name")
            if not display_title:
                technique_meta = read_meta(technique_path)
                display_title = technique_meta.get("title")

            if not display_title:
                display_title = technique_path.stem.replace("-", " ").title()

            notes_value = entry.get("notes") or entry.get("focus")
            notes = str(notes_value).strip() if notes_value else ""

            resolved.append(
                {
                    "title": str(display_title),
                    "path": technique_path,
                    "notes": notes,
                }
            )

        return resolved

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

            price_mode: str | None = item.get("price_mode")
            pricing_field = item.get("pricing")
            pricing_region: str | None = None
            pricing_supplier: str | None = None
            pricing_unit_override: str | None = None

            if isinstance(pricing_field, dict):
                price_mode = price_mode or pricing_field.get("mode")
                pricing_region = pricing_field.get("region")
                pricing_supplier = pricing_field.get("supplier")
                pricing_unit_override = pricing_field.get("unit")
            elif isinstance(pricing_field, str):
                price_mode = price_mode or pricing_field

            unit_cost_field = item.get("unit_cost")
            unit_cost_label: str | None = None
            if isinstance(unit_cost_field, dict):
                unit_cost = unit_cost_field.copy()
                mode_value = unit_cost.pop("mode", None)
                if price_mode is None and isinstance(mode_value, str):
                    price_mode = mode_value
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

            price_mode_value = _normalise(price_mode)
            if not price_mode_value:
                price_mode_value = "latest"

            line_total_ranges: dict[str, tuple[Decimal, Decimal]] = {}

            if price_mode_value == "range" and material_path:
                range_unit_filter = pricing_unit_override or unit_hint or purchase_unit
                price_ranges = _material_price_ranges(
                    material_purchases,
                    region=pricing_region,
                    supplier=pricing_supplier,
                    unit=range_unit_filter,
                )
                if price_ranges:
                    range_strings: list[str] = []
                    for currency_code in sorted(price_ranges.keys()):
                        low, high = price_ranges[currency_code]
                        if low == high:
                            range_text = _format_currency(low, currency_code)
                        else:
                            range_text = f"{_format_currency(low, currency_code)} - {_format_currency(high, currency_code)}"
                        range_strings.append(range_text)

                    per_reference = pricing_unit_override or explicit_unit or purchase_unit
                    per_suffix = ""
                    if per_reference:
                        per_value = str(per_reference)
                        if per_value.lower().startswith("per "):
                            per_suffix = f" {per_value}"
                        else:
                            per_suffix = f" per {per_value}"

                    summary_text = "<br>".join(range_strings)
                    if per_suffix:
                        summary_text = f"{summary_text}{per_suffix}"
                    range_label = f"{summary_text} (recorded range)" if summary_text else "Recorded price range"

                    if quantity_decimal is not None:
                        for currency_code, (low, high) in price_ranges.items():
                            line_total_ranges[currency_code] = (
                                quantity_decimal * low,
                                quantity_decimal * high,
                            )

                    if unit_cost_label:
                        unit_cost_label = f"{unit_cost_label}<br><small>{range_label}</small>"
                    else:
                        unit_cost_label = range_label

                    unit_cost_currency = None
                    unit_cost_amount = None
                    unit_cost_per = None
                else:
                    price_mode_value = "latest"

            unit_cost_decimal: Decimal | None = None
            if unit_cost_amount is not None:
                try:
                    unit_cost_decimal = Decimal(str(unit_cost_amount))
                except Exception:
                    unit_cost_decimal = None

            line_total_decimal: Decimal | None = None
            if unit_cost_decimal is not None and unit_cost_currency and quantity_decimal is not None:
                line_total_decimal = quantity_decimal * unit_cost_decimal

            if (
                line_total_decimal is not None
                and unit_cost_currency
                and not line_total_ranges
            ):
                currency_code = str(unit_cost_currency).upper()
                line_total_ranges[currency_code] = (
                    line_total_decimal,
                    line_total_decimal,
                )

            usage_type_info = _resolve_usage_type(item, material_meta)

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
                    "line_total_ranges": line_total_ranges,
                    "usage_type": usage_type_info.get("key"),
                    "usage_type_display": usage_type_info.get("display"),
                    "usage_type_modifier": usage_type_info.get("modifier"),
                }
            )

        return results

    def _bill_of_material_totals(items: list[dict]) -> list[tuple[str, Decimal, Decimal]]:
        totals: dict[str, dict[str, Decimal]] = {}
        for item in items:
            range_totals = item.get("line_total_ranges") or {}
            if range_totals:
                for currency_code, (low_value, high_value) in range_totals.items():
                    if low_value is None or high_value is None:
                        continue
                    code = str(currency_code).upper()
                    bucket = totals.setdefault(code, {"low": Decimal("0"), "high": Decimal("0")})
                    bucket["low"] += low_value
                    bucket["high"] += high_value
                continue

            currency = item.get("unit_cost_currency")
            line_total = item.get("line_total_decimal")
            if not currency or line_total is None:
                continue
            code = str(currency).upper()
            bucket = totals.setdefault(code, {"low": Decimal("0"), "high": Decimal("0")})
            bucket["low"] += line_total
            bucket["high"] += line_total

        ordered: list[tuple[str, Decimal, Decimal]] = []
        for currency_code in sorted(totals.keys()):
            data = totals[currency_code]
            ordered.append((currency_code, data["low"], data["high"]))
        return ordered

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
                cost = []
                for currency, low_total, high_total in bom_totals:
                    entry: dict[str, object] = {"currency": currency}
                    if low_total == high_total:
                        entry["amount"] = low_total
                    else:
                        entry["amount_low"] = low_total
                        entry["amount_high"] = high_total
                    cost.append(entry)
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
                    amount_low = value.get("amount_low")
                    amount_high = value.get("amount_high")
                    currency = value.get("currency")
                    region = value.get("region")
                    note = value.get("note")

                    parts: list[str] = []
                    has_range = amount_low is not None and amount_high is not None

                    if has_range:
                        low_value = amount_low
                        high_value = amount_high
                        try:
                            low_decimal = Decimal(str(low_value))
                            high_decimal = Decimal(str(high_value))
                        except Exception:
                            low_decimal = None
                            high_decimal = None

                        if currency and low_decimal is not None and high_decimal is not None:
                            low_text = _format_currency(low_decimal, currency)
                            high_text = _format_currency(high_decimal, currency)
                        elif low_decimal is not None and high_decimal is not None:
                            low_text = _format_decimal(low_decimal)
                            high_text = _format_decimal(high_decimal)
                        else:
                            low_text = str(low_value) if low_value is not None else ""
                            high_text = str(high_value) if high_value is not None else ""

                        range_text = " - ".join(filter(None, [low_text, high_text])).strip()
                        if range_text:
                            parts.append(range_text)
                        elif currency:
                            parts.append(str(currency).upper())
                    else:
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

    def _normalise_unit(value: str | None) -> str:
        normalised = _normalise(value)
        if normalised.startswith("per "):
            return normalised[4:]
        return normalised

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
            unit_key = _normalise_unit(unit)
            unit_matches = [
                p for p in candidates if _normalise_unit(p.get("unit")) == unit_key
            ]
            candidates = unit_matches or candidates

        def sort_key(purchase: dict):
            parsed = _parse_date(purchase.get("date"))
            return (parsed or datetime.min, purchase.get("supplier") or "")

        return sorted(candidates, key=sort_key, reverse=True)[0]

    def _material_price_ranges(
        purchases: list[dict],
        *,
        region: str | None = None,
        supplier: str | None = None,
        unit: str | None = None,
    ) -> dict[str, tuple[Decimal, Decimal]]:
        if not purchases:
            return {}

        region_key = _normalise(region) if region else ""
        supplier_key = _normalise(supplier) if supplier else ""
        unit_key = _normalise_unit(unit) if unit else ""

        filtered: list[dict] = []
        for purchase in purchases:
            if region_key and _normalise(purchase.get("region")) != region_key:
                continue
            if supplier_key and _normalise(purchase.get("supplier")) != supplier_key:
                continue
            if unit_key and _normalise_unit(purchase.get("unit")) != unit_key:
                continue
            filtered.append(purchase)

        if not filtered:
            return {}

        ranges: dict[str, list[Decimal]] = {}
        for purchase in filtered:
            price_block = purchase.get("price") or {}
            amount = price_block.get("amount")
            currency = price_block.get("currency")
            if amount is None or not currency:
                continue
            try:
                amount_decimal = Decimal(str(amount))
            except Exception:
                continue
            currency_code = str(currency).upper()
            ranges.setdefault(currency_code, []).append(amount_decimal)

        result: dict[str, tuple[Decimal, Decimal]] = {}
        for currency_code, values in ranges.items():
            if not values:
                continue
            result[currency_code] = (min(values), max(values))

        return result

    @env.macro
    def render_tools_required(path: str | None = None, title: str | None = None) -> str:
        meta_source = Path(path) if path else Path(env.page.file.abs_src_path)
        tools = _tools_required(meta_source)

        if not tools:
            return ""

        table_lines = [
            "| Tool | Purpose |",
            "| --- | --- |",
        ]

        for tool in tools:
            name_cell, purpose_cell = _render_tool_row(tool)
            table_lines.append(f"| {name_cell} | {purpose_cell} |")

        return "\n".join(table_lines)

    def _usage_type_label(display: str, modifier: str | None = None) -> str:
        if not display:
            return ""

        classes = ["bom-cost-label"]
        modifier_value = str(modifier or "").strip()
        if modifier_value:
            safe_modifier = re.sub(r"[^a-z0-9-]", "-", modifier_value)
            classes.append(f"bom-cost-label--{safe_modifier}")

        class_attr = " ".join(classes)
        return f'<span class="{class_attr}">{escape(str(display))}</span>'

    def _render_bill_of_material_row(item: dict, page_dir_abs: Path) -> tuple[str, str, str, str]:
        material_cell = ""
        material_page_rel: Path | None = item.get("material_page")
        title = item.get("title") or ""

        if material_page_rel is not None:
            material_abs = docs_dir / material_page_rel
            rel_path = os.path.relpath(material_abs, start=page_dir_abs)
            link_label = title or material_page_rel.stem
            material_cell = f"[{link_label}]({rel_path.replace(os.sep, '/')})"
        elif title:
            material_cell = title

        usage_type_display = item.get("usage_type_display")
        usage_type_modifier = item.get("usage_type_modifier")
        label_html = _usage_type_label(usage_type_display, usage_type_modifier)

        description = item.get("description")
        notes = item.get("notes")
        if description:
            description_html = description
            if material_cell:
                if label_html:
                    material_cell = f"{material_cell}<br>{label_html} <small>{description_html}</small>"
                else:
                    material_cell = f"{material_cell}<br><small>{description_html}</small>"
            else:
                if label_html:
                    material_cell = f"{label_html} <small>{description_html}</small>"
                else:
                    material_cell = description_html
        elif label_html:
            material_cell = f"{material_cell}<br>{label_html}" if material_cell else label_html

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

        return material_cell, quantity_cell, unit_cost_cell, line_cost_cell

    def _render_tool_row(tool: dict) -> tuple[str, str]:
        name_value = str(tool.get("name") or "")
        name_cell = _format_table_cell(name_value)

        link_value = tool.get("link")
        if link_value:
            href = escape(str(link_value), quote=True)
            label = name_cell or escape(str(link_value))
            name_cell = f"<a href=\"{href}\">{label}</a>"

        purpose_value = str(tool.get("purpose") or "")
        purpose_cell = _format_table_cell(purpose_value)

        notes_value = tool.get("notes")
        if notes_value:
            notes_text = str(notes_value)
            if notes_text.startswith("<"):
                notes_html = notes_text
            else:
                notes_html = _format_table_cell(notes_text)
            if purpose_cell:
                purpose_cell = f"{purpose_cell}<br><small>{notes_html}</small>"
            else:
                purpose_cell = f"<small>{notes_html}</small>"

        return name_cell, purpose_cell

    def _format_table_cell(value: str) -> str:
        if not value:
            return ""
        escaped = escape(value)
        return escaped.replace("|", "&#124;").replace("\n", "<br>")

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
            material_cell, quantity_cell, unit_cost_cell, line_cost_cell = _render_bill_of_material_row(
                item, page_dir_abs
            )
            table_lines.append(
                f"| {material_cell} | {quantity_cell} | {unit_cost_cell} | {line_cost_cell} |"
            )

        totals = _bill_of_material_totals(items)
        for currency, low_total, high_total in totals:
            formatted_total = _format_total_display(currency, low_total, high_total)
            table_lines.append(
                f"| **Total** |  |  | **{formatted_total}** |"
            )

        return "\n".join(table_lines)

    def _render_technique_requirements_bill_of_materials(
        meta_source: Path,
    ) -> str:
        techniques = _resolve_project_techniques(meta_source)

        if not techniques:
            return ""

        page_rel = Path(env.page.file.src_path)
        page_dir_abs = docs_dir / page_rel.parent
        table_lines = [
            "| Technique | Material | Quantity | Unit Cost | Line Cost |",
            "| --- | --- | --- | --- | --- |",
        ]
        aggregated_items: list[dict] = []
        empty_notes: list[str] = []
        populated_techniques: list[tuple[dict, list[dict]]] = []

        for technique in techniques:
            display_title = technique["title"]
            note = technique.get("notes") or ""
            technique_path = technique["path"]

            items = _bill_of_material_items(technique_path)
            if not items:
                if note:
                    note_html = _format_table_cell(str(note))
                    empty_notes.append(
                        f"<p><strong>{escape(display_title)}:</strong> <em>{note_html}</em></p>"
                    )
                else:
                    empty_notes.append(
                        f"<p><strong>{escape(display_title)}:</strong> <em>No bill of materials recorded yet.</em></p>"
                    )
                continue

            aggregated_items.extend(items)
            populated_techniques.append((technique, items))

        for index, (technique, items) in enumerate(populated_techniques):
            display_title = technique["title"]
            note = technique.get("notes") or ""

            technique_label = _format_table_cell(str(display_title))
            note_html = _format_table_cell(str(note)) if note else ""

            for item_index, item in enumerate(items):
                material_cell, quantity_cell, unit_cost_cell, line_cost_cell = _render_bill_of_material_row(
                    item, page_dir_abs
                )
                technique_cell = technique_label if item_index == 0 else ""
                if item_index == 0 and note_html:
                    if technique_cell:
                        technique_cell = f"{technique_cell}<br><small><em>{note_html}</em></small>"
                    else:
                        technique_cell = f"<small><em>{note_html}</em></small>"

                table_lines.append(
                    f"| {technique_cell} | {material_cell} | {quantity_cell} | {unit_cost_cell} | {line_cost_cell} |"
                )

            technique_totals = _bill_of_material_totals(items)
            for currency, low_total, high_total in technique_totals:
                formatted_total = _format_total_display(currency, low_total, high_total)
                table_lines.append(
                    f"| **{_format_table_cell(str(display_title))} total** |  |  |  | **{formatted_total}** |"
                )

            if index < len(populated_techniques) - 1:
                table_lines.append("| <small>&nbsp;</small> |  |  |  |  |")

        if not aggregated_items:
            return "No bill of materials recorded yet."

        grand_totals = _bill_of_material_totals(aggregated_items)
        consumable_items: list[dict] = []
        reusable_items: list[dict] = []

        for item in aggregated_items:
            usage_key = str(item.get("usage_type") or "").lower()
            if usage_key == "reusable":
                reusable_items.append(item)
            else:
                consumable_items.append(item)

        consumable_totals = _bill_of_material_totals(consumable_items)
        reusable_totals = _bill_of_material_totals(reusable_items)

        def _totals_to_map(totals: list[tuple[str, Decimal, Decimal]]) -> dict[str, tuple[Decimal, Decimal]]:
            return {currency: (low_total, high_total) for currency, low_total, high_total in totals}

        consumable_map = _totals_to_map(consumable_totals)
        reusable_map = _totals_to_map(reusable_totals)
        grand_map = _totals_to_map(grand_totals)

        currency_keys = sorted(
            set(grand_map.keys())
            | set(consumable_map.keys())
            | set(reusable_map.keys())
        )

        for currency in currency_keys:
            consumable_low, consumable_high = consumable_map.get(
                currency, (Decimal("0"), Decimal("0"))
            )
            reusable_low, reusable_high = reusable_map.get(
                currency, (Decimal("0"), Decimal("0"))
            )
            grand_low, grand_high = grand_map.get(currency, (Decimal("0"), Decimal("0")))

            expected_low = consumable_low + reusable_low
            expected_high = consumable_high + reusable_high

            if expected_low != grand_low or expected_high != grand_high:
                grand_low, grand_high = expected_low, expected_high

            formatted_consumable = _format_total_display(
                currency, consumable_low, consumable_high
            )
            formatted_reusable = _format_total_display(
                currency, reusable_low, reusable_high
            )
            formatted_grand = _format_total_display(currency, grand_low, grand_high)

            consumable_label = _usage_type_label("Consumables subtotal", "consumable")
            reusable_label = _usage_type_label("Reusable subtotal", "reusable")
            grand_label = "<strong>Grand total</strong>"

            consumable_cell = (
                f"{consumable_label} <strong>{formatted_consumable}</strong>"
            )
            reusable_cell = (
                f"{reusable_label} <strong>{formatted_reusable}</strong>"
            )
            grand_cell = f"{grand_label} <strong>{formatted_grand}</strong>"

            table_lines.append(
                "| "
                + f"{consumable_cell}"
                + " | <strong>+</strong> | "
                + f"{reusable_cell}"
                + " | <strong>=</strong> | "
                + f"{grand_cell}"
                + " |"
            )

        extra_notes = "\n".join(empty_notes)
        table_html = "\n".join(table_lines)
        return f"{table_html}\n\n{extra_notes}".strip()

    def _render_technique_requirements_tools(meta_source: Path) -> str:
        techniques = _resolve_project_techniques(meta_source)

        if not techniques:
            return ""

        table_lines = [
            "| Tool | Techniques | Purpose |",
            "| --- | --- | --- |",
        ]
        empty_notes: list[str] = []
        grouped_tools: dict[str, dict[str, object]] = {}

        for technique in techniques:
            display_title = technique["title"]
            note = technique.get("notes") or ""
            technique_path = technique["path"]

            tools = _tools_required(technique_path)
            if not tools:
                if note:
                    note_html = _format_table_cell(str(note))
                    empty_notes.append(
                        f"<p><strong>{escape(display_title)}:</strong> <em>{note_html}</em></p>"
                    )
                else:
                    empty_notes.append(
                        f"<p><strong>{escape(display_title)}:</strong> <em>No tools recorded yet.</em></p>"
                    )
                continue

            technique_label = _format_table_cell(str(display_title))

            for tool in tools:
                raw_name = str(tool.get("name") or "").strip()
                if not raw_name:
                    continue

                normalized_name = raw_name.casefold()
                entry = grouped_tools.setdefault(
                    normalized_name,
                    {
                        "name": raw_name,
                        "link": tool.get("link"),
                        "purposes": [],
                        "notes": [],
                        "techniques": [],
                    },
                )

                if not entry["name"] and raw_name:
                    entry["name"] = raw_name

                link_value = tool.get("link")
                if link_value and not entry["link"]:
                    entry["link"] = link_value

                purpose_value = str(tool.get("purpose") or "").strip()
                if purpose_value and purpose_value not in entry["purposes"]:
                    entry["purposes"].append(purpose_value)

                notes_value = tool.get("notes")
                if notes_value is not None:
                    notes_text = str(notes_value)
                    if notes_text and notes_text not in entry["notes"]:
                        entry["notes"].append(notes_text)

                if technique_label and technique_label not in entry["techniques"]:
                    entry["techniques"].append(technique_label)

        if not grouped_tools:
            return "No tools recorded yet."

        grouped_entries = [
            grouped_tools[normalized_name]
            for normalized_name in sorted(grouped_tools.keys())
        ]

        for entry in grouped_entries:
            name_value = str(entry["name"])
            name_cell = _format_table_cell(name_value)
            link_value = entry.get("link")
            if link_value:
                href = escape(str(link_value), quote=True)
                label = name_cell or escape(str(link_value))
                name_cell = f"<a href=\"{href}\">{label}</a>"

            techniques_cell = "<br>".join(entry["techniques"])

            purpose_parts: list[str] = []
            for purpose in entry["purposes"]:
                formatted = _format_table_cell(purpose)
                if formatted:
                    purpose_parts.append(formatted)

            purpose_cell = "<br>".join(purpose_parts)

            note_cells: list[str] = []
            for note in entry["notes"]:
                if note.startswith("<"):
                    note_cells.append(note)
                else:
                    formatted_note = _format_table_cell(note)
                    if formatted_note:
                        note_cells.append(formatted_note)

            if note_cells:
                notes_html = "<br>".join(note_cells)
                if purpose_cell:
                    purpose_cell = f"{purpose_cell}<br><small>{notes_html}</small>"
                else:
                    purpose_cell = f"<small>{notes_html}</small>"

            table_lines.append(
                f"| {name_cell} | {techniques_cell} | {purpose_cell} |"
            )

        extra_notes = "\n".join(empty_notes)
        table_html = "\n".join(table_lines)
        if extra_notes:
            return f"{table_html}\n\n{extra_notes}".strip()
        return table_html

    @env.macro
    def render_technique_requirements_bill_of_materials(
        path: str | None = None,
    ) -> str:
        meta_source = Path(path) if path else Path(env.page.file.abs_src_path)
        return _render_technique_requirements_bill_of_materials(meta_source)

    @env.macro
    def render_technique_requirements_tools(path: str | None = None) -> str:
        meta_source = Path(path) if path else Path(env.page.file.abs_src_path)
        return _render_technique_requirements_tools(meta_source)

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
