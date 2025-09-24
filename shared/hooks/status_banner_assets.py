"""MkDocs hook to inject environment-specific status banner assets."""

from __future__ import annotations

from typing import Any


def on_config(config: Any, **_: Any) -> Any:
    """Append status banner assets based on `extra.status_banner_variant`."""
    extra = getattr(config, "extra", None) or {}
    variant = extra.get("status_banner_variant")
    if not variant:
        return config

    # Ensure the lists exist so we can append safely.
    javascript = list(getattr(config, "extra_javascript", []) or [])
    stylesheet = list(getattr(config, "extra_css", []) or [])

    banner_js = f"js/{variant}-banner.js"
    banner_css = f"css/{variant}-banner.css"

    if banner_js not in javascript:
        javascript.append(banner_js)
    if banner_css not in stylesheet:
        stylesheet.append(banner_css)

    config.extra_javascript = javascript
    config.extra_css = stylesheet
    return config
