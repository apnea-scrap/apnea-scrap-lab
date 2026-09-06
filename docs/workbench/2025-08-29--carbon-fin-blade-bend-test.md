# Carbon Fin Blade Bend Test

## Purpose

The goal was to develop a repeatable way to compare carbon fin blade hardness and eventually translate the behaviour of an existing blade into a laminate layer count for a blade of another length.

The discussion initially explored a rig using dive weights, a weight belt and measurements at several points along the blade. That was not the method ultimately used.

## Implemented test

In practice, the blade was bent through 90° over a kitchen scale. The scale reading provided the resistance measurement at that bend and became the practical way to compare blade hardness.

Blade span remains important when interpreting the reading. The working hypothesis was that, for blades producing the same scale reading at the same bend, a longer blade would feel softer and a shorter blade would feel harder.

## Candidate hardness measure

The conversation proposed normalising the force at the 90° bend by blade span:

```text
H = F90 / L
```

Here, `F90` is the force associated with the scale reading and `L` is the blade span. This is an unvalidated candidate index rather than the implemented measurement itself or an established commercial standard.

## Length and layer-count exploration

The discussion considered two different design objectives:

- maintaining similar static stiffness when changing blade length; and
- maintaining similar perceived effort when changing blade length.

For equal width and material, a simplified linear beam model suggested that maintaining stiffness would require thickness to scale approximately with length:

```text
t2 = t1 × L2 / L1
```

A later single-kick effort proxy combined the proposed hardness index with a length term:

```text
E = H + γL³
```

The intention was to calibrate `γ` from a reference blade, calculate a target hardness for another length, and then translate the required rigidity into laminate thickness and ply count. These equations were exploratory and were not calibrated or validated.

## Earlier rig exploration

Before settling on the kitchen-scale method, the conversation proposed:

- clamping the blade root;
- loading the middle and tip using dive weights restrained by a weight belt;
- using twice as much load at the tip as at the middle;
- photographing the deflected blade against a grid; and
- recording local bend angles near `0.3L`, `0.6L`, and `0.9L`.

This rig was not implemented and is retained only as design history.

## Limitations and open measurements

- The exact root support, scale contact point and method of producing the 90° bend were not recorded.
- It was not recorded whether the scale reading included fixture preload.
- No blade spans, layups, scale readings or repeatability results were captured in the conversation.
- A static scale test does not reproduce the distributed and dynamic hydrodynamic loading of a kick.
- Linear cantilever equations require qualification at a 90° large deflection.
- The proposed `H` index still needs comparison with perceived in-water hardness.
- The `γL³` term and suggested calibration shares were generated assumptions, not measured hydrodynamic relationships.
- Consolidated ply thickness depends on the actual fabric, resin content and laminating process, so generic per-ply figures cannot serve as build specifications.
