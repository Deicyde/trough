---
declaration: module
origin: cited
lean: ProbabilisticTheory.EffectValuedMeasure, ProbabilisticTheory.EffectValuedMeasure.ext, ProbabilisticTheory.EffectValuedMeasure.map_empty, ProbabilisticTheory.EffectValuedMeasure.map_univ, ProbabilisticTheory.EffectValuedMeasure.countably_additive, ProbabilisticTheory.EffectValuedMeasure.eventFinset, ProbabilisticTheory.EffectValuedMeasure.atomSum, ProbabilisticTheory.EffectValuedMeasure.atomSum_nonneg
statement: formalized
proof: formalized
---

# Effect-valued measures

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.EffectValuedMeasure`, [PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean): 22 declarations (1 instance with no name), 10 with a docstring.

> Effect-valued measures: countably additive assignments of effects to events.

## i. Overview

> An effect-valued measure with outcomes in `Ω` assigns to each event, a measurable set of outcomes,
> an effect: the impossible event gets `0`, the certain event gets `1`, and the effects of disjoint
> events add up, countably. Every measurement has one, sending an event to the effect testing whether
> the outcome lands in it. For self-adjoint operators effect-valued measures are the POVMs.
>
> On a finite discrete outcome space an effect-valued measure is the same as a family of effects
> adding up to `1`, one for each outcome.

## ii. Key results

> - `EffectValuedMeasure Ω E` : an effect-valued measure with outcomes in `Ω`.
> - `EffectValuedMeasure.ofFintype` : the effect-valued measure of a normalized family of effects.
> - `EffectValuedMeasure.map_union_of_disjoint` : additivity on two disjoint events.
> - `EffectValuedMeasure.coe_apply_eq_atomSum` : on a finite outcome space, the effect of an event
>   is the sum of the effects of its outcomes.
> - `EffectValuedMeasure.mapOutcome` : relabeling outcomes along a measurable map.

## iv. References

> * None.

## A. Effect-valued measures

**`ProbabilisticTheory.EffectValuedMeasure`**, a structure, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L60).

> An effect-valued measure: `∅ ↦ 0`, `univ ↦ 1`, countably additive.

```lean
structure EffectValuedMeasure (Ω : Type*) [MeasurableSpace Ω] (E : Type*) [OrderUnitSpace E] where
  /-- The effect assigned to each event. -/
  toFun : ∀ s : Set Ω, MeasurableSet s → Effect E
  /-- The impossible event gets `0`. -/
  map_empty' : toFun ∅ .empty = 0
  /-- The certain event gets `1`. -/
  map_univ' : toFun .univ .univ = 1
  /-- The effects of countably many disjoint events add up to the effect of their union. -/
  countably_additive' : ∀ (s : ℕ → Set Ω) (hs : ∀ n, MeasurableSet (s n)),
    Pairwise (Disjoint on s) →
      IsLUB (Set.range fun N => ∑ n ∈ Finset.range N, (toFun (s n) (hs n) : E))
        (toFun (⋃ n, s n) (.iUnion hs) : E)
```

**An instance with no name**, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L75).

```lean
instance : CoeFun (EffectValuedMeasure Ω E) fun _ => ∀ s : Set Ω, MeasurableSet s → Effect E
```

**`ProbabilisticTheory.EffectValuedMeasure.ext`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L79).

```lean
lemma ext {μ ν : EffectValuedMeasure Ω E} (h : ∀ s hs, μ s hs = ν s hs) : μ = ν
```

**`ProbabilisticTheory.EffectValuedMeasure.map_empty`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L83).

```lean
lemma map_empty (μ : EffectValuedMeasure Ω E) : μ ∅ .empty = 0
```

**`ProbabilisticTheory.EffectValuedMeasure.map_univ`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L86).

```lean
lemma map_univ (μ : EffectValuedMeasure Ω E) : μ .univ .univ = 1
```

**`ProbabilisticTheory.EffectValuedMeasure.countably_additive`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L88).

```lean
lemma countably_additive (μ : EffectValuedMeasure Ω E) {s : ℕ → Set Ω}
    (hs : ∀ n, MeasurableSet (s n)) (hd : Pairwise (Disjoint on s)) :
    IsLUB (Set.range fun N => ∑ n ∈ Finset.range N, (μ (s n) (hs n) : E))
      (μ (⋃ n, s n) (.iUnion hs) : E)
```

## B. Atomic effect sums

**`ProbabilisticTheory.EffectValuedMeasure.eventFinset`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L104).

> The outcomes of `s` as a finite set.

```lean
noncomputable def eventFinset (s : Set Ω) : Finset Ω
```

**`ProbabilisticTheory.EffectValuedMeasure.atomSum`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L109).

> The sum of the atomic effects belonging to an event.

```lean
noncomputable def atomSum (a : Ω → Effect E) (s : Set Ω) : E
```

**`ProbabilisticTheory.EffectValuedMeasure.atomSum_nonneg`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L113).

```lean
lemma atomSum_nonneg (a : Ω → Effect E) (s : Set Ω) : 0 ≤ atomSum a s
```

**`ProbabilisticTheory.EffectValuedMeasure.atomSum_mono`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L117).

```lean
lemma atomSum_mono (a : Ω → Effect E) {s t : Set Ω} (hst : s ⊆ t) :
    atomSum a s ≤ atomSum a t
