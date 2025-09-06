---
title: Flex test rig v1 — weight belt test
version: v1
status: active
estimated_cost: 10
time_to_implement: 1
waiting_time: 0
---
# Flex test rig v1 — weight belt test

**Goal**
Measure how much load makes the **tip vertical (90°)** and where the blade bends (root, mid, tip).

---

## Setup
- **Clamp**: Fix the blade root flat with ≈80 mm clamped depth. Use rubber pads to protect and prevent slip.
- **Span**: Measure blade length `L` from clamp line to tip.
- **Marks**: Put dots on one edge at:
  - Root zone ≈ `0.3 L`
  - Mid zone ≈ `0.6 L`
  - Tip zone ≈ `0.9 L`
- **Weight belt loading**:
  - Wrap a weight belt snugly around the blade.
  - Place dive weights **on top** of the blade at the **tip (L)** and **mid zone (0.6 L)**.
  - Keep a **2:1 ratio** — twice as much load at the tip as at the mid.
  - Ensure weights are centered so they press straight down, not on the rails.
- **Camera**: Place a phone side-on, level with blade mid-height.
- **Reference**: Tape a ruler or printed grid behind the blade.

---

## Step 1 — Load until tip is vertical
1. Add weights to tip and mid (2:1 ratio).
2. After each step, check the **tip angle** with an angle finder or from the side photo.
3. Stop when the last 20 mm of the tip points straight down (≈90°).
4. Record total weight used (belt + dive weights).

Formula:

F90 = m × 9.81 (N)

---

## Step 2 — Measure bend at 3 zones
- Take a side photo at that load.
- From the grid/photo, estimate local slope (angle) at each zone:
  - **θ_root** at `0.3 L`
  - **θ_mid** at `0.6 L`
  - **θ_tip** at `0.9 L`

---

## Data to record
- Clamp depth (mm)
- Blade span `L` (mm)
- Load method: belt with weights on top (tip + mid, 2:1 ratio)
- **F90** (N)
- **θ_root, θ_mid, θ_tip** (degrees at F90)
