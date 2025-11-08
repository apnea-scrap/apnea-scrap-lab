---
title: 'Research Notes: Monofin Layer Stack'
date:
  created: 2025-12-09
  updated: 2025-12-09
authors:
- julian-g
categories:
- Research Notes
tags:
- Monofins
- Layering
- Predicting Flex
readtime: 4
summary: Notes on translating the Bluewater Freediving monofin cross-section into a DIY layer plan and validating it with Predicting Flex inputs for a 520 × 700 mm blade.
links:
- Predicting Flex technique: techniques/predicting-flex/index.md
- Predicting Flex calculator release: blog/posts/2025-10-20-flex-predict-calculator/index.md
- DIY carbon monofin BOM: blog/posts/2025-09-26-diy-carbon-monofin-bom/index.md
---

This note records the **monofin layer stack** derived from the Bluewater Freediving reference photo and cross-checked with the Predicting Flex technique.

<!-- more -->

Reference photo: [Bluewater Freediving monofin internals](https://www.bluewaterfreediving.com/wp-content/uploads/2024/02/monofin__45463_zoom.jpg).

## What the reference image shows

- Six ribs rise off the foot plate with progressively shorter carbon caps. The staggered rib height maintains rocker even with a softer tip.
- The outer two ribs blend into the side rails, indicating a **load path shared between rails and central ribs**.
- Carbon cloth at the foot is visibly thicker and overlaps the rails before tapering, confirming at least **6 layers near the foot pocket** plus the rib caps.

These points match the earlier [DIY monofin BOM notes](../2025-09-26-diy-carbon-monofin-bom/index.md): wide blades combine lateral ribs with an aggressive taper.

## Predicting Flex setup

The geometry was entered into the tapered cantilever beam calculator described on the [Predicting Flex technique](../../../techniques/predicting-flex/index.md) page with the following parameters:

| Input | Value |
| --- | --- |
| Free blade length | 520 mm |
| Blade width | 700 mm |
| Layers at foot | 6 |
| Layers at tip | 2 |
| Minimum layer length | 100 mm |

Model output:

- Angle at tip (under max load): 90.1°
- Load required for 90° deflection: 46.6 N (≈4.75 kg)
- Second moment of area at foot: 452.81 mm⁴
- Second moment of area at tip: 16.77 mm⁴
- Hydrodynamic resistance score at 5 N: 23.11 units
- Hydrodynamic resistance score at 10 N: 21.81 units
- Hydrodynamic resistance score at 46.6 N: 12.55 units

These values keep the load at the tip at 46.6 N, which is roughly four times the stiffness of a single long freediving blade.

Current working stack: 6→4→2 layers, 100 mm minimum overlap, and rib tapers only after the cloth count steps down.
