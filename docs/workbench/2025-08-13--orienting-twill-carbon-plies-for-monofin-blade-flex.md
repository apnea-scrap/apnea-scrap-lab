# Orienting twill carbon plies for monofin blade flex

## Context

The question was how to interpret a CETMA explanation that a carbon monofin blade must control deformation in three directions:

- 0° along the blade length;
- 90° across its width; and
- ±45° diagonally.

A monofin is a wide plate rather than two narrow independent blades. It can therefore combine intended longitudinal bending with transverse bowl or “spoon” deformation, twist, and independent movement of its outer corners.

The available reinforcement was twill carbon cloth. Its weave, areal weight, fibre type, balance, resin system, cured-ply thickness, blade geometry, and target stiffness were not supplied. No laminate was manufactured or tested in the conversation.

## Response received

### 0° longitudinal behaviour

Longitudinal bending was described as the primary useful blade flex. It stores and returns elastic energy through the kick. The laminate needs enough longitudinal stiffness to transmit load while remaining compliant enough to form the intended flex curve.

### 90° transverse behaviour

Transverse curvature can make the wide blade bowl or spoon. The response said this may allow more flow to leave laterally and reduce useful propulsion. Fibres running across the blade and the overall transverse laminate stiffness influence this deformation.

### ±45° diagonal behaviour

Diagonal fibres were described as carrying in-plane shear and resisting blade twist, independent corner droop, and deformation near the ends of the water rails.

### Using twill cloth

A nominally balanced 2×2 twill contains fibres in its warp and weft directions. If those cloth axes are aligned with the blade, they provide 0° and 90° reinforcement in the same ply. Rotating the cloth by 45° places its two fibre directions at +45° and -45° relative to the blade.

The response therefore proposed mixing aligned and bias-cut twill plies and using local patches, strips, and ply drop-offs to tune different blade regions. It also recommended a laminate symmetric about its mid-plane to reduce cure distortion and unintended coupling.

## Durable design principles

Treat the monofin as an anisotropic plate rather than choosing a ply count from longitudinal flex alone:

- aligned twill plies contribute jointly to longitudinal and transverse stiffness;
- bias-oriented twill primarily changes shear and torsional response, while still contributing to other stiffness terms;
- the position of each ply through the thickness strongly influences bending stiffness;
- laminate balance and symmetry affect extension, bending, shear, and twist coupling;
- local reinforcement must transition gradually to avoid abrupt stiffness and thickness changes; and
- useful longitudinal flex must be balanced against spooning, torsion, root loading, corner motion, and fatigue.

## Generated layup concepts

The response generated six-, eight-, and ten-ply examples using combinations of:

- full aligned plies;
- full bias plies;
- centre-spine strips;
- edge strips;
- transverse bands;
- bias-oriented tip patches; and
- progressively shortened inner plies near the trailing edge.

Their design intent was to show how complete and local plies could tune regions of a blade. The exact counts, ordering, widths, lengths, and stiffness labels were not calculated, built, or adopted and are not a usable laminate schedule.

## Editorial corrections

- A 2×2 twill is not guaranteed to contain equal fibre weight in both directions. The fabric datasheet must establish whether it is balanced.
- Symmetry alone is insufficient to characterise the laminate. Balance and unwanted extension–shear, bending–twist, and other coupling terms must also be checked.
- Adding a straight-cut twill ply increases both 0° and 90° reinforcement; it cannot selectively add only one of those directions.
- Rotating a woven ply changes its complete stiffness contribution, not only its resistance to one named deformation.
- Local transverse bands, edge strips, and patches create thickness steps, resin-rich edges, load concentrations, and possible print-through unless their terminations are designed and tapered.
- Bias plies on the outside are not automatically impact-tolerant; carbon laminates remain vulnerable to impact and edge damage.
- The claims that particular local strips would prevent spooning or that particular tip patches would prevent corner lag were unvalidated.
- Suggested six-, eight-, and ten-ply stiffness classes, 30–40 mm strips, 120–150 mm patches, and 15–25 mm mould camber were unsupported guesses.
- Required glass-transition temperature, bag pressure, resin fraction, post-cure, and mould curvature must follow the selected material system and validated manufacturing process.
- The cloth-yield calculation was incorrect. Four 650 × 600 mm full plies have a net area of 1.56 m² before nesting and cutting losses and cannot come from a 1 m² sheet.
- The stated relationship between spooning, lateral water escape, rail-end deformation, and propulsion efficiency was qualitative and had no measurements in this conversation.

## Proposed development process

1. Record the cloth warp/weft weights, fibre grade, resin, cured-ply thickness, and processing limits.
2. Define blade planform, root constraints, water-rail geometry, target mass, and intended flex profile.
3. Define measurable longitudinal bending, transverse bending, and torsional stiffness targets.
4. Manufacture balanced and symmetric coupons using aligned and mixed aligned/bias twill.
5. Measure bending, torsion, mass, thickness, fibre/resin content, cure quality, and failure behaviour.
6. Build reduced blade prototypes with controlled, tapered ply drop-offs.
7. Compare deformation under symmetric and asymmetric foot loads.
8. Use measured laminate properties in a plate or finite-element model.
9. Select a full blade laminate only after coupon and prototype results agree sufficiently with the model.
