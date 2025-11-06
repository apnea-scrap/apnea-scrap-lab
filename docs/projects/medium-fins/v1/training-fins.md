---
status: concept
techniques:
  - title: Foot pockets
    focus: Choosing the foot pockets
    path: techniques/choosing-bifin-footpockets/v1/short-rails.md
  - title: Base Support
    focus: Creating a laminating base
    path: techniques/creating-laminating-base/v3/cardboard-support.md
  - title: Laminating Carbon
    focus: Creating the carbon laminate
    path: techniques/laminating-carbon/v1/wet-layup.md
    consumable_scaling_factor: 3
  - title: Vacuum Bagging
    focus: Reducing the resin percentage of the laminate
    path: techniques/vacuum-bagging-carbon/v2/edge-sealed-bagging.md
  - title: Cutting Cured Carbon
    focus: Producing the final shape
    path: techniques/cutting-cured-carbon/v1/junior-hacksaw.md
  - title: Finishing Carbon
    focus: Finishing the carbon laminate surface
    path: techniques/finishing-carbon/v1/epoxy-and-clear-coat.md
  - title: Gluing Fin Rails
    focus: Gluing Fin Rails
    path: techniques/gluing-fin-rails/v2/marine-adhesive.md

---

---
# {{ parent_child_title() }}
{{ status_banner() }}

Medium training fins, short enough to fit in the gym bag but long enough to have proper water resistance.

## Planning

### Foot pockets ready
Make sure your foot pockets are on hand before you start. If you still need to choose a pair, follow the steps in [Choosing the foot pockets](../../../techniques/choosing-bifin-footpockets/v1/short-rails.md). Once the pockets are sorted, lay out a fresh cutting template with [Laminated paper cutting template](../../../techniques/cutting-template/v1/paper-laminate.md).

**Heads-up:** The dimensions below assume 170 mm of blade will slide into the foot pocket. Measure your pockets to confirm before cutting.

### Specifications / Dimensions
Target outline for each blade:

- **Width:** 18 cm
- **Total length:** 17 cm + 43 cm = 60 cm
    - 0–17 cm: inside the foot pocket (flat section)
    - 17–60 cm: free blade to the trailing edge

#### Layer schedule (one blade)
- Reserve 17 cm from the heel line for the bend zone.
- Layer 1: 20 cm × 60 cm
- Layer 2: 20 cm × 35 cm
- Layer 3: 20 cm × 45 cm
- Layer 4: 20 cm × 60 cm top ply


| ![Expanded Laminate View](expanded.svg) | ![Laminate Thickness Profile](thickness.svg) |
|-----------------------------------------|----------------------------------------------|
| Expanded Laminate View                  | Laminate Thickness Profile                   |


#### Cutting plan

|  | ![Cutting plan for both blades](cutting_plan.svg) |  |
|--|---------------------------------------------------|--|
|  | Cutting plan for both blades                      |  |

### Estimating the flex
Start with the [Flex predictor modelling](../../../techniques/predicting-flex/v1/tapered-cantilever-beam.md) workflow to sanity-check the layup. Adjust the layer stack and bend allowance until the predicted deflection matches your training goal.

| ![Bending Calculation](bending_calculation.png) | ![Bending Profile](bending_profile.png) |
|-------------------------------------------------|-----------------------------------------|
| Bending Calculation                             | Bending Profile                         |


Predicted:

- Load required for 90° = 10.4 N (1.06 kg)
- Hydrodynamic resistance score  5N = 3.41 units
- Hydrodynamic resistance score 10N = 2.16 units

The predicted code for this fin would be (see [hydrodynamic resistance codes](../../../techniques/encoding-fin-properties/v1/hydrodynamic-resistance-codes.md)): 
```
C430-T10-R34-F13
```

## Reference images

| ![Base Preparation and Seall](mf_base_seal.jpeg) | ![Base Ready](mf_base_ready.jpeg)   |
|--------------------------------------------------|-------------------------------------|
| Base Preparation and Seal                        | Base Ready                          |

| ![Carbon Cloth](mf_carbon_sheet.jpeg) | ![Carbon Layers](mf_carbon_cutouts.jpeg) |
|---------------------------------------|------------------------------------------|
| Carbon Cloth                          | Carbon Layers                            |

| ![Wet Carbon Laminate](mf_wet_laminate.jpeg) | ![Cured Carbon Laminate](mf_cured_laminate.jpeg) |
|----------------------------------------------|--------------------------------------------------|
| Wet Carbon Laminate                          | Cured Carbon Laminate                            |

| ![Cut Carbon To Shape](mf_prep_the_cut.jpeg) | ![Glued Rails](mf_glued_rails.jpeg) |
|----------------------------------------------|-------------------------------------|
| Cut Carbon To Shape                          | Glued Rails                         |

| ![Footpockets](mf_footpockets.jpeg) | ![Complete fins](mf_complete_fins.jpeg)          |
|-------------------------------------|---------------|
| Footpockets                         | Complete fins |



## Time needed

{{ render_project_time_breakdown() }}

## Bill of Materials
{{ render_technique_requirements_bill_of_materials() }}

## Tools Required
{{ render_technique_requirements_tools() }}

## Instructions
1. Build a 1000 mm × 600 mm laminating base following [Creating a laminating base](../../../techniques/creating-laminating-base/v3/cardboard-support.md) so both blades can be laminated at the same time.
2. Lay up the carbon according to the schedule above, using the steps in [Manual wet layup stack](../../../techniques/laminating-carbon/v1/wet-layup.md).
3. Pull the stack under vacuum to tighten the fiber volume, referencing [Edge-sealed bagging](../../../techniques/vacuum-bagging-carbon/v2/edge-sealed-bagging.md).
4. Trim the cured laminate to the template with the [Junior hacksaw method](../../../techniques/cutting-cured-carbon/v1/junior-hacksaw.md).
5. Seal the surface with the approach in [Epoxy and clear coat finish](../../../techniques/finishing-carbon/v1/epoxy-and-clear-coat.md).
6. Bond the rails using the guidance in [Marine adhesive](../../../techniques/gluing-fin-rails/v2/marine-adhesive.md).

## Results

### Desired vs Predicted vs Actual

I've recorded the flex using the [Kitchen Scale Test](../../../techniques/measuring-flex/v2/kitchen-scale-test.md).

|                     | Desired | Actual | Notes                                         |
|---------------------|---------|--------|-----------------------------------------------|
| Free blade size     | 430mm   | 410mm  | Ok                                            |
| Blade width         | 180mm   | 190mm  | Ok                                            |
| Load for 90 degrees | 1.1kg   | 1.4kg  | Smaller blade and maybe the rails add tension |

### Water trial

Overall the fins performed pretty well:
- feels good with hip-driven movements
- feels heavier (expected) than the Power Fins but lighter (expected) than full-length carbon blades
- the blade felt soft in the water, the fin was bending gradually with the kick

|                     | Desired    | Actual     | Notes             |
|---------------------|------------|------------|-------------------|
| Hydro resistance    | ~3.4 units | ~3.4 units | feels about right |

Plugging the numbers into the [Flex calculator](../../../techniques/predicting-flex/v1/tapered-cantilever-beam.md), I get the following numbers:

- Hydrodynamic resistance score  5N = 3.66 units
- Hydrodynamic resistance score 10N = 2.32 units

Judging from the above, the code for this turned out to be (see [hydrodynamic resistance codes](../../../techniques/encoding-fin-properties/v1/hydrodynamic-resistance-codes.md)): 
```
C410-T14-R36-F13
```
