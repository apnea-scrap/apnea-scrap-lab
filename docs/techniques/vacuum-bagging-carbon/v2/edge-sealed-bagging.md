---
status: concept
bill_of_materials:
  - material: materials/vacuum-bagging-kit.md
    description: Manual pump with heavy-duty storage bags for low-cost vacuum pulls
    quantity:
      amount: 1
      unit: kit
  - material: materials/butyl-sealing-tape.md
    description: Continuous bead around the laminating base
    quantity:
      amount: 0.4
      unit: 15 m roll (12 mm)
  - material: materials/breather-cloth.md
    description: Under-bag airflow path and resin catch
    quantity:
      amount: 0.12
      unit: 5 m pack (1 m wide)
      display: 0.6 m (1 m wide)


time_to_implement: 0.5
waiting_time: 0
tools_required:
  - name: Metal roller or rounded tool
    purpose: Press the butyl sealing tape firmly to the base
  - name: DIY Vacuum gauge
    purpose: Estimate when vacuum reaches 80% atmospheric pressure
  - name: Scissors
    purpose: Cut materials like fabric, film, or templates to size
  - name: Window cleaner
    purpose: Degrease surfaces before bonding or sealing
---
# {{ parent_child_title() }}
{{ status_banner() }}

## Goal
To enable vacuum bagging of larger parts by sealing a cut vacuum bag directly to the laminating base using butyl tape, while achieving a controlled and measurable vacuum level.

## Specifications / Dimensions
- Suitable for medium to large parts (size limited only by base and bag film availability)
- Target vacuum level: ~80% vacuum (-0.2 bar relative to atmosphere)
- Requires a rigid, smooth laminating base for edge sealing

## Time needed

{{ render_technique_time_overview() }}

## Bill of Materials

{{ render_bill_of_materials() }}

## Tools Required
{{ render_tools_required() }}

See this page for how to make a DIY Vacuum Gauge: [Trapped Baloon Vacuum Gauge](../../measuring-vacuum/v2/trapped-baloon.md)

## Instructions (step-by-step)

1. Clean the laminating base edges thoroughly using a cloth and window cleaner to ensure the butyl tape adheres
   properly.
2. Cut a sheet of vacuum bag film with sufficient margin to cover the part completely on all sides.
3. Apply a continuous strip of butyl sealing tape along the edges of the laminating base.
4. Lay the vacuum bag film over the base, pressing it firmly into the butyl tape to create an airtight seal.
5. Ensure the vacuum valve is positioned away from critical laminate parts such as the free blade.
6. Arrange breather cloth around the part to support airflow under the bag, and place an extra layer beneath the valve.
7. Pump manually while monitoring the gauge, stopping once ~80% atmospheric pressure (-0.2 bar) is achieved.
8. Check for leaks by verifying the gauge holds steady for at least 10 minutes. If vacuum drops, inspect and reseal the
   edges as needed.

## Limitations
- Requires a clean and smooth base surface for proper sealing; dust, grease, or moisture will cause leaks
- More setup time compared to enclosed bagging
