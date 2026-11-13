---
declaration: module
origin: cited
lean: ProbabilisticTheory.MeasurableProjectionResolution, ProbabilisticTheory.MeasurableProjectionResolution.ext, ProbabilisticTheory.MeasurableProjectionResolution.map_empty, ProbabilisticTheory.MeasurableProjectionResolution.map_univ, ProbabilisticTheory.MeasurableProjectionResolution.isJordanProjection, ProbabilisticTheory.MeasurableProjectionResolution.map_inter, ProbabilisticTheory.MeasurableProjectionResolution.jordanOrthogonal_of_disjoint, ProbabilisticTheory.MeasurableProjectionResolution.countably_additive
statement: formalized
proof: formalized
---

# Projection resolutions

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.ProjectionResolution`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean): 20 declarations (2 instances with no name), 18 with a docstring.

> Projection resolutions: projection-valued effect measures and their bounded Borel calculus.

## i. Overview

> A projection resolution is an effect-valued measure whose values are Jordan projections and whose
> value on an intersection is the Jordan product of the values. Integrating bounded measurable
> functions against it gives a bounded Borel functional calculus.

## ii. Key results

> - `MeasurableProjectionResolution` : projection resolutions.
> - `MeasurableProjectionResolution.jordanOrthogonal_of_disjoint` : disjoint sets give orthogonal
>   projections.
> - `MeasurableProjectionResolution.boundedBorel` : the bounded Borel functional calculus.

## iv. References

> * None.

**`ProbabilisticTheory.MeasurableProjectionResolution`**, a structure, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L52).

> A projection resolution: an effect-valued measure whose values are Jordan projections, with the
> value on an intersection the Jordan product of the values.

```lean
structure MeasurableProjectionResolution (Ω : Type*) [MeasurableSpace Ω] (E : Type*)
    [IsJordanOrderUnit E] where
  /-- The underlying countably additive effect-valued measure. -/
  toEffectValuedMeasure : EffectValuedMeasure Ω E
  /-- Every measurable event is a Jordan projection. -/
  isJordanProjection' : ∀ s hs,
    JordanAlgebra.IsJordanProjection (toEffectValuedMeasure s hs : E)
  /-- Intersection of measurable events is multiplication of their projections. -/
  map_inter' : ∀ s t hs ht,
    (toEffectValuedMeasure s hs : E) * (toEffectValuedMeasure t ht : E) =
      (toEffectValuedMeasure (s ∩ t) (hs.inter ht) : E)
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L66).

```lean
instance : CoeOut (MeasurableProjectionResolution Ω E) (EffectValuedMeasure Ω E)
```

**An instance with no name**, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L69).

```lean
instance : CoeFun (MeasurableProjectionResolution Ω E) fun _ =>
    ∀ s : Set Ω, MeasurableSet s → Effect E
```

**`ProbabilisticTheory.MeasurableProjectionResolution.ext`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L76).

> Projection resolutions are determined by their event projections.  This is purely structural
> and belongs below JBW: normal-state separation is only one later way to establish its premise.

```lean
lemma ext {P Q : MeasurableProjectionResolution Ω E}
    (h : ∀ s hs, (P s hs : E) = (Q s hs : E)) : P = Q
```

**`ProbabilisticTheory.MeasurableProjectionResolution.map_empty`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L89).

> The impossible event is the zero effect.

```lean
lemma map_empty (P : MeasurableProjectionResolution Ω E) :
    P ∅ MeasurableSet.empty = 0
```

**`ProbabilisticTheory.MeasurableProjectionResolution.map_univ`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L94).

> The whole outcome space is the unit effect.

```lean
lemma map_univ (P : MeasurableProjectionResolution Ω E) :
    P Set.univ MeasurableSet.univ = 1
```

**`ProbabilisticTheory.MeasurableProjectionResolution.isJordanProjection`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L99).

> Each event of a measurable projection resolution is an intrinsic Jordan projection.

