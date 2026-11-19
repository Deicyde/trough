---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.EndpointData, ClassicalMechanics.HohmannOptimality.EndpointData.w, ClassicalMechanics.HohmannOptimality.EndpointData.impulse₁, ClassicalMechanics.HohmannOptimality.EndpointData.impulse₂, ClassicalMechanics.HohmannOptimality.EndpointData.cost, ClassicalMechanics.HohmannOptimality.EndpointData.feasible, ClassicalMechanics.HohmannOptimality.EndpointData.impulse₁_nonneg, ClassicalMechanics.HohmannOptimality.EndpointData.impulse₂_nonneg
statement: formalized
proof: formalized
---

# Optimality over normalized endpoint velocities

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.EndpointOptimality`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean): 17 declarations, 8 with a docstring.

> The Hohmann endpoint velocities minimize the total impulse.

## i. Overview

> Conservation of normalized energy and signed angular momentum supplies the endpoint constraints.
> Taking nonnegative square roots gives lower bounds for the two impulses and the equality
> conditions.

## ii. Key results

> - `endpoint_equality_characterization` gives the main result of this module.

## iv. References

> - [ref: hohmann\_prussing\_1992]. Prussing studies the two-impulse global comparison.

## A. The endpoint comparison and equality case

**`ClassicalMechanics.HohmannOptimality.EndpointData`**, a structure, [line 46](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L46).

> Two endpoint velocities in their own oriented radial/tangential frames.
> The two conservation equalities are endpoint constraints, NOT a theorem that
> arbitrary supplied data form a Kepler arc. Newton arcs are connected separately.

```lean
structure EndpointData (s : Shape) where
  /-- The normalized radial velocity at the inner endpoint. -/
  radial₁ : ℝ
  /-- The normalized prograde tangential velocity at the inner endpoint. -/
  tangent₁ : ℝ
  /-- The normalized radial velocity at the outer endpoint. -/
  radial₂ : ℝ
  /-- The normalized prograde tangential velocity at the outer endpoint. -/
  tangent₂ : ℝ
  /-- The endpoints have the same signed angular momentum. -/
  angular : tangent₂ = s.alpha * tangent₁
  /-- The endpoints have the same specific mechanical energy. -/
  energy : radial₁^2+tangent₁^2-2 = radial₂^2+tangent₂^2-2*s.alpha
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.w`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L63).

> Twice the normalized specific energy of the endpoint data.

```lean
def w {s : Shape} (z : EndpointData s) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.impulse₁`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L65).

> The departure impulse magnitude for the normalized endpoint data.

```lean
def impulse₁ {s : Shape} (z : EndpointData s) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.impulse₂`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L68).

> The arrival impulse magnitude for the normalized endpoint data.

```lean
def impulse₂ {s : Shape} (z : EndpointData s) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.cost`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L71).

> The sum of the impulse magnitudes for the specified transfer.

```lean
def cost {s : Shape} (z : EndpointData s) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.feasible`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L73).

```lean
lemma feasible {s : Shape} (z : EndpointData s) : s.Feasible z.w z.tangent₁
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.impulse₁_nonneg`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L80).

```lean
lemma impulse₁_nonneg {s : Shape} (z : EndpointData s) : 0 ≤ z.impulse₁
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.impulse₂_nonneg`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L82).

```lean
lemma impulse₂_nonneg {s : Shape} (z : EndpointData s) : 0 ≤ z.impulse₂
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.impulse₁_sq`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L84).

```lean
lemma impulse₁_sq {s : Shape} (z : EndpointData s) :
    z.impulse₁^2 = z.radial₁^2+(z.tangent₁-1)^2
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.impulse₂_sq`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L87).

```lean
lemma impulse₂_sq {s : Shape} (z : EndpointData s) :
    z.impulse₂^2 = z.radial₂^2+(z.tangent₂-s.circularOuter)^2
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.impulse₁_sq_invariant`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L90).

```lean
lemma impulse₁_sq_invariant {s : Shape} (z : EndpointData s) :
    z.impulse₁^2 = s.burnSquare₁ z.w z.tangent₁
```

**`ClassicalMechanics.HohmannOptimality.EndpointData.impulse₂_sq_invariant`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L95).

```lean
lemma impulse₂_sq_invariant {s : Shape} (z : EndpointData s) :
    z.impulse₂^2 = s.burnSquare₂ z.w z.tangent₁
```

**`ClassicalMechanics.HohmannOptimality.endpoint_impulses_lower_bound`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L107).

> A global inequality over ALL feasible endpoint velocities, not merely a
> stationary-point or small-perturbation calculation.

```lean
lemma endpoint_impulses_lower_bound (s : Shape) (z : EndpointData s) :
    s.burnH₁ ≤ z.impulse₁ ∧ s.burnH₂ ≤ z.impulse₂
```

**`ClassicalMechanics.HohmannOptimality.endpoint_total_lower_bound`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L117).

```lean
lemma endpoint_total_lower_bound (s : Shape) (z : EndpointData s) :
    s.costH ≤ z.cost
```

**`ClassicalMechanics.HohmannOptimality.hohmannEndpoints`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L123).

> A feasible corner achieving the lower bound; physical attainment is H1.

```lean
def hohmannEndpoints (s : Shape) : EndpointData s
```

**`ClassicalMechanics.HohmannOptimality.hohmannEndpoints_cost`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L131).

```lean
lemma hohmannEndpoints_cost (s : Shape) : (hohmannEndpoints s).cost = s.costH
```

**`ClassicalMechanics.HohmannOptimality.endpoint_equality_characterization`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean#L146).

> Equality forces both endpoint radial velocities to vanish and fixes signed
> angular momentum. No claim of uniqueness of flight time or orientation.

```lean
lemma endpoint_equality_characterization (s : Shape) (z : EndpointData s)
    (heq : z.cost = s.costH) :
    z.tangent₁ = s.hH ∧ z.tangent₂ = s.alpha*s.hH ∧
      z.radial₁ = 0 ∧ z.radial₂ = 0
```

## Depends on

- [Dimensionless Hohmann parameters](../part-02/hohmann-optimality-shape.md)

## Proof depends on

- [Lower bounds on the two Hohmann impulses](hohmann-optimality-endpointbounds.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointOptimality.lean)
