# Rope-guided underwater pool camera rover

## Goal

Build a DIY underwater camera rover that automatically follows a freediver
from the side at approximately 1–2 m/s. An iPhone in a waterproof enclosure
records through its ultrawide camera and performs visual tracking.

## Evolved architecture

The design converged on:

- Two vertically stacked, tensioned ropes along the pool
- Suction-cup anchors and ratchet tensioning modelled on the local pool's
  temporary lane-rope system
- Spacers approximately one metre from each wall to establish rope separation
- One main rope for propulsion and primary guidance
- A second rope contacted by a small extension arm for roll and orientation
  control
- A compact sealed body surrounding the main drive rope
- Side-view filming throughout the dive
- Direct rope drive rather than a propeller or external tow

This layout was inferred from the visible DiveEye competition camera: a
streamlined, rugby-ball-like enclosure around one rope, with a small arm
reaching the stabilising rope. The internal DiveEye mechanism was not
documented.

Wiral LITE was identified as the closest consumer reference architecture: a
compact, reversible camera carriage travelling quickly on a tensioned UHMWPE
line. It is useful as a blueprint, but the product itself is explicitly not
waterproof and would require substantial redesign rather than simple sealing.

## Drive system

A propeller was rejected because of delayed response, overshoot, turbulence,
and poor low-speed control. Passive towing was rejected because it requires an
operator who can see the athlete and can fall out of synchronisation.

The current direction is a custom pinch drive assembled from reusable
components:

- One brushed motor
- Reversible RC motor controller
- Polyurethane or rubber drive roller
- Spring-loaded idler
- Optional second mechanically synchronised drive roller if one contact point
  slips
- Wet, externally accessible rollers and guides
- Sealed electronics and motor enclosure
- Replaceable bearings, springs, and other chlorine-exposed components

A capstan was considered smoother and less prone to slipping, but required
more rope routing, a larger drum, guides, and more complex packaging. Pinch
drive remained the preferred first prototype.

The target speed implies approximately 380–760 RPM for a 50 mm drive wheel at
1–2 m/s. The suggested power figures—30–80 W cruising and 100–200 W peak—were
rough estimates rather than measured requirements.

## Track and materials

Dyneema/HMPE was preferred over stainless wire because it is lighter, easier
to handle, does not rust, and suits compliant pinch rollers. A jacketed or
coated line was suggested to improve handling and provide a more consistent
traction surface.

The exact rope diameter, separation, tension, roller profile, and pinch preload
remain unresolved.

## Tracking and control

The iPhone would perform one-dimensional visual servoing:

1. Detect a marker worn on the side of the diver.
2. Measure its horizontal position in the image.
3. Compare it with the desired framing position.
4. Command the rover to accelerate or decelerate along the rope.
5. Stop if the marker is lost or an end stop is reached.

Possible marker designs included fabric AprilTags, fluorescent strips, and
retroreflective strips illuminated from beside the camera. Because filming is
always from the side and hydrodynamic drag matters, a thin fabric or reflective
marker attached to the side of the suit became more relevant than a rigid
square marker. No marker was selected.

The suggested software stack was:

- AVFoundation for the camera
- Vision for tracking
- Swift for the iPhone application
- BLE commands to an adjacent ESP32
- Reversible brushed ESC for motor control
- Communication watchdog and physical end stops

The iPhone and controller would occupy separate waterproof enclosures. BLE
might work if their antennas are mounted directly beside each other with
almost no intervening water, but this requires testing.

## Rejected shortcuts

- Pool-cleaning and inspection robots: properly submersible but too slow
- Propeller-driven ROVs: insufficiently precise for smooth side tracking
- Amphibious stunt RC car: dual motors, uncertain two-metre waterproofing, and
  unsuitable wheels
- Rotated RC-car chassis: potentially useful mechanically, but still required
  extensive sealing and rope-specific rollers
- Powered rope ascenders and small winches: generally too slow
- Direct adaptation of Wiral LITE: not waterproof

## Editorial notes

The response repeatedly presented inferred DiveEye internals as likely facts,
supplied unverified prices and product speeds, and treated compressed estimates
as engineering specifications. It also incorrectly suggested that neutral
buoyancy reduces hydrodynamic drag.

AprilTag dimensions and detection ranges, BLE operation through two submerged
enclosures, suction-anchor capacity, motor power, and wet-rope traction all
need measurement. The chosen architecture and discarded alternatives are the
durable record; image-search placeholders, transient prices, and unsupported
certainty are omitted.