```lean
lemma isJordanProjection (P : MeasurableProjectionResolution Ω E)
    (s : Set Ω) (hs : MeasurableSet s) :
    JordanAlgebra.IsJordanProjection (P s hs : E)
```

**`ProbabilisticTheory.MeasurableProjectionResolution.map_inter`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L105).

> The projection product computes measurable intersection.

```lean
lemma map_inter (P : MeasurableProjectionResolution Ω E)
    (s t : Set Ω) (hs : MeasurableSet s) (ht : MeasurableSet t) :
    (P s hs : E) * (P t ht : E) = P (s ∩ t) (hs.inter ht)
```

**`ProbabilisticTheory.MeasurableProjectionResolution.jordanOrthogonal_of_disjoint`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L111).

> Disjoint measurable events have Jordan-orthogonal projections.

```lean
lemma jordanOrthogonal_of_disjoint (P : MeasurableProjectionResolution Ω E)
    {s t : Set Ω} (hs : MeasurableSet s) (ht : MeasurableSet t) (hdisj : Disjoint s t) :
    JordanAlgebra.JordanOrthogonal (P s hs : E) (P t ht : E)
```

**`ProbabilisticTheory.MeasurableProjectionResolution.countably_additive`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L122).

> The inherited countable-additivity law, stated in the ambient ordered Jordan algebra.

```lean
lemma countably_additive (P : MeasurableProjectionResolution Ω E) (s : ℕ → Set Ω)
    (hsm : ∀ n, MeasurableSet (s n)) (hs : Pairwise (Disjoint on s)) :
    IsLUB (Set.range fun N : ℕ => ∑ n ∈ Finset.range N, (P (s n) (hsm n) : E))
      (P (⋃ n, s n) (MeasurableSet.iUnion hsm) : E)
```

## A. Bounded Borel calculus

> The resolution does not duplicate the order-unit integral: in a JB algebra, which is complete in
> its order-unit norm, this section gives that integral its spectral-calculus name.

**`ProbabilisticTheory.MeasurableProjectionResolution.boundedBorel`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L145).

> The bounded Borel calculus of a measurable projection resolution. This is the existing
> effect-valued integral applied to the underlying measure, not a parallel construction.

```lean
noncomputable def boundedBorel (P : MeasurableProjectionResolution Ω E) (f : Ω → ℝ)
    (hf : Measurable f) {M : ℝ} (hM : ∀ x, |f x| ≤ M) : E
```

**`ProbabilisticTheory.MeasurableProjectionResolution.nonneg_boundedBorel`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L150).

> A nonnegative bounded Borel function has a positive value under the resolution calculus.

```lean
lemma nonneg_boundedBorel (P : MeasurableProjectionResolution Ω E) (f : Ω → ℝ)
    (hf : Measurable f) {M : ℝ} (hM : ∀ x, |f x| ≤ M) (hf0 : ∀ x, 0 ≤ f x) :
    0 ≤ P.boundedBorel f hf hM
```

**`ProbabilisticTheory.MeasurableProjectionResolution.boundedBorel_indep_of_bound`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L157).

> The bounded Borel value is independent of the particular valid uniform bound used to
> construct the completed order-unit integral.

```lean
lemma boundedBorel_indep_of_bound (P : MeasurableProjectionResolution Ω E) (f : Ω → ℝ)
    (hf : Measurable f) {M M' : ℝ} (hM : ∀ x, |f x| ≤ M) (hM' : ∀ x, |f x| ≤ M') :
    P.boundedBorel f hf hM = P.boundedBorel f hf hM'
```

**`ProbabilisticTheory.MeasurableProjectionResolution.boundedBorel_add`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L163).

> The bounded Borel calculus is additive.

```lean
lemma boundedBorel_add (P : MeasurableProjectionResolution Ω E) {f g : Ω → ℝ}
    (hf : Measurable f) {M : ℝ} (hM : ∀ x, |f x| ≤ M)
    (hg : Measurable g) {M' : ℝ} (hM' : ∀ x, |g x| ≤ M')
    (hfg : Measurable (f + g)) (hMfg : ∀ x, |(f + g) x| ≤ M + M') :
    P.boundedBorel (f + g) hfg hMfg =
      P.boundedBorel f hf hM + P.boundedBorel g hg hM'
```

