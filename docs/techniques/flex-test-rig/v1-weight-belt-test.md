---
title: Flex test rig v1 — weight belt test
version: v1
status: active
estimated_cost: 10
time_to_implement: 1
waiting_time: 0
---
# Flex test rig v1 — weight belt test
{{ status_banner() }}

## Goal
Measure how much load makes the **tip vertical (90°)** and where the blade bends (root, mid, tip).

## Specifications / Dimensions
- Clamp depth ≈80 mm on the blade root
- Marks at 0.3 L (root), 0.6 L (mid), and 0.9 L (tip)
- Weights applied in a 2:1 ratio (tip:mid)

## Materials / Bill of Materials
- Weight belt
- Dive weights
- Ruler or printed grid
- Tape for securing the reference grid

## Tools Required
- Clamp with rubber pads
- Camera or smartphone
- Angle finder or protractor

## Instructions (step-by-step)

### Step 1 — Load until tip is vertical
1. Add weights to tip and mid (2:1 ratio).
2. After each step, check the **tip angle** with an angle finder or from the side photo.
3. Stop when the last 20 mm of the tip points straight down (≈90°).
4. Record total weight used (belt + dive weights).

Formula:

F90 = m × 9.81 (N)

---

### Step 2 — Measure bend at 3 zones
- Take a side photo at that load.
- From the grid/photo, estimate local slope (angle) at each zone:
  - **θ_root** at `0.3 L`
  - **θ_mid** at `0.6 L`
  - **θ_tip** at `0.9 L`

## Data to Record / Results
- Clamp depth (mm)
- Blade span `L` (mm)
- Load method: belt with weights on top (tip + mid, 2:1 ratio)
- **F90** (N)
- **θ_root, θ_mid, θ_tip** (degrees at F90)

## Tips, Trade-offs, or Limitations
- Ensure weights are centered so they press straight down, not on the rails.
- Use a stable bench to avoid vibrations while measuring angles.
