# Comparing Carbon and Fibreglass Fin Layups

## Context

The purpose was to compare the layups required for carbon and fibreglass fins. The working assumption was that a fibreglass fin would require more layers, or greater overall laminate thickness, to achieve bending stiffness comparable to a carbon fin.

A carbon-laminate modulus of approximately 32 GPa was used as the reference for estimating:

- the modulus of a comparable fibreglass laminate;
- how much thicker the fibreglass layup might need to be; and
- a practical, approximate carbon-to-fibreglass layer comparison.

## Response received

Representative fibre-level Young's moduli were given as approximately 70–80 GPa for E-glass, 85–95 GPa for S-glass, 230–250 GPa for standard-modulus carbon, 280–300 GPa for intermediate-modulus carbon, and 350–400+ GPa for high-modulus carbon.

The response proposed estimating laminate modulus with a rule of mixtures:

```text
E ≈ Vf Ef + (1 − Vf) Em
```

It then suggested applying a factor of roughly 0.5–0.65 to a woven or quasi-isotropic laminate relative to a unidirectional laminate. Using the reported carbon-laminate modulus as a reference, it estimated a comparable E-glass laminate at about 10 GPa and an S-glass laminate at about 12 GPa.

For equal bending stiffness, the response used the thickness relationship:

```text
h_glass / h_carbon = (E_carbon / E_glass)^(1/3)
```

This gave estimated thickness ratios of approximately 1.47 for E-glass and 1.39 for S-glass. The useful order-of-magnitude conclusion was that a fibreglass fin would need to be roughly 1.4–1.5 times as thick as the carbon laminate for similar bending stiffness, assuming comparable geometry and laminate behaviour.

The response also offered rough ply substitutions: about three E-glass plies for one carbon ply at equal ply thickness, or five to six E-glass plies for one carbon ply at equal fabric weight. It suggested starting experimentally by replacing two glass plies with one carbon ply. Additional suggestions included increasing fibre fraction through compaction, reducing weave crimp, using unidirectional reinforcement, and post-curing.

## Editorial notes

- The initial modulus table described fibre properties, not finished-laminate properties.
- A measured laminate modulus of 32 GPa does not determine its fibre volume fraction without knowing the fibre, resin, orientation, weave, and test method.
- The estimated glass modulus and 1.4–1.5 thickness ratio are useful only as order-of-magnitude comparisons.
- There is no universal carbon-to-glass ply conversion. The cured thickness, fabric weight, fibre orientation, resin fraction, and stacking sequence of both materials are required to turn the thickness comparison into a layer count.
- The proposed three-ply and five-to-six-ply substitutions are too configuration-dependent to treat as design rules.
- The suggestion to place carbon close to the laminate's neutral axis is not appropriate when the objective is bending stiffness. Reinforcement farther from the neutral axis contributes more strongly to bending stiffness. An outer glass layer could still be used as a sacrificial or impact-protection layer, with carbon positioned beneath it and away from the neutral axis.
- No replacement layup was reported as implemented.

## Unresolved inputs

- Carbon and fibreglass fabric weights, weaves, and fibre orientations.
- Cured thickness per ply and the intended stacking sequence.
- Resin system and fibre volume fraction.
- The source or measurement method for the 32 GPa carbon-laminate value.
- Desired fin thickness, flex profile, and loading direction.