```

**`ProbabilisticTheory.EffectValuedMeasure.atomSum_univ`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L126).

```lean
lemma atomSum_univ (a : Ω → Effect E) : atomSum a Set.univ = ∑ x, (a x : E)
```

**`ProbabilisticTheory.EffectValuedMeasure.atomSum_partialSums`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L130).

```lean
lemma atomSum_partialSums (a : Ω → Effect E) (s : ℕ → Set Ω)
    (hd : Pairwise (Disjoint on s)) (N : ℕ) :
    (∑ n ∈ Finset.range N, atomSum a (s n)) = atomSum a (⋃ n < N, s n)
```

**`ProbabilisticTheory.EffectValuedMeasure.exists_partialUnion_eq_iUnion`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L153).

> On a finite outcome space, the union of a sequence of events is already the union of an initial
> segment.

```lean
lemma exists_partialUnion_eq_iUnion [Finite Ω] (s : ℕ → Set Ω) :
    ∃ N, ⋃ n < N, s n = ⋃ n, s n
```

## C. Finite-outcome effect-valued measures

**`ProbabilisticTheory.EffectValuedMeasure.ofFintype`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L166).

> A normalized finite family of atomic effects as an effect-valued measure.

```lean
noncomputable def ofFintype (a : Ω → Effect E) (ha : ∑ x, (a x : E) = 1) :
    EffectValuedMeasure Ω E
```

**`ProbabilisticTheory.EffectValuedMeasure.coe_ofFintype_apply`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L190).

```lean
lemma coe_ofFintype_apply (a : Ω → Effect E) (ha : ∑ x, (a x : E) = 1)
    (s : Set Ω) (hs : MeasurableSet s) : ((ofFintype a ha) s hs : E) = atomSum a s
```

**`ProbabilisticTheory.EffectValuedMeasure.coe_ofFintype_singleton`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L196).

```lean
lemma coe_ofFintype_singleton (a : Ω → Effect E) (ha : ∑ x, (a x : E) = 1) (x : Ω)
    (hx : MeasurableSet {x}) : ((ofFintype a ha) {x} hx : E) = a x
```

## D. Finite additivity and atomic reconstruction

**`ProbabilisticTheory.EffectValuedMeasure.map_union_of_disjoint`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L205).

> An effect-valued measure is additive on two disjoint events.

```lean
lemma map_union_of_disjoint (M : EffectValuedMeasure Ω E) {s t : Set Ω}
    (hs : MeasurableSet s) (ht : MeasurableSet t) (hd : Disjoint s t) :
    (M (s ∪ t) (hs.union ht) : E) = M s hs + M t ht
```

**`ProbabilisticTheory.EffectValuedMeasure.coe_apply_finset`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L227).

> The effect of a finite event is the sum of the effects of its outcomes.

```lean
lemma coe_apply_finset (M : EffectValuedMeasure Ω E) (t : Finset Ω) :
    (M t t.measurableSet : E) = ∑ x ∈ t, (M {x} (measurableSet_singleton x) : E)
```

**`ProbabilisticTheory.EffectValuedMeasure.coe_apply_eq_atomSum`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L238).

> On a finite discrete outcome space, a measurement is the sum of its singleton effects.

```lean
lemma coe_apply_eq_atomSum (M : EffectValuedMeasure Ω E) (s : Set Ω) (hs : MeasurableSet s) :
    (M s hs : E) = atomSum (fun x => M {x} (measurableSet_singleton x)) s
```

**`ProbabilisticTheory.EffectValuedMeasure.ext_of_singleton`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L245).

> Two measurements on a finite discrete space agree when all singleton effects agree.

```lean
lemma ext_of_singleton {M N : EffectValuedMeasure Ω E}
    (h : ∀ x, M {x} (measurableSet_singleton x) = N {x} (measurableSet_singleton x)) :
    M = N
```

## E. Relabeling outcomes

**`ProbabilisticTheory.EffectValuedMeasure.mapOutcome`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L265).

> Relabel the outcomes of an effect-valued measure along a measurable map.

```lean
def mapOutcome (N : EffectValuedMeasure Ω' E) (f : Ω' → Ω) (hf : Measurable f) :
    EffectValuedMeasure Ω E
```

**`ProbabilisticTheory.EffectValuedMeasure.coe_mapOutcome_apply`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean#L276).

```lean
lemma coe_mapOutcome_apply (N : EffectValuedMeasure Ω' E) (f : Ω' → Ω) (hf : Measurable f)
    (s : Set Ω) (hs : MeasurableSet s) : (N.mapOutcome f hf s hs : E) = N (f ⁻¹' s) (hf hs)
```

## Depends on

- [Effects](../../../physlib/probabilistictheory/effect/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/EffectValuedMeasure.lean)
