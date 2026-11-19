---
declaration: module
origin: cited
lean: Channel.orderUnitNorm_apply_le, Channel.norm_apply_le, Channel.continuous, Channel.toContinuousLinearMap, Channel.toContinuousLinearMap_apply
statement: formalized
proof: formalized
---

# Channels are contractions

The module `Physlib.ProbabilisticTheory.Channel.Norm`, [Physlib/ProbabilisticTheory/Channel/Norm.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Norm.lean): 5 declarations, 4 with a docstring.

> Unital positive linear maps are contractions with respect to the order-unit norm and are
> therefore continuous.

## i. Overview

> An observable lies between the positive and negative multiples of the certain outcome set by
> its order-unit norm. A channel preserves both inequalities and the certain outcome, so the
> same bound holds for its image.

## ii. Key results

> - `Channel.norm_apply_le`: Channels are contractions.
> - `Channel.continuous`: Channels are continuous.
> - `Channel.toContinuousLinearMap`: Channels as continuous linear maps.

## iv. References

## A. Contractivity and continuity

**`Channel.orderUnitNorm_apply_le`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Norm.lean#L49).

> Unital positive linear maps are contractions for the order-unit norm.

```lean
lemma orderUnitNorm_apply_le (T : Channel P Q) (x : P.Observables) :
    orderUnitNorm (T x) ≤ orderUnitNorm x
```

**`Channel.norm_apply_le`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Norm.lean#L57).

> Unital positive linear maps are contractions for the norm.

```lean
lemma norm_apply_le (T : Channel P Q) (x : P.Observables) : ‖T x‖ ≤ ‖x‖
```

**`Channel.continuous`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Norm.lean#L62).

> Unital positive linear maps are continuous.

```lean
lemma continuous (T : Channel P Q) : Continuous T
```

**`Channel.toContinuousLinearMap`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Norm.lean#L66).

> A unital positive linear map regarded as a continuous linear map.

```lean
noncomputable def toContinuousLinearMap (T : Channel P Q) : P.Observables →L[ℝ] Q.Observables
```

**`Channel.toContinuousLinearMap_apply`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Norm.lean#L69).

```lean
lemma toContinuousLinearMap_apply (T : Channel P Q) (x : P.Observables) :
    T.toContinuousLinearMap x = T x
```

## Depends on

- [Channels between observable spaces](basic.md)
- [Archimedean order-unit spaces (Physlib)](../orderunit/archimedean.md)

## Sources

- [Physlib/ProbabilisticTheory/Channel/Norm.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Norm.lean)
