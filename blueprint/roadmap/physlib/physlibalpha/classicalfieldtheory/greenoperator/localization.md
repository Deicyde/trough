---
declaration: module
origin: cited
lean: GreenOperator.PastLocalization, GreenOperator.PastLocalization.mem_past_bound, GreenOperator.PastLocalization.sourceAt, GreenOperator.PastLocalization.sourceAt_agrees, GreenOperator.PastLocalization.predecessor_mem_past_bound, GreenOperator.PastLocalization.retardedValue, GreenOperator.PastLocalization.retardedValue_eq_on_past_bound, GreenOperator.PastLocalization.retardedValue_eventuallyEq
statement: formalized
proof: formalized
---

# Localization and extension of retarded responses

The module `PhyslibAlpha.ClassicalFieldTheory.GreenOperator.Localization`, [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean): 33 declarations, 28 with a docstring.

> A past compact source is cut off to compact pieces.

## i. Overview

> A past compact source is cut off to compact pieces. The retarded responses to the pieces define a
> response to the whole source.

## ii. Key results

> - `PastLocalization` : The geometric and cutoff data for localizing past-compact sections to compact
>   test sections.
> - `sourceAt` : Each source has a compact truncation adapted to the observation event.
> - `retardedValue` : The pointwise retarded response obtained from observation-adapted compact
>   truncations.
> - `retardedSection` : The glued retarded field as an admissible section.
> - `retardedExtension` : The two-sided linear Green extension to all past-compact sources.
> - `truncationRadius` : A positive ball radius enclosing the relevant compact part of the source.
> - `truncationBump` : A smooth compact bump equal to one near the relevant source intersection.
> - `bumpTruncate` : A bump truncation is a compact admissible source, not an assumed larger-support
>   solution.

## iv. References

> None.

## A. Compact localization of past-compact sources

> - `PastLocalization` : The geometric and cutoff data for localizing past-compact sections to compact
>   test sections.
> - `sourceAt` : Each source has a compact truncation adapted to the observation event.
> - `retardedValue` : The pointwise retarded response obtained from observation-adapted compact
>   truncations.
>
> Lemmas: `mem_past_bound`, `sourceAt_agrees`, `predecessor_mem_past_bound`,
> `retardedValue_eq_on_past_bound`, `retardedValue_eventuallyEq`, `retardedValue_mem`,
> `homogeneous_eq_zero`, `pastCompactOperator_injective`.

## B. Constructing Green extensions by local compact truncation

> - `retardedSection` : The glued retarded field as an admissible section.
> - `retardedExtension` : The two-sided linear Green extension to all past-compact sources.
>
> Lemmas: `retardedSection_solves`, `retardedValue_support`, `retardedSection_support`,
> `retardedSection_mem_pastCompactFields`, `pastCompactOperator_surjective`,
> `retardedExtension_solves`, `retardedExtension_eq_section`, `retardedExtension_support`,
> `pastCompact_unique`, `futureSupportedOperator_injective` and more.

## C. Compact source localization by smooth bump functions

> - `truncationRadius` : A positive ball radius enclosing the relevant compact part of the source.
> - `truncationBump` : A smooth compact bump equal to one near the relevant source intersection.
> - `bumpTruncate` : A bump truncation is a compact admissible source, not an assumed larger-support
>   solution.
> - `ofBumpFunctions` : Construct all local compact-source truncation data from bump stability and
>   causal topology.
>
> Lemmas: `truncationRadius_pos`, `mem_truncation_ball`, `bumpTruncate_support`,
> `bumpTruncate_agrees`.

**`GreenOperator.PastLocalization`**, a structure, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L96).

> The geometric and cutoff data for localizing past-compact sections to compact test sections.

