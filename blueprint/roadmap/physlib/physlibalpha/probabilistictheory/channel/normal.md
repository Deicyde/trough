---
declaration: module
origin: cited
lean: PositiveLinearMap.IsNormal, PositiveLinearMap.isNormal_id, PositiveLinearMap.IsNormal.comp, PositiveLinearMap.IsNormal.isLUB_partialSums, ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal, ProbabilisticTheory.UnitalPositiveLinearMap.isNormal_id, ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.comp
statement: formalized
proof: formalized
---

# Normal channels

The module `PhyslibAlpha.ProbabilisticTheory.Channel.Normal`, [PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean): 7 declarations, 3 with a docstring.

> Normal positive maps and channels: those preserving suprema of increasing sequences.

## i. Overview

> A channel is normal when it preserves least upper bounds of increasing sequences. Every channel
> preserves finite sums; a normal channel also preserves countable sums of positive elements.

## ii. Key results

> - `UnitalPositiveLinearMap.IsNormal`
> - `PositiveLinearMap.IsNormal.isLUB_partialSums` : a normal map preserves countable sums of
>   positive elements.

## iv. References

> * None.

## A. Normal positive maps

**`PositiveLinearMap.IsNormal`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean#L48).

> A positive linear map is normal when it preserves least upper bounds of increasing
> sequences.

```lean
def IsNormal (φ : E →ₚ[ℝ] F) : Prop
```

**`PositiveLinearMap.isNormal_id`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean#L51).

```lean
lemma isNormal_id : (PositiveLinearMap.id ℝ E).IsNormal
```

**`PositiveLinearMap.IsNormal.comp`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean#L53).

```lean
lemma IsNormal.comp {φ : E →ₚ[ℝ] F} {ψ : F →ₚ[ℝ] G} (hφ : φ.IsNormal) (hψ : ψ.IsNormal) :
    (ψ.comp φ).IsNormal
```

**`PositiveLinearMap.IsNormal.isLUB_partialSums`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean#L58).

> A normal map preserves countable sums of positive elements.

```lean
lemma IsNormal.isLUB_partialSums {φ : E →ₚ[ℝ] F} (hφ : φ.IsNormal) {f : ℕ → E}
    (hf : ∀ n, 0 ≤ f n) {x : E} (hx : IsLUB (Set.range fun N => ∑ n ∈ Finset.range N, f n) x) :
    IsLUB (Set.range fun N => ∑ n ∈ Finset.range N, φ (f n)) (φ x)
```

## B. Normal channels

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal`**, an abbrev, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean#L75).

> A channel is normal when its underlying positive linear map is.

```lean
abbrev IsNormal (φ : Channel E F) : Prop
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isNormal_id`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean#L77).

```lean
lemma isNormal_id : (UnitalPositiveLinearMap.id ℝ E).IsNormal
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.comp`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean#L79).

```lean
lemma IsNormal.comp {φ : Channel E F} {ψ : Channel F G} (hφ : φ.IsNormal) (hψ : ψ.IsNormal) :
    (ψ.comp φ).IsNormal
```

## Depends on

- [Channels](basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Normal.lean)
