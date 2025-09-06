---
title: Vacuum gauge v1 — syringe gauge
version: v1
status: active
maturity: stable
estimated_cost: 10
time_to_implement: 1
waiting_time: 0
---
# Vacuum gauge v1 — syringe gauge

A simple gauge to monitor mild vacuum (~81 kPa absolute, −20 kPa gauge) directly **inside** a vacuum bag.
It uses Boyle’s law: trapped air expands as pressure drops, moving a rubber plunger seal you can read through the bag.

---

## Parts
- 1 × syringe (10 mL or 20 mL, ideally **thin barrel** for more travel)
- Luer-lock or push-on **tip cap** (to seal airtight)
- Candle wax (for plunger lubrication)
- Breather fabric (to wrap gauge and protect from resin)
- Permanent marker (to mark calibration lines)

---

## Build Steps
1. **Modify plunger**
   - Remove plunger from syringe.
   - Cut off the **plastic rod**, leaving only the **rubber seal**.

2. **Prepare barrel**
   - Clean inside of syringe.
   - Lightly rub **candle wax** on the rubber seal for low friction.

3. **Seal the syringe**
   - Insert rubber seal back into barrel at the **start volume**:
     - 5 mL mark for a 10 mL syringe
     - 10 mL mark for a 20 mL syringe
   - Cap the tip airtight with a Luer-lock or push-on tip cap.

4. **Mark the scale**
   - Draw an **ambient mark** at the initial plunger position.
   - Mark your **target 80% atmospheric (~81 kPa abs)**:
     - 10 mL syringe → +1.25 mL (plunger moves ~7.6 mm on standard barrel, ~20 mm on thin insulin barrel)
     - 20 mL syringe → +2.5 mL (plunger moves ~8.9 mm)

5. **Wrap and place**
   - Wrap syringe loosely in breather fabric so resin cannot touch it.
   - Place it on top of breather stack, markings facing upward for reading through film.

---

## Calibration Reference
Target positions relative to **start volume**:

| Absolute Pressure | % of Atmosphere | 10 mL Syringe (start 5 mL) | 20 mL Syringe (start 10 mL) |
|-------------------|-----------------|----------------------------|-----------------------------|
| 101 kPa           | 100% (ambient)  | 5.0 mL                     | 10.0 mL                     |
| 95 kPa            | 94%             | 5.33 mL (Δ0.33)            | 10.67 mL (Δ0.67)            |
| 90 kPa            | 89%             | 5.63 mL (Δ0.63)            | 11.26 mL (Δ1.26)            |
| 85 kPa            | 84%             | 5.96 mL (Δ0.96)            | 11.92 mL (Δ1.92)            |
| **81 kPa**        | **80% target**  | **6.25 mL (Δ1.25)**        | **12.5 mL (Δ2.5)**          |
| 75 kPa            | 74%             | 6.75 mL (Δ1.75)            | 13.5 mL (Δ3.5)              |

*Δ = plunger movement from ambient*

---

## Tips
- **Thin syringes = more visible plunger travel.** An insulin-style syringe can give ~2–3× more movement than a standard barrel.
- Always mark **ambient** before sealing.
- Wrap well in breather; the plunger must not be glued by resin.
- Works best for **mild vacuum** (~−20 kPa gauge).

---

## Advantages
- Ultra-cheap (under $1 in parts)
- No electronics, no second syringe needed
- Fully sealed, safe to place inside bag
- Large visible plunger movement with thin syringes
- Perfect for confirming steady ~80% atmospheric pressure during cure
