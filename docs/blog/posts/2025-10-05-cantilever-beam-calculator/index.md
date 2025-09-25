---
title: 'Research Notes: Playing With Cantilever Beam Calculator for Fin Blades'
date:
  created: 2025-10-05
  updated: 2025-10-06
authors:
- julian-g
categories:
- Research Notes
tags:
- Modeling
- Blade Mechanics
- Carbon Layup
readtime: 2
summary: Sanity-checking how a simple cantilever beam model compares to real freediving
  fin blades.
links:
- Measuring flex technique: techniques/measuring-flex/index.md
- Cantilever calculator notebook: projects/short-fins/index.md
- Creating laminating base technique: techniques/creating-laminating-base/index.md
---

I wanted to see how a simple cantilever beam model matches what happens with freediving fins. The idea is that a fin blade is essentially a thin rectangular beam clamped at the footpocket and loaded at the tip by the force of the water.

<!-- more -->

---

### Young’s modulus
- **Prepreg sheet ([Easy Composites high-strength carbon fibre sheet](https://www.easycomposites.co.uk/high-strength-carbon-fibre-sheet)):** ~32.4 GPa
- **Wet layup + vacuum bagging:** 20–40 GPa, depending on resin content and fibre fraction
    - More resin → lower \(E\)
    - Better fibre alignment and compaction → higher \(E\)

---

### Moment of inertia \(I\)
For a rectangular section:

$$
I = \frac{b h^{3}}{12}
$$

- Blade width: \(b = 180\,\text{mm}\)
- Thickness (3 layers @ 0.31 mm each): \(h = 0.93\,\text{mm}\)

$$
I \approx 12.1\,\text{mm}^4
$$

⚠️ This assumes **uniform thickness** along the length. Real fins are tapered, so actual \(I(x)\) varies with position.

---

### Cantilever beam calculator inputs
Using the [online cantilever calculator](https://calcresource.com/statics-cantilever-beam.html):

- **Structure**
    - Length \(L = 250\,\text{mm}\)
    - Elastic modulus \(E = 32\,\text{GPa} = 32{,}000\,\text{N/mm}^2\)
    - Moment of inertia \(I = 12\,\text{mm}^4\)
- **Imposed loading**
    - Point load at tip
    - \(P = 2\,\text{kg}\)

---

### Results
- Tip slope: ~–91°

---

### Takeaway
With only 2 kg load at the tip, the test piece bends almost to a right angle. This matches freediving practice: once a fin bends to ~90°, extra load doesn’t increase thrust, because the blade is already “giving way” to the water.

This simple cantilever model helps build some intuition into how many layers are needed to achieve a desired stiffness.
