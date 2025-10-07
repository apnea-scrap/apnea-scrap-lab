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
    consumable_scaling_factor: 2
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
    - 17–25 cm: transition and bend within the rails
    - 25–60 cm: free blade to the trailing edge

#### Layer schedule (one blade)
- Reserve 17 cm from the heel line for the bend zone.
- Layer 1: 20 cm × 60 cm
- Layer 2: 20 cm × 25 cm
- Layer 3: 20 cm × 45 cm
- Layer 4: 20 cm × 60 cm top ply


| TODO                   | TODO |
|------------------------|----------------------------------------------|
| Expanded Laminate View | Laminate Thickness Profile                   |

#### Cutting plan

|  | TODO |  |
|--|-------------------------------------------------|--|
|  | Cutting plan for one blade                      |  |

### Estimating the flex
Start with the [Flex predictor modelling](../../../techniques/predicting-flex/v1/tapered-cantilever-beam.md) workflow to sanity-check the layup. Adjust the layer stack and bend allowance until the predicted deflection matches your training goal.

| TODO | TODO |
|-------------------------------------------------|-----------------------------------------|
| Bending Calculation                             | Bending Profile                         |


Predicted:

- Load required for 90° = 35.3 N (3.60 kg)
- Hydrodynamic resistance score  5N = 2.71 units
- Hydrodynamic resistance score 10N = 2.38 units

The predicted code for this fin would be (see [hydrodynamic resistance codes](../../../techniques/encoding-fin-properties/v1/hydrodynamic-resistance-codes.md)): 
```
C250-T35-R27-F03
```

## Reference images

| TODO |TODO |
|-------------------------------------|-------------------------------------------|
| Footpockets                         | Cured Laminate                       |

| TODO | TODO |
|---------------------------------|-------------------------------|
| Complete fins                   | Nice and compact              |


## Time needed

{{ render_project_time_breakdown() }}

## Bill of Materials
{{ render_technique_requirements_bill_of_materials() }}

## Tools Required
{{ render_technique_requirements_tools() }}

## Instructions
1. Build a 500 mm × 300 mm laminating base following [Creating a laminating base](../../../techniques/creating-laminating-base/v3/cardboard-support.md) so one blade can be laminated at a time.
2. Lay up the carbon according to the schedule above, using the steps in [Manual wet layup stack](../../../techniques/laminating-carbon/v1/wet-layup.md).
3. Pull the stack under vacuum to tighten the fiber volume, referencing [Edge-sealed bagging](../../../techniques/vacuum-bagging-carbon/v2/edge-sealed-bagging.md).
4. Trim the cured laminate to the template with the [Junior hacksaw method](../../../techniques/cutting-cured-carbon/v1/junior-hacksaw.md).
5. Seal the surface with the approach in [Epoxy and clear coat finish](../../../techniques/finishing-carbon/v1/epoxy-and-clear-coat.md).
6. Bond the rails using the guidance in [Marine adhesive](../../../techniques/gluing-fin-rails/v2/marine-adhesive.md).

## Results

### Desired vs Predicted vs Actual

I've recorded the flex using the [Kitchen Scale Test](../../../techniques/measuring-flex/v2/kitchen-scale-test.md).

|                     | Desired  | Actual | Notes                                                                                          |
|---------------------|----------|--------|------------------------------------------------------------------------------------------------|
| Free blade size     | TODO    | TODO   |                                                           |
| Load for 90 degrees | TODO    | TODO  |       |

### Water trial

Overall the fins performed pretty well but favour a particular style of kicking:

- feels lighter than Cressi Clio 
- slightly heavier than swim training fins 
- sprinting feels good as that engages the blade properly
- feels too light (low surface area) for slow, hip-driven movements

|                     | Desired    | Actual |
|---------------------|------------|--------|
| Hydro resistance    | ~2.7 units | 2?     |

Plugging the numbers into the [Flex calculator](../../../techniques/predicting-flex/v1/tapered-cantilever-beam.md), I get the following numbers:

- Hydrodynamic resistance score  5N = 2.54 units
- Hydrodynamic resistance score 10N = 2.30 units

Judging from the above, the code for this turned out to be (see [hydrodynamic resistance codes](../../../techniques/encoding-fin-properties/v1/hydrodynamic-resistance-codes.md)): 
```
C230-T50-R25-F02
```
