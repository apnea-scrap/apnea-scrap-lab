# Aluminium bridge for a modular bifin-pocket monofin

## Context

The project was a modular freediving monofin using two ordinary bifin foot pockets and a DIY carbon-fibre monofin blade. The modular approach would allow foot pockets or experimental blades to be replaced without rebuilding the entire assembly.

The principal failure concern was asymmetric leg loading. Because the bifin pockets transmit force separately, one leg can twist or bend the blade more than the other, concentrating stress around the centre and potentially causing cracking or delamination.

No drawing, CAD file, structural calculation, prototype, or test result was produced during the conversation.

## Adopted design direction

- Couple the two bifin foot pockets with an aluminium bridge.
- Reuse the two existing mounting positions from each foot pocket, giving four fasteners in total.
- Place all four mounting holes on one straight line, matching the existing pocket geometry.
- Sandwich the carbon blade between the aluminium bridge and the foot pockets.
- Position the bridge at the back or heel side of the foot pockets.
- Begin by evaluating a 4 mm aluminium plate.
- Keep the bridge removable so different blades and pockets can be tested.

The intended stack was described as:

```text
bolt head
aluminium bridge
carbon blade
foot-pocket base
washer and locknut
```

The precise meaning of “at the back of the foot pocket” still needs to be established in a side-view drawing, including the plate's fore-aft location and which surfaces directly contact the blade.

## Proposed plate features

The bridge would be one wide plate spanning both pockets. It would have:

- four inline mounting holes located from direct measurements or a tracing of the real pockets;
- rounded corners and thoroughly deburred edges;
- broad bearing areas around the fasteners;
- no sharp edge bearing directly against the flexing blade;
- an outline that spreads asymmetric load over a wider part of the blade; and
- electrical and moisture isolation between the aluminium, carbon fibre, and stainless fasteners.

The response proposed approximately 135 × 65 mm, 4 mm thickness, and alloys such as 6061-T6 or 5083. It also gave example hole spacing. These were speculative starting points rather than adopted dimensions; actual geometry had not been measured.

A rigid bridge can shift the blade's highest stress to the edge of the plate. The bridge shape and the blade layup therefore need a gradual stiffness transition rather than an abrupt hard boundary.

## Fabrication advice received

The suggested workshop process was:

1. Measure or trace the existing foot-pocket hole locations.
2. Transfer the hole centres and plate outline accurately to the aluminium.
3. Clamp the material and cut it using a metal-cutting jigsaw or bandsaw.
4. Drill pilot holes and then clearance holes with sharp HSS or cobalt bits and suitable cutting lubricant.
5. Deburr both sides of every hole.
6. Round the plate corners and smooth all edges with files and abrasives.
7. Assemble with stainless fasteners, large bearing washers, and vibration-resistant nuts.
8. Tighten evenly while checking that the plate, blade, and foot pockets remain seated without local distortion.

The response suggested rubber or neoprene between the aluminium and carbon. That was an option, not an adopted interface design.

## Editorial corrections

- A proposed 6.5 mm hole is excessively large for an M4 fastener and is closer to clearance for an M6 fastener. Hole diameter must match the selected bolt and the positional tolerance actually required.
- Scoring a bend line with a hacksaw or rotary tool would intentionally introduce a fatigue-critical stress concentration and should not be part of the design.
- Minimum bend radius depends on alloy, temper, grain direction, tooling, and bend angle. A generic `3 × thickness` value does not establish that a particular 4 mm plate can be formed safely.
- Claims of less than 1 mm deflection and survival under 20–40 kg loads were unsupported because plate geometry, support conditions, foot load, torque, and fastener preload were not modelled.
- A 4 mm plate is not automatically strong enough merely because it is difficult to bend by hand. The relevant case is cyclic, asymmetric loading through the actual mounting geometry.
- The aluminium bridge does not inherently prevent blade delamination. It can redistribute load or move the failure point to its edge.
- Carbon fibre and aluminium form a strong galvanic couple in salt water, and stainless fasteners add another dissimilar metal. Interfaces, hole walls, and fasteners require electrical isolation and sealing.
- A compliant rubber layer may reduce local contact stress, but it can also creep, relax bolt preload, and allow fretting. Its material and thickness must be engineered and tested.
- Drilled carbon holes require adequate edge distance, local layup reinforcement, clean machining, sealed edges, and controlled bearing pressure. Epoxy applied to the hole edge alone is not a complete reinforcement scheme.

## Open design inputs

- Foot-pocket make, model, and measured four-hole coordinates.
- A side and top view defining exactly where the bridge sits.
- Plate length, depth, outline, alloy, temper, and surface treatment.
- Carbon-blade thickness, layup, hole reinforcement, and intended flex transition.
- Fastener diameter, material, torque or preload, washers, and locking method.
- Electrical-isolation and water-sealing system for the carbon/aluminium/stainless interfaces.
- Expected asymmetric force, torque, fatigue cycles, and acceptable deflection.
- Whether the plate should remain flat or follow the pocket or blade angle.
- Bench proof-load, fatigue, saltwater-exposure, and pool-test procedures.
