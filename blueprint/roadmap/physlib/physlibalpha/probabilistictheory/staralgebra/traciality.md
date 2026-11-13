---
declaration: module
origin: cited
lean: ProbabilisticTheory.Weight.IsTracial, ProbabilisticTheory.Weight.IsTracial.toPositiveLinearMap_star_mul_self, ProbabilisticTheory.UnitalPositiveLinearMap.IsTracial, ProbabilisticTheory.Weight.IsState.isTracial
statement: formalized
proof: formalized
---

# Tracial states and weights

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.Traciality`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean): 4 declarations, 4 with a docstring.

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

**`ProbabilisticTheory.Weight.IsTracial`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L49).

> A weight is tracial when its finite positive-linear extensions assign equal values to `x† x`
> and `x x†`.

```lean
def IsTracial (w : Weight A) : Prop
```

**`ProbabilisticTheory.Weight.IsTracial.toPositiveLinearMap_star_mul_self`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L59).

> A finite tracial weight's real positive-linear extension has equal values on `x† x` and
> `x x†`.

```lean
lemma toPositiveLinearMap_star_mul_self (ht : w.IsTracial) (hw : w.IsFinite) (x : A) :
    hw.toPositiveLinearMap (star x * x) = hw.toPositiveLinearMap (x * star x)
```

## B. Tracial states

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsTracial`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L74).

> A state is tracial when it assigns equal values to `x† x` and `x x†`.

```lean
def IsTracial (s : 𝓢[ℝ, A]) : Prop
```

**`ProbabilisticTheory.Weight.IsState.isTracial`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean#L83).

> The state of a tracial weight assigns equal values to `x†x` and `xx†`.

```lean
lemma isTracial (hw : w.IsState) (ht : w.IsTracial) :
    ∀ x : A, hw.toState (star x * x) = hw.toState (x * star x)
```

## Depends on

- [States and finite normalized weights](../state/weightequivalence.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Traciality.lean)
