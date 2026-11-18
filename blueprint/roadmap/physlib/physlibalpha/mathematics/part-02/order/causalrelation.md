---
declaration: module
origin: cited
lean: CausalRelation, CausalRelation.reverse, CausalRelation.causalFuture, CausalRelation.causalPast, CausalRelation.causalHull, CausalRelation.subset_causalFuture, CausalRelation.subset_causalPast, CausalRelation.causalFuture_mono
statement: formalized
proof: formalized
---

# Causal support geometry

The module `PhyslibAlpha.Mathematics.Order.CausalRelation`, [PhyslibAlpha/Mathematics/Order/CausalRelation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean): 28 declarations, 14 with a docstring.

## i. Overview

> Causal futures and pasts describe the allowed support of linear field responses.

## ii. Key results

> - `reverse` : Reversing the causal direction exchanges retarded and advanced support.
> - `reverse` : Reversing the causal direction exchanges retarded and advanced support.
> - `causalFuture` : The events reachable from at least one event of a source set.
> - `causalPast` : The events able to influence at least one event of a target set.
> - `causalHull` : The union of the causal past and future of a set.
> - `IsSpacelikeCompact` : A closed field support is spacelike compact when it lies in the causal hull
>   of a compact set.
> - `HasCompactCausalDiamonds` : Compact causal diamonds are the geometric compactness input for Green
>   exactness.
> - `causalFuture` : The events reachable from at least one event of a source set.

## iv. References

> None.

## A. Causal support geometry

> - `reverse` : Reversing the causal direction exchanges retarded and advanced support.
> - `reverse` : Reversing the causal direction exchanges retarded and advanced support.
> - `causalFuture` : The events reachable from at least one event of a source set.
> - `causalPast` : The events able to influence at least one event of a target set.
> - `causalHull` : The union of the causal past and future of a set.
> - `IsSpacelikeCompact` : A closed field support is spacelike compact when it lies in the causal hull
>   of a compact set.
> - `HasCompactCausalDiamonds` : Compact causal diamonds are the geometric compactness input for Green
>   exactness.
>
> Lemmas: `subset_causalFuture`, `subset_causalPast`, `causalFuture_mono`, `causalPast_mono`,
> `causalHull_mono`, `causalFuture_empty`, `causalPast_empty`, `causalFuture_union`,
> `causalPast_union`, `causalFuture_idem` and more.

## B. Past-compact and future-compact support

> - `causalFuture` : The events reachable from at least one event of a source set.
> - `IsPastCompact` : A set is past compact when its intersection with the causal past of every
>   compact set is compact.
>
> Lemmas: `mono`, `isPastCompact_empty`, `union`, `causalFuture_inter_causalPast`,
> `isPastCompact_of_futureSupported`, `isClosed_causalFuture`.

**`CausalRelation`**, a structure, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L76).

> The causal relation used to bound field propagation. Further geometric hypotheses belong
> in the results requiring them rather than in this minimal structure.

```lean
structure CausalRelation (M : Type*) where
  /-- An event can influence a causally later event. -/
  Precedes : M → M → Prop
  /-- Every event lies in its own causal future. -/
  refl : ∀ p, Precedes p p
  /-- Successive causal propagation is causal. -/
  trans : ∀ {p q r}, Precedes p q → Precedes q r → Precedes p r
```

**`CausalRelation.reverse`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L90).

> Reversing the causal direction exchanges retarded and advanced support.

```lean
def reverse : CausalRelation M
```

**`CausalRelation.causalFuture`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L96).

> The events reachable from at least one event of a source set.

```lean
def causalFuture (A : Set M) : Set M
```

**`CausalRelation.causalPast`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L99).

> The events able to influence at least one event of a target set.

```lean
def causalPast (A : Set M) : Set M
```

**`CausalRelation.causalHull`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L102).

> The union of the causal past and future of a set.

```lean
def causalHull (A : Set M) : Set M
```

**`CausalRelation.subset_causalFuture`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L104).

```lean
lemma subset_causalFuture : A ⊆ C.causalFuture A
```

**`CausalRelation.subset_causalPast`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L107).

```lean
lemma subset_causalPast : A ⊆ C.causalPast A
```

**`CausalRelation.causalFuture_mono`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L110).

```lean
lemma causalFuture_mono (h : A ⊆ B) : C.causalFuture A ⊆ C.causalFuture B
```

**`CausalRelation.causalPast_mono`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L113).

```lean
lemma causalPast_mono (h : A ⊆ B) : C.causalPast A ⊆ C.causalPast B
```

**`CausalRelation.causalHull_mono`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L116).

```lean
lemma causalHull_mono (h : A ⊆ B) : C.causalHull A ⊆ C.causalHull B
```

**`CausalRelation.causalFuture_empty`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L120).

