---
catalog: module
lean: MeasureTheory.HasFiniteSupport, MeasureTheory.HasFiniteSupport.exists_eq_sum_smul_dirac, MeasureTheory.HasFiniteSupport.isFiniteMeasure, MeasureTheory.NullMeasurableSet.of_hasFiniteSupport
statement: formalized
proof: formalized
---

# Measures supported on finite sets

`Cslib.Foundations.MeasureTheory.FiniteSupport`, in [Cslib/Foundations/MeasureTheory/FiniteSupport.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/MeasureTheory/FiniteSupport.lean), by Samuel Schlesinger, Thomas Waring.

> For a measure that vanishes off a finite set, every set is null-measurable if
> singletons are measurable. Finite support is preserved by finite products of
> finite measures. These facts let sample-complexity arguments in learning
> theory measure failure events of *arbitrary* (non-measurable) learners under
> finitely supported adversarial distributions.
>
> `HasFiniteSupport` records this property as a typeclass, with an instance for
> finite products.
>
> The [PFR project](https://github.com/teorth/pfr/blob/master/PFR/ForMathlib/Entropy/Measure.lean)
> has an equivalent `ProbabilityTheory.FiniteSupport` class, expressed using an almost-everywhere
> `Finset` witness.
>
> ## Main statements
>
> - `MeasureTheory.HasFiniteSupport`: a measure vanishes off some finite set.
> - `MeasureTheory.HasFiniteSupport.exists_eq_sum_smul_dirac`: on a space with measurable
>   singletons, a measure with finite support is a finite sum of Dirac measures weighted by
>   its singleton masses.
> - `MeasureTheory.HasFiniteSupport.isFiniteMeasure`: a sigma-finite measure with finite
>   support is finite.
> - `MeasureTheory.NullMeasurableSet.of_hasFiniteSupport`: on a space with measurable
>   singletons, every set is null-measurable for a measure with finite support,
>   including finite products.

`MeasureTheory.HasFiniteSupport` (class, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/MeasureTheory/FiniteSupport.lean#L49))

> A measure vanishes off a finite set.

```lean
class HasFiniteSupport {α : Type*} [MeasurableSpace α] (μ : Measure α) : Prop where
  /-- Some finite set has null complement. -/
  exists_finite_measure_compl_zero : ∃ s : Set α, s.Finite ∧ μ sᶜ = 0
```

`MeasureTheory.HasFiniteSupport.exists_eq_sum_smul_dirac` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/MeasureTheory/FiniteSupport.lean#L56))

> On a space with measurable singletons, a measure with finite support is a finite sum
> of Dirac measures weighted by its singleton masses. This is `Measure.ae_mem_finset_iff`
> applied to a finite support.

```lean
theorem HasFiniteSupport.exists_eq_sum_smul_dirac {α : Type*} [MeasurableSpace α]
    [MeasurableSingletonClass α] (μ : Measure α) [HasFiniteSupport μ] :
    ∃ s : Finset α, μ = ∑ a ∈ s, μ {a} • Measure.dirac a
```

`MeasureTheory.HasFiniteSupport.isFiniteMeasure` (instance, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/MeasureTheory/FiniteSupport.lean#L66))

> A sigma-finite measure with finite support is finite.

```lean
instance (priority := 100) HasFiniteSupport.isFiniteMeasure {α : Type*} [MeasurableSpace α]
    (μ : Measure α) [HasFiniteSupport μ] [SigmaFinite μ] : IsFiniteMeasure μ
```

`MeasureTheory.NullMeasurableSet.of_hasFiniteSupport` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/MeasureTheory/FiniteSupport.lean#L75))

> On a space with measurable singletons, every set is null-measurable for a measure
> with finite support.

```lean
theorem NullMeasurableSet.of_hasFiniteSupport {α : Type*} [MeasurableSpace α]
    [MeasurableSingletonClass α] {μ : Measure α} [HasFiniteSupport μ]
    (t : Set α) : NullMeasurableSet t μ
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/MeasureTheory/FiniteSupport.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/MeasureTheory/FiniteSupport.lean)
