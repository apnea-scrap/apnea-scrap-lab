# AGENTS.md

---

## 1) Requirements

* Python 3.12 or newer (must be on PATH)
* Git installed

---

## 2) Quickstart setup

```bash
# from the repo root
python -m venv .venv
. .venv/bin/activate

python -m pip install --upgrade pip wheel
pip install -r requirements.txt
```

---

## 3) Local preview

Run the MkDocs development server:

```bash
mkdocs serve -f mkdocs.local.yml -a 127.0.0.1:8000
```

Preview at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 4) Build & deploy

**Do not build manually.**  
Production builds and deployment are handled by GitHub Actions in [`.github/workflows/pages.yml`](.github/workflows/pages.yml).

---

## 5) Troubleshooting

* **`mkdocs: command not found`** → venv not active or MkDocs not installed. Activate `.venv` and reinstall requirements.
* **SSL/network issues during `pip install`** → retry with `--retries 5` or use a mirror via `PIP_INDEX_URL`.

---

## 6) Conventions

* Always work inside `.venv`.
* Never install packages globally.
* Keep `requirements.txt` minimal and pinned where possible.

