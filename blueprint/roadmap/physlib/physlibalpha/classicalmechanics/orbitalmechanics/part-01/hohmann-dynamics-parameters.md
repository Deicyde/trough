---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.Parameters, ClassicalMechanics.HohmannTransfer.Parameters.a, ClassicalMechanics.HohmannTransfer.Parameters.e, ClassicalMechanics.HohmannTransfer.Parameters.b, ClassicalMechanics.HohmannTransfer.Parameters.n, ClassicalMechanics.HohmannTransfer.Parameters.transferTime, ClassicalMechanics.HohmannTransfer.Parameters.r₂_pos, ClassicalMechanics.HohmannTransfer.Parameters.sum_pos
statement: formalized
proof: formalized
---

# Parameters of an outward Hohmann transfer

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Parameters`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean): 28 declarations, 6 with a docstring.

> The two circular radii determine the transfer ellipse.

## i. Overview

> The central gravitational parameter and the two radii determine the semiaxes, eccentricity, mean
> motion and half-period.

## ii. Key results

> - `Parameters.transferTime_eq` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. Elliptic geometry and transfer time

**`ClassicalMechanics.HohmannTransfer.Parameters`**, a structure, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L52).

> The positive gravitational parameter and the ordered circular radii.

```lean
structure Parameters where
  /-- The central gravitational parameter. -/
  mu : ℝ
  /-- The radius of the inner circular orbit. -/
  r₁ : ℝ
  /-- The radius of the outer circular orbit. -/
  r₂ : ℝ
  /-- The gravitational parameter is positive. -/
  mu_pos : 0 < mu
  /-- The inner radius is positive. -/
  r₁_pos : 0 < r₁
  /-- The outer radius exceeds the inner radius. -/
  outward : r₁ < r₂
```

**`ClassicalMechanics.HohmannTransfer.Parameters.a`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L69).

> The semimajor axis of the transfer ellipse.

```lean
def a (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.Parameters.e`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L71).

> The eccentricity of the transfer ellipse.

```lean
def e (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.Parameters.b`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L73).

> The semiminor axis of the transfer ellipse.

```lean
def b (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.Parameters.n`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L75).

> The mean motion of the transfer ellipse.

```lean
def n (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.Parameters.transferTime`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L77).

> The time to coast from periapsis to apoapsis.

```lean
def transferTime (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.Parameters.r₂_pos`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L79).

```lean
lemma r₂_pos (p : Parameters) : 0 < p.r₂
```

**`ClassicalMechanics.HohmannTransfer.Parameters.sum_pos`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L80).

```lean
lemma sum_pos (p : Parameters) : 0 < p.r₁ + p.r₂
```

**`ClassicalMechanics.HohmannTransfer.Parameters.a_pos`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L81).

```lean
lemma a_pos (p : Parameters) : 0 < p.a
```

**`ClassicalMechanics.HohmannTransfer.Parameters.e_pos`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L82).

```lean
lemma e_pos (p : Parameters) : 0 < p.e
```

**`ClassicalMechanics.HohmannTransfer.Parameters.e_lt_one`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L83).

```lean
lemma e_lt_one (p : Parameters) : p.e < 1
```

**`ClassicalMechanics.HohmannTransfer.Parameters.b_pos`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L87).

```lean
lemma b_pos (p : Parameters) : 0 < p.b
```

**`ClassicalMechanics.HohmannTransfer.Parameters.b_sq`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L89).

```lean
lemma b_sq (p : Parameters) : p.b ^ 2 = p.r₁ * p.r₂
```

**`ClassicalMechanics.HohmannTransfer.Parameters.n_pos`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L91).

```lean
lemma n_pos (p : Parameters) : 0 < p.n
```

**`ClassicalMechanics.HohmannTransfer.Parameters.n_sq`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L93).

```lean
lemma n_sq (p : Parameters) : p.n ^ 2 = p.mu / p.a ^ 3
```

**`ClassicalMechanics.HohmannTransfer.Parameters.a_ne`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L95).

```lean
lemma a_ne (p : Parameters) : p.a ≠ 0
```

**`ClassicalMechanics.HohmannTransfer.Parameters.n_ne`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L96).

```lean
lemma n_ne (p : Parameters) : p.n ≠ 0
```

**`ClassicalMechanics.HohmannTransfer.Parameters.r₁_ne`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L97).

```lean
lemma r₁_ne (p : Parameters) : p.r₁ ≠ 0
```

**`ClassicalMechanics.HohmannTransfer.Parameters.r₂_ne`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L98).

```lean
lemma r₂_ne (p : Parameters) : p.r₂ ≠ 0
```

**`ClassicalMechanics.HohmannTransfer.Parameters.one_sub_e_pos`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L99).

```lean
lemma one_sub_e_pos (p : Parameters) : 0 < 1 - p.e
```

**`ClassicalMechanics.HohmannTransfer.Parameters.one_add_e_pos`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L100).

```lean
lemma one_add_e_pos (p : Parameters) : 0 < 1 + p.e
```

**`ClassicalMechanics.HohmannTransfer.Parameters.a_mul_one_sub_e`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L101).

```lean
lemma a_mul_one_sub_e (p : Parameters) : p.a * (1 - p.e) = p.r₁
```

**`ClassicalMechanics.HohmannTransfer.Parameters.a_mul_one_add_e`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L105).

```lean
lemma a_mul_one_add_e (p : Parameters) : p.a * (1 + p.e) = p.r₂
```

**`ClassicalMechanics.HohmannTransfer.Parameters.b_sq_ellipse`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L109).

```lean
lemma b_sq_ellipse (p : Parameters) : p.b ^ 2 = p.a ^ 2 * (1 - p.e ^ 2)
```

**`ClassicalMechanics.HohmannTransfer.Parameters.n_sq_mul_a_cube`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L114).

```lean
lemma n_sq_mul_a_cube (p : Parameters) : p.n ^ 2 * p.a ^ 3 = p.mu
```

**`ClassicalMechanics.HohmannTransfer.Parameters.transferTime_pos`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L117).

```lean
lemma transferTime_pos (p : Parameters) : 0 < p.transferTime
```

**`ClassicalMechanics.HohmannTransfer.Parameters.transferTime_sq`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L119).

```lean
lemma transferTime_sq (p : Parameters) :
    p.transferTime ^ 2 * p.mu = Real.pi ^ 2 * p.a ^ 3
```

**`ClassicalMechanics.HohmannTransfer.Parameters.transferTime_eq`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean#L125).

```lean
lemma transferTime_eq (p : Parameters) :
    p.transferTime = Real.pi * Real.sqrt (p.a ^ 3 / p.mu)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Parameters.lean)
