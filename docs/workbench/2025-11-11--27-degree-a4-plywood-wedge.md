# 27-Degree A4 Plywood Wedge

## Context

The goal was to make a cheap, DIY-friendly wedge supporting an A4-sized sheet at 27 degrees. The top surface could not be punctured. The design initially also needed to come apart easily for flat storage.

The material choice evolved from acrylic to plywood. A 1.5 mm A4 plywood sheet was selected as a lightweight alternative to 2 mm acrylic, and the flat sheet and triangular supports were ultimately made from plywood.

## Geometry and cutting plan

The triangular supports were defined by:

- sloping edge: 210 mm;
- base: approximately 187 mm;
- height: approximately 95 mm; and
- base angle: approximately 27 degrees.

A 187 × 95 mm rectangle can be divided diagonally into two supports. Three of these rectangles fit on an A4 sheet by placing the 187 mm dimension across the sheet's 210 mm width and three 95 mm dimensions along its 297 mm length. This gives a theoretical yield of six triangles per A4 sheet, subject to cutting kerf and edge margins.

## Material comparison received

The response compared sheet materials using bending stiffness proportional to `E × thickness³`. Taking a representative plywood modulus of 8 GPa and an acrylic modulus of 3.2 GPa, it estimated:

```text
(8 × 1.5³) / (3.2 × 2³) ≈ 1.05
```

On that basis, 1.5 mm plywood was described as having roughly the same bending stiffness as 2 mm acrylic while being lighter, less brittle, and easier to cut. Risks noted for thin plywood included flex when unsupported, variation in flatness, warping with humidity, and the need for sealing around moisture.

This comparison is only an estimate because plywood stiffness varies with species, veneer construction, and grain direction.

## Joint options considered

The discussion considered permanent glue joints, plywood gussets, slots and tabs, magnets, dowels, small L-brackets, removable mounting strips, low-tack tape, 3M VHB, and Dual Lock.

Permanent glue was initially rejected because of the flat-storage requirement. Small hidden brackets with removable double-sided adhesive then became the preferred direction. The response distinguished permanent VHB tape from replaceable Command-style strips and reclosable Dual Lock, but no specific removable product or bracket layout was adopted.

## Implemented design and outcome

The completed design used plywood held together by plastic corner braces and superglue. It worked well in practice.

This successful construction was permanent, so the original requirement for easy disassembly was not carried into the implemented design. The tape-based and reclosable arrangements remained alternatives considered rather than the chosen solution.
