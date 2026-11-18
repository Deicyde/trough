---
declaration: module
origin: cited
lean: ProbabilisticTheory.EffectValuedMeasure.IsPartition, ProbabilisticTheory.EffectValuedMeasure.simpleValue, ProbabilisticTheory.EffectValuedMeasure.simpleValue_apply_of_mem, ProbabilisticTheory.EffectValuedMeasure.apply_congr, ProbabilisticTheory.EffectValuedMeasure.apply_iUnion_eq_sum_of_eventually_empty, ProbabilisticTheory.EffectValuedMeasure.apply_union_of_disjoint, ProbabilisticTheory.EffectValuedMeasure.apply_biUnion_of_disjoint, ProbabilisticTheory.EffectValuedMeasure.apply_iUnion_of_disjoint
statement: formalized
proof: formalized
---

# Integrating simple functions against an effect-valued measure

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.Integral`, [PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean): 15 declarations, 15 with a docstring.

> The integral of simple functions against an effect-valued measure, linear and positive.

## i. Overview

> An effect-valued measure `μ` assigns an effect to every event. Integrating a simple function `∑ᵢ cᵢ
> 𝟙\_\{sᵢ}` against it gives `∑ᵢ cᵢ μ(sᵢ)`. The effect-valued measure is finitely additive, so this does
> not depend on how the function is written: two partitions representing the same function give the
> same value, by passing to their common refinement. The integral is linear and positive.

## ii. Key results

> - `EffectValuedMeasure.apply_iUnion_of_disjoint` : finite additivity.
> - `EffectValuedMeasure.IsPartition` : finite measurable partitions.
> - `EffectValuedMeasure.simpleIntegral` : the integral `∑ᵢ cᵢ μ(sᵢ)` of a simple function.
> - `EffectValuedMeasure.simpleIntegral_eq_of_pointwise_eq` : the integral depends only on the
>   function.
> - `EffectValuedMeasure.simpleIntegral_nonneg` : the integral is positive.

## iv. References

> * None.

## A. Finite measurable partitions and simple functions

> Nothing here refers to `E` or to a POVM at all yet: a partition and the simple function it carries
> are facts about `Ω` alone.

**`ProbabilisticTheory.EffectValuedMeasure.IsPartition`**, a structure, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L62).

> `s` is a finite measurable partition of `Ω`: its pieces are measurable, pairwise disjoint, and
> cover `Ω`. This is the "unbundled `he : ∑ i, e i = 1`" of `Measurement.toChannel`
> transported to the measure-theoretic setting: there, a finite family of
> effects summing to the certain event; here, a finite family of sets whose indicators sum to the
> constant function `1`.

```lean
structure IsPartition {ι : Type*} [Fintype ι] (s : ι → Set Ω) : Prop where
  /-- Every piece of the partition is measurable. -/
  measurable : ∀ i, MeasurableSet (s i)
  /-- Distinct pieces of the partition are disjoint. -/
  disjoint : ∀ i j, i ≠ j → Disjoint (s i) (s j)
  /-- The pieces cover all of `Ω`. -/
  cover : ⋃ i, s i = Set.univ
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleValue`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L71).

> The simple function `∑ᵢ cᵢ 𝟙_{sᵢ}` of a partition.

```lean
noncomputable def simpleValue {ι : Type*} [Fintype ι] (c : ι → ℝ) (s : ι → Set Ω) (x : Ω) : ℝ
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleValue_apply_of_mem`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L76).

> At a point lying in piece `i` of the partition, the simple function evaluates to `c i`: every
> other term of the defining sum vanishes since the pieces are pairwise disjoint.

```lean
lemma simpleValue_apply_of_mem {ι : Type*} [Fintype ι] {c : ι → ℝ} {s : ι → Set Ω}
    (hs : IsPartition s) {x : Ω} {i : ι} (hx : x ∈ s i) : simpleValue c s x = c i
