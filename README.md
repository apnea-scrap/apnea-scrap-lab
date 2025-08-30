# ApneaScrap Lab

DIY freediving gear knowledge base. Techniques, versions, and test procedures for short fins, monofin and neck weight. Built with MkDocs Material and deployed on GitHub Pages.

---

## Features

- Clean documentation site with tabs for Projects and Techniques
- Versioned techniques with labels like use_case and maturity
- Pool vs Max use cases captured per version
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
   use_case: max
   status: active
   maturity: beta
   cost_level: medium
   tooling_level: medium
   time_level: medium
   date: 2025-08-13
   ---
   ```
3. Update the comparison table in `docs/techniques/carbon-layup/index.md` to include the new version.
4. Commit and push. The site will rebuild automatically.

### Pool vs Max labeling
Use the `use_case:` label in front matter and reflect it in the technique index comparison table.

### Embed a YouTube video
Use the `yt` macro defined in `main.py`.
```markdown
{{ yt("VIDEO_ID", "Glue fin rails - demo") }}
```

---

## Macros reference

Macros live in `main.py`.

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
