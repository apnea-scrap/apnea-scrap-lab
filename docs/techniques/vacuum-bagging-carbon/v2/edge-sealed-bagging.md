---
status: research
bill_of_materials:
  - material: materials/vacuum-bagging-kit.md
    description: Manual pump with heavy-duty storage bags for low-cost vacuum pulls
    quantity: 1
    unit: kit
    purchase:
      region: UK
      unit: kit
  - material: materials/butyl-sealing-tape.md
    description: Continuous bead around the laminating base
    quantity: 0.4
    unit: roll
    purchase:
      region: UK
      unit: 15 m roll (12 mm)
  - material: materials/breather-cloth.md
    description: Under-bag airflow path and resin catch
    quantity: 0.6
    unit: metre
    purchase:
      region: UK
      unit: linear metre (1 m wide)
  - name: DIY Vacuum gauge
    description: Inline gauge to monitor vacuum level
    quantity: 1
    unit: gauge
    unit_cost:
      amount: 2.00
      currency: GBP

time_to_implement: 0.5
waiting_time: 0
---
# {{ parent_child_title() }}
{{ status_banner() }}

## Goal
To enable vacuum bagging of larger parts by sealing a cut vacuum bag directly to the laminating base using butyl tape, while achieving a controlled and measurable vacuum level.

## Specifications / Dimensions
- Suitable for medium to large parts (size limited only by base and bag film availability)
- Target vacuum level: ~80% vacuum (-0.2 bar relative to atmosphere)
- Requires a rigid, smooth laminating base for edge sealing

## Bill of Materials

{{ render_bill_of_materials() }}

## Tools Required
- Metal roller or rounded tool (for pressing sealant tape firmly)
- Scissors or utility knife (for cutting bag film and breather cloth)
- Cleaning cloth and window cleaner

## Instructions (step-by-step)

1. Clean the laminating base edges thoroughly using a cloth and window cleaner to ensure the butyl tape adheres
   properly.
2. Cut a sheet of vacuum bag film with sufficient margin to cover the part completely on all sides.
3. Apply a continuous strip of butyl sealing tape along the edges of the laminating base.
4. Lay the vacuum bag film over the base, pressing it firmly into the butyl tape to create an airtight seal.
5. Ensure the vacuum valve is positioned away from critical laminate parts such as the free blade.
6. Arrange breather cloth around the part to support airflow under the bag, and place an extra layer beneath the valve.
7. Pump manually while monitoring the gauge, stopping once ~80% vacuum (-0.2 bar) is achieved.
8. Check for leaks by verifying the gauge holds steady for at least 10 minutes. If vacuum drops, inspect and reseal the
   edges as needed.

## Limitations
- Requires a clean and smooth base surface for proper sealing; dust, grease, or moisture will cause leaks
- More setup time compared to enclosed bagging
