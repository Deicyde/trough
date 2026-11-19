---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.circularRate, ClassicalMechanics.HohmannTransfer.circularSpeed, ClassicalMechanics.HohmannTransfer.circularPosition, ClassicalMechanics.HohmannTransfer.circularVelocity, ClassicalMechanics.HohmannTransfer.circularRate_pos, ClassicalMechanics.HohmannTransfer.circularRate_sq, ClassicalMechanics.HohmannTransfer.circularSpeed_pos, ClassicalMechanics.HohmannTransfer.circularSpeed_sq
statement: formalized
proof: formalized
---

# Circular orbits for the Hohmann transfer

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Circular`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean): 13 declarations, 4 with a docstring.

> The two circular coasts obey the same central force law.

## i. Overview

> A circular orbit rotates uniformly at the rate determined by the radius and gravitational
> parameter. The phase is free so its position can meet the transfer ellipse at an apsis.

## ii. Key results

> - `circular_newton` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. Circular positions, velocities, and accelerations

**`ClassicalMechanics.HohmannTransfer.circularRate`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L44).

> The angular rate of a circular orbit of radius `R`.

```lean
def circularRate (mu R : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.circularSpeed`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L46).

> The speed of a circular orbit of radius `R`.

```lean
def circularSpeed (mu R : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.circularPosition`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L48).

> The position on a prograde circle with the given initial phase.

```lean
def circularPosition (mu R phase t : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.circularVelocity`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L52).

> The velocity on a prograde circle with the given initial phase.

```lean
def circularVelocity (mu R phase t : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.circularRate_pos`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L56).

```lean
lemma circularRate_pos {mu R : ℝ} (hm : 0 < mu) (hR : 0 < R) :
    0 < circularRate mu R
```

**`ClassicalMechanics.HohmannTransfer.circularRate_sq`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L58).

```lean
lemma circularRate_sq {mu R : ℝ} (hm : 0 < mu) (hR : 0 < R) :
    circularRate mu R ^ 2 = mu/R^3
```

**`ClassicalMechanics.HohmannTransfer.circularSpeed_pos`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L61).

```lean
lemma circularSpeed_pos {mu R : ℝ} (hm : 0 < mu) (hR : 0 < R) :
    0 < circularSpeed mu R
```

**`ClassicalMechanics.HohmannTransfer.circularSpeed_sq`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L63).

```lean
lemma circularSpeed_sq {mu R : ℝ} (hm : 0 < mu) (hR : 0 < R) :
    circularSpeed mu R ^ 2 = mu/R
```

**`ClassicalMechanics.HohmannTransfer.circularSpeed_eq_rate`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L66).

```lean
lemma circularSpeed_eq_rate {mu R : ℝ} (hm : 0 < mu) (hR : 0 < R) :
    R*circularRate mu R = circularSpeed mu R
```

**`ClassicalMechanics.HohmannTransfer.norm_circularPosition`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L71).

```lean
lemma norm_circularPosition {mu R : ℝ} (hR : 0 < R) (phase t : ℝ) :
    ‖circularPosition mu R phase t‖ = R
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_circularPosition`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L76).

```lean
lemma hasDerivAt_circularPosition (mu R phase t : ℝ) :
    HasDerivAt (circularPosition mu R phase) (circularVelocity mu R phase t) t
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_circularVelocity`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L84).

```lean
lemma hasDerivAt_circularVelocity (mu R phase t : ℝ) :
    HasDerivAt (circularVelocity mu R phase)
      (-(circularRate mu R)^2 • circularPosition mu R phase t) t
```

**`ClassicalMechanics.HohmannTransfer.circular_newton`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean#L95).

```lean
lemma circular_newton {mu R : ℝ} (hm : 0 < mu) (hR : 0 < R)
    (phase t : ℝ) :
    deriv (deriv (circularPosition mu R phase)) t =
      -(mu/‖circularPosition mu R phase t‖^3) • circularPosition mu R phase t
```

## Depends on

- [Planar coordinates for the Hohmann transfer](hohmann-dynamics-plane.md)

## Proof depends on

- [Circular Orbit Vis Viva](../../../../physlib/classicalmechanics/orbitalmechanics/visviva.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Circular.lean)
