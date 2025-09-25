---
title: 'Research Notes: Blade Stiffness and Profiles'
date:
  created: 2025-09-28
  updated: 2025-09-29
authors:
- julian-g
categories:
- Research Notes
tags:
- Blade Stiffness
- Design References
- Bifins
readtime: 3
summary: Quick reference on how tip load and bending profiles interact for bifin blades.
links:
- Measuring flex technique: techniques/measuring-flex/index.md
- Short fins project: projects/short-fins/index.md
- Future gear roadmap: projects/future-gear/index.md
---

I finally pulled together a quick reference for how **tip load** ("hardness") and **bending profile** play together on long freediving blades. The clearest explanation I have found so far comes from this breakdown: ▶️ [Blade stiffness explained](https://www.youtube.com/watch?v=P52S1Bxy0Mc).

<!-- more -->

The short version: two variables define how a blade feels in the water.

- **Load (tip stiffness in kg)** — how much weight it takes to bend the blade to **90°**.
- **Bending profile** — where the blade gives way once it reaches that load.

The [Fin Flex Comparison Chart](https://fishingbigisland.wordpress.com/2017/12/03/fin-flex-comparison-chart/) and its [stiffness plot](https://fishingbigisland.wordpress.com/wp-content/uploads/2017/12/finstiffness2.png) show fin stiffness spanning roughly **15–40 units of force** across the models compared.

Ninety degrees is the useful limit. After that the blade just folds over, stalls, and stops storing energy. Most long fins (XT Diving, C4, Leaderfins, etc.) fall in the **80–90 cm** length range, so that’s the baseline for comparing these values.

The nuance: fins that bend closer to the footpocket always feel softer—even if the tip load matches a “harder” blade. When the flex starts near your feet the blade unloads early, the water sheds faster, and the kick feels lighter. If the bend moves toward the tip, it holds shape longer and feels stiffer.

---

## Hardness vs. Profile Table

| Kg Tip Load | Type 1 | Type 2 | Type 3 | Type 4 | Type 5 |
|-------------|--------|--------|--------|--------|--------|
| 0.7 | X | X | X | X | SSS |
| 0.8 | X | X | SSS | SSS | SS |
| 0.9 | X | SSS | SS | SS | S |
| 1.0 | SSS | SS | S - SS | S | MS |
| 1.1 | SS | S | S | MS | M |
| 1.2 | S | S - MS | MS | M | M - MH |
| 1.3 | MS | MS - M | MS - M | MH | H |
| 1.4 | M | M | M | H | HH |
| 1.5 | M | MH | MH | HH | HHH |
| 1.6 | MH | H | H | HHH | X |
| 1.7 | H | HH | HH | X | X |
| 1.8 | H | HH | X | X | X |

Legend: SSS = very soft, SS = soft, S = slightly soft, MS = medium soft, M = medium, MH = medium hard, H = hard, HH/HHH = very hard, X = not recommended.

---

## Technique Notes

Profiles **1, 2, and 3** reward **short, hip-driven kicks with a small amplitude**. Overkicking just pushes them beyond the 90° sweet spot and you lose efficiency. Profiles **4 and 5** hang onto stiffness longer, so they tolerate larger kicks before collapsing.

![Finning techniques chart from XT Diving](https://xtdiving.com/wp-content/uploads/2023/08/Choosing-Finning-Techniques_1.jpg)

For training, I’m leaning toward the softer profiles paired with a **0.9–1.1 kg** tip load. They feel forgiving, still snap back cleanly, and keep the effort focused on clean technique instead of raw leg power.
