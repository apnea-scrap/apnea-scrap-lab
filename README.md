# ApneaScrap Lab

DIY freediving gear knowledge base. Techniques, versions, and test procedures for short fins, monofin and neck weight. Built with MkDocs Material and deployed on GitHub Pages.

---

## Features

- Clean documentation site with tabs for Projects and Techniques
- Versioned techniques with standard metadata (status, estimated cost, implementation time h, waiting time h)
- Comparison tables generated automatically from page metadata
- Bill of materials tables rendered from front matter so costs stay linked to recorded purchases
- Material pages list regional supplier history via macros fed by front matter
- Macro for YouTube embeds
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
   mkdocs serve -f mkdocs.local.yml -a 127.0.0.1:8000
   ```
   Open http://127.0.0.1:8000 to view the site.

4. Build the static site
   ```bash
   mkdocs build -f mkdocs.main.yml --site-dir site
   ```
   The generated HTML goes into the `site/` folder.

## GitHub workflow & environments

Every push runs the GitHub Actions workflow at
`.github/workflows/pages.yml`, which builds and deploys the site.
The deploy job uses **GitHub Environments** so branch rules apply:
`github-pages` for production and `previews` for all other branches.

All builds publish to the same GitHub Pages root. The workflow simply
changes the path: `main` writes to `/` while other branches go under
`/preview/<branch>`.

| Branch         | MkDocs config        | Environment    | Published URL                                     |
| -------------- | -------------------- | -------------- | ------------------------------------------------- |
| `main`         | `mkdocs.main.yml`    | `github-pages` | <https://lab.apneascrap.com/>                     |
| any other      | `mkdocs.preview.yml` | `previews`     | <https://lab.apneascrap.com/preview/<branch>/>    |

Preview URLs use a sanitized branch name (slashes → dashes), so each push has
its own preview site. The production site updates when changes land on `main`.

---

## How to modify content

### Edit navigation
Open `mkdocs.yml` and add or reorder pages in the `nav:` section.

### Add a new technique version
1. Create a new file under the technique folder, for example:
   ```
   docs/techniques/carbon-layup/v2-max.md
   ```
2. Add labels at the top using front matter:
  ```markdown
  ---
  title: Carbon layup v2 - max taper
  version: v2
  status: active
  maturity: beta
  estimated_cost:
    - amount: 33.29
      currency: GBP
      region: UK
      note: Based on Jun 2025 UK purchase history
  bill_of_materials:
    - material: materials/carbon-fiber-fabric.md
      description: 200 g/m² 3K cloth
      quantity: 0.3
      unit: m²
      purchase:
        region: UK
        unit: m² (1 m wide)
    - name: Consumables pack
      description: Gloves, brushes, mixing sticks
      quantity: 1
      unit_cost:
        amount: 3.50
        currency: GBP
  time_to_implement: 3
  waiting_time: 12
  ---
  ```
3. Add `{{ render_bill_of_materials() }}` where you want the rendered table to appear.
4. The comparison table on the technique index updates automatically from this metadata.
5. `estimated_cost` accepts a list of dictionaries so you can record regional estimates (keys: `amount`, `currency`, `region`, and optional `note`).
6. Commit and push. The site will rebuild automatically.

### Embed a YouTube video
Use the `yt` macro defined in `main.py`.
```markdown
{{ yt("VIDEO_ID", "Glue fin rails - demo") }}
```

---

## Macros reference

Macros live in `main.py`.

- `{{ yt("VIDEO_ID", "Title") }}` embeds a responsive privacy friendly YouTube iframe
- `{{ versions_table() }}` builds a version comparison table for the current folder based on front matter metadata
- `{{ status_banner() }}` shows a coloured banner with the current page status
- `{{ render_bill_of_materials() }}` converts the front matter bill of materials into a table, automatically pulling pricing from linked material pages when available
- `{{ render_material_purchases() }}` groups a material page’s purchase history by region and renders supplier tables

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
