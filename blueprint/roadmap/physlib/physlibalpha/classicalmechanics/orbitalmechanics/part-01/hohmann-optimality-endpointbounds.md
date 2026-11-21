---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.gap₁_low, ClassicalMechanics.HohmannOptimality.gap₁_high, ClassicalMechanics.HohmannOptimality.gap₂_low, ClassicalMechanics.HohmannOptimality.gap₂_high, ClassicalMechanics.HohmannOptimality.low_factor₁_pos, ClassicalMechanics.HohmannOptimality.low_factor₂_pos, ClassicalMechanics.HohmannOptimality.high_factor₁_pos, ClassicalMechanics.HohmannOptimality.high_factor₂_pos
statement: formalized
proof: formalized
---

# Lower bounds on the two Hohmann impulses

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.EndpointBounds`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean): 12 declarations, 4 with a docstring.

> Each impulse has a lower bound over the feasible invariant pairs.

## i. Overview

> Split the comparison by signed angular momentum relative to the Hohmann value. Factoring the cost
> difference gives a sum of nonnegative terms in each case.

## ii. Key results

> - `first_square_lower_bound` gives the main result of this module.

## iv. References

> - [ref: hohmann\_prussing\_1992]. Prussing studies the two-impulse global comparison.

## A. The two squared cost inequalities

**`ClassicalMechanics.HohmannOptimality.gap₁_low`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L43).

> Exact nonnegative certificate on the h ≤ hH half-plane.

```lean
lemma gap₁_low (s : Shape) (w h : ℝ) :
    s.burnSquare₁ w h - s.burnH₁ ^ 2 =
      (w + 2*s.alpha - s.alpha^2*h^2) +
      (s.hH-h)*(2-s.alpha^2*(h+s.hH))
```

**`ClassicalMechanics.HohmannOptimality.gap₁_high`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L50).

```lean
lemma gap₁_high (s : Shape) (w h : ℝ) :
    s.burnSquare₁ w h - s.burnH₁ ^ 2 =
      (w+2-h^2) + (h-s.hH)*(h+s.hH-2)
```

**`ClassicalMechanics.HohmannOptimality.gap₂_low`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L56).

```lean
lemma gap₂_low (s : Shape) (w h : ℝ) :
    s.burnSquare₂ w h - s.burnH₂ ^ 2 =
      (w+2*s.alpha-s.alpha^2*h^2) +
      s.alpha*(s.hH-h)*(2*s.circularOuter-s.alpha*(h+s.hH))
```

**`ClassicalMechanics.HohmannOptimality.gap₂_high`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L63).

```lean
lemma gap₂_high (s : Shape) (w h : ℝ) :
    s.burnSquare₂ w h - s.burnH₂ ^ 2 =
      (w+2-h^2) + (h-s.hH)*(h+s.hH-2*s.alpha*s.circularOuter)
```

**`ClassicalMechanics.HohmannOptimality.low_factor₁_pos`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L69).

```lean
lemma low_factor₁_pos (s : Shape) {h : ℝ} (hh : h ≤ s.hH) :
    0 < 2 - s.alpha^2*(h+s.hH)
```

**`ClassicalMechanics.HohmannOptimality.low_factor₂_pos`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L73).

```lean
lemma low_factor₂_pos (s : Shape) {h : ℝ} (hh : h ≤ s.hH) :
    0 < 2*s.circularOuter-s.alpha*(h+s.hH)
```

**`ClassicalMechanics.HohmannOptimality.high_factor₁_pos`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L77).

```lean
lemma high_factor₁_pos (s : Shape) {h : ℝ} (hh : s.hH ≤ h) :
    0 < h+s.hH-2
```

**`ClassicalMechanics.HohmannOptimality.high_factor₂_pos`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L79).

```lean
lemma high_factor₂_pos (s : Shape) {h : ℝ} (hh : s.hH ≤ h) :
    0 < h+s.hH-2*s.alpha*s.circularOuter
```

**`ClassicalMechanics.HohmannOptimality.first_square_lower_bound`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L83).

> Every feasible competitor pays at least the Hohmann first impulse.

```lean
lemma first_square_lower_bound (s : Shape) {w h : ℝ} (hf : s.Feasible w h) :
    s.burnH₁ ^ 2 ≤ s.burnSquare₁ w h
```

**`ClassicalMechanics.HohmannOptimality.second_square_lower_bound`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L97).

> The second impulse separately also attains its global minimum at Hohmann.

```lean
lemma second_square_lower_bound (s : Shape) {w h : ℝ} (hf : s.Feasible w h) :
    s.burnH₂ ^ 2 ≤ s.burnSquare₂ w h
```

**`ClassicalMechanics.HohmannOptimality.first_square_strict_of_h_ne`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L112).

```lean
lemma first_square_strict_of_h_ne (s : Shape) {w h : ℝ}
    (hf : s.Feasible w h) (hne : h ≠ s.hH) :
    s.burnH₁ ^ 2 < s.burnSquare₁ w h
```

**`ClassicalMechanics.HohmannOptimality.invariant_pair_of_first_square_eq`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean#L125).

> The unique minimizer is an invariant pair, not a unique time-parametrized
> trajectory: rotations and extra revolutions still have the same cost.

```lean
lemma invariant_pair_of_first_square_eq (s : Shape) {w h : ℝ}
    (hf : s.Feasible w h) (heq : s.burnSquare₁ w h = s.burnH₁^2) :
    h = s.hH ∧ w = s.energyH
```

## Depends on

- [Dimensionless Hohmann parameters](../part-02/hohmann-optimality-shape.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/EndpointBounds.lean)
