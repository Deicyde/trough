---
declaration: theorem
origin: cited
lean: TauCeti.bochner, TauCeti.bochner_probabilityMeasure, TauCeti.bochner_euclideanSpace, TauCeti.isPositiveDefiniteSub_iff_exists_pontryaginMeasureTransform_eq, TauCeti.IsPositiveDefiniteSub.exists_pontryaginMeasureTransform_eq_of_continuousAt, TauCeti.bochner_charFun_real, TauCeti.bochner_charFun, TauCeti.bochner_posSemidef
statement: formalized
proof: formalized
---

# Bochner's theorem

A function `F` on a finite-dimensional real inner-product space is
continuous and positive definite if and only if it is the Fourier-convention transform
`v ↦ ∫ q, fourierAtom v q ∂μ` of a unique finite Borel measure `μ`. Bochner (1932); Rudin,
*Fourier Analysis on Groups*, Theorem 1.4.3.

```lean
TauCeti.bochner.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (F : V → ℂ) :
  Continuous F ∧ TauCeti.IsPositiveDefiniteSub F ↔
    ∃! μ, MeasureTheory.IsFiniteMeasure μ ∧ ∀ (v : V), F v = ∫ (q : V), TauCeti.fourierAtom v q ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Converse half of Bochner's theorem](converse-half-of-bochners-theorem.md)
- [Existence half of Bochner's theorem](existence-half-of-bochners-theorem.md)
- [Lévy's continuity theorem, including existence](../../../probability/standard-probability-distributions-and-their-ele/levys-continuity-theorem-including-existence.md)
- [The representing measure of Bochner's theorem](the-representing-measure-of-bochners-theorem.md)
- [Spectral theorem for strongly continuous unitary representations, cyclic form](../../part-02/fourier/spectral-theorem-for-strongly-continuous-unitary.md)
- [Uniqueness half of Bochner's theorem](../../part-02/bochner/uniqueness-half-of-bochners-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.bochner`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.bochner).

## Other forms

**Bochner's theorem for normalized functions.** Formalized in Tau Ceti as [`TauCeti.bochner_probabilityMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.bochner_probabilityMeasure).

```lean
TauCeti.bochner_probabilityMeasure.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (F : V → ℂ) :
  Continuous F ∧ TauCeti.IsPositiveDefiniteSub F ∧ F 0 = 1 ↔
    ∃! μ,
      MeasureTheory.IsProbabilityMeasure μ ∧ ∀ (v : V), F v = ∫ (q : V), TauCeti.fourierAtom v q ∂μ
```

**Bochner's theorem on `ℝᵈ`.** Formalized in Tau Ceti as [`TauCeti.bochner_euclideanSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.bochner_euclideanSpace).

```lean
TauCeti.bochner_euclideanSpace (d : ℕ) (F : EuclideanSpace ℝ (Fin d) → ℂ) :
  Continuous F ∧ TauCeti.IsPositiveDefiniteSub F ↔
    ∃! μ,
      MeasureTheory.IsFiniteMeasure μ ∧
        ∀ (v : EuclideanSpace ℝ (Fin d)),
          F v = ∫ (q : EuclideanSpace ℝ (Fin d)), TauCeti.fourierAtom v q ∂μ
```

**Bochner's theorem on a discrete abelian group.** Formalized in Tau Ceti as [`TauCeti.isPositiveDefiniteSub_iff_exists_pontryaginMeasureTransform_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/DiscreteGroup.html#TauCeti.isPositiveDefiniteSub_iff_exists_pontryaginMeasureTransform_eq).

```lean
TauCeti.isPositiveDefiniteSub_iff_exists_pontryaginMeasureTransform_eq.{u_1} {G : Type u_1}
  [AddCommGroup G] [TopologicalSpace G] [DiscreteTopology G]
  [MeasurableSpace (PontryaginDual (Multiplicative G))]
  [BorelSpace (PontryaginDual (Multiplicative G))] (φ : G → ℂ) :
  TauCeti.IsPositiveDefiniteSub φ ↔ ∃ μ, (↑μ).InnerRegular ∧ μ.pontryaginMeasureTransform = φ
```

**Bochner's theorem on a locally compact abelian group, existence half.** Formalized in Tau Ceti as [`TauCeti.IsPositiveDefiniteSub.exists_pontryaginMeasureTransform_eq_of_continuousAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/LocallyCompactGroup.html#TauCeti.IsPositiveDefiniteSub.exists_pontryaginMeasureTransform_eq_of_continuousAt).

```lean
TauCeti.IsPositiveDefiniteSub.exists_pontryaginMeasureTransform_eq_of_continuousAt.{u_1}
  {G : Type u_1} [AddCommGroup G] [TopologicalSpace G] [IsTopologicalAddGroup G]
  [LocallyCompactSpace G] [MeasurableSpace (PontryaginDual (Multiplicative G))]
  [BorelSpace (PontryaginDual (Multiplicative G))] {φ : G → ℂ}
  (hφ : TauCeti.IsPositiveDefiniteSub φ) (hφ₀ : ContinuousAt φ 0) :
  ∃ μ, (↑μ).InnerRegular ∧ μ.pontryaginMeasureTransform = φ
```

**Bochner's theorem on the real line, in its classical form.** Formalized in Tau Ceti as [`TauCeti.bochner_charFun_real`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/CharFun/Bochner.html#TauCeti.bochner_charFun_real).

```lean
TauCeti.bochner_charFun_real (F : ℝ → ℂ) :
  Continuous F ∧ TauCeti.IsPositiveDefiniteSub F ↔
    ∃! μ,
      MeasureTheory.IsFiniteMeasure μ ∧
        ∀ (x : ℝ), F x = ∫ (ξ : ℝ), Complex.exp (↑x * ↑ξ * Complex.I) ∂μ
```

**Bochner's theorem, characteristic-function form.** Formalized in Tau Ceti as [`TauCeti.bochner_charFun`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/CharFun/Bochner.html#TauCeti.bochner_charFun).

```lean
TauCeti.bochner_charFun.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (F : V → ℂ) :
  Continuous F ∧ TauCeti.IsPositiveDefiniteSub F ↔
    ∃! μ, MeasureTheory.IsFiniteMeasure μ ∧ MeasureTheory.charFun μ = F
```

**Bochner's theorem, kernel form.** Formalized in Tau Ceti as [`TauCeti.bochner_posSemidef`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.bochner_posSemidef).

```lean
TauCeti.bochner_posSemidef.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (F : V → ℂ) :
  (Continuous F ∧ Matrix.PosSemidef fun a b => F (a - b)) ↔
    ∃! μ, MeasureTheory.IsFiniteMeasure μ ∧ ∀ (v : V), F v = ∫ (q : V), TauCeti.fourierAtom v q ∂μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.bochner`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.bochner)
- [Source of `TauCeti.bochner` in TauCeti/Analysis/Bochner/BochnerTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Bochner/BochnerTheorem.lean#L240)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OneParameterSemigroups/STATUS.md)
