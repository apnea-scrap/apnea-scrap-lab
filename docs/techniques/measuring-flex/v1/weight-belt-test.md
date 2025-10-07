---
status: legacy
time_to_implement: 0.25
waiting_time: 0
tools_required:
  - name: Clamp with rubber pads
    purpose: Secure the blade without marking the rails
  - name: Camera or smartphone
    purpose: Record the deflection for later comparison
  - name: Angle finder or protractor
    purpose: Measure the bend angle at the target load
bill_of_materials:
  - name: Weight belt with pockets
    description: Holds weights in place to load the fin tip and mid-span
    quantity:
      amount: 1
      unit: belt
  - name: Dive weights
    description: Individual weights to create the 2:1 tip-to-mid loading ratio
    quantity:
      amount: 3
      unit: weights
      display: Mix of weights to reach target load
  - name: Rigid ruler or printed grid
    description: Visual reference to observe bend angles along the blade span
    quantity:
      amount: 1
      unit: reference board
  - name: Masking tape
    description: Secures the grid or ruler to the support structure
    quantity:
      amount: 1
      unit: roll
---
# {{ parent_child_title() }}
{{ status_banner() }}

## Goal
Measure the load required to make the **tip vertical (90°)** and observe where the blade bends (root, mid, tip).

## Specifications / Dimensions
- Clamp depth ≈80 mm on the blade root
- Marks at 0.3 L (root), 0.6 L (mid), and 0.9 L (tip)
- Weights applied in a 2:1 ratio (tip:mid)

## Time needed

{{ render_technique_time_overview() }}

## Bill of Materials

{{ render_bill_of_materials() }}

## Tools Required
{{ render_tools_required() }}

## Instructions
- **Step 1 — Load until tip is vertical**  
  Add weights to tip and mid (2:1 ratio) and stop when the last 20 mm of the tip points straight (≈90°). Record the total weight.

  Formula:  
  `F90 = m × 9.81 (N)`

- **Step 2 — Measure bend at 3 zones**  
  Take a side photo at the load and estimate local slope (angle) at each zone:
  - `θ_root` at 0.3 L
  - `θ_mid` at 0.6 L
  - `θ_tip` at 0.9 L

## Data to Record
- Clamp depth (mm)
- Blade span L (mm)
- Load method: belt with weights on top (tip + mid, 2:1 ratio)
- **F90** (N)
- **θ_root, θ_mid, θ_tip** (degrees at F90)

## Limitations
- Dive weights limit fine-tuning of the scale  