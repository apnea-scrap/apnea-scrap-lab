# Balloon threshold indicator for mild vacuum bagging

## Context

The DIY carbon-fin layup needed a cheap way to confirm pressure inside an already sealed, transparent vacuum bag. The measuring device itself needed to sit inside the bag, without an external hose.

The clarified target was an internal absolute pressure equal to approximately 80% of atmospheric pressure:

- about 81 kPa absolute when ambient pressure is 101.3 kPa;
- about -20 kPa gauge pressure; and
- about 6 inHg of vacuum.

This is a 20% reduction from atmospheric pressure, not “80% vacuum.”

## Final implemented design

The implemented indicator used:

- a transparent or visibly inspectable rigid plastic container inside the vacuum bag; and
- a sealed, partially inflated balloon inside that container.

As bag pressure fell, the gas trapped inside the balloon expanded. Its ambient starting volume was calculated so that the balloon filled the available container volume when the bag reached approximately 80% of atmospheric pressure.

The resulting device was a visible threshold indicator:

- balloon not yet filling the container: target pressure not yet reached;
- balloon just filling the container: approximately at the target; and
- balloon strongly constrained by the container: below the target pressure, without a quantitative reading of how far below.

This design removed the sliding seal and static-friction problem encountered in the syringe prototype.

## Idealised calculation

For approximately constant temperature, Boyle's law gives:

\[
P_1V_1=P_2V_2
\]

At the target:

\[
P_2=0.8P_1
\]

Therefore:

\[
V_2=\frac{P_1}{P_2}V_1=1.25V_1
\]

If the usable internal container volume is \(V_c\), and the balloon is intended to fill that volume at the target pressure, then the ideal ambient starting volume is:

\[
V_1=0.8V_c
\]

The calculation should use the measured ambient pressure as \(P_1\) when better accuracy is required, rather than assuming standard atmospheric pressure.

## Development history: internal syringe gauge

The conversation first developed a sealed Boyle-law syringe gauge. A capped syringe trapped a known air volume at ambient pressure, while its piston was exposed to bag pressure. At 80% atmospheric pressure, the predicted trapped volume was 1.25 times the starting volume:

- 5 mL would expand to 6.25 mL; and
- 10 mL would expand to 12.5 mL.

Several versions attempted to keep the bag film away from the moving plunger, including a cage, a second syringe barrel, and finally a free rubber piston with its plastic rod removed.

The physical test failed: friction between the available syringe barrel and rubber piston was too high for the mild pressure differential to move it reliably.

The generated syringe diagrams were ephemeral chat artifacts and are not preserved here.

## Why the syringe failed

The available driving force was:

\[
F=\Delta P A
\]

where \(\Delta P\) was only about 20 kPa and \(A\) was the piston area. Static friction, seal deformation, and hysteresis dominated the intended movement.

A narrower syringe would have produced more travel for the same volume change, but its smaller piston area would also have reduced the pressure force. The response discussed the increased travel without initially acknowledging this opposing effect.

Attempts to reduce friction with candle wax did not make the available syringes work. Later suggestions involving sanding seals, abrading barrels, drilled bleed holes, or wax mixed with olive oil were not adopted.

## Editorial notes

- A mechanical vacuum gauge placed wholly inside the bag will not necessarily show bag vacuum if its pressure port and reference side both experience bag pressure. It needs a sealed reference or an absolute-pressure mechanism.
- A capped syringe includes dead volume in its tip and cap; barrel markings alone do not give total trapped volume.
- Temperature affects both the syringe and balloon gas volumes during a warm cure.
- Millimetre-travel estimates based on assumed syringe bore dimensions were not reliable calibration values.
- Sanding a piston seal or barrel risks leakage, scratches, inconsistent friction, and poor repeatability.
- Vegetable oil was incorrectly described as universally inert, non-volatile, and harmless to rubber. It can oxidise, interact with some elastomers, migrate, and contaminate composite surfaces.
- Any grease, wax, oil, balloon treatment, or release contamination must remain isolated from the laminate and bonding surfaces.
- A balloon is not an ideal zero-tension membrane. Elastic tension, folds, wall thickness, shape, contact friction, and ageing shift the pressure at which it fills the container.
- Contact with the container changes the balloon's pressure-volume behaviour as the target is approached.

## Calibration and use

The implemented geometry can be calculated using the ideal gas relationship, but its actual threshold should be calibrated as an assembly:

1. Measure the usable container volume.
2. Establish the balloon's ambient starting volume.
3. Place the complete indicator in a test bag alongside a reference absolute-pressure gauge.
4. Reduce pressure slowly and record when the balloon first fills the intended container volume.
5. Adjust initial balloon fill until that event occurs at \(0.8P_1\).
6. Repeat the cycle to assess friction, hysteresis, leakage, and repeatability.
7. If curing above room temperature, calibrate or compensate at representative temperature.

## Outcome

The final implemented solution was the plastic-container and partially filled balloon indicator. It provided a cheap, visible indication that the bag had reached approximately 80% of atmospheric pressure, without requiring sliding seals, electronics, or an external pressure line.
