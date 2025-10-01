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
    consumable_scaling_factor: 2
  - title: Vacuum Bagging
    focus: Reducing the resin percentage of the laminate
    path: techniques/vacuum-bagging-carbon/v1/enclosed-bagging.md
  - title: Cutting Cured Carbon
    focus: Producing the final shape
    path: techniques/cutting-cured-carbon/v1/junior-hacksaw.md
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

## Planning

### Foot pockets ready
Make sure your foot pockets are on hand before you start. If you still need to choose a pair, follow the steps in [Choosing the foot pockets](../../../techniques/choosing-bifin-footpockets/v1/short-rails.md). Once the pockets are sorted, lay out a fresh cutting template with [Laminated paper cutting template](../../../techniques/cutting-template/v1/paper-laminate.md).

**Heads-up:** The dimensions below assume 150 mm of blade will slide into the foot pocket. Measure your pockets to confirm before cutting.

### Specifications / Dimensions
Target outline for each blade:

- **Width:** 18 cm
- **Total length:** 40 cm
    - 0–15 cm: inside the foot pocket (flat section)
    - 15–23 cm: transition and bend within the rails
    - 23–40 cm: free blade to the trailing edge

#### Layer schedule (one blade)
- Reserve 15 cm from the heel line for the bend zone.
- Layer 1: 20 cm × 40 cm
- Layer 2: 20 cm × 30 cm
- Layer 3: two strips at 10 cm × 40 cm each, running along the edges for rail reinforcement
- Layer 4: 20 cm × 40 cm top ply

_TODO: add thickness profile graphic_
_TODO: add laminate stack table_

#### Cutting plan
- _TODO: document full cutting plan for two blades_

### Estimating the flex
Start with the [Flex predictor modelling](../../../techniques/predicting-flex/v1/tapered-cantilever-beam.md) workflow to sanity-check the layup. Adjust the layer stack and bend allowance until the predicted deflection matches your training goal.

- _TODO: record bending moment targets_
- _TODO: capture free-blade bend profile once measured_

## Reference images
_TODO: add foot pocket reference photo_
_TODO: add laminate stack photo_
_TODO: add finished blade photo_

## Bill of Materials
{{ render_technique_requirements_bill_of_materials() }}

## Tools Required
{{ render_technique_requirements_tools() }}

## Instructions
1. Build a 500 mm × 300 mm laminating base following [Creating a laminating base](../../../techniques/creating-laminating-base/v1/wood-support.md) so one blade can be laminated at a time.
2. Lay up the carbon according to the schedule above, using the steps in [Manual wet layup stack](../../../techniques/laminating-carbon/v1/wet-layup.md).
3. Pull the stack under vacuum to tighten the fiber volume, referencing [Enclosed bagging](../../../techniques/vacuum-bagging-carbon/v1/enclosed-bagging.md).
4. Trim the cured laminate to the template with the [Junior hacksaw method](../../../techniques/cutting-cured-carbon/v1/junior-hacksaw.md).
5. Seal the surface with the approach in [Epoxy and clear coat finish](../../../techniques/finishing-carbon/v1/epoxy-and-clear-coat.md).
6. Bond the rails using the guidance in [Two-part plastic to carbon adhesive](../../../techniques/gluing-fin-rails/v1/two-part-plastic-carbon-adhesive.md).

## Results
### Dimensions
- _TODO: log actual finished width, length, and rail taper_

### Flex notes
Record measured deflection using the [Weight belt test](../../../techniques/measuring-flex/v1/weight-belt-test.md) once prototypes are complete.

_TODO: compare measured flex against the predictions_