```lean
structure PastLocalization (C : CausalRelation M) (P : LocalOperator S) where
  /-- Compact observation bounds whose causal pasts are neighborhoods. -/
  bound : M → Set M
  /-- Every observation bound is compact. -/
  bound_compact : ∀ x, IsCompact (bound x)
  /-- The causal past of an observation bound contains a neighborhood of the event. -/
  bound_neighborhood : ∀ x, C.causalPast (bound x) ∈ 𝓝 x
  /-- Admissible fields glue from local representatives. -/
  local_fields : IsLocalFieldSpace S
  /-- The causal future of a compact set is closed. -/
  closed_compact_future : ∀ K : Set M, IsCompact K → IsClosed (C.causalFuture K)
  /-- Compact source truncation near the causal past of a compact observation set. -/
  truncate : P.pastCompactFields C → (K : Set M) → IsCompact K → P.compactSources
  /-- Truncation agrees as germs with the source throughout that causal past. -/
  truncate_agrees : ∀ f K hK x, x ∈ C.causalPast K →
    ((truncate f K hK).val : M → V) =ᶠ[𝓝 x] (f.val : M → V)
  /-- Compact truncation introduces no support outside the original source. -/
  truncate_support : ∀ f K hK,
    tsupport ((truncate f K hK).val : M → V) ⊆ tsupport (f.val : M → V)
```

**`GreenOperator.PastLocalization.mem_past_bound`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L126).

```lean
lemma mem_past_bound (x : M) : x ∈ C.causalPast (L.bound x)
```

**`GreenOperator.PastLocalization.sourceAt`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L130).

> Each source has a compact truncation adapted to the observation event.

```lean
def sourceAt (f : P.pastCompactFields C) (x : M) : P.compactSources
```

**`GreenOperator.PastLocalization.sourceAt_agrees`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L133).

```lean
lemma sourceAt_agrees (f : P.pastCompactFields C) (x : M) {y : M}
    (hy : y ∈ C.causalPast (L.bound x)) :
    ((L.sourceAt f x).val : M → V) =ᶠ[𝓝 y] (f.val : M → V)
```

**`GreenOperator.PastLocalization.predecessor_mem_past_bound`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L138).

```lean
lemma predecessor_mem_past_bound {x y : M} (hyx : C.Precedes y x) :
    y ∈ C.causalPast (L.bound x)
```

**`GreenOperator.PastLocalization.retardedValue`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L144).

> The pointwise retarded response obtained from observation-adapted compact truncations.

```lean
def retardedValue (G : RetardedGreenOperator C P) (f : P.pastCompactFields C) : M → V
```

**`GreenOperator.PastLocalization.retardedValue_eq_on_past_bound`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L149).

> Retarded responses of different admissible truncations agree locally.
> No limit or convergence of the truncation family is required.

```lean
lemma retardedValue_eq_on_past_bound (G : RetardedGreenOperator C P)
    (f : P.pastCompactFields C) (x : M) {y : M}
    (hy : y ∈ C.causalPast (L.bound x)) :
    L.retardedValue G f y = (G.toLinearMap (L.sourceAt f x) : M → V) y
```

**`GreenOperator.PastLocalization.retardedValue_eventuallyEq`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L161).

> Near any event the response is an ordinary compact-source Green response.

```lean
lemma retardedValue_eventuallyEq (G : RetardedGreenOperator C P)
    (f : P.pastCompactFields C) (x : M) :
    L.retardedValue G f =ᶠ[𝓝 x] (G.toLinearMap (L.sourceAt f x) : M → V)
```

**`GreenOperator.PastLocalization.retardedValue_mem`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L168).

> The pointwise construction is admissible by local gluing.

```lean
lemma retardedValue_mem (G : RetardedGreenOperator C P) (f : P.pastCompactFields C) :
    L.retardedValue G f ∈ S
```

**`GreenOperator.PastLocalization.homogeneous_eq_zero`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L174).

> A past-compact homogeneous field vanishes, proved from compact Green identities and cutoffs.

```lean
lemma homogeneous_eq_zero (G : RetardedGreenOperator C P) (u : P.pastCompactFields C)
    (hPu : P.operator u.val = 0) : u.val = 0
```

**`GreenOperator.PastLocalization.pastCompactOperator_injective`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L193).

