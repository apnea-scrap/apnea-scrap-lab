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
        rows = []
        for file in sorted(base.glob("**/*.md")):
            if file.name == "index.md":
                continue
            meta = read_meta(file)
            rel_path = file.relative_to(base)
            link_text = " ".join(rel_path.with_suffix("").parts).replace("-", " ")
            link = f"[{link_text}]({rel_path.as_posix()})"
            cost = meta.get("estimated_cost")
            impl = meta.get("time_to_implement")
            wait = meta.get("waiting_time")
            rows.append(
                (
                    link,
                    meta.get("status", ""),
                    f"£{cost}" if cost is not None else "",
                    f"{impl}h" if impl is not None else "",
                    f"{wait}h" if wait is not None else "",
                )
            )

        if not rows:
            return "No versions documented yet."

        header = (
            "| Version | Status | Estimated Cost (£) | Implementation Time (h) | Waiting Time (h) |"
        )
        separator = "|---|---|---|---|---|"
        lines = [header, separator]
        for link, status, cost, impl, wait in rows:
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
