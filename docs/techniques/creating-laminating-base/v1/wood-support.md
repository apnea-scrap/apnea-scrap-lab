---
status: legacy
time_to_implement: 1
waiting_time: 0
tools_required:
  - name: Wood saw
    purpose: Cut the laminating base supports to length
  - name: Screwdriver
    purpose: Drive screws to secure brackets and maintain the angle
  - name: Tape measure
    purpose: Check dimensions and spacing during setup
  - name: Sandpaper
    purpose: Prepare and smooth surfaces for better adhesion and finish
bill_of_materials:
  - material: materials/acrylic-sheet.md
    name: Acrylic sheet (A3)
    description: 3 mm clear sheet cut to 420 × 297 mm
    quantity:
      amount: 1
      unit: 1 sheet A3 sheet (2 mm)
  - material: materials/acrylic-sheet.md
    name: Acrylic sheet (A4)
    description: 2 mm clear sheet cut to 210 x 297 mm
    quantity:
      amount: 1
      unit: 1 sheet A4 sheet (2 mm)
  - name: Softwood board offcuts
    description: 1 cm thick timber for base and angled supports
    quantity:
      amount: 1
      unit: set
    usage_type: reusable
    unit_cost:
      amount: 5.00
      currency: GBP
  - name: Angle brackets and screws
    description: Two galvanised brackets with matching screws
    quantity:
      amount: 1
      unit: set
    usage_type: reusable
    unit_cost:
      amount: 4.20
      currency: GBP
  - name: Double sided-tape
    description: Thin acrylic tape to secure sheets to timber
    quantity:
      amount: 1
      unit: roll
    unit_cost: Inexpensive
---
# {{ parent_child_title() }}
{{ status_banner() }}

25° wooden base with acrylic sheets for laminating carbon fin blades.

## Goal
Create a rigid angled surface to support fin blades during lamination.

## Specifications / Dimensions

**Dimensions**

- **Long Side (Flat)**:
    - Minimum width: **25cm** (to accommodate 20cm blade width and additional room).
    - Minimum length: **30cm** (to fit a 25cm blade length and additional room).
- **Angled Side (23°–25° Incline)**:
    - Angle: **23 degrees** (or 25° based on matching geometry).
    - Minimum width: **25cm** (to match blade width).
    - Minimum length: **20cm** (to fit 15cm blade length and extra space).

## Reference Images

| ![Support Structure](support_all.jpeg) | ![Brackets and Side](support_brakets.jpeg) |
|----------------------------------------|--------------------------------------------|
| Full Support Structure                 | Brackets and Side Supports                 |

## Time needed

{{ render_technique_time_overview() }}

## Bill of Materials

{{ render_bill_of_materials() }}

## Tools Required
{{ render_tools_required() }}

## Instructions (step-by-step)

1. **Base Construction**
    - Use 1cm thick timber to create a solid base.
    - Cut wooden side supports to a **23°–25° angle** to replicate blade geometry.
    - Secure side supports to the flat base using **metal brackets** for rigidity.

2. **Laminating Platform**
    - Tape clear **Acrylic Perspex sheets** (A3 and A4 sizes) onto the wooden base using thin **double-sided adhesive
      tape**.
    - Ensure the surface is smooth and taut to properly press against the blade.

## Data to Record / Results
- Notes on surface flatness after cure
- Any deformation or movement during lamination

## Limitations

- **Does not scale well**: In order to create bigger fins, the wooden structure needs to be re-worked.
- **Vacuum Bag Fit**: Ensure the base with acrylic layers fits entirely into the vacuum bag.
- **Air Trapping Issue**: The gap between the angled section and wooden supports bends the acrylic during vacuum bagging
