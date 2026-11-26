---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.periSpeed, ClassicalMechanics.HohmannTransfer.apoSpeed, ClassicalMechanics.HohmannTransfer.periSpeed_pos, ClassicalMechanics.HohmannTransfer.apoSpeed_pos, ClassicalMechanics.HohmannTransfer.position_departure, ClassicalMechanics.HohmannTransfer.position_arrival, ClassicalMechanics.HohmannTransfer.velocity_departure, ClassicalMechanics.HohmannTransfer.velocity_arrival
statement: formalized
proof: formalized
---

# Apsidal speeds on the Hohmann ellipse

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Endpoints`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean): 14 declarations, 2 with a docstring.

> The transfer velocity is tangential at both apses.

## i. Overview

> Evaluating the actual time derivative at departure and arrival gives the periapsis and apoapsis
> speeds. These speeds admit closed forms in the two orbital radii.

## ii. Key results

> - `periSpeed_formula` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. Positions and velocities at the apses

**`ClassicalMechanics.HohmannTransfer.periSpeed`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L42).

> The transfer speed at periapsis.

```lean
def periSpeed (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.apoSpeed`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L44).

> The transfer speed at apoapsis.

```lean
def apoSpeed (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.periSpeed_pos`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L46).

```lean
lemma periSpeed_pos (p : Parameters) : 0 < periSpeed p
```

**`ClassicalMechanics.HohmannTransfer.apoSpeed_pos`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L48).

```lean
lemma apoSpeed_pos (p : Parameters) : 0 < apoSpeed p
```

**`ClassicalMechanics.HohmannTransfer.position_departure`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L50).

```lean
lemma position_departure (p : Parameters) : position p 0 = pack p.r₁ 0
```

**`ClassicalMechanics.HohmannTransfer.position_arrival`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L52).

```lean
lemma position_arrival (p : Parameters) :
    position p p.transferTime = pack (-p.r₂) 0
```

**`ClassicalMechanics.HohmannTransfer.velocity_departure`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L54).

```lean
lemma velocity_departure (p : Parameters) : velocity p 0 = pack 0 (periSpeed p)
```

**`ClassicalMechanics.HohmannTransfer.velocity_arrival`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L56).

```lean
lemma velocity_arrival (p : Parameters) :
    velocity p p.transferTime = pack 0 (-apoSpeed p)
```

**`ClassicalMechanics.HohmannTransfer.periSpeed_sq`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L62).

```lean
lemma periSpeed_sq (p : Parameters) :
    periSpeed p ^ 2 = 2*p.mu*p.r₂/(p.r₁*(p.r₁+p.r₂))
```

**`ClassicalMechanics.HohmannTransfer.apoSpeed_sq`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L77).

```lean
lemma apoSpeed_sq (p : Parameters) :
    apoSpeed p ^ 2 = 2*p.mu*p.r₁/(p.r₂*(p.r₁+p.r₂))
```

**`ClassicalMechanics.HohmannTransfer.periSpeed_formula`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L89).

```lean
lemma periSpeed_formula (p : Parameters) :
    periSpeed p = Real.sqrt (2*p.mu*p.r₂/(p.r₁*(p.r₁+p.r₂)))
```

**`ClassicalMechanics.HohmannTransfer.apoSpeed_formula`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L98).

```lean
lemma apoSpeed_formula (p : Parameters) :
    apoSpeed p = Real.sqrt (2*p.mu*p.r₁/(p.r₂*(p.r₁+p.r₂)))
```

**`ClassicalMechanics.HohmannTransfer.norm_velocity_departure`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L107).

```lean
lemma norm_velocity_departure (p : Parameters) : ‖velocity p 0‖ = periSpeed p
```

**`ClassicalMechanics.HohmannTransfer.norm_velocity_arrival`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean#L109).

```lean
lemma norm_velocity_arrival (p : Parameters) :
    ‖velocity p p.transferTime‖ = apoSpeed p
```

## Depends on

- [Time derivatives of the Hohmann ellipse](hohmann-dynamics-differentiation.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Endpoints.lean)
