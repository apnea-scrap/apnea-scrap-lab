import yaml

def define_env(env):
    @env.macro
    def fins_variants():
        with open("shared/variants/fins.yml") as f:
            data = yaml.safe_load(f)
        header = "| Variant | Blade length (mm) | Blade width (mm) | Base size (mm) | Cloth area (m²) | Notes |\n"
        header += "|---|---:|---:|---:|---:|---|\n"
        rows, order = [], ["short","medium","long"]
        for k in order:
            if k not in data:
                continue
            v = data[k]
            b = v.get("base_size_mm", [0, 0])
            rows.append(f"| {k.title()} | {v['blade_length_mm']} | {v['blade_width_mm']} | {b[0]}×{b[1]} | {v['cloth_area_m2']} | {v.get('notes','')} |")
        return header + "\n".join(rows)

    @env.macro
    def yt(id, title="", ratio="56.25%"):
        title = title or "YouTube video"
        return f'''<div style="position:relative;padding-top:{ratio};">
  <iframe src="https://www.youtube-nocookie.com/embed/{id}" title="{title}" loading="lazy" allowfullscreen
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"></iframe>
</div>'''