```

## B. Finite additivity

> `EffectValuedMeasure` only bundles *countable* additivity (`countably_additive`). Finite
> additivity is the special case of a family that is eventually `∅`, and the least upper bound of an
> eventually-constant, nondecreasing sequence (nondecreasing since every value of `μ` is a
> nonnegative effect) is just its eventual value — which is what lets us read finite sums off
> `countably_additive` directly.

**`ProbabilisticTheory.EffectValuedMeasure.apply_congr`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L101).

> Applying `μ` only depends on the set, not on which proof of measurability is supplied — an
> immediate consequence of `Set` equality and proof irrelevance, recorded here since it comes up
> whenever a set is simplified (e.g. `if`-reduced) mid-computation.

```lean
lemma apply_congr (μ : EffectValuedMeasure Ω E) {s t : Set Ω} (h : s = t)
    {hs : MeasurableSet s} {ht : MeasurableSet t} : (μ s hs : E) = (μ t ht : E)
```

**`ProbabilisticTheory.EffectValuedMeasure.apply_iUnion_eq_sum_of_eventually_empty`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L109).

> Padding a finite disjoint family with `∅` and applying countable additivity: past the point
> where every remaining piece is `∅`, the partial sums have stabilized, and since they are also
> nondecreasing (every value of `μ` is a nonnegative effect), that stable value is already the least
> upper bound `countably_additive` promises — so it computes `μ` of the union.

```lean
lemma apply_iUnion_eq_sum_of_eventually_empty (μ : EffectValuedMeasure Ω E) (t : ℕ → Set Ω)
    (htm : ∀ n, MeasurableSet (t n)) (htd : ∀ m n, m ≠ n → Disjoint (t m) (t n)) {N : ℕ}
    (hN : ∀ n, N ≤ n → t n = ∅) :
    (μ (⋃ n, t n) (MeasurableSet.iUnion htm) : E) =
      ∑ n ∈ Finset.range N, (μ (t n) (htm n) : E)
```

**`ProbabilisticTheory.EffectValuedMeasure.apply_union_of_disjoint`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L145).

> Binary additivity of `μ`, derived from countable additivity by padding a two-element family
> with `∅`.

```lean
lemma apply_union_of_disjoint (μ : EffectValuedMeasure Ω E) {A B : Set Ω}
    (hA : MeasurableSet A) (hB : MeasurableSet B) (hAB : Disjoint A B) :
    (μ (A ∪ B) (hA.union hB) : E) = (μ A hA : E) + (μ B hB : E)
```

**`ProbabilisticTheory.EffectValuedMeasure.apply_biUnion_of_disjoint`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L199).

> Finite additivity of `μ` over a pairwise disjoint family indexed by a `Finset`, with the
> disjointness only required on the labels actually occurring in `s`. Proved by induction on the
> `Finset`, peeling one element off at a time using binary additivity
> (`apply_union_of_disjoint`).

```lean
lemma apply_biUnion_of_disjoint {ι : Type*} [DecidableEq ι] (μ : EffectValuedMeasure Ω E)
    (f : ι → Set Ω) (hfm : ∀ i, MeasurableSet (f i)) (s : Finset ι)
    (hfd : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Disjoint (f i) (f j)) :
    (μ (⋃ i ∈ s, f i) (s.measurableSet_biUnion fun i _ => hfm i) : E) =
      ∑ i ∈ s, (μ (f i) (hfm i) : E)
```

**`ProbabilisticTheory.EffectValuedMeasure.apply_iUnion_of_disjoint`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L237).

> Finite additivity of `μ` over a `Fintype`-indexed pairwise disjoint family: the workhorse used
> throughout the rest of this file.

```lean
lemma apply_iUnion_of_disjoint {ι : Type*} [Fintype ι] [DecidableEq ι]
    (μ : EffectValuedMeasure Ω E) (f : ι → Set Ω) (hfm : ∀ i, MeasurableSet (f i))
    (hfd : ∀ i j, i ≠ j → Disjoint (f i) (f j)) :
    (μ (⋃ i, f i) (MeasurableSet.iUnion hfm) : E) = ∑ i, (μ (f i) (hfm i) : E)
```

## C. The integral of a simple function

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L251).

> The integral of the simple function `∑ i, c i • 𝟙_{s i}` against `μ`: `∑ i, c i • μ(s i)`.
> Well-defined independently of the chosen partition by `simpleIntegral_eq_of_pointwise_eq`, and
> this is exactly `Measurement.toChannel` in the case where every piece of
> the partition is a single point mass.

```lean
noncomputable def simpleIntegral {ι : Type*} [Fintype ι] (μ : EffectValuedMeasure Ω E)
    (c : ι → ℝ) (s : ι → Set Ω) (hs : IsPartition s) : E
