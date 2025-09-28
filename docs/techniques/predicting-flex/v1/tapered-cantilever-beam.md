---
status: research
estimated_cost:
  - amount: 0
    currency: GBP
    region: UK
time_to_implement: 1
waiting_time: 0
---
# {{ parent_child_title() }}
{{ status_banner() }}

## Goal

Estimate deflection and curvature profiles for a planned blade using simple inputs such as length, taper, and modulus,
allowing iterative layup adjustments without material usage.

The process involves dividing the blade into many small slices, calculating the bending contribution of each slice based
on layer thickness, and summing these contributions to determine the overall deflection. The applied load is adjusted
until the tip reaches the desired angle, after which SVG visualizations and inertia values are generated.

The calculations follow Euler–Bernoulli beam theory principles. You can explore cantilever beam
calculations [here](https://calcresource.com/statics-cantilever-beam.html).


## Calculator
{{ flex_predictor_embed() }}

## Limitations

- Simplifies the fin as a tapered Euler–Bernoulli beam, which may not capture all real-world complexities.
- Approximates the values for E (modulus) and I (moment of inertia), making precise computation challenging.
