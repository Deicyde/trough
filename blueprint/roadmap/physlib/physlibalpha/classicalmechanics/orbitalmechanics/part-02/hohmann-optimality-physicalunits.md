---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.Units, ClassicalMechanics.HohmannOptimality.Units.r₂_pos, ClassicalMechanics.HohmannOptimality.Units.r₁_ne, ClassicalMechanics.HohmannOptimality.Units.r₂_ne, ClassicalMechanics.HohmannOptimality.Units.shape, ClassicalMechanics.HohmannOptimality.Units.speed, ClassicalMechanics.HohmannOptimality.Units.circular₂, ClassicalMechanics.HohmannOptimality.Units.bound
statement: formalized
proof: formalized
---

# Restoring physical units to the Hohmann bounds

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.PhysicalUnits`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean): 19 declarations, 8 with a docstring.

> The normalized lower bound scales by the inner circular speed.

## i. Overview

> The physical radial and tangential endpoint components are normalized by the inner circular
> speed. The cost scales linearly and the feasibility equations are preserved.

## ii. Key results

> - `PhysicalEndpoints.physical_lower_bound` gives the main result of this module.

## iv. References

> - [ref: hohmann\_prussing\_1992]. Prussing studies the two-impulse global comparison.

## A. Physical endpoint data and normalization

**`ClassicalMechanics.HohmannOptimality.Units`**, a structure, [line 42](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L42).

> The gravitational parameter and the ordered physical radii for the comparison.

```lean
structure Units where
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

**`ClassicalMechanics.HohmannOptimality.Units.r₂_pos`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L58).

```lean
lemma r₂_pos (p : Units) : 0 < p.r₂
```

**`ClassicalMechanics.HohmannOptimality.Units.r₁_ne`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L59).

```lean
lemma r₁_ne (p : Units) : p.r₁ ≠ 0
```

**`ClassicalMechanics.HohmannOptimality.Units.r₂_ne`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L60).

```lean
lemma r₂_ne (p : Units) : p.r₂ ≠ 0
```

**`ClassicalMechanics.HohmannOptimality.Units.shape`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L63).

> The reciprocal radius ratio associated with the physical radii.

```lean
def shape (p : Units) : Shape
```

**`ClassicalMechanics.HohmannOptimality.Units.speed`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L69).

> The inner circular speed used as the unit of velocity.

```lean
def speed (p : Units) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Units.circular₂`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L71).

> The outer circular speed in physical units.

```lean
def circular₂ (p : Units) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Units.bound`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L73).

> The Hohmann cost bound in physical units.

```lean
def bound (p : Units) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Units.speed_pos`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L75).

```lean
lemma speed_pos (p : Units) : 0 < p.speed
```

**`ClassicalMechanics.HohmannOptimality.Units.speed_ne`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L76).

```lean
lemma speed_ne (p : Units) : p.speed ≠ 0
```

**`ClassicalMechanics.HohmannOptimality.Units.speed_sq`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L77).

```lean
lemma speed_sq (p : Units) : p.speed^2 = p.mu/p.r₁
```

**`ClassicalMechanics.HohmannOptimality.Units.mu_over_r₂`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L79).

```lean
lemma mu_over_r₂ (p : Units) : p.mu/p.r₂ = p.shape.alpha*p.speed^2
```

**`ClassicalMechanics.HohmannOptimality.Units.circular₂_eq_sqrt`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L84).

```lean
lemma circular₂_eq_sqrt (p : Units) : p.circular₂ = Real.sqrt (p.mu/p.r₂)
```

**`ClassicalMechanics.HohmannOptimality.PhysicalEndpoints`**, a structure, [line 98](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L98).

> Physical endpoint velocities sharing the same energy and angular momentum.

```lean
structure PhysicalEndpoints (p : Units) where
  /-- The radial velocity at the inner endpoint. -/
  radial₁ : ℝ
  /-- The prograde tangential velocity at the inner endpoint. -/
  tangent₁ : ℝ
  /-- The radial velocity at the outer endpoint. -/
  radial₂ : ℝ
  /-- The prograde tangential velocity at the outer endpoint. -/
  tangent₂ : ℝ
  /-- The endpoints have the same signed angular momentum. -/
  angular : p.r₁*tangent₁ = p.r₂*tangent₂
  /-- The endpoints have the same specific mechanical energy. -/
  energy : radial₁^2+tangent₁^2-2*p.mu/p.r₁ =
    radial₂^2+tangent₂^2-2*p.mu/p.r₂
```

**`ClassicalMechanics.HohmannOptimality.PhysicalEndpoints.cost`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L116).

> The sum of the impulse magnitudes for the specified transfer.

```lean
def cost {p : Units} (z : PhysicalEndpoints p) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.PhysicalEndpoints.normalized`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L121).

> The endpoint data expressed in the inner radius and circular speed units.

```lean
def normalized {p : Units} (z : PhysicalEndpoints p) : EndpointData p.shape
```

**`ClassicalMechanics.HohmannOptimality.PhysicalEndpoints.norm_scale`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L141).

```lean
lemma norm_scale (a b v : ℝ) (hv : 0 < v) :
    v*Real.sqrt ((a/v)^2+(b/v)^2) = Real.sqrt (a^2+b^2)
```

**`ClassicalMechanics.HohmannOptimality.PhysicalEndpoints.cost_eq_scaled`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L152).

```lean
lemma cost_eq_scaled {p : Units} (z : PhysicalEndpoints p) :
    z.cost = p.speed*z.normalized.cost
```

**`ClassicalMechanics.HohmannOptimality.PhysicalEndpoints.physical_lower_bound`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean#L164).

```lean
lemma physical_lower_bound {p : Units} (z : PhysicalEndpoints p) : p.bound ≤ z.cost
```

## Depends on

- [Optimality over normalized endpoint velocities](../part-01/hohmann-optimality-endpointoptimality.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PhysicalUnits.lean)
