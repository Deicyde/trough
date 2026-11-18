---
declaration: module
origin: cited
lean: ProbabilityMeasure.exists_map_eq_of_continuous_of_compl_range_null, ProbabilityMeasure.averageMap, ProbabilityMeasure.integral_averageMap, ProbabilityMeasure.condition, ProbabilityMeasure.condition_compl_apply, ProbabilityMeasure.measure_smul_condition_eq_restrict, ProbabilityMeasure.replacePart, ProbabilityMeasure.replacePart_toMeasure
statement: formalized
proof: formalized
---

# Lifting, averaging and conditioning probability measures

The module `PhyslibAlpha.Mathematics.MeasureTheory.LiftingAndConditioning`, [PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean): 10 declarations, 5 with a docstring.

> Lifting, averaging, conditioning and replacing parts of probability measures.

## i. Overview

> This file collects operations on probability measures used in Choquet's theorem. A probability
> measure on the compact range of a continuous map is the image of a probability measure on its
> source. The images of one measure under two maps can be averaged. A measure can be conditioned on an
> event of positive probability. Finally, the part of a measure on an event can be handed to another
> measure.

## ii. Key results

> - `ProbabilityMeasure.exists_map_eq_of_continuous_of_compl_range_null` proves that a probability
>   measure on the range of a continuous map lifts to its source.
> - `ProbabilityMeasure.averageMap` is the average of two images of a measure.
> - `ProbabilityMeasure.condition` conditions a measure on an event.
> - `ProbabilityMeasure.replacePart` replaces the part of a measure on an event.

## iv. References

> * None.

## A. Lifting through a compact continuous map

**`ProbabilityMeasure.exists_map_eq_of_continuous_of_compl_range_null`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L67).

> A probability measure charging only the range of a continuous map from a compact space lifts
> through that map: integration against it is a positive functional on continuous functions on the
> domain, which extends and is represented by a measure.

```lean
lemma exists_map_eq_of_continuous_of_compl_range_null (q : X → Y) (hq : Continuous q)
    (mu : ProbabilityMeasure Y) (hmu : (mu : Measure Y) (Set.range q)ᶜ = 0) :
    ∃ nu : ProbabilityMeasure X, nu.map q = mu
```

## B. Averaging two pushforwards

**`ProbabilityMeasure.averageMap`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L94).

> The average of the two pushforwards of a probability measure.

```lean
noncomputable def averageMap (rho : ProbabilityMeasure A) (f g : A → B)
    (hf : AEMeasurable f rho) (hg : AEMeasurable g rho) : ProbabilityMeasure B
```

**`ProbabilityMeasure.integral_averageMap`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L107).

```lean
lemma integral_averageMap {rho : ProbabilityMeasure A} {f g : A → B}
    (hf : AEMeasurable f rho) (hg : AEMeasurable g rho) {u : B → ℝ}
    (hu : Integrable u (rho.map f))
    (hv : Integrable u (rho.map g)) :
    ∫ x, u x ∂(averageMap rho f g hf hg : Measure B) =
      ((1 : ℝ) / 2) * (∫ x, u (f x) ∂(rho : Measure A)) +
        ((1 : ℝ) / 2) * (∫ x, u (g x) ∂(rho : Measure A))
```

## C. Conditioning and replacing part of a measure

**`ProbabilityMeasure.condition`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L135).

> The conditional law of a probability measure on a positive-measure event.

```lean
noncomputable def condition (mu : ProbabilityMeasure B) (S : Set B)
    (hS : (mu : Measure B) S ≠ 0) : ProbabilityMeasure B
```

**`ProbabilityMeasure.condition_compl_apply`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L140).

```lean
lemma condition_compl_apply (mu : ProbabilityMeasure B) {S : Set B}
    (hSm : MeasurableSet S) (hS : (mu : Measure B) S ≠ 0) :
    (condition mu S hS : Measure B) Sᶜ = 0
```

**`ProbabilityMeasure.measure_smul_condition_eq_restrict`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L147).

```lean
lemma measure_smul_condition_eq_restrict (mu : ProbabilityMeasure B) {S : Set B}
    (hSm : MeasurableSet S) (hS : (mu : Measure B) S ≠ 0) :
    (mu : Measure B) S • (condition mu S hS : Measure B) = (mu : Measure B).restrict S
```

**`ProbabilityMeasure.replacePart`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L156).

> Replace the mass of `mu` on `S` by the same amount of another probability measure.

```lean
noncomputable def replacePart (mu eta : ProbabilityMeasure B) (S : Set B)
    (hS : MeasurableSet S) : ProbabilityMeasure B
```

**`ProbabilityMeasure.replacePart_toMeasure`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L165).

```lean
lemma replacePart_toMeasure (mu eta : ProbabilityMeasure B) (S : Set B)
    (hS : MeasurableSet S) :
    (replacePart mu eta S hS : Measure B) =
      (mu : Measure B).restrict Sᶜ + (mu : Measure B) S • (eta : Measure B)
```

**`ProbabilityMeasure.integral_eq_restrict_compl_add_condition`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L172).

> Integrating against `mu` splits into the part off `S` plus the mass of `S` times the
> conditional integral on `S`.

```lean
lemma integral_eq_restrict_compl_add_condition (mu : ProbabilityMeasure B) {S : Set B}
    (hS : MeasurableSet S) (hpos : (mu : Measure B) S ≠ 0) {f : B → ℝ}
    (hf : Integrable f (mu : Measure B)) :
    ∫ x, f x ∂(mu : Measure B) = ∫ x, f x ∂((mu : Measure B).restrict Sᶜ) +
      ((mu : Measure B) S).toReal * ∫ x, f x ∂(condition mu S hpos : Measure B)
```

**`ProbabilityMeasure.integral_replacePart`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean#L181).

```lean
lemma integral_replacePart (mu eta : ProbabilityMeasure B) (S : Set B) (hS : MeasurableSet S)
    {f : B → ℝ} (hmu : Integrable f (mu : Measure B)) (heta : Integrable f (eta : Measure B)) :
    ∫ x, f x ∂(replacePart mu eta S hS : Measure B) = ∫ x, f x ∂((mu : Measure B).restrict Sᶜ) +
      ((mu : Measure B) S).toReal * ∫ x, f x ∂(eta : Measure B)
```

## Depends on

- [Integration as a continuous functional](integrationfunctional.md)

## Proof depends on

- [Positive functionals are integrals](positivefunctionalintegral.md)

## Sources

- [PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/LiftingAndConditioning.lean)
