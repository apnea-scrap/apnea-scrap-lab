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

    @env.macro
    def render_bill_of_materials(path: str | None = None) -> str:
        page = Path(env.page.file.src_path)
        meta_source = Path(path) if path else Path(env.page.file.abs_src_path)
        meta = read_meta(meta_source)
        items = meta.get("bill_of_materials", []) or []

        if not items:
            return "No bill of materials recorded yet."

        page_dir = page.parent

        rows: list[tuple[str, str, str, str]] = []
        total_amount: Decimal | None = None
        total_currency: str | None = None

        for item in items:
            material_path = item.get("material")
            description = item.get("description")
            name = item.get("name")
            quantity = item.get("quantity")
            unit = item.get("unit")
            notes = item.get("notes")
            unit_cost = item.get("unit_cost", {}) or {}

            material_cell = ""
            if material_path:
                material_page = Path(material_path)
                if material_page.is_absolute():
                    material_page = material_page.relative_to(docs_dir)
                if material_page.suffix != ".md":
                    material_page = material_page.with_suffix(".md")
                material_abs = docs_dir / material_page
                material_meta = read_meta(material_abs)
                title = name or material_meta.get("title") or material_page.stem.replace("-", " ").title()
                rel_path = os.path.relpath(material_page.as_posix(), page_dir.as_posix())
                material_cell = f"[{title}]({rel_path.replace(os.sep, '/')})"
            elif name:
                material_cell = name

            if description:
                suffix = description if notes else description
                material_cell = f"{material_cell}<br><small>{suffix}</small>" if material_cell else suffix

            if notes:
                note_html = notes if notes.startswith("<") else notes
                if material_cell:
                    material_cell += f"<br><small>{note_html}</small>"
                else:
                    material_cell = f"<small>{note_html}</small>"

            quantity_cell = ""
            if quantity is not None:
                try:
                    quantity_value = Decimal(str(quantity))
                    quantity_cell = _format_decimal(quantity_value)
                except Exception:
                    quantity_cell = str(quantity)
                if unit:
                    quantity_cell = f"{quantity_cell} {unit}"
            elif unit:
                quantity_cell = unit

            unit_cost_amount = unit_cost.get("amount")
            unit_cost_currency = unit_cost.get("currency")
            unit_cost_per = unit_cost.get("per")
            unit_cost_supplier = unit_cost.get("supplier")
            unit_cost_date = unit_cost.get("date")
            unit_cost_note = unit_cost.get("note")

            unit_cost_details = []
            formatted_unit_cost = ""
            if unit_cost_amount is not None and unit_cost_currency:
                try:
                    amount_decimal = Decimal(str(unit_cost_amount))
                    formatted_unit_cost = _format_currency(amount_decimal, unit_cost_currency)
                except Exception:
                    formatted_unit_cost = f"{unit_cost_currency} {unit_cost_amount}"
                if unit_cost_per:
                    formatted_unit_cost += f" per {unit_cost_per}"
            elif unit_cost_amount is not None:
                formatted_unit_cost = str(unit_cost_amount)
            elif unit_cost_currency:
                formatted_unit_cost = unit_cost_currency

            formatted_date = _format_date(unit_cost_date)
            if formatted_date:
                unit_cost_details.append(formatted_date)
            if unit_cost_supplier:
                unit_cost_details.append(unit_cost_supplier)
            if unit_cost_note:
                unit_cost_details.append(unit_cost_note)
            if unit_cost_details:
                details = ", ".join(unit_cost_details)
                formatted_unit_cost = f"{formatted_unit_cost} ({details})" if formatted_unit_cost else f"({details})"

            line_cost_cell = ""
            if unit_cost_amount is not None and unit_cost_currency and quantity is not None:
                try:
                    quantity_decimal = Decimal(str(quantity))
                    amount_decimal = Decimal(str(unit_cost_amount))
                    line_total = quantity_decimal * amount_decimal
                    line_cost_cell = _format_currency(line_total, unit_cost_currency)

                    if total_currency is None:
                        total_currency = unit_cost_currency
                        total_amount = line_total
                    elif unit_cost_currency == total_currency:
                        total_amount = (total_amount or Decimal("0")) + line_total
                    else:
                        total_currency = None
                        total_amount = None
                except Exception:
                    line_cost_cell = ""

            rows.append(
                (
                    material_cell or "",
                    quantity_cell,
                    formatted_unit_cost,
                    line_cost_cell,
                )
            )

        table_lines = [
            "| Material | Quantity | Unit Cost | Line Cost |",
            "| --- | --- | --- | --- |",
        ]
        for material_cell, quantity_cell, unit_cost_cell, line_cost_cell in rows:
            table_lines.append(
                f"| {material_cell} | {quantity_cell} | {unit_cost_cell} | {line_cost_cell} |"
            )

        if total_currency and total_amount is not None:
            table_lines.append(
                f"| **Total** |  |  | **{_format_currency(total_amount, total_currency)}** |"
            )

        return "\n".join(table_lines)

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
