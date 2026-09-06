# Short Fin Layup and Layer-Stack Visualisation

## Short-fin specification

Target geometry:

- Finished width: 18 cm.
- Total length: 40 cm.
- Foot-pocket section to bend: 15 cm.
- Bend to end of foot-pocket rail: 8 cm.
- Free blade beyond the rail: 17 cm.

Material:

- 200 g/m², 2×2 twill, 3K carbon-fibre cloth.
- Natural 0°/90° orientation.

`3K` means that each tow contains approximately 3,000 carbon filaments. It describes tow filament count, not ply weight, stiffness or strength by itself.

## Layup

1. One 20 × 40 cm full ply.
2. One 20 × 30 cm ply, ending at 30 cm.
3. Two 10 × 40 cm side strips intended to reinforce the rail areas.
4. One 20 × 40 cm full ply.

## Cutting plan

Cut one blade from a 30 × 100 cm sheet:

- Two 20 × 40 cm pieces.
- Two 10 × 40 cm pieces.
- One 20 × 30 cm piece.

The total cloth area is 0.30 m² per blade.

## Layer-stack visualisation

Several exploded-stack SVGs were generated, but their stacking and perspective were unsatisfactory. The adopted direction was to separate the representation of each layer from the composition of the complete diagram:

- Create one SVG for each logical laminate layer.
- Give every layer a shared coordinate system and footprint.
- Pass an ordered list of layer SVGs to a composition tool.
- Apply a consistent rotation or skew.
- Offset each layer according to its order.
- Render a 45° exploded isometric stack.
- Allow layer order and spacing to change without redrawing the layer SVGs.

The side-reinforcement layer can be represented by one SVG containing both strips.

The conversation described such a composer, but no durable implementation or source file was produced. The generated sandbox SVG files were also not preserved.

## Editorial notes and unresolved details

- A 6K or 12K fabric is not necessarily heavier per ply; areal weight and weave construction determine that.
- Generated soft and medium alternatives, unidirectional additions, ply-thickness estimates and resin-ratio targets were not part of the recorded build.
- Resin-system details introduced by the assistant were not supplied by the user and are not retained.
- The exact lateral placement of the two 10 cm strips remains ambiguous. Together they span 20 cm, so they do not form narrow edge bands unless they overlap, overhang or leave a defined central gap.
- The root alignment of the 20 × 30 cm ply is implied but was not stated explicitly.
- No cured thickness, finished mass, bend profile or performance result was reported.
