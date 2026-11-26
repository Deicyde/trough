---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.global_two_impulse_endpoint_optimality, ClassicalMechanics.HohmannOptimality.global_two_impulse_newton_lower_bound, ClassicalMechanics.HohmannOptimality.finite_three_impulse_counterexample
statement: formalized
proof: formalized
---

# Global two-impulse Hohmann bounds

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.PublicStatement`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PublicStatement.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PublicStatement.lean): 3 declarations, 3 with a docstring.

> Every allowed Newtonian comparison arc satisfies the Hohmann lower bound.

## i. Overview

> The global comparison is over two impulses between coplanar circular orbits with the same
> orientation. The coast has free time and phase. A finite three-impulse cost comparison
> distinguishes the larger class.

## ii. Key results

> - `global_two_impulse_newton_lower_bound` gives the main result of this module.

## iv. References

> - [ref: hohmann\_prussing\_1992]. Prussing studies the two-impulse global comparison.

## A. The lower bound and the finite cost comparison

**`ClassicalMechanics.HohmannOptimality.global_two_impulse_endpoint_optimality`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PublicStatement.lean#L45).

> Global means all feasible TWO-impulse, coplanar, co-oriented circle-to-circle
> transfers, with free departure phase and flight time. A coast may have radial
> velocity, negative momentum, or nonnegative energy. No third burn is allowed.

```lean
lemma global_two_impulse_endpoint_optimality (s : Shape) :
    (∀ z : EndpointData s, s.costH ≤ z.cost) ∧
    (hohmannEndpoints s).cost=s.costH ∧
    (∀ z : EndpointData s, z.cost=s.costH →
      z.tangent₁=s.hH ∧ z.tangent₂=s.alpha*s.hH ∧
      z.radial₁=0 ∧ z.radial₂=0)
```

**`ClassicalMechanics.HohmannOptimality.global_two_impulse_newton_lower_bound`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PublicStatement.lean#L56).

> The global inequality applies to genuinely differentiable Newtonian coast
> arcs; conservation is proved in KeplerConservation rather than postulated.

```lean
lemma global_two_impulse_newton_lower_bound (p : Units) (a : KeplerArc p.mu)
    (h₀ : (a.state a.t₀).radius=p.r₁) (h₁ : (a.state a.t₁).radius=p.r₂) :
    p.bound ≤ (a.state a.t₀).impulse p.speed+(a.state a.t₁).impulse p.circular₂
```

**`ClassicalMechanics.HohmannOptimality.finite_three_impulse_counterexample`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PublicStatement.lean#L63).

> An unrestricted all-maneuver assertion is false: a finite 1→64→16
> bielliptic construction has strictly smaller delta-v than Hohmann 1→16.

```lean
lemma finite_three_impulse_counterexample :
    (9/1000 : ℝ) < Bielliptic.hohmannCost 16 - Bielliptic.cost Bielliptic.«example»
```

## Depends on

- [The cost of a finite bielliptic transfer](../part-01/hohmann-optimality-bielliptic.md)
- [Kepler conservation and two-impulse bounds](hohmann-optimality-keplerconservation.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PublicStatement.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PublicStatement.lean)
