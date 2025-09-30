---
title: Materials Directory
---
# Materials Directory

A single place to keep track of every consumable, component, or tool that feeds into ApneaScrap Lab builds.
Each page now stores the **purchase history** we have personally recorded so that
techniques can reference a neutral material while still pointing back to real prices.

Only the regions where we hold purchase data are listed. At the moment that means the United Kingdom.
When new data comes in for other locales we can extend each page with additional purchase rows.

## How to contribute

1. Create or update the material page with:
   - a short overview and any usage notes;
   - the `material` front matter block shown below, including at least one purchase entry for every supplier-region pair;
   - a `{{ render_material_purchases() }}` call so the macro can turn the recorded purchases into tables grouped by region.
2. Link techniques and projects to the material page instead of hard-coding suppliers inside a build guide.
3. When logging a new technique version, add a `bill_of_materials` list in the front matter and render it with
   `{{ render_bill_of_materials() }}`. Reference materials via their page path and set `quantity.unit` so the macro can
   match the recorded purchase data automatically. Skip `purchase` hints on technique entries—the macro infers the
   correct record from the unit you supply. Quantities default to the chosen purchase unit, so you only need to describe
   the amount being used.

## Usage types for the bill of materials

Not every material behaves the same once it has been purchased. Resins, carbon
cloth, and other supplies are consumed during a build, while acrylic base
plates or footpockets stay in service for many projects. Rather than tracking
per-build usage manually, classify each material with a simple `usage_type`
flag so totals can be split into consumable spend versus reusable assets when a
BOM is rendered.

### 1. Declare the usage type on each material

Add a `material.costing.usage_type` field to every material page. Use
`consumable` for items that are spent during a build (the default if omitted)
and `reusable` for tooling or hardware that comes back after the build.

```yaml
---
title: PVA Release Agent
material:
  costing:
    usage_type: consumable
---
```

```yaml
---
title: Acrylic Base Plate
material:
  costing:
    usage_type: reusable
---
```

### 2. Let BOM entries inherit the usage type

BOM items that reference a material page automatically take on that page's
`usage_type`. If you need to describe a custom part that is not listed in the
materials directory, set the flag directly on the BOM line so renderers can
categorise it correctly:

```yaml
bill_of_materials:
  - material: materials/pva-release-agent.md  # inherits `consumable`
  - title: Custom jig
    usage_type: reusable
```

This minimal metadata is enough for downstream tooling to distinguish
consumable purchases from reusable kit without modelling amortisation or
tracking build counts.

Need a new material? Duplicate the template below.

```markdown
---
title: Example Material
material:
  purchases:
    - supplier: "Supplier name"
      url: "https://example.com/product"
      region: UK
      date: 2025-06
      unit: example-unit
      price:
        amount: 12.34
        currency: GBP
      notes: "What makes this purchase representative"
---
# Example Material

## Overview
Describe the purpose of the material and what to look for.

## Purchase history

{{ render_material_purchases() }}

## Usage notes
- Bullet points covering weights, dimensions, compatible systems, etc.

## Related techniques
- [Technique name](../techniques/...)
```

Add techniques to the "Related techniques" section so it stays easy to see where a material is consumed.