```lean
lemma causalFuture_empty : C.causalFuture ∅ = ∅
```

**`CausalRelation.causalPast_empty`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L125).

```lean
lemma causalPast_empty : C.causalPast ∅ = ∅
```

**`CausalRelation.causalFuture_union`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L130).

```lean
lemma causalFuture_union : C.causalFuture (A ∪ B) = C.causalFuture A ∪ C.causalFuture B
```

**`CausalRelation.causalPast_union`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L142).

```lean
lemma causalPast_union : C.causalPast (A ∪ B) = C.causalPast A ∪ C.causalPast B
```

**`CausalRelation.causalFuture_idem`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L154).

```lean
lemma causalFuture_idem : C.causalFuture (C.causalFuture A) = C.causalFuture A
```

**`CausalRelation.causalPast_idem`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L161).

```lean
lemma causalPast_idem : C.causalPast (C.causalPast A) = C.causalPast A
```

**`CausalRelation.IsSpacelikeCompact`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L169).

> A closed field support is spacelike compact when it lies in the causal hull of a compact set.
> No equivalence with a Cauchy-surface definition is asserted without geometric hypotheses.

```lean
def IsSpacelikeCompact [TopologicalSpace M] (A : Set M) : Prop
```

**`CausalRelation.IsSpacelikeCompact.mono`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L172).

```lean
lemma IsSpacelikeCompact.mono [TopologicalSpace M]
    (hB : C.IsSpacelikeCompact B) (h : A ⊆ B) : C.IsSpacelikeCompact A
```

**`CausalRelation.HasCompactCausalDiamonds`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L179).

> Compact causal diamonds are the geometric compactness input for Green exactness.
> This does not by itself assert every part of global hyperbolicity.

```lean
def HasCompactCausalDiamonds [TopologicalSpace M] : Prop
```

**`CausalRelation.HasCompactCausalDiamonds.reverse`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L184).

> Compact causal diamonds are unchanged by reversing time orientation.

```lean
lemma HasCompactCausalDiamonds.reverse [TopologicalSpace M]
    (h : C.HasCompactCausalDiamonds) : C.reverse.HasCompactCausalDiamonds
```

**`CausalRelation.IsPastCompact`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L197).

> A set is past compact when its intersection with the causal past of every compact set is
> compact.

```lean
def IsPastCompact (A : Set M) : Prop
```

**`CausalRelation.isPastCompact_empty`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L200).

```lean
lemma isPastCompact_empty : C.IsPastCompact ∅
```

**`CausalRelation.IsPastCompact.union`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L204).

```lean
lemma IsPastCompact.union (hA : C.IsPastCompact A) (hB : C.IsPastCompact B) :
    C.IsPastCompact (A ∪ B)
```

**`CausalRelation.IsPastCompact.mono`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L211).

> A closed subset of a past-compact set remains past compact.

```lean
lemma IsPastCompact.mono (hB : C.IsPastCompact B) (hA : IsClosed A) (hAB : A ⊆ B) :
    C.IsPastCompact A
```

**`CausalRelation.causalFuture_inter_causalPast`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L224).

> Causal transitivity localizes a future inside the past of an observation set.

```lean
lemma causalFuture_inter_causalPast (A K : Set M) :
    C.causalFuture A ∩ C.causalPast K =
      C.causalFuture (A ∩ C.causalPast K) ∩ C.causalPast K
```

**`CausalRelation.IsPastCompact.causalFuture`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L235).

> Compact causal diamonds imply that the future of a past-compact source is past compact.

```lean
lemma IsPastCompact.causalFuture (hC : C.HasCompactCausalDiamonds) (hA : C.IsPastCompact A) :
    C.IsPastCompact (C.causalFuture A)
```

**`CausalRelation.isPastCompact_of_futureSupported`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L242).

> Closed support in the future of a compact set is past compact under compact-diamond geometry.

```lean
lemma isPastCompact_of_futureSupported (hC : C.HasCompactCausalDiamonds)
    (hA : IsClosed A) {K : Set M} (hK : IsCompact K) (hAK : A ⊆ C.causalFuture K) :
    C.IsPastCompact A
```

**`CausalRelation.IsPastCompact.isClosed_causalFuture`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean#L249).

> Local upper causal bounds and closed compact futures imply closed futures of past-compact sets.
> These are geometric hypotheses, independent of the field equation or Green operators.

```lean
lemma IsPastCompact.isClosed_causalFuture
    (hclosed : ∀ K : Set M, IsCompact K → IsClosed (C.causalFuture K))
    (hlocal : ∀ p : M, ∃ K : Set M, IsCompact K ∧ C.causalPast K ∈ 𝓝 p)
    (hA : C.IsPastCompact A) : IsClosed (C.causalFuture A)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Order/CausalRelation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/CausalRelation.lean)
