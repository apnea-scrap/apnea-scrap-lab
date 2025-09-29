---
title: Short fins v1 — project sketch
version: v1
status: planning
maturity: concept
techniques:
  - title: Manual wet layup stack
    focus: Layer schedule for the baseline short fin laminate.
    path: techniques/laminating-carbon/v1/wet-layup.md
  - title: Laminated paper cutting template
    focus: Build a durable outline for the blade profile and trimming plan.
    path: techniques/cutting-template/v1/paper-laminate.md
  - title: Flex predictor modelling
    focus: Use the cantilever calculator to sanity check the flex goals before laminating.
    path: techniques/predicting-flex/v1/tapered-cantilever-beam.md
---

# Short fins v1 — project sketch
{{ status_banner() }}

Early outline for producing compact training fins with predictable flex and repeatable templates.

## Planning the laminate layers
- Capture preliminary layup ideas using the [Manual wet layup stack](../../techniques/laminating-carbon/v1/wet-layup.md) technique.
- Record fabric weights, orientations, and any taper adjustments needed for short blades.
- Note resin targets so we can compare against the predicted flex results later.

## Estimating flex
- Start with the [Flex predictor modelling](../../techniques/predicting-flex/v1/tapered-cantilever-beam.md) calculator to estimate the target tip deflection.
- Plug in the tentative laminate schedule and iterate until the simulated stiffness matches the desired feel.
- Add comments for expected body weight range or training scenarios this setup should support.

## Planning the cutting sheet
- Reference the [Laminated paper cutting template](../../techniques/cutting-template/v1/paper-laminate.md) to prepare blade outlines.
- Jot down quantities for each size variant and how they fit on the raw carbon sheets.
- Capture trimming allowances so the cured laminate nests cleanly within the template.

## Bill of Materials
{{ render_technique_requirements("bill_of_materials") }}

## Tools Required
{{ render_technique_requirements("tools") }}

## Instructions
1. Build or update the cutting template using the steps from [Laminated paper cutting template](../../techniques/cutting-template/v1/paper-laminate.md).
2. Simulate the layup in [Flex predictor modelling](../../techniques/predicting-flex/v1/tapered-cantilever-beam.md) and lock in the target flex window.
3. Execute the laminate following [Manual wet layup stack](../../techniques/laminating-carbon/v1/wet-layup.md), capturing cure notes for future revisions.
4. Trim and finish the blades, feeding discoveries back into the technique pages as refinements.

## Results
### Size targets
- Placeholder: document blade length, width at the foot pocket, and trailing edge taper once prototypes are cut.

### Flex notes
- Placeholder: summarise measured deflection, bend profile, and any rider feedback compared with predictions.

## Testing Notes
- Placeholder: record pool and open-water impressions, durability observations, and next steps for iteration.

## Version references
{{ versions_table("projects/short-fins") }}
