---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.instCoeVectorMeasure, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.instCoeFun, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.isStarProjection, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.univ, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.apply_eq_zero_of_not_measurableSet, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.comp_self, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.comp_of_disjoint
statement: formalized
proof: formalized
---

# Weak-operator spectral measures

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Basic`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean): 21 declarations (1 instance with no name), 5 with a docstring.

> Projection-valued measures that are countably additive in the weak operator topology.

## i. Overview

> A spectral measure of an unbounded self-adjoint operator is a projection-valued measure that is
> countably additive in the weak operator topology, that is, on each pair of vectors.
> `WOTSpectralMeasure` is such a measure, valued in `H →WOT[ℂ] H`. Its values are commuting
> projections, orthogonal on disjoint sets and multiplicative on intersections. A spectral measure
> that is countably additive in norm is in particular a weak spectral measure, and weak spectral
> measures push forward along measurable maps.

## ii. Key results

> - `WOTSpectralMeasure` : a projection-valued measure, countably additive in the weak operator
>   topology.
> - `WOTSpectralMeasure.comp_eq_of_inter` : `μ A μ B = μ (A ∩ B)`.
> - `WOTSpectralMeasure.map` : the pushforward along a measurable map.
> - `SpectralMeasure.toWOT` : a norm-additive spectral measure as a weak spectral measure.

## iv. References

> * None.

**An instance with no name**, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L59).

```lean
instance (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] :
    HasUniqueDiv (H →WOT[ℂ] H)
```

## A. The structure and its basic algebra

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure`**, a structure, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L70).

> A projection-valued measure that is countably additive in the weak operator topology.

```lean
structure WOTSpectralMeasure
    (α : Type*) [MeasurableSpace α]
    (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    extends VectorMeasure α (H →WOT[ℂ] H) where
  isStarProjection' : ∀ A, IsStarProjection (measureOf' A)
  univ' : measureOf' univ = 1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.instCoeVectorMeasure`**, an instance, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L85).

```lean
instance instCoeVectorMeasure : Coe (WOTSpectralMeasure α H)
    (VectorMeasure α (H →WOT[ℂ] H))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.instCoeFun`**, an instance, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L88).

```lean
instance instCoeFun : CoeFun (WOTSpectralMeasure α H) fun _ ↦ Set α → H →WOT[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.isStarProjection`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L91).

```lean
lemma isStarProjection (A : Set α) : IsStarProjection (μS A)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.univ`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L94).

```lean
lemma univ : μS univ = 1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.apply_eq_zero_of_not_measurableSet`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L96).

```lean
lemma apply_eq_zero_of_not_measurableSet {A : Set α} (hA : ¬MeasurableSet A) : μS A = 0
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.comp_self`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L99).

```lean
lemma comp_self (A : Set α) : μS A * μS A = μS A
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.comp_of_disjoint`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L102).

```lean
lemma comp_of_disjoint {A B : Set α} (h : Disjoint A B) (hA : MeasurableSet A)
    (hB : MeasurableSet B) : μS A * μS B = 0
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.comp_eq_of_inter`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L112).

```lean
lemma comp_eq_of_inter {A B : Set α} (hA : MeasurableSet A) (hB : MeasurableSet B) :
    μS A * μS B = μS (A ∩ B)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.commute`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L121).

```lean
lemma commute (A B : Set α) : Commute (μS A) (μS B)
```

## B. Pushforward along a measurable map

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.map`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L129).

> Push a weak spectral measure forward along a measurable change of spectral variable.

```lean
def map {β : Type*} [MeasurableSpace β] (f : α → β) (hf : Measurable f) :
    WOTSpectralMeasure β H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.map_apply`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L144).

```lean
lemma map_apply {β : Type*} [MeasurableSpace β] (f : α → β) (hf : Measurable f)
    {S : Set β} (hS : MeasurableSet S) :
    μS.map f hf S = μS (f ⁻¹' S)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.map_map_apply`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L150).

```lean
lemma map_map_apply {β γ : Type*} [MeasurableSpace β] [MeasurableSpace γ]
    (f : α → β) (g : β → γ) (hf : Measurable f) (hg : Measurable g)
    {S : Set γ} (hS : MeasurableSet S) :
    (μS.map f hf).map g hg S = μS ((g ∘ f) ⁻¹' S)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.map_map`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L157).

```lean
lemma map_map {β γ : Type*} [MeasurableSpace β] [MeasurableSpace γ]
    (f : α → β) (g : β → γ) (hf : Measurable f) (hg : Measurable g) :
    (μS.map f hf).map g hg = μS.map (g ∘ f) (hg.comp hf)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.map_id`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L165).

```lean
lemma map_id : μS.map id measurable_id = μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.hasSum_inner`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L174).

> The σ-additivity statement seen by vectors and test vectors. This is often more convenient
> than mentioning the `WOT` type directly when proving spectral formulas.

```lean
lemma hasSum_inner {f : ℕ → Set α} (hf : ∀ i, MeasurableSet (f i))
    (hdisj : Pairwise (Disjoint on f)) (x y : H) :
    HasSum (fun i ↦ ⟪y, μS (f i) x⟫_ℂ) ⟪y, μS (⋃ i, f i) x⟫_ℂ
```

## C. Coming from a norm-continuous `SpectralMeasure`

**`SpectralMeasure.toWOTMap`**, a def, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L212).

> Forgetting norm σ-additivity and retaining weak-operator σ-additivity.

```lean
def toWOTMap : (H →L[ℂ] H) →+ (H →WOT[ℂ] H)
```

**`SpectralMeasure.continuous_toWOTMap`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L218).

```lean
lemma continuous_toWOTMap : Continuous (toWOTMap (H := H))
```

**`SpectralMeasure.toWOT`**, a def, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L224).

> A `SpectralMeasure`, viewed in the weak-operator-topology type `H →WOT[ℂ] H`.

```lean
def toWOT (μS : SpectralMeasure α H) : WOTSpectralMeasure α H
```

**`SpectralMeasure.toWOT_apply`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean#L245).

```lean
lemma toWOT_apply (μS : SpectralMeasure α H) (A : Set α) : μS.toWOT A =
    ContinuousLinearMapWOT.ofCLM (μS A)
```

## Depends on

- [Spectral measures](../../../../physlib/quantummechanics/operators/spectraltheory/spectralmeasure.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Basic.lean)
