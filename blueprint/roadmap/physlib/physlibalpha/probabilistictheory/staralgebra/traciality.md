---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.Weight.IsTracial, PhyslibAlpha.ProbabilisticTheory.Weight.IsTracial.toPositiveLinearMap_star_mul_self, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.IsTracial, PhyslibAlpha.ProbabilisticTheory.Weight.IsState.isTracial, PhyslibAlpha.ProbabilisticTheory.LinearMap.IsTracial, PhyslibAlpha.ProbabilisticTheory.LinearMap.isTracial_iff_star_mul_self_eq_mul_star_self
statement: formalized
proof: formalized
---

# Tracial states and weights

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.Traciality`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean): 6 declarations, 6 with a docstring.

> Tracial weights and tracial states.

## i. Overview

> A state `ω` is tracial when `ω (a⋆ a) = ω (a a⋆)`. For a complex-linear functional this is
> equivalent to `f (a b) = f (b a)`. A finite tracial weight gives a tracial state.

## ii. Key results

> - `UnitalPositiveLinearMap.IsTracial` : tracial states.
> - `Weight.IsTracial` : tracial weights.

## iv. References

> * None.

## A. Tracial weights

**`PhyslibAlpha.ProbabilisticTheory.Weight.IsTracial`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L52).

> A weight is tracial when its finite positive-linear extensions assign equal values to `x† x`
> and `x x†`.

```lean
def IsTracial (w : Weight A) : Prop
```

**`PhyslibAlpha.ProbabilisticTheory.Weight.IsTracial.toPositiveLinearMap_star_mul_self`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L62).

> A finite tracial weight's real positive-linear extension has equal values on `x† x` and
> `x x†`.

```lean
lemma toPositiveLinearMap_star_mul_self (ht : w.IsTracial) (hw : w.IsFinite) (x : A) :
    hw.toPositiveLinearMap (star x * x) = hw.toPositiveLinearMap (x * star x)
```

## B. Tracial states

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.IsTracial`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L77).

> A state is tracial when it assigns equal values to `x† x` and `x x†`.

```lean
def IsTracial (s : 𝓢[ℝ, A]) : Prop
```

**`PhyslibAlpha.ProbabilisticTheory.Weight.IsState.isTracial`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L86).

> The state of a tracial weight assigns equal values to `x†x` and `xx†`.

```lean
lemma isTracial (hw : w.IsState) (ht : w.IsTracial) :
    ∀ x : A, hw.toState (star x * x) = hw.toState (x * star x)
```

## C. Tracial functionals

**`PhyslibAlpha.ProbabilisticTheory.LinearMap.IsTracial`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L101).

> A complex-linear functional is tracial when it is invariant under cyclic permutations.

```lean
def IsTracial (f : A →ₗ[ℂ] ℂ) : Prop
```

**`PhyslibAlpha.ProbabilisticTheory.LinearMap.isTracial_iff_star_mul_self_eq_mul_star_self`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L105).

> Equality on `x†x` and `xx†` characterizes tracial complex-linear functionals.

```lean
lemma isTracial_iff_star_mul_self_eq_mul_star_self (f : A →ₗ[ℂ] ℂ) :
    f.IsTracial ↔ ∀ x : A, f (star x * x) = f (x * star x)
```

## Depends on

- [States and finite normalized weights](../state/weightequivalence.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean)
