---
declaration: theorem
origin: cited
lean: TauCeti.bcr_semigroup_bochner
statement: formalized
proof: formalized
---

# TauCeti.bcr\_semigroup\_bochner

**The Berg--Christensen--Ressel representation theorem** (Berg--Christensen--Ressel 4.1.13).
A function on the involutive semigroup `ℝ≥0 × V`, for `V` a finite-dimensional real inner-product
space, is positive definite, continuous and bounded **if and only if** it is the Laplace--Fourier
transform of a unique finite measure on `ℝ≥0 × V`:

`F (t, a) = ∫ (p, q), exp (-t p) * exp (-2πi⟪a, q⟫) dμ (p, q)`.

The forward direction is `TauCeti.exists_representsLaplaceFourier` together with the transform
injectivity of `TauCeti.RepresentsLaplaceFourier.unique`; the converse direction is the elementary
fact that such a transform is positive definite, continuous, and bounded by the total mass.

```lean
TauCeti.bcr_semigroup_bochner.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (F : NNReal × V → ℂ) :
  TauCeti.IsSemigroupGroupPD F ∧ Continuous F ∧ Bornology.IsBounded (Set.range F) ↔
    ∃! μ, TauCeti.RepresentsLaplaceFourier μ F
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bochner's theorem](bochners-theorem.md)
- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](../../part-07/weighted-orthogonal-l2-bases-completeness-hilber/moment-determinacy-exponential-moment-form-the-r.md)
- [TauCeti.hausdorff\_bernstein\_widder](tauceti-hausdorff-bernstein-widder.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.bcr_semigroup_bochner`](https://taucetiproject.org/docs/TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/Existence.html#TauCeti.bcr_semigroup_bochner).

## Sources

- [Tau Ceti documentation: `TauCeti.bcr_semigroup_bochner`](https://taucetiproject.org/docs/TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/Existence.html#TauCeti.bcr_semigroup_bochner)
- [Source of `TauCeti.bcr_semigroup_bochner` in TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/Existence.lean#L95)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OneParameterSemigroups/STATUS.md)
