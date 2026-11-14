---
declaration: module
origin: cited
lean: Choquet.mix, Choquet.coe_mix, Choquet.half, Choquet.half_coe, Choquet.mixHalf, Choquet.continuous_mixHalf, Choquet.IsConvexFunction, Choquet.isConvexFunction_apply
statement: formalized
proof: formalized
---

# Mixtures in a convex set

The module `PhyslibAlpha.Mathematics.Convex.Choquet.Mixture`, [PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean): 11 declarations, 8 with a docstring.

> Mixtures of points in a convex set, convex functions, and extreme points as non-midpoints.

## i. Overview

> In a convex set `S` any two points can be mixed: `t x + (1 - t) y` lies in `S` for `0 ≤ t ≤ 1`. For
> states this means preparing `x` with probability `t` and `y` otherwise. A function on `S` is convex
> when its value at a mixture is at most the mixture of its values.
>
> A point of `S` is extreme when it is not a mixture of other points. For states, the extreme points
> are the pure states. A point that is not extreme is the midpoint of two different points of `S`.

## ii. Key results

> - `Choquet.mix` is the mixture of two points of a convex set.
> - `Choquet.IsConvexFunction` states that a function on `S` lies below its chords.
> - `Choquet.exists_mixHalf_eq_of_notMem_extremePoints` proves that a point that is not extreme is the
>   midpoint of two different points.

## iv. References

> * None.

## A. Mixtures

**`Choquet.mix`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L60).

> The mixture `t x + (1 - t) y` of two points of a convex set.

```lean
def mix (x y : S) (t : unitInterval) : S
```

**`Choquet.coe_mix`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L63).

```lean
lemma coe_mix (x y : S) (t : unitInterval) :
    (mix hS x y t : V) = (t : ℝ) • (x : V) + (1 - (t : ℝ)) • (y : V)
```

**`Choquet.half`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L67).

> The weight `1/2`.

```lean
noncomputable def half : unitInterval
```

**`Choquet.half_coe`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L69).

```lean
lemma half_coe : (half : ℝ) = 1 / 2
```

**`Choquet.mixHalf`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L72).

> The midpoint of a pair of points.

```lean
noncomputable def mixHalf (p : S × S) : S
```

**`Choquet.continuous_mixHalf`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L74).

```lean
lemma continuous_mixHalf [TopologicalSpace V] [IsTopologicalAddGroup V] [ContinuousSMul ℝ V] :
    Continuous (mixHalf hS)
```

## B. Convex functions

**`Choquet.IsConvexFunction`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L87).

> A function on `S` lying below the chord of every mixture.

```lean
def IsConvexFunction (f : S → ℝ) : Prop
```

**`Choquet.isConvexFunction_apply`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L91).

> Continuous linear functionals are convex on `S`.

```lean
lemma isConvexFunction_apply [TopologicalSpace V] (ℓ : V →L[ℝ] ℝ) :
    IsConvexFunction hS fun y => ℓ y
```

## C. Extreme points as non-midpoints

**`Choquet.mixHalf_notMem_extremePoints`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L101).

> The midpoint of two distinct points is not extreme.

```lean
lemma mixHalf_notMem_extremePoints {p q : S} (hpq : p ≠ q) :
    (mixHalf hS (p, q) : V) ∉ S.extremePoints ℝ
```

**`Choquet.sub_smul_eq_of_mixHalf`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L108).

> Two points of `S` on either side of `a x₁ + b x₂` at weight distance `min a b`.

```lean
lemma sub_smul_eq_of_mixHalf {x₁ x₂ : V} {a b r : ℝ} :
    ((a + r) • x₁ + (b - r) • x₂) - ((a - r) • x₁ + (b + r) • x₂) = (2 * r) • (x₁ - x₂)
```

**`Choquet.exists_mixHalf_eq_of_notMem_extremePoints`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean#L113).

> A non-extreme point of `S` is the midpoint of two distinct points of `S`.

```lean
lemma exists_mixHalf_eq_of_notMem_extremePoints {x : S} (hx : (x : V) ∉ S.extremePoints ℝ) :
    ∃ p q : S, p ≠ q ∧ mixHalf hS (p, q) = x
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/Mixture.lean)
