---
status: proven
techniques:
  - title: Foot pockets
    focus: Choosing the foot pockets
    path: techniques/choosing-bifin-footpockets/v1/short-rails.md
  - title: Base Support
    focus: Creating a laminating base
    path: techniques/creating-laminating-base/v4/plywood-corner-brace.md
  - title: Laminating Carbon
    focus: Creating the carbon laminate
    path: techniques/laminating-carbon/v1/wet-layup.md
    consumable_scaling_factor: 6
  - title: Vacuum Bagging
    focus: Reducing the resin percentage of the laminate
    path: techniques/vacuum-bagging-carbon/v1/enclosed-bagging.md
  - title: Cutting Cured Carbon
    focus: Producing the final shape
    path: techniques/cutting-cured-carbon/v1/junior-hacksaw.md
  - title: Finishing Carbon
    focus: Finishing the carbon laminate surface
    path: techniques/finishing-carbon/v2/clear-coat-and-acrylic-paint.md
  - title: Gluing Fin Rails
    focus: Gluing Fin Rails
    path: techniques/gluing-fin-rails/v3/two-part-plus-superglue.md

---

---
# {{ parent_child_title() }}
{{ status_banner() }}

Full-length competition fins, long and flexible to maximise efficiency.

## Planning

### Foot pockets ready
Make sure your foot pockets are on hand before you start. If you still need to choose a pair, follow the steps in [Choosing the foot pockets](../../../techniques/choosing-bifin-footpockets/v1/short-rails.md). Once the pockets are sorted, lay out a fresh cutting template with [Laminated paper cutting template](../../../techniques/cutting-template/v1/paper-laminate.md).

**Heads-up:** The dimensions below assume 170 mm of blade will slide into the foot pocket. Measure your pockets to confirm before cutting.

### Specifications / Dimensions
Target outline for each blade:

- **Width:** 18 cm
- **Total length:** 17 cm + 58 cm = 75 cm
    - 0–17 cm: inside the foot pocket (flat section)
    - 17–75 cm: free blade to the trailing edge

#### Layer schedule (one blade)

For this build I am going to be using a triangles to smooth the transition between the various thickness levels.

- Reserve 17 cm from the heel line for the bend zone.
- Layer 1: 20 cm × 80 cm
- Layer 2a: 20 cm × 80 cm half triangle
- Layer 2b: 20 cm × 80 cm the other half triangle
- Layer 3: 20 cm × 60 cm
- Layer 4: 20 cm × 40 cm
- Layer 5: 20 cm × 80 cm top ply


| ![Expanded Laminate View](expanded.svg) | ![Laminate Thickness Profile](thickness.svg) |
|-----------------------------------------|----------------------------------------------|
| Expanded Laminate View                  | Laminate Thickness Profile                   |


#### Cutting plan

|  | ![Cutting plan for one blade](cutting_plan.svg) | ![Cutting plan for one blade](cutting_plan.svg) |  |
|--|-------------------------------------------------|-------------------------------------------------|--|
|  | Cutting plan for first blade                    | Cutting plan for second blade (identical)       |  |

### Estimating the flex
Start with the [Flex predictor modelling](../../../techniques/predicting-flex/v1/tapered-cantilever-beam.md) workflow to sanity-check the layup. Adjust the layer stack and bend allowance until the predicted deflection matches your training goal.

Free blade length [mm]: 580
Blade width [mm]: 180
Layers at foot: 6
Layers at tip: 3
Min layer length [mm]: 150

| ![Bending Calculation](bending_calculation.png) | ![Bending Profile](bending_profile.png) |
|-------------------------------------------------|-----------------------------------------|
| Bending Calculation                             | Bending Profile                         |


Predicted:

- Load required for 90° = 16.7 N (1.70 kg)
- Hydrodynamic resistance score 5N = 5.71 units
- Hydrodynamic resistance score 10N = 4.32 units

