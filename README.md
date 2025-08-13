# ApneaScrap Lab

DIY freediving gear knowledge base. Methods, builds, materials and test procedures for fins, monofins and neck weights. Built with MkDocs Material and deployed on GitHub Pages.

---

## Features

- Clean documentation site with tabs for Methods, Projects, Tests and Materials
- Versioned methods with labels like use_case and maturity
- Pool vs Max variants captured per version
- Shared size variants for fins (short, medium, long) from a single YAML file
- Macros for reusable tables and YouTube embeds
- GitHub Actions that build and publish automatically on every push to main

---

## Prerequisites

- Python 3.9+
- Git
- Optional: a GitHub account with a repo named `apnea-scrap-lab`

---

## Quick start

1. Prepare the venv
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies
   ```bash
   python -m pip install -r requirements.txt
   ```

3. Preview locally
   ```bash
   mkdocs serve
   ```
   Open http://127.0.0.1:8000 to view the site.

4. Build the static site
   ```bash
   mkdocs build --strict
   ```
   The generated HTML goes into the `site/` folder.

---

## Publish on GitHub Pages

This repo contains a workflow at `.github/workflows/pages.yml` that builds and deploys on every push to `main`.

Steps:
1. Push to GitHub
   ```bash
   git add .
   git commit -m "Initial site"
   git push origin main
   ```
2. In GitHub, open Settings → Pages and keep Source set to GitHub Actions.
3. Wait for the workflow to pass. Your site will be available at:
   - `https://apnea-scrap.github.io/apnea-scrap-lab/` by default
   - Or your custom domain if configured

---

## Use a custom domain

If you own `apneascrap.com`:
1. Put a file `docs/CNAME` with this exact content:
   ```
   apneascrap.com
   ```
2. In GitHub → Settings → Pages → Custom domain, enter `apneascrap.com` and save.
3. DNS records at your registrar:
   - Apex A records to GitHub Pages
     ```
     @  185.199.108.153
     @  185.199.109.153
     @  185.199.110.153
     @  185.199.111.153
     ```
   - Optional `www` CNAME
     ```
     www  apnea-scrap.github.io
     ```
4. Enable Enforce HTTPS after the certificate is issued.

---

## Project structure

```
mkdocs.yml                 # Site configuration
main.py                    # MkDocs macros
requirements.txt           # Python deps
.github/workflows/pages.yml
shared/variants/fins.yml   # Short, medium, long size data
docs/
  index.md
  methods/
    acrylic-base/
      index.md
      v1-wood-support.md
      v2-acrylic-wedges.md
    carbon-layup/
      index.md
      v1.md
    glue-fin-rails/
      index.md
      v1.md
    surface-finish/
      index.md
      v1.md
    neck-weight/
      index.md
      v1-shot-inner-tube.md
      v2-molded-sleeve.md
  projects/
    fins-monofins/
      README.md
      builds/
        index.md
        pool.md
        max.md
    neck-weight/
      README.md
      builds/
        index.md
  tests/flex-test-rig.md
  materials/suppliers.md
```

---

## How to modify content

### Edit navigation
Open `mkdocs.yml` and add or reorder pages in the `nav:` section.

### Add a new method version
1. Create a new file under the method folder, for example:
   ```
   docs/methods/carbon-layup/v2-max.md
   ```
2. Add labels at the top using front matter:
   ```markdown
   ---
   title: Carbon layup v2 - max taper
   version: v2
   use_case: max
   status: active
   maturity: beta
   cost_level: medium
   tooling_level: medium
   time_level: medium
   date: 2025-08-13
   ---
   ```
3. Update the comparison table in `docs/methods/carbon-layup/index.md` to include the new version.
4. Commit and push. The site will rebuild automatically.

### Pool vs Max labeling
Use the `use_case:` label in front matter and reflect it in the method index comparison table.

### Short, Medium, Long variants
The table is generated from a single YAML file using a macro.

- Data file: `shared/variants/fins.yml`
- Use in any Markdown page:
  ```markdown
  ## Variants
  {{ fins_variants() }}
  ```

To add a new size, edit `shared/variants/fins.yml` and rebuild or push to main.

### Embed a YouTube video
Use the `yt` macro defined in `main.py`.
```markdown
{{ yt("VIDEO_ID", "Glue fin rails - demo") }}
```

---

## Macros reference

Macros live in `main.py`.

- `{{ fins_variants() }}` renders a table based on `shared/variants/fins.yml`
- `{{ yt("VIDEO_ID", "Title") }}` embeds a responsive privacy friendly YouTube iframe

Restart `mkdocs serve` if you modify `main.py` to reload macros.

---

## Images, CAD and heavy files

## Troubleshooting

- Build fails with missing plugin  
  Install dependencies again: `pip install -r requirements.txt`

- Site builds but is missing pages  
  Check the `nav:` paths in `mkdocs.yml`. Paths are relative to the `docs/` folder.

- Custom domain does not pick up HTTPS  
  Wait for the certificate to issue, then toggle Enforce HTTPS. Confirm DNS A records.

- Macros do not render  
  Confirm `mkdocs-macros-plugin` is listed under `plugins:` in `mkdocs.yml` and restart `mkdocs serve`.
