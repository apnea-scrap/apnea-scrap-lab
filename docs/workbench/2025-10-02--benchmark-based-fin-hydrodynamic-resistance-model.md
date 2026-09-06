# Benchmark-Based Fin Hydrodynamic Resistance Model

## Context

The goal was to develop a simple way to compare the hydrodynamic resistance of fin designs, especially blades with different lengths and bending profiles.

The exploration began with absolute drag estimates for flat plates at different angles. It then considered changing blade length, representing a flexible blade by its root and tip angles, integrating resistance across the blade, inverse design searches, graphs and torque. Absolute velocity-based results became confusing, so the adopted direction was a relative benchmark model.

## Final approach

It works by splitting the fin into slices, figuring out how much each slice pushes on the water based on its angle, and then adding everything together. It uses a small training fin as the benchmark — 1 unit of resistance — so any other fin is just measured as a multiple of that.

The benchmark is:

- Width: 150 mm.
- Length: 100 mm.
- Hydrodynamic resistance: 1 unit.

For another blade:

1. Interpolate the local angle between the root and tip along the blade.
2. Calculate a projected-resistance contribution for each slice.
3. Sum the slices.
4. Divide the result by the result for the benchmark blade.

This produces a dimensionless comparison such as `2.5 units`, meaning that the model assigns the blade 2.5 times the resistance of the benchmark under equivalent assumed conditions.

## Design evolution

- The first model treated the blade as a rigid flat plate at one angle.
- The angle convention was reversed during the discussion to describe bending over the course of a kick.
- A flexible blade was then represented by root and tip angles with linear interpolation between them.
- The blade was divided into small slices so that local contributions could be integrated across its surface.
- Calculators were proposed for total drag, inverse searches for length-and-tip-angle combinations, plotted solutions and joint torque.
- Torque was explicitly removed from the final summary.
- Absolute force and velocity scaling were replaced by the relative benchmark.

## Editorial notes and limitations

- The final implementation must define its angle convention explicitly because the conversation used more than one convention.
- The drag-coefficient interpolation and linear root-to-tip bend profile were modelling assumptions, not validated measurements.
- The relative score compares geometry under equivalent assumed conditions; it does not predict force in newtons.
- The JavaScript calculators were intermediate prototypes, not an adopted implementation.
- The discussion of ankle, knee and hip torque was removed from the adopted approach.
- No comparison against measured fin resistance or perceived in-water effort was reported.