The predicted code for this fin would be (see [hydrodynamic resistance codes](../../../techniques/encoding-fin-properties/v1/hydrodynamic-resistance-codes.md)): 
```
C580-T17-R57-F15
```

## Reference images

| ![Laminating Support](lf_base.jpeg) | ![Laminating Base](lf_base_and_epoxy.jpeg) |
|-------------------------------------|--------------------------------------------|
| Laminating Support                  | Laminating Base                                |

| ![Carbon Cloth](lf_cloth.jpeg) | ![Wet Laminate](lf_laminate.jpeg) |
|--------------------------------|-----------------------------------|
| Base Ready                     | Wet Laminate                      |

| ![Laminate Peel Ply](lf_laminate_ply.jpeg) | ![Vacuum Bagging](lf_vacuum.jpeg) |
|--------------------------------------------|-----------------------------------|
| Laminate Peel Ply                          | Vacuum Bagging                    |

| ![Prepping to Cut](lf_cutting_start.jpeg) | ![Cutting Done](lf_cutting_done.jpeg) |
|-------------------------------------------|---------------------------------------|
| Prepping to Cut                           | Cutting Done                          |

| ![Glueing Fin Rails](lf_glueing.jpeg) | ![Finishing Layer](lf_finishing.jpeg) |
|---------------------------------------|---------------------------------------|
| Glueing Fin Rails                     | Finishing Layer                       |

| ![Footpockets](lf_footpockets.png) | ![lf_final.jpeg](lf_final.jpeg)  |
|------------------------------------|----------------------------------|
| Footpockets                        | Complete Fins                    |

## Time needed

{{ render_project_time_breakdown() }}

## Bill of Materials
{{ render_technique_requirements_bill_of_materials() }}

## Tools Required
{{ render_technique_requirements_tools() }}

## Instructions
1. Build a 1000 mm × 600 mm laminating base following [Creating a laminating base](../../../techniques/creating-laminating-base/v4/plywood-corner-brace.md) so both blades can be laminated at the same time.
2. Lay up the carbon according to the schedule above, using the steps in [Manual wet layup stack](../../../techniques/laminating-carbon/v1/wet-layup.md).
3. Pull the stack under vacuum to tighten the fiber volume, referencing [Enclosed bagging](../../../techniques/vacuum-bagging-carbon/v1/enclosed-bagging.md).
4. Trim the cured laminate to the template with the [Junior hacksaw method](../../../techniques/cutting-cured-carbon/v1/junior-hacksaw.md).
5. Seal the surface with the approach in [Clear coat and acrylic paint](../../../techniques/finishing-carbon/v2/clear-coat-and-acrylic-paint.md).
6. Bond the rails using the guidance in [Two-part adhesive plus super glue](../../../techniques/gluing-fin-rails/v3/two-part-plus-superglue.md).

## Results

### Desired vs Predicted vs Actual

I've recorded the flex using the [Kitchen Scale Test](../../../techniques/measuring-flex/v2/kitchen-scale-test.md).

|                     | Desired | Predicted | Actual | Notes                                                      |
|---------------------|---------|-----------|--------|------------------------------------------------------------|
| Free blade size     | 580mm   | 580mm     | 580mm  | Matched                                                    |
| Blade width         | 180mm   | 180mm     | 180mm  | Matched                                                    |
| Load for 90 degrees | 1.2kg   | 1.70kg    | 1.30kg | Lower actual due to tapered cuts shifting bend to mid-blade |

### Water trial

Feels a bit soft but heavier than the training fins.

|                     | Desired | Actual | Notes                      |
|---------------------|---------|--------|----------------------------|
| Hydro resistance 5N | 5.0     | 5.0    | Soft but acceptable feel   |
| Hydro resistance 10N| 4.0     | 4.0    | Heavier than training fins |

Judging from the above, the code for this turned out to be (see [hydrodynamic resistance codes](../../../techniques/encoding-fin-properties/v1/hydrodynamic-resistance-codes.md)): 
```
C580-T13-R50-F10
```