> One-sided uniqueness is a consequence of local compact truncation and the compact Green
> inverse.

```lean
lemma pastCompactOperator_injective (G : RetardedGreenOperator C P) :
    Function.Injective (P.pastCompactOperator C)
```

**`GreenOperator.PastLocalization.retardedSection`**, a def, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L210).

> The glued retarded field as an admissible section.

```lean
def retardedSection (f : P.pastCompactFields C) : S
```

**`GreenOperator.PastLocalization.retardedSection_solves`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L214).

> The glued field solves the full past-compact source equation.

```lean
lemma retardedSection_solves (f : P.pastCompactFields C) :
    P.operator (L.retardedSection G f) = f.val
```

**`GreenOperator.PastLocalization.retardedValue_support`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L225).

> Pointwise support of the glued response lies in the future of the source.

```lean
lemma retardedValue_support (f : P.pastCompactFields C) :
    Function.support (L.retardedValue G f) ⊆ C.causalFuture (tsupport (f.val : M → V))
```

**`GreenOperator.PastLocalization.retardedSection_support`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L233).

> The topological support bound follows from the closed future of a past-compact source.

```lean
lemma retardedSection_support (f : P.pastCompactFields C) :
    tsupport (L.retardedSection G f : M → V) ⊆ C.causalFuture (tsupport (f.val : M → V))
```

**`GreenOperator.PastLocalization.retardedSection_mem_pastCompactFields`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L241).

> Causal support and compact diamonds put the constructed response in the full past-compact
> class.

```lean
lemma retardedSection_mem_pastCompactFields (hC : C.HasCompactCausalDiamonds)
    (f : P.pastCompactFields C) : L.retardedSection G f ∈ P.pastCompactFields C
```

**`GreenOperator.PastLocalization.pastCompactOperator_surjective`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L249).

> Existence on the larger support class is constructed from local compact responses.

```lean
lemma pastCompactOperator_surjective (hC : C.HasCompactCausalDiamonds) :
    Function.Surjective (P.pastCompactOperator C)
```

**`GreenOperator.PastLocalization.retardedExtension`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L256).

> The two-sided linear Green extension to all past-compact sources.

```lean
noncomputable def retardedExtension (hC : C.HasCompactCausalDiamonds) :
    P.pastCompactFields C ≃ₗ[𝕜] P.pastCompactFields C
```

**`GreenOperator.PastLocalization.retardedExtension_solves`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L262).

> The constructed extension solves the source equation.

```lean
lemma retardedExtension_solves (hC : C.HasCompactCausalDiamonds) (f : P.pastCompactFields C) :
    P.pastCompactOperator C (L.retardedExtension G hC f) = f
```

**`GreenOperator.PastLocalization.retardedExtension_eq_section`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L268).

> The abstract linear inverse equals the explicitly glued local response.

```lean
lemma retardedExtension_eq_section (hC : C.HasCompactCausalDiamonds)
    (f : P.pastCompactFields C) :
    (L.retardedExtension G hC f).val = L.retardedSection G f
```

**`GreenOperator.PastLocalization.retardedExtension_support`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L279).

> The full past-compact extension retains the sharp causal support bound.

```lean
lemma retardedExtension_support (hC : C.HasCompactCausalDiamonds) (f : P.pastCompactFields C) :
    tsupport ((L.retardedExtension G hC f).val : M → V) ⊆
      C.causalFuture (tsupport (f.val : M → V))
```

**`GreenOperator.PastLocalization.pastCompact_unique`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L287).

> Uniqueness for admissible fields in the full past-compact class.

```lean
lemma pastCompact_unique {u v : S}
    (hu : u ∈ P.pastCompactFields C) (hv : v ∈ P.pastCompactFields C)
    (heq : P.operator u = P.operator v) : u = v
```

**`GreenOperator.PastLocalization.futureSupportedOperator_injective`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L296).

> One-sided uniqueness on compactly generated future support is now a theorem.

```lean
lemma futureSupportedOperator_injective (hC : C.HasCompactCausalDiamonds) :
    Function.Injective (P.futureSupportedOperator C)
```

