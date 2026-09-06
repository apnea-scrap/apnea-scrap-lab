# Mylar-Bag and Tube Vital-Capacity Meter

## Goal

Create a low-cost device for measuring the volume of one full exhalation using an inflatable reservoir that unfolds without the increasing elastic resistance of a balloon.

The intended measurement is vital capacity, not a complete spirometry flow profile.

## Selected concept

- Use a flexible Mylar bag with a valve.
- Place the bag inside a rigid plastic tube of constant cross-section.
- Use a sliding lid or follower above the bag.
- As the bag fills, or when the filled bag is compressed into a repeatable shape, it moves the follower along the tube.
- Read the follower position against a scale attached to the tube.

The conversation did not settle whether the bag should remain inside the tube while exhaling or be filled first and then placed under the follower.

## Calibration

The proposed one-time calibration was:

1. Add known water volumes to the bag in increments such as 0.5 L.
2. Place the bag in the same tube and follower arrangement used for air measurements.
3. Mark the follower position for each known volume.
4. Empty and dry the bag.
5. Use the resulting displacement scale for subsequent exhaled-air measurements.

For an ideal constant-area tube:

```text
volume = tube cross-sectional area × follower travel
```

Empirical calibration would account for some bag folding and dead space.

## Sizing information received

The response described typical adult vital capacity as roughly 4-6 L and suggested that some taller or trained freedivers may reach 7-9 L. It proposed a device capacity of approximately 9 L for freediving use.

These were generic ranges, not a prediction of the builder's lung volume.

## Alternatives considered

- Elastic balloons were rejected because their pressure changes as they stretch.
- Sequential chamber systems were rejected because threshold valves add complexity.
- Visual markings on an unconstrained flexible bag were considered unreliable because its shape can vary.
- Water displacement for every measurement was considered cumbersome.
- Weighing the inflated bag on a kitchen scale was rejected.

## Corrections and limitations

- The kitchen-scale method is not merely imprecise because of exhaled humidity. An expanding bag displaces ambient air, so buoyancy largely offsets the mass of the gas added. An ordinary scale cannot reliably derive volume by dividing the apparent weight change by air density.
- A Mylar bag is low-stretch, but it does not provide a fixed geometry or perfectly constant pressure.
- A sliding follower adds friction and load. Both can create back-pressure and make the measurement dependent on the mechanism.
- The space outside the bag must remain vented so the follower is not compressing trapped external air.
- A boxed-wine valve is not necessarily a one-way air valve or a proven gas-tight connection.
- Chambered bottles would not fill sequentially merely by connecting different check valves; a reliable switching mechanism would be required.
- The apparatus would measure exhaled volume only. It would not measure timed spirometry quantities such as FEV₁.

## Unresolved design inputs

- Tube diameter and length.
- Target maximum capacity.
- Follower mass, friction and clearance.
- Whether measurement occurs during exhalation or after filling.
- Bag dead volume and repeatable folding behaviour.
- Valve leakage and connection design.
- Back-pressure across the full measurement range.
- Calibration repeatability.
- No prototype or test result was reported.
