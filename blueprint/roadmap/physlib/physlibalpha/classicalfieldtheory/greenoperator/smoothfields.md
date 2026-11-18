---
declaration: module
origin: cited
lean: GreenOperator.Minkowski.pastLocalization, GreenOperator.Minkowski.futureLocalization, GreenOperator.Minkowski.smoothFields_bumpStable, GreenOperator.Minkowski.smoothPastLocalization, GreenOperator.Minkowski.smoothFutureLocalization, GreenOperator.Minkowski.isCompact_causalPast_inter, GreenOperator.Minkowski.isCompact_causalFuture_inter, GreenOperator.Minkowski.tsupport_cutoff_subset
statement: formalized
proof: formalized
---

# Smooth spacetime fields as Green operator input

The module `PhyslibAlpha.ClassicalFieldTheory.GreenOperator.SmoothFields`, [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean): 10 declarations, 8 with a docstring.

## i. Overview

> Smooth fields on spacetime admit past and future localization and temporal cutoffs.

## ii. Key results

> - `pastLocalization` : Retarded localization for every admissible field space with local gluing and
>   bump stability.
> - `futureLocalization` : Advanced localization uses the same field hypotheses and the reversed
>   verified causal geometry.
> - `smoothPastLocalization` : All past-compact smooth fields admit the compact truncations required
>   by the general theory.
> - `smoothFutureLocalization` : The same analytic field class supplies advanced localization after
>   causal reversal.

## iv. References

> None.

## A. Localization of admissible fields in Minkowski spacetime

> - `pastLocalization` : Retarded localization for every admissible field space with local gluing and
>   bump stability.
> - `futureLocalization` : Advanced localization uses the same field hypotheses and the reversed
>   verified causal geometry.

## B. Localization of smooth spacetime fields

> - `smoothPastLocalization` : All past-compact smooth fields admit the compact truncations required
>   by the general theory.
> - `smoothFutureLocalization` : The same analytic field class supplies advanced localization after
>   causal reversal.
>
> Lemmas: `smoothFields_bumpStable`.

## C. Temporal cutoffs of spacelike-compact smooth fields

> Lemmas: `isCompact_causalPast_inter`, `isCompact_causalFuture_inter`, `tsupport_cutoff_subset`,
> `tsupport_cutoff_sub_subset`, `smoothHasCausalCutoffs`.

**`GreenOperator.Minkowski.pastLocalization`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L78).

> Retarded localization for every admissible field space with local gluing and bump stability.

```lean
def pastLocalization (hlocal : IsLocalFieldSpace S)
    (hmul : ∀ (b : ContDiffBump (0 : SpaceTime d)) (u : S), (fun x => b x • u.val x) ∈ S) :
    PastLocalization (causalRelation d) P
```

**`GreenOperator.Minkowski.futureLocalization`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L86).

> Advanced localization uses the same field hypotheses and the reversed verified causal
> geometry.

```lean
def futureLocalization (hlocal : IsLocalFieldSpace S)
    (hmul : ∀ (b : ContDiffBump (0 : SpaceTime d)) (u : S), (fun x => b x • u.val x) ∈ S) :
    PastLocalization (causalRelation d).reverse P
```

**`GreenOperator.Minkowski.smoothFields_bumpStable`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L97).

> Smooth scalar bump multiplication preserves the smooth admissible field space.

```lean
lemma smoothFields_bumpStable (b : ContDiffBump (0 : SpaceTime d)) (u : smoothFields d V) :
    (fun x => b x • u.val x) ∈ smoothFields d V
```

**`GreenOperator.Minkowski.smoothPastLocalization`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L103).

> All past-compact smooth fields admit the compact truncations required by the general theory.

```lean
def smoothPastLocalization (P : LocalOperator (smoothFields d V)) :
    PastLocalization (causalRelation d) P
```

**`GreenOperator.Minkowski.smoothFutureLocalization`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L108).

> The same analytic field class supplies advanced localization after causal reversal.

```lean
def smoothFutureLocalization (P : LocalOperator (smoothFields d V)) :
    PastLocalization (causalRelation d).reverse P
```

**`GreenOperator.Minkowski.isCompact_causalPast_inter`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L117).

> The part of the causal past of a compact set with nonnegative time is compact.

```lean
lemma isCompact_causalPast_inter {K : Set (SpaceTime d)} (hK : IsCompact K) :
    IsCompact ((causalRelation d).causalPast K ∩ {x | 0 ≤ x.timeComponent})
```

**`GreenOperator.Minkowski.isCompact_causalFuture_inter`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L153).

> The part of the causal future of a compact set with time at most one is compact.

```lean
lemma isCompact_causalFuture_inter {K : Set (SpaceTime d)} (hK : IsCompact K) :
    IsCompact ((causalRelation d).causalFuture K ∩ {x | x.timeComponent ≤ 1})
```

**`GreenOperator.Minkowski.tsupport_cutoff_subset`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L194).

```lean
lemma tsupport_cutoff_subset (u : SpaceTime d → V) :
    tsupport (fun x : SpaceTime d => Real.smoothTransition x.timeComponent • u x) ⊆
      {x | 0 ≤ x.timeComponent} ∩ tsupport u
```

**`GreenOperator.Minkowski.tsupport_cutoff_sub_subset`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L203).

```lean
lemma tsupport_cutoff_sub_subset (u : SpaceTime d → V) :
    tsupport (fun x : SpaceTime d => (Real.smoothTransition x.timeComponent - 1) • u x) ⊆
      {x | x.timeComponent ≤ 1} ∩ tsupport u
```

**`GreenOperator.Minkowski.smoothHasCausalCutoffs`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean#L213).

> Every smooth field space has the temporal cutoff splitting of spacelike-compact fields.

```lean
lemma smoothHasCausalCutoffs (P : LocalOperator (smoothFields d V)) :
    P.HasCausalCutoffs (causalRelation d)
```

## Depends on

- [The causal propagator and causal uniqueness](causalpropagator.md)
- [Localization and extension of retarded responses](localization.md)
- [Light cones in time and space](../../relativity/causality/lightcone.md)
- [Smooth fields and distributions on spacetime](../../spaceandtime/spacetime/fields.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/SmoothFields.lean)
