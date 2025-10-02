---
status: research
---
# {{ parent_child_title() }}
{{ status_banner() }}

## Goal

Estimate deflection and curvature profiles for a planned blade using simple inputs such as length, taper, and modulus,
allowing iterative layup adjustments without material usage.

The technique relies on two main computations:

### Bending analysis

The process involves dividing the blade into many small slices, calculating the bending contribution of each slice based
on layer thickness, and summing these contributions to determine the overall deflection. The applied load is adjusted
until the tip reaches the desired angle, after which SVG visualizations and inertia values are generated.

### Hydrodynamic resistance score

The hydrodynamic resistance estimate follows the same slicing approach. Each slice contributes a push on the water based
on its local angle, and the model adds those contributions together to get a total resistance figure. A small training
fin is used as the benchmark: its resistance is defined as one unit, so any other fin is reported as a multiple of that
baseline score.

The calculations follow Euler–Bernoulli beam theory principles. You can explore cantilever beam
calculations [here](https://calcresource.com/statics-cantilever-beam.html).


## Calculator
{{ flex_predictor_embed() }}

## Limitations

- Simplifies the fin as a tapered Euler–Bernoulli beam, which may not capture all real-world complexities.
- Approximates the values for E (modulus) and I (moment of inertia), making precise computation challenging.
