---
status: proven
time_to_implement: 0.25
waiting_time: 0
---
# {{ parent_child_title() }}
{{ status_banner() }}

## Goal
Create a repeatable four-field code that captures fin length, tip stiffness, and hydrodynamic resistance so different blades can be compared at a glance.

## Time needed

{{ render_technique_time_overview() }}

## Inputs to capture
- Free blade length beyond the pocket shoulder (mm)
- Tip load that holds the blade at a 90° bend (kg)
- Hydrodynamic resistance score at **5 N** kickoff load
- Hydrodynamic resistance score at **10 N** follow-through load

The resistance scores come from the benchmark model in the research note on [hydrodynamic kick resistance](../../../blog/posts/2025-10-30-fin-hydrodynamic-resistance/index.md). The short training fin (150 mm × 100 mm, 0.015 m²) is fixed at **1.0 unit** at both loads; any other blade is reported as a multiple of that benchmark.

## Code structure

| Field | Format | What it captures | How to calculate | Example |
|-------|--------|------------------|------------------|---------|
| `C###` | Three digits | Free blade length in millimetres | Measure shoulder-to-tip distance and round to the nearest 10 mm | `C600` → 600 mm free blade |
| `T##` | Two digits | Tip load at 90° bend (kg ×10) | Weigh the mass that keeps the tip vertical; multiply kg by 10 and round | `T12` → 1.2 kg tip load |
| `R##` | Two digits | Relative resistance at 5N (×10) | Compute \(R_{5N}\); multiply by 10 and round | `R49` → 4.9 units at 5 N |
| `F##` | Two digits | Resistance drop between 5N and 10 N (×10) | \(F = R_{5N} - R_{10N}\); ensure minimum of 0, multiply by 10 and round | `F20` → drop of 2.0 units |

The final code concatenates the fields with hyphens: `C600-T12-R49-F20`.

## Instructions (step-by-step)

1. **Measure the free blade length**

    - Lay the blade flat and measure from the pocket shoulder to the tip.
    - Round to the nearest 10 mm to produce `C###`.

2. **Record the 90° tip load**

    - Use your flex rig (see the [measuring flex](../../measuring-flex/index.md) techniques) to find the weight that holds the tip vertical.
    - Convert the mass to kilograms, multiply by 10, round to the nearest whole number, and format as `T##`.

3. **Estimate resistance at 5 N and 10 N**

    - Use the hydrodynamic benchmark model (bench test or the [flex predictor tool](../../predicting-flex/v1/tapered-cantilever-beam.md)) to obtain the dimensionless resistance scores at 5 N and 10 N.

4. **Encode the hydrodynamic behaviour**

    - Multiply the 5 N score by 10, round to the nearest whole number, and format as `R##`.
    - Subtract the 10 N score from the 5 N score (bottoming out at zero), multiply the result by 10, round, and format as `F##`.

5. **Publish the code**

    - Join the four parts with hyphens.
    - Include the code alongside measurements, build notes, or test tables so others can compare builds quickly.

## Example

The long carbon blade that bends mid-span in the research note measured:

- Free blade length: 600 mm
- Tip load: 1.2 kg to reach 90°
- Resistance: 4.9 units at 5 N, 2.9 units at 10 N

Encoding:

```
C600-T12-R49-F20
```

## References
- [Research Notes: Comparing Fin Hydrodynamic Kick Resistance](../../../blog/posts/2025-10-30-fin-hydrodynamic-resistance/index.md)