**`ProbabilisticTheory.MeasurableProjectionResolution.boundedBorel_smul`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L172).

> The bounded Borel calculus is real-homogeneous.

```lean
lemma boundedBorel_smul (P : MeasurableProjectionResolution Ω E) (c : ℝ) {f : Ω → ℝ}
    (hf : Measurable f) {M : ℝ} (hM : ∀ x, |f x| ≤ M)
    (hcf : Measurable (c • f)) (hMcf : ∀ x, |(c • f) x| ≤ |c| * M) :
    P.boundedBorel (c • f) hcf hMcf = c • P.boundedBorel f hf hM
```

**`ProbabilisticTheory.MeasurableProjectionResolution.boundedBorel_indicator`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L179).

> The functional calculus of an indicator is the projection of the event.

```lean
lemma boundedBorel_indicator (P : MeasurableProjectionResolution Ω E) {s : Set Ω}
    (hs : MeasurableSet s) :
    P.boundedBorel (s.indicator fun _ : Ω => (1 : ℝ)) (measurable_const.indicator hs)
        (M := 1) (by intro x; by_cases hx : x ∈ s <;> simp [hx]) = (P s hs : E)
```

**`ProbabilisticTheory.MeasurableProjectionResolution.boundedBorel_one`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L221).

> The constant-one bounded Borel function integrates to the order unit.  This is the
> normalization of the inherited effect-valued measure, recovered from the indicator law for the
> whole outcome space.

```lean
lemma boundedBorel_one (P : MeasurableProjectionResolution Ω E) :
    P.boundedBorel (fun _ : Ω => (1 : ℝ)) measurable_const (M := 1) (by intro _; simp) = 1
```

**`ProbabilisticTheory.MeasurableProjectionResolution.boundedBorelEffect`**, a def, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L228).

> A measurable `[0,1]`-valued bounded function has an effect-valued bounded Borel calculus.
> This packages positivity and normalization once at the shared projection-resolution layer; every
> JBW projection resolution inherits it.

```lean
noncomputable def boundedBorelEffect (P : MeasurableProjectionResolution Ω E) (f : Ω → ℝ)
    (hf : Measurable f) (hf0 : ∀ x, 0 ≤ f x) (hf1 : ∀ x, f x ≤ 1) : Effect E
```

**`ProbabilisticTheory.MeasurableProjectionResolution.coe_boundedBorelEffect`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L274).

> Coercing the bounded Borel effect forgets only its established interval bounds.

```lean
lemma coe_boundedBorelEffect (P : MeasurableProjectionResolution Ω E) (f : Ω → ℝ)
    (hf : Measurable f) (hf0 : ∀ x, 0 ≤ f x) (hf1 : ∀ x, f x ≤ 1) :
    (P.boundedBorelEffect f hf hf0 hf1 : E) =
      P.boundedBorel f hf (M := 1)
        (fun x => by rw [abs_of_nonneg (hf0 x)]; exact hf1 x)
```

**`ProbabilisticTheory.MeasurableProjectionResolution.ext_of_forall_boundedBorel_eq`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean#L283).

> The bounded Borel calculus determines a projection resolution.  It suffices to compare every
> bounded measurable function because indicators recover exactly the event projections.

```lean
lemma ext_of_forall_boundedBorel_eq {P Q : MeasurableProjectionResolution Ω E}
    (h : ∀ (f : Ω → ℝ) (hf : Measurable f) {M : ℝ} (hM : ∀ x, |f x| ≤ M),
      P.boundedBorel f hf hM = Q.boundedBorel f hf hM) : P = Q
```

## Depends on

- [Normed Jordan algebras and JB-algebras](jb-basic.md)
- [Moments, variance and Jordan projections](observable.md)
- [Integrating bounded functions against an effect-valued measure](../../measurement/boundedintegral.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/ProjectionResolution.lean)
