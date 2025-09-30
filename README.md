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
  bill_of_materials:
    - material: materials/carbon-fiber-fabric.md
      description: 200 g/m² 3K cloth
      quantity:
        amount: 0.3
        unit: m² (1 m wide)
    - name: Consumables pack
      description: Gloves, brushes, mixing sticks
      quantity:
        amount: 1
        unit: pack
      unit_cost:
        amount: 3.50
        currency: GBP
  tools_required:
    - name: Gloves
      purpose: Protect your hands while handling resin
    - name: Mixing sticks
      purpose: Blend resin and hardener thoroughly
  time_to_implement: 3
  waiting_time: 12
  ---
  ```
  Every bill of materials entry must either reference a material page (setting `quantity.unit` so the macro can match a
  recorded purchase) or provide its own `name`. Use `quantity.amount` for the numerical value and set
  `quantity.unit` whenever you want to control the rendered unit or are defining an inline item. Provide
  `quantity.display` if you need full control over how the quantity appears in the rendered table. When linking a
  material page, skip the legacy `purchase` block—the macro automatically selects the recorded purchase using the
  `quantity.unit` you provide. List recurring equipment under `tools_required`, adding a `name` for each tool and a
  short `purpose` that explains why it is needed for the process.
  To show the recorded price spread instead of the latest purchase, add `pricing: range` (or
  `pricing: { mode: range, unit: pair }` to filter by unit) to the BOM entry that references the material. The range is
  calculated from the stored purchases, so totals are left blank for that row.
3. Add a `## Tools Required` section near the top of the page (for example right after `{{ status_banner() }}`) and place `{{ render_tools_required() }}` inside it to render the tools list captured in front matter.
4. Add `{{ render_bill_of_materials() }}` where you want the rendered table to appear.
5. The comparison table on the technique index automatically calculates estimated costs from the bill of materials.
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
- `{{ render_tools_required() }}` outputs the front matter tools list as a table with optional links and notes;
  each tool entry must provide a `name` and `purpose`
- `{{ render_bill_of_materials() }}` converts the front matter bill of materials into a table, automatically pulling pricing from linked material pages when available; set `unit_cost: "Inexpensive option"` (or any label string) on a BOM entry when you want the table to display that note instead of a numeric price
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
