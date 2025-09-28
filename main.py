from pathlib import Path
import re
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