**`GreenOperator.PastLocalization.retardedExtension_mem_futureSupportedFields`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L306).

> The extension preserves support in the future of any one compact source bound.

```lean
lemma retardedExtension_mem_futureSupportedFields (hC : C.HasCompactCausalDiamonds)
    (f : P.futureSupportedFields C) :
    (L.retardedExtension G hC
      ⟨f.val, P.futureSupportedFields_le_pastCompactFields C hC f.property⟩).val ∈
      P.futureSupportedFields C
```

**`GreenOperator.PastLocalization.futureSupportedOperator_surjective`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L321).

> Solvability on compactly generated future support is proved by restricting the constructed
> past-compact extension. It is not an additional existence assumption.

```lean
lemma futureSupportedOperator_surjective (hC : C.HasCompactCausalDiamonds) :
    Function.Surjective (P.futureSupportedOperator C)
```

**`GreenOperator.PastLocalization.truncationRadius`**, a def, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L338).

> A positive ball radius enclosing the relevant compact part of the source.

```lean
def truncationRadius (f : P.pastCompactFields C) (K : Set E) (hK : IsCompact K) : ℝ
```

**`GreenOperator.PastLocalization.truncationRadius_pos`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L342).

```lean
lemma truncationRadius_pos (f : P.pastCompactFields C) (K : Set E) (hK : IsCompact K) :
    0 < truncationRadius f K hK
```

**`GreenOperator.PastLocalization.truncationBump`**, a def, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L347).

> A smooth compact bump equal to one near the relevant source intersection.

```lean
def truncationBump (f : P.pastCompactFields C) (K : Set E) (hK : IsCompact K) :
    ContDiffBump (0 : E)
```

**`GreenOperator.PastLocalization.mem_truncation_ball`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L355).

```lean
lemma mem_truncation_ball (f : P.pastCompactFields C) (K : Set E) (hK : IsCompact K)
    {x : E} (hx : x ∈ tsupport (f.val : E → V)) (hp : x ∈ C.causalPast K) :
    x ∈ Metric.ball (0 : E) (truncationBump f K hK).rIn
```

**`GreenOperator.PastLocalization.bumpTruncate`**, a def, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L362).

> A bump truncation is a compact admissible source, not an assumed larger-support solution.

```lean
def bumpTruncate (f : P.pastCompactFields C) (K : Set E) (hK : IsCompact K) :
    P.compactSources
```

**`GreenOperator.PastLocalization.bumpTruncate_support`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L370).

> Truncating by multiplication introduces no support outside the source.

```lean
lemma bumpTruncate_support (f : P.pastCompactFields C) (K : Set E) (hK : IsCompact K) :
    tsupport ((bumpTruncate hmul f K hK).val : E → V) ⊆ tsupport (f.val : E → V)
```

**`GreenOperator.PastLocalization.bumpTruncate_agrees`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L375).

> The truncation agrees as germs on the entire causal past of the observation set.

```lean
lemma bumpTruncate_agrees (f : P.pastCompactFields C) (K : Set E) (hK : IsCompact K)
    (x : E) (hx : x ∈ C.causalPast K) :
    ((bumpTruncate hmul f K hK).val : E → V) =ᶠ[𝓝 x] (f.val : E → V)
```

**`GreenOperator.PastLocalization.ofBumpFunctions`**, a def, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean#L393).

> Construct all local compact-source truncation data from bump stability and causal topology.
> No existence or uniqueness of a Green response is an input.

```lean
def ofBumpFunctions (hlocal : IsLocalFieldSpace S)
    (hclosed : ∀ K : Set E, IsCompact K → IsClosed (C.causalFuture K))
    (hbound : ∀ x : E, ∃ K : Set E, IsCompact K ∧ C.causalPast K ∈ 𝓝 x) :
    PastLocalization C P
```

## Depends on

- [Green operators and causally supported fields](basic.md)

## Proof depends on

- [The causal propagator and causal uniqueness](causalpropagator.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Localization.lean)
