---
status: research
time_to_implement: 1
waiting_time: 0
tools_required:
  - name: Knife or scissors
    purpose: Trim tubing and syringe components to length
  - name: Permanent marker
    purpose: Mark graduations and reference points on the gauge
bill_of_materials:
  - name: 10 mL syringe
    description: Thin barrel syringe for plunger travel
    quantity:
      amount: 1
    unit_cost: Inexpensive
  - name: Luer-lock tip cap
    description: Single cap to seal the syringe tip
    quantity:
      amount: 1
    unit_cost: Inexpensive
  - name: Candle wax shavings
    description: Small amount to lubricate the rubber seal
    quantity:
      amount: 0.05
      unit: block
    unit_cost: Inexpensive
---
# {{ parent_child_title() }}
{{ status_banner() }}

## Tools Required
{{ render_tools_required() }}

A simple gauge to monitor mild vacuum (~81 kPa absolute, −20 kPa gauge) directly **inside** a vacuum bag.
It uses Boyle’s law: trapped air expands as pressure drops, moving a rubber plunger seal you can read through the bag.

## Goal
Monitor vacuum level inside a bag using plunger movement.

## Bill of Materials

{{ render_bill_of_materials() }}

## Instructions (step-by-step)
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

---

## Data to Record / Results
Record plunger position at ambient and at target pressure.

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

## Limitations

- The friction between the plunger and the barrel might affect precision
