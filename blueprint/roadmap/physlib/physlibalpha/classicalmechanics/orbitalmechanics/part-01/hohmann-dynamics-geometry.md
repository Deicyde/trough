---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.D, ClassicalMechanics.HohmannTransfer.radial, ClassicalMechanics.HohmannTransfer.ellipse, ClassicalMechanics.HohmannTransfer.velocityAtAnomaly, ClassicalMechanics.HohmannTransfer.D_lower, ClassicalMechanics.HohmannTransfer.D_upper, ClassicalMechanics.HohmannTransfer.D_pos, ClassicalMechanics.HohmannTransfer.D_ne
statement: formalized
proof: formalized
---

# Geometry of the Hohmann ellipse

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Geometry`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean): 18 declarations, 4 with a docstring.

> The eccentric anomaly parameterizes the transfer ellipse.

## i. Overview

> The attracting centre is at the origin. The distance from the focus lies between the two circular
> radii, with equality at the two apses.

## ii. Key results

> - `norm_ellipse` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. The ellipse and its apses

**`ClassicalMechanics.HohmannTransfer.D`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L43).

> The focus distance divided by the semimajor axis.

```lean
def D (p : Parameters) (u : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.radial`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L45).

> The distance from the attracting focus at a given eccentric anomaly.

```lean
def radial (p : Parameters) (u : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.ellipse`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L47).

> The position on the transfer ellipse at the given eccentric anomaly.

```lean
def ellipse (p : Parameters) (u : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.velocityAtAnomaly`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L50).

> The physical velocity on the transfer ellipse at the given anomaly.

```lean
def velocityAtAnomaly (p : Parameters) (u : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.D_lower`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L54).

```lean
lemma D_lower (p : Parameters) (u : ℝ) : 1 - p.e ≤ D p u
```

**`ClassicalMechanics.HohmannTransfer.D_upper`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L57).

```lean
lemma D_upper (p : Parameters) (u : ℝ) : D p u ≤ 1 + p.e
```

**`ClassicalMechanics.HohmannTransfer.D_pos`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L60).

```lean
lemma D_pos (p : Parameters) (u : ℝ) : 0 < D p u
```

**`ClassicalMechanics.HohmannTransfer.D_ne`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L62).

```lean
lemma D_ne (p : Parameters) (u : ℝ) : D p u ≠ 0
```

**`ClassicalMechanics.HohmannTransfer.radial_pos`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L63).

```lean
lemma radial_pos (p : Parameters) (u : ℝ) : 0 < radial p u
```

**`ClassicalMechanics.HohmannTransfer.ellipse_squared_radius`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L65).

```lean
lemma ellipse_squared_radius (p : Parameters) (u : ℝ) :
    (ellipse p u).re ^ 2 + (ellipse p u).im ^ 2 = (radial p u)^2
```

**`ClassicalMechanics.HohmannTransfer.norm_ellipse`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L76).

```lean
lemma norm_ellipse (p : Parameters) (u : ℝ) : ‖ellipse p u‖ = radial p u
```

**`ClassicalMechanics.HohmannTransfer.radial_bounds`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L79).

```lean
lemma radial_bounds (p : Parameters) (u : ℝ) :
    p.r₁ ≤ radial p u ∧ radial p u ≤ p.r₂
```

**`ClassicalMechanics.HohmannTransfer.ellipse_ne_zero`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L86).

```lean
lemma ellipse_ne_zero (p : Parameters) (u : ℝ) : ellipse p u ≠ 0
```

**`ClassicalMechanics.HohmannTransfer.D_zero`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L91).

```lean
lemma D_zero (p : Parameters) : D p 0 = 1 - p.e
```

**`ClassicalMechanics.HohmannTransfer.D_pi`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L92).

```lean
lemma D_pi (p : Parameters) : D p Real.pi = 1 + p.e
```

**`ClassicalMechanics.HohmannTransfer.ellipse_zero`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L93).

```lean
lemma ellipse_zero (p : Parameters) : ellipse p 0 = pack p.r₁ 0
```

**`ClassicalMechanics.HohmannTransfer.ellipse_pi`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L96).

```lean
lemma ellipse_pi (p : Parameters) : ellipse p Real.pi = pack (-p.r₂) 0
```

**`ClassicalMechanics.HohmannTransfer.ellipse_periodic`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean#L99).

```lean
lemma ellipse_periodic (p : Parameters) : Function.Periodic (ellipse p) (2*Real.pi)
```

## Depends on

- [Parameters of an outward Hohmann transfer](hohmann-dynamics-parameters.md)
- [Planar coordinates for the Hohmann transfer](hohmann-dynamics-plane.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Geometry.lean)
