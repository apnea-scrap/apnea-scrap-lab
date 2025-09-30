---
status: active
techniques:
  - title: Foot pockets
    focus: Choosing the foot pockets
    path: techniques/choosing-bifin-footpockets/v1/short-rails.md
  - title: Base Support
    focus: Creating a laminating base
    path: techniques/creating-laminating-base/v1/wood-support.md
  - title: Laminating Carbon
    focus: Creating the carbon laminate
    path: techniques/laminating-carbon/v1/wet-layup.md
  - title: Vacuum Bagging
    focus: Reducing the resin percentage of the laminate
    path: techniques/vacuum-bagging-carbon/v1/enclosed-bagging.md
  - title: Cutting Cured Carbon
    focus: Producing the final shape
    path: techniques/vacuum-bagging-carbon/v1/enclosed-bagging.md
  - title: Finishing Carbon
    focus: Finishing the carbon laminate surface
    path: techniques/finishing-carbon/v1/epoxy-and-clear-coat.md
  - title: Gluing Fin Rails 
    focus: Gluing Fin Rails
    path: techniques/gluing-fin-rails/v1/two-part-plastic-carbon-adhesive.md

---

---
# {{ parent_child_title() }}
{{ status_banner() }}

Early outline for producing compact training fins with predictable flex and repeatable templates.

## Planning the laminate layers
- Capture preliminary layup ideas using the [Manual wet layup stack](../../../techniques/laminating-carbon/v1/wet-layup.md) technique.
- Record fabric weights, orientations, and any taper adjustments needed for short blades.
- Note resin targets so we can compare against the predicted flex results later.

## Estimating flex
- Start with the [Flex predictor modelling](../../../techniques/predicting-flex/v1/tapered-cantilever-beam.md) calculator to estimate the target tip deflection.
- Plug in the tentative laminate schedule and iterate until the simulated stiffness matches the desired feel.
- Add comments for expected body weight range or training scenarios this setup should support.

## Planning the cutting sheet
- Reference the [Laminated paper cutting template](../../../techniques/cutting-template/v1/paper-laminate.md) to prepare blade outlines.
- Jot down quantities for each size variant and how they fit on the raw carbon sheets.
- Capture trimming allowances so the cured laminate nests cleanly within the template.

## Bill of Materials
{{ render_technique_requirements("bill_of_materials") }}

## Tools Required
{{ render_technique_requirements("tools") }}

## Instructions
1. Build or update the cutting template using the steps from [Laminated paper cutting template](../../../techniques/cutting-template/v1/paper-laminate.md).
2. Simulate the layup in [Flex predictor modelling](../../../techniques/predicting-flex/v1/tapered-cantilever-beam.md) and lock in the target flex window.
3. Execute the laminate following [Manual wet layup stack](../../../techniques/laminating-carbon/v1/wet-layup.md), capturing cure notes for future revisions.
4. Trim and finish the blades, feeding discoveries back into the technique pages as refinements.

## Results
### Size targets
- Placeholder: document blade length, width at the foot pocket, and trailing edge taper once prototypes are cut.

### Flex notes
- Placeholder: summarise measured deflection, bend profile, and any rider feedback compared with predictions.

## Testing Notes
- Placeholder: record pool and open-water impressions, durability observations, and next steps for iteration.
