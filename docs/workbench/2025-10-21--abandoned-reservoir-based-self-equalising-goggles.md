# Abandoned Reservoir-Based Self-Equalising Goggles

## Context

The end goal was a DIY pair of air-filled, self-equalising goggles. Liquid-filled goggles were excluded.

The theoretical investigation progressed through:

1. Membrane-based self-equalisation.
2. A compressed-air cylinder with a suction-operated valve.
3. A low-pressure syringe reservoir with flow control.
4. A passive compressible reservoir connected directly to the rigid goggles.
5. A plastic-container and partially filled balloon arrangement.

The passive direction was attractive because it removed valves and regulators. No version of the design was implemented or tested.

## Theoretical passive design

The final theoretical arrangement was:

- a plastic container;
- a partially filled balloon inside it;
- a connection between the balloon’s airspace and the rigid goggles; and
- an air quantity calculated so that the balloon would fill the container at 80% of atmospheric pressure.

The intended principle was that increasing ambient pressure would compress the balloon while the goggle cups retained their volume, allowing the connected airspace to track the pressure change.

## Sizing model received

Let:

- `Vg` be the rigid goggle air volume at the surface;
- `Vc` be the usable volume change of the external reservoir; and
- `P` be absolute pressure in atmospheres.

The proposed minimum reservoir capacity was:

```text
Vc ≥ Vg × (P - 1)
```

Using approximately one additional atmosphere per 10 metres, the theoretical depth at which the reservoir reached its collapse limit was expressed as:

```text
depth ≈ 10 × Vc / Vg metres
```

For 30 ml goggles and 250 ml of usable reservoir displacement, the response calculated:

- 100% collapse: about 83 m;
- 90% usable collapse: about 75 m; and
- 80% usable collapse: about 67 m.

These were idealised Boyle’s-law capacity calculations, not tested depth ratings.

## Decision not to pursue

The concept was not pursued because any air reservoir introduces a changing buoyancy load:

- The reservoir adds positive buoyancy near the surface.
- Fixed ballast would be needed to compensate for it.
- As the air compresses with depth, that buoyancy disappears.
- The compensating ballast remains, making the system progressively more negative.
- The diver would have to work against that negative load.

The Boyle’s-law calculations describe gas-volume capacity but do not make the overall system practical.

## Rejected mitigations

The conversation considered:

- adding ballast;
- streamlining the reservoir;
- distributing the volume across flat bladders;
- incorporating the reservoir into the strap;
- reducing reservoir size with pneumatic assistance; and
- returning to a compressed-air cartridge.

These did not resolve the core issue that gas volume supplies buoyancy near the surface and progressively loses it with depth while any compensating ballast remains.

## Editorial notes

- No prototype was built and no bench, pool, depth, leak, drag or buoyancy testing was performed.
- The earlier suggestion to add roughly 120–150 g of ballast treated neutral buoyancy at one depth as sufficient and missed the changing load across the dive.
- The sizing equations assume isothermal compression, negligible balloon stiffness, a rigid goggle volume, no leakage and a known usable reservoir displacement.
- The conversation sometimes treated nominal container size as usable air volume. The relevant value would be the balloon’s actual volume change before reaching either its collapse limit or the container walls.
- Commercial examples and detailed generated valve designs were not adopted and are omitted.
- No alternative self-equalising-goggle design was selected.
