---
declaration: module
origin: cited
lean: UnitalPositiveLinearMap.orderUnitNorm_apply_le, UnitalPositiveLinearMap.norm_apply_le, UnitalPositiveLinearMap.continuous, UnitalPositiveLinearMap.toContinuousLinearMap, UnitalPositiveLinearMap.toContinuousLinearMap_apply
statement: formalized
proof: formalized
---

# Channels are contractions

The module `Physlib.ProbabilisticTheory.Channel.Norm`, [Physlib/ProbabilisticTheory/Channel/Norm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Norm.lean): 5 declarations, 4 with a docstring.

> Unital positive linear maps are contractions with respect to the order-unit norm and are
> therefore continuous.

## i. Overview

> The norm bound follows from the characterization of the order-unit norm in terms of states.
> Every state on the codomain pulls back along a channel to a state on the domain, so evaluating
> the image of an observable cannot exceed its original norm.

## ii. Key results

> - `UnitalPositiveLinearMap.norm_apply_le`: Channels are contractions.
> - `UnitalPositiveLinearMap.continuous`: Channels are continuous.
> - `UnitalPositiveLinearMap.toContinuousLinearMap`: Channels as continuous linear maps.

## iv. References

## A. Contractivity and continuity

**`UnitalPositiveLinearMap.orderUnitNorm_apply_le`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Norm.lean#L48).

> Unital positive linear maps are contractions for the order-unit norm.

```lean
lemma orderUnitNorm_apply_le (T : E →ₚ₁[ℝ] F) (x : E) :
    orderUnitNorm (T x) ≤ orderUnitNorm x
```

**`UnitalPositiveLinearMap.norm_apply_le`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Norm.lean#L58).

> Unital positive linear maps are contractions for the norm.

```lean
lemma norm_apply_le (T : E →ₚ₁[ℝ] F) (x : E) : ‖T x‖ ≤ ‖x‖
```

**`UnitalPositiveLinearMap.continuous`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Norm.lean#L63).

> Unital positive linear maps are continuous.

```lean
lemma continuous (T : E →ₚ₁[ℝ] F) : Continuous T
```

**`UnitalPositiveLinearMap.toContinuousLinearMap`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Norm.lean#L67).

> A unital positive linear map regarded as a continuous linear map.

```lean
noncomputable def toContinuousLinearMap (T : E →ₚ₁[ℝ] F) : E →L[ℝ] F
```

**`UnitalPositiveLinearMap.toContinuousLinearMap_apply`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Norm.lean#L70).

```lean
lemma toContinuousLinearMap_apply (T : E →ₚ₁[ℝ] F) (x : E) :
    T.toContinuousLinearMap x = T x
```

## Depends on

- [Positive unital maps](basic.md)
- [Archimedean order-unit spaces](../orderunit/archimedean.md)

## Proof depends on

- [States](../state/basic.md)
- [Separation by states](../state/separation.md)

## Sources

- [Physlib/ProbabilisticTheory/Channel/Norm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Norm.lean)
