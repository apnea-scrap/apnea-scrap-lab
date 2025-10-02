---
title: 'Research Notes: Comparing Fin Hydrodynamic Kick Resistance'
date:
  created: 2025-10-30
  updated: 2025-10-30
authors:
- julian-g
categories:
- Research Notes
tags:
- Hydrodynamics
- Modeling
- Bifins
readtime: 6
summary: A simple, dimensionless framework for comparing how heavy different fins feel in the water.
links:
- Blade stiffness profiles: blog/posts/2025-09-28-blade-stiffness-profiles/index.md
- Flex predict calculator: blog/posts/2025-10-20-flex-predict-calculator/index.md
---

When I talk about how "heavy" a fin feels, what I'm really pointing at is the **hydrodynamic resistance** the blade builds as it sweeps through the water. The raw feeling is easy to notice, but hard to quantify. To make comparisons across builds, I pulled together a quick benchmark-based model so every fin gets an apples-to-apples resistance score.

<!-- more -->

## Step 1: Define the Benchmark

Start with a short training fin: **150 mm wide** and **100 mm long**, for a blade area of **0.015 m²**. That combination gets the baseline resistance score of **1.0 unit** at both the 5 N and 10 N test points.

This keeps the arithmetic friendly because everything else scales relative to the trainer blade.

## Step 2: Scale Other Fins Relative to the Baseline

In this simplified model the drag force \(F\) that a fin generates is proportional to three things:

1. **Area**: the square meters of blade the water "sees".
2. **Projected angle factor**: how much of that area is presented to the flow once the blade bends.
3. **Bend distribution**: where along the blade the flex concentrates.

The baseline handles the constants, so every fin boils down to a **relative resistance ratio**:

\[
R_\text{relative} = \frac{F_\text{fin}}{F_\text{benchmark}}
\]

Because the benchmark force \(F_\text{benchmark} = 1\), the ratio reads directly: a fin that generates twice the integrated force of the trainer comes out at **2.0 units**.

## Step 3: What the Ratio Buys Us

- **No velocity assumptions.** As long as we compare fins at the same kick speed, the water velocity cancels out of the math.
- **Dimensionless scores.** "This blade is 3× as heavy as a short trainer blade" is immediately understandable.
- **Design clarity.** Every experiment, whether you try longer carbon layups, different tapers, or alternative resins, boils down to a single comparable number.

## Step 4: Worked Example

Say you build a carbon bifin that measures **0.20 m wide** and **0.60 m long**. The blade area grows to **0.12 m²**. On area alone that's an **8.0× increase** over the benchmark.

Real blades bend. A long, soft carbon blade can feel about **5.0 units** right as the kick starts, but as the stroke continues and the blade folds, the effective resistance can relax to roughly **2.5 units**. That matches the in-water feel: heavier to initiate than a swim trainer, then quickly easing into the 2-3× range once the blade is moving.

## Resistance Table

The table below applies the same logic to a range of carbon layups and a couple of well-known polymer fins. The measurements capture two points in the kick cycle: **5 N** to show initial resistance, and **10 N** to show how much stiffness the blade hangs onto deeper in the stroke. The \(\Delta R\) column highlights how quickly the blade drops off between the two loads.

| Fin type | Notation | 5 N | 10 N | ΔR |
|----------|----------|-----|------|----|
| Swim training fin | (baseline) | 1.0 | 1.0 | 0.0 |
| Short fin 230 (4.5 kg) | C230-T45-R25-F02 | 2.5 | 2.3 | 0.2 |
| Medium 400 root (1.2 kg) | C400-T12-R29-F16 | 2.9 | 1.3 | 1.6 |
| Medium 400 mid (1.2 kg) | C400-T12-R34-F12 | 3.4 | 2.2 | 1.2 |
| Medium 400 tip (1.2 kg) | C400-T12-R37-F11 | 3.7 | 2.6 | 1.1 |
| Long 600 root (1.2 kg) | C600-T12-R45-F24 | 4.5 | 2.1 | 2.4 |
| Long 600 mid (1.2 kg) | C600-T12-R49-F20 | 4.9 | 2.9 | 2.0 |
| Long 600 tip (1.2 kg) | C600-T12-R55-F16 | 5.5 | 3.9 | 1.6 |
| CRESSI Clio fins | (not carbon) | 3.5 | 3.3 | 0.2 |
| Seac Sub Talent fins | (not carbon) | 6.3 | 6.1 | 0.2 |

**Legend**

- **C\<Length\>**: carbon blade with \<Length\> mm of free blade beyond the foot pocket.
- **T...**: tip load at a 90° bend, reported as kg ×10 (≈ newtons).
- **R...**: initiation resistance at 5 N (×10, no decimal).
- **F...**: flex drop defined as \(R_5 - R_{10}\) (×10, no decimal).

## How to Use the Numbers

- **Match training to goals.** Want to mimic a heavy competition blade? Hunt for ratios near **5-6 units**. Need technique reps without fatigue? Stay under **3 units**.
- **Link the feel between fins.** Pick a trainer with a resistance score close to your target long blade so every pool session reinforces the same kick effort you expect in open water.
- **Plan for flex drop.** Soft long blades often start around **5 units** at the first pulse but settle near **2-3 units** mid-stroke, like the long 600 root layout in the table. Pick the trainer that mirrors both the initial hit and the follow-through.
- **Tune prototypes.** If a test build lands too stiff, you now know how far to trim width or taper the layers to target a ratio.
- **Compare across materials.** The polymer fins show that softer plastics can still rival carbon blades on raw resistance when the area is large enough.

## Next Steps

The [flex prediction calculator](../2025-10-20-flex-predict-calculator/index.md) now rolls this resistance math into its bend-profile workflow, so you can estimate hydrodynamic resistance straight from a flex test. From here I want to collect more field notes to see how closely the ratios track perceived effort across different divers.
