# AGENTS.md

---

## 1) Requirements

* Python 3.12 or newer installed and on PATH
* Git installed

---

## 2) Create or refresh the virtual environment

If `.venv` already exists, skip to **Activate the venv**.

```bash
# from the repo root
python -m venv .venv

# Upgrade pip and wheel inside the venv (recommended)
. .venv/bin/activate  # see Windows below
python -m pip install --upgrade pip wheel
pip install -r requirements.txt
```

---

## 3) Activate the venv

Activation ensures `python`, `pip`, and CLI tools resolve from `.venv`.

macOS or Linux (bash/zsh):

```bash
. .venv/bin/activate
```

---

## 4) Commands agents should use

All commands in this section assume the venv is active.

### 4.1 Run the MkDocs dev server

```bash
mkdocs serve
```

Local preview: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 4.2 Build the site

```bash
mkdocs build --clean
```

Artifacts: `site/`

---

## 5) Typical agent flows

### Agent

1. Activate venv
2. `mkdocs serve` for local preview at [http://127.0.0.1:8000](http://127.0.0.1:8000)
3. `mkdocs build --clean` for CI artifacts

---

## 6) Troubleshooting

* **`mkdocs: command not found`**: The venv is not active or MkDocs is not installed in it. Activate `.venv` and reinstall requirements.
* **SSL or network issues** during `pip install`: retry with `--retries 5` or use a mirror via `PIP_INDEX_URL`.

---

## 7) Conventions

* Never install global packages for this project. Always use `.venv`.
* Scripts and CLIs are expected to run with the venv activated.
* Keep `requirements.txt` minimal and pinned to compatible major versions when possible.

