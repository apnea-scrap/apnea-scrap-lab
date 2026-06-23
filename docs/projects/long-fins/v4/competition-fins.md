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
    path: techniques/laminating-carbon/v2/wet-layup-1250mm-cloth.md
    consumable_scaling_factor: 2
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

Full-length competition fins tuned to the extra-stiff side for a stronger kick response.
This v4 builds on the stiff v3 concept with the updated layup and 1250 mm carbon cloth plan.

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

- Reserve 20 cm (17+3cm tolerance) from the heel line for the bend zone.
- Layer 1: 20 cm × 80 cm
- Layer 2a: 20 cm × 80 cm half triangle
- Layer 2b: 20 cm × 80 cm the other half triangle
- Layer 3: 20 cm x 80(-35) ^ mid shape triangle
- Layer 4: 20 cm x 75(-15) V side shape
- Layer 5: 20 cm x 55(-10) V side shape
- Layer 6: 20 cm x 45(-10) V side shape
- Layer 7: 20 cm x 35(-10) V side shape
- Layer 8: 20 cm × 80 cm top ply


| ![Expanded Laminate View](expanded.svg)  | ![Laminate Thickness Profile](thickness.svg) |
|------------------------------------------|----------------------------------------------|
| Expanded Laminate View                   | Laminate Thickness Profile                   |


#### Cutting plan

|  | ![Cutting plan for both blades](cutting_plan.svg) |  |
|--|---------------------------------------------------|--|
|  | Cutting plan for both blades                      |  |

### Estimating the flex
Start with the [Flex predictor modelling](../../../techniques/predicting-flex/v1/tapered-cantilever-beam.md) workflow to sanity-check the layup. Adjust the layer stack and bend allowance until the predicted deflection matches your training goal.

Free blade length [mm]: 580
Blade width [mm]: 180
Layers at foot: 8
Layers at tip: 2
Min layer length [mm]: 100

| ![Bending Calculation](bending_calculation.png) | ![Bending Profile](bending_profile.png) |
|-------------------------------------------------|-----------------------------------------|
| Bending Calculation                             | Bending Profile                         |

Note: In the real blade, the actual bending point will move toward mid-blade. We are cutting out triangles to push more stiffness toward the foot.

Predicted:

- Load required for 90° = 17.8 N (1.82 kg)
- Hydrodynamic resistance score 5N = 6.14 units
- Hydrodynamic resistance score 10N = 5.22 units
- Hydrodynamic resistance score MaxLoad = 4.00 units

The predicted code for this fin would be (see [hydrodynamic resistance codes](../../../techniques/encoding-fin-properties/v1/hydrodynamic-resistance-codes.md)): 
```
C580-18-R61-F10
```

## Reference images

| ![Laminating Support](lf_base.jpeg) | ![Laminating Base](lf_base_and_epoxy.jpeg) |
|-------------------------------------|--------------------------------------------|
| Laminating Support                  | Laminating Base                            |

| ![Carbon Cloth](lf_cloth.jpeg) | ![Cutting Carbon Cloth](v4-cutting-cloth.png) |
|--------------------------------|-----------------------------------------------|
| Carbon Cloth                   | Cutting Carbon Cloth                          |

| ![Wet Laminate](lf_laminate.jpeg) | ![Extra Stiff Layer Stack](v4-layers.png) |
|-----------------------------------|-------------------------------------------|
| Wet Laminate                      | Extra Stiff Layer Stack                   |

| ![Laminate Peel Ply](lf_laminate_ply.jpeg) | ![Vacuum Bagging](lf_vacuum.jpeg) |
|--------------------------------------------|-----------------------------------|
| Laminate Peel Ply                          | Vacuum Bagging                    |

| ![Prepping to Cut](lf_cutting_start.jpeg) | ![Cutting Done](lf_cutting_done.jpeg) |
|-------------------------------------------|---------------------------------------|
| Prepping to Cut                           | Cutting Done                          |

| ![Footpockets](lf_footpockets.png) | ![Glueing Fin Rails](lf_glueing.jpeg) |
|------------------------------------|---------------------------------------|
| Footpockets                        | Glueing Fin Rails                     |

| | ![Finished Extra Stiff Competition Fins](v4-final.png) |  |
|-|--------------------------------------------------------|--|
| | Finished Extra Stiff Competition Fins                  |  |

## Time needed

{{ render_project_time_breakdown() }}

## Bill of Materials
{{ render_technique_requirements_bill_of_materials() }}

## Tools Required
{{ render_technique_requirements_tools() }}

## Instructions
1. Build a 1000 mm × 600 mm laminating base following [Creating a laminating base](../../../techniques/creating-laminating-base/v4/plywood-corner-brace.md) so both blades can be laminated at the same time.
2. Lay up the carbon according to the schedule above, using the steps in [1250 mm cloth wet layup stack](../../../techniques/laminating-carbon/v2/wet-layup-1250mm-cloth.md).
3. Pull the stack under vacuum to tighten the fiber volume, referencing [Enclosed bagging](../../../techniques/vacuum-bagging-carbon/v1/enclosed-bagging.md).
4. Trim the cured laminate to the template with the [Junior hacksaw method](../../../techniques/cutting-cured-carbon/v1/junior-hacksaw.md).
5. Seal the surface with the approach in [Clear coat and acrylic paint](../../../techniques/finishing-carbon/v2/clear-coat-and-acrylic-paint.md).
6. Bond the rails using the guidance in [Two-part adhesive plus super glue](../../../techniques/gluing-fin-rails/v3/two-part-plus-superglue.md).

## Results

### Desired vs Predicted vs Actual

Record the flex after fabrication using the [Kitchen Scale Test](../../../techniques/measuring-flex/v2/kitchen-scale-test.md).

|                     | Desired   | Predicted  | Actual | Notes                                                                                |
|---------------------|-----------|------------|--------|--------------------------------------------------------------------------------------|
| Free blade size     | 580mm     | 580mm      | 580mm  | Matched                                                                              |
| Blade width         | 180mm     | 180mm      | 180mm  | Matched                                                                              |
| Load for 90 degrees | 1.8-2.0kg | 1.82kg     | 2.8kg  | Proper stiff, had issues with the vacuum, laminated during high external temperature |

### Water trial

Felt much stiffer than expected, the fins where delivering good power into the water, kick from the hip.
But it was hard to turn with them in the pool, this is because they where not bending when retrieving the legs.s

|                     | Desired | Actual | Notes                                                                   |
|---------------------|---------|--------|-------------------------------------------------------------------------|
| Hydro resistance 5N | 5.0     | 6.0    | Very stiff in the water, the feel got close to the Seac Sub Talent fins |
| Hydro resistance 10N| 4.0     | 5.5    | The fins where only bending under high load                             |

Final code after build and testing (see [hydrodynamic resistance codes](../../../techniques/encoding-fin-properties/v1/hydrodynamic-resistance-codes.md)): 
```
C580-T28-R60-F05
```
