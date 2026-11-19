---
declaration: theorem
origin: cited
lean: TauCeti.representsLaplaceFourier_iff_forall_spatialSlice_eq
statement: formalized
proof: formalized
---

# The slice criterion for the Berg--Christensen--Ressel representation

A measure
on `ℝ≥0 × V` represents `F` by its Laplace--Fourier transform if and only if each of its spatial
slices is the Bochner measure of the corresponding continuous positive-definite time slice of
`F`. The existence half of the representation theorem is exactly the problem of producing a
measure with these prescribed slices.

```lean
TauCeti.representsLaplaceFourier_iff_forall_spatialSlice_eq.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] {μ : MeasureTheory.Measure (NNReal × V)} {F : NNReal × V → ℂ}
  (hFpd : ∀ (t : NNReal), TauCeti.IsPositiveDefiniteSub fun a => F (t, a))
  (hFcont : ∀ (t : NNReal), Continuous fun a => F (t, a)) :
  TauCeti.RepresentsLaplaceFourier μ F ↔
    ∀ (t : NNReal), TauCeti.spatialSlice μ t = TauCeti.bochnerMeasure fun a => F (t, a)
```

## Depends on

- [The representing measure of Bochner's theorem](the-representing-measure-of-bochners-theorem.md)

## Proof depends on

- [Bochner's theorem](bochners-theorem.md)
- [Converse half of Bochner's theorem](converse-half-of-bochners-theorem.md)
- [Uniqueness half of Bochner's theorem](../../part-03/bochner/uniqueness-half-of-bochners-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.representsLaplaceFourier_iff_forall_spatialSlice_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/Slice.html#TauCeti.representsLaplaceFourier_iff_forall_spatialSlice_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.representsLaplaceFourier_iff_forall_spatialSlice_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/Slice.html#TauCeti.representsLaplaceFourier_iff_forall_spatialSlice_eq)
- [Source of `TauCeti.representsLaplaceFourier_iff_forall_spatialSlice_eq` in TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/Slice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/Slice.lean#L342)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OneParameterSemigroups/STATUS.md)