```

**`ProbabilisticTheory.EffectValuedMeasure.apply_eq_sum_inter`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L258).

> On a partition, the piece `s i` decomposes as the union of its intersections with every piece
> of a second partition `s'`: `s'` covers `Ω`, so intersecting with `s i` covers `s i`. Used to
> refine two partitions to their common refinement in `simpleIntegral_eq_of_pointwise_eq`.

```lean
lemma apply_eq_sum_inter {ι ι' : Type*} [Fintype ι] [Fintype ι'] [DecidableEq ι']
    (μ : EffectValuedMeasure Ω E) {s : ι → Set Ω} {s' : ι' → Set Ω} (hs : IsPartition s)
    (hs' : IsPartition s') (i : ι) :
    (μ (s i) (hs.measurable i) : E) =
      ∑ j, (μ (s i ∩ s' j) ((hs.measurable i).inter (hs'.measurable j)) : E)
```

**`ProbabilisticTheory.EffectValuedMeasure.apply_eq_sum_inter'`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L274).

> The symmetric counterpart of `apply_eq_sum_inter`, with the roles of the two partitions
> swapped: the piece `s' j` decomposes as the union of its intersections with every piece of `s`.

```lean
lemma apply_eq_sum_inter' {ι ι' : Type*} [Fintype ι] [Fintype ι'] [DecidableEq ι]
    (μ : EffectValuedMeasure Ω E) {s : ι → Set Ω} {s' : ι' → Set Ω} (hs : IsPartition s)
    (hs' : IsPartition s') (j : ι') :
    (μ (s' j) (hs'.measurable j) : E) =
      ∑ i, (μ (s i ∩ s' j) ((hs.measurable i).inter (hs'.measurable j)) : E)
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral_eq_of_pointwise_eq`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L284).

> **The simple integral depends only on the function.** Two partitions describing the same
> function give the same integral, by passing to the common refinement.

```lean
lemma simpleIntegral_eq_of_pointwise_eq {ι ι' : Type*} [Fintype ι] [Fintype ι'] [DecidableEq ι]
    [DecidableEq ι'] (μ : EffectValuedMeasure Ω E) (c : ι → ℝ) (s : ι → Set Ω) (hs : IsPartition s)
    (c' : ι' → ℝ)
    (s' : ι' → Set Ω) (hs' : IsPartition s')
    (hval : ∀ x, simpleValue c s x = simpleValue c' s' x) :
    simpleIntegral μ c s hs = simpleIntegral μ c' s' hs'
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral_add`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L318).

> The simple integral is additive in the weights, over a fixed partition.

```lean
lemma simpleIntegral_add (μ : EffectValuedMeasure Ω E) (c₁ c₂ : ι → ℝ) (s : ι → Set Ω)
    (hs : IsPartition s) :
    simpleIntegral μ (c₁ + c₂) s hs = simpleIntegral μ c₁ s hs + simpleIntegral μ c₂ s hs
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral_smul`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L326).

> The simple integral is homogeneous in the weights, over a fixed partition.

```lean
lemma simpleIntegral_smul (μ : EffectValuedMeasure Ω E) (r : ℝ) (c : ι → ℝ) (s : ι → Set Ω)
    (hs : IsPartition s) :
    simpleIntegral μ (r • c) s hs = r • simpleIntegral μ c s hs
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral_nonneg`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean#L335).

> The simple integral of a nonnegative simple function is nonnegative — matching `μ`'s own
> positivity: every term `c i • μ(s i)` is a nonnegative scalar times a nonnegative effect.

```lean
lemma simpleIntegral_nonneg (μ : EffectValuedMeasure Ω E) {c : ι → ℝ} (hc : ∀ i, 0 ≤ c i)
    (s : ι → Set Ω) (hs : IsPartition s) : 0 ≤ simpleIntegral μ c s hs
```

## Depends on

- [Effect-valued measures](effectvaluedmeasure.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Integral.lean)
