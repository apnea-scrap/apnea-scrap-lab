---
title: Materials Directory
---
# Materials Directory

A single place to keep track of every consumable, component, or tool that feeds into ApneaScrap Lab builds.
Each page now stores the **unit of measure** and **purchase history** we have personally recorded so that
techniques can reference a neutral material while still pointing back to real prices.

Only the regions where we hold purchase data are listed. At the moment that means the United Kingdom.
When new data comes in for other locales we can extend each page with additional purchase rows.

## How to contribute

1. Create or update the material page with:
   - a short overview and any usage notes;
   - the `material` front matter block shown below, including at least one purchase entry;
   - a purchase history table scoped to the regions where you have receipts.
2. Link techniques and projects to the material page instead of hard-coding suppliers inside a build guide.
3. When logging a new technique version, add a `bill_of_materials` list in the front matter and render it with
   `{{ render_bill_of_materials() }}`. This keeps the bill in sync with recorded purchase data and makes the total cost
   explicit.

Need a new material? Duplicate the template below.

```markdown
---
title: Example Material
material:
  default_unit: example-unit
  purchases:
    - supplier: "Supplier name"
      url: "https://example.com/product"
      region: UK
      date: 2025-06
      unit: per example-unit
      price:
        amount: 12.34
        currency: GBP
      notes: "What makes this purchase representative"
---
# Example Material

## Overview
Describe the purpose of the material and what to look for.

## Purchase history (UK)
| Date | Supplier | Unit price | Notes |
| --- | --- | --- | --- |
| Jun 2025 | [Supplier name](https://example.com/product) | £12.34 per example-unit | 200 g/m², 1 m wide |

## Usage notes
- Bullet points covering weights, dimensions, compatible systems, etc.

## Related techniques
- [Technique name](../techniques/...)
```

Add techniques to the "Related techniques" section so it stays easy to see where a material is consumed.
