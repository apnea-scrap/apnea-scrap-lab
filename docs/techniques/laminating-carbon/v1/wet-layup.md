---
status: active
bill_of_materials:
  - material: materials/carbon-fiber-fabric.md
    description: 0.3 m² of 200 g/m² 3K 2/2 twill cloth
    quantity: 0.3
    unit: m²
    purchase:
      region: UK
      unit: m² (1 m wide)
  - material: materials/laminating-epoxy-system.md
    description: 200 g mixed resin (approx. 200 ml)
    quantity: 0.4
    unit: 500 ml kit
    purchase:
      region: UK
      unit: 500 ml kit
  - material: materials/pva-release-agent.md
    description: Two thin coats on the laminating base
    quantity: 0.07
    unit: 500 ml bottle
    purchase:
      region: UK
      unit: 500 ml bottle
  - material: materials/peel-ply.md
    description: Two layers cut to the blade outline
    quantity: 0.6
    unit: metre
    purchase:
      region: UK
      unit: linear metre (1.5 m wide)
  - material: materials/breather-cloth.md
    description: Wrap to improve vacuum bleed
    quantity: 0.5
    unit: metre
    purchase:
      region: UK
      unit: linear metre (1 m wide)
    notes: Optional for manual pump setups
  - material: materials/vacuum-storage-bags.md
    description: Large bag enclosure (one bag from a pack of two)
    quantity: 0.5
    unit: pack
    purchase:
      region: UK
      unit: pack of 2 (55 × 85 cm)
  - material: materials/manual-vacuum-pump.md
    description: Manual pump amortised over repeated builds
    quantity: 0.1
    unit: pump
    purchase:
      region: UK
      unit: pump kit
    notes: Optional; reuse across laminations
  - name: Consumables pack
    description: Gloves, mixing sticks, acetone wipes
    quantity: 1
    unit_cost:
      amount: 3.50
      currency: GBP
time_to_implement: 3
waiting_time: 12
---
# {{ parent_child_title() }}
{{ status_banner() }}

Baseline recipe with 0/90 twill and simple taper.

## Goal
Produce a basic carbon blade using a manual wet layup.

## Specifications / Dimensions
- Uses 0/90 3K twill carbon cloth
- Geometry and taper follow the chosen cutting template

## Bill of Materials

{{ render_bill_of_materials() }}

- Digital scale accurate to 1 g for measuring resin and hardener.
- Plastic finned roller (75 mm) to consolidate the laminate.

## Tools Required
- Nitrile gloves
- Mixing pots and sticks
- Laminating brushes
- Plastic finned roller (75 mm)
- Scissors for cutting fabric
- Digital scale
- Optional: vacuum storage bags and hand pump

## Reference Images

| ![Wet Carbon Laminate](sf_laminate_wet.jpeg) | ![Cured Carbon Laminate  ](sf_laminate_cured.jpeg) |
|-------------------------------------------|--------------------------------------------------|
| Wet Carbon Laminate                       | Cured Carbon Laminate                       |


## Instructions (step-by-step)

**0. Safety first**

- Wear **nitrile gloves** and work in a **well-ventilated area** to avoid exposure to harmful fumes.

---

**1. Prepare the work surface**

1. Pour a small amount of the **PVA mold release agent** into a cup.
2. Using a **brush**, apply the release agent **thinly and evenly** over the working surface or mold.
   - Tip: see this **[video at 2:00](https://youtu.be/neh6zDt7vD8?si=0ocFH4VtYBHPhHzH)** for guidance.

---

**2. Cut the carbon fiber cloth**

- Measure and cut the **carbon fiber cloth** to the desired dimensions.
- Ensure smooth cuts to maintain structural strength along the fiber weave.

---

**3. Prepare the epoxy resin**

1. Pour **epoxy resin** into a mixing pot.
   - Use a **ratio of 100:30 by weight** (resin:hardener).
   - Example: for **100 g of resin**, add **30 g of hardener**.
2. Use the **digital scale** for precise measurement.
3. Mix the resin and hardener thoroughly, but **gently**, to avoid introducing air bubbles.

---

**4. Lay the resin and carbon cloth**

1. Spread an even layer of **resin** directly onto the prepared mold or surface.
2. Lay the **carbon fiber cloth** over the resin layer.
3. Apply another layer of resin over the cloth using the **brush** and smooth it out with the **roller**.
   - Tip: use the roller to eliminate trapped air and ensure the **cloth adheres evenly**.

---

**5. Apply peel ply**

1. Once the laminate layers are complete, apply **two layers of peel ply** over the top surface.
   - Peel ply absorbs **excess resin** and helps achieve a uniform finish.
2. Optional: include a **breather layer** to improve vacuum results (future upgrade).
3. Optional: if using vacuum storage bags, place the prepared laminate inside, seal, and apply **vacuum pressure** using the pump.

---

**6. Clean-up**

1. Clean all reusable tools (e.g., brushes) with **acetone** immediately after use.
2. Discard **used gloves, cups, and mixing sticks** responsibly.

## Limitations
- Manual layup can trap more resin compared to vacuum processes.
- Work time is limited once resin is mixed; prepare all materials in advance.
