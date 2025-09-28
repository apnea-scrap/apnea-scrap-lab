---
status: research
bill_of_materials:
  - material: materials/vacuum-bag-film.md
    description: Cut large enough for flange seal and pleats
    quantity: 1.2
    unit: metre
    purchase:
      region: UK
      unit: linear metre (760 mm wide)
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
  - material: materials/vacuum-gauge.md
    description: Inline gauge to monitor vacuum level
    quantity: 1
    unit: gauge
    purchase:
      region: UK
      unit: gauge
  - material: materials/manual-vacuum-pump.md
    description: Manual pump for edge-sealed bag
    quantity: 1
    unit: pump
    purchase:
      region: UK
      unit: pump kit
time_to_implement: 5
waiting_time: 12
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
1. Clean the edges of the laminating base with a cloth and window cleaner to ensure proper adhesion of the butyl tape.
2. Cut a sheet of vacuum bag film large enough to cover the part with margin on all sides.
3. Apply butyl sealing tape along the edges of the laminating base.
4. Place the vacuum bag film over the base and press it firmly into the butyl tape to create a continuous edge seal.
5. Install the vacuum pump connector and vacuum gauge through the bag film or at a pre-made port.
6. Place breather cloth around the part to maintain airflow under the bag.
7. Start pumping manually and monitor the gauge. Stop when ~80% vacuum (-0.2 bar) is reached.
8. Check for leaks by observing if the gauge holds steady for at least 10 minutes. If vacuum drops, inspect and reseal edges.

## Limitations
- Requires a clean and smooth base surface for proper sealing; dust, grease, or moisture will cause leaks
- More setup time compared to enclosed bagging
