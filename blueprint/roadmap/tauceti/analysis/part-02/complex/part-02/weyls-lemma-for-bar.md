---
declaration: theorem
origin: cited
lean: TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq, TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn, TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq
statement: formalized
proof: formalized
---

# Weyl's lemma for `\bar∂`

A distributional solution with finite-dimensional complex
coefficients agrees almost everywhere on its domain with a holomorphic function.

```lean
TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℂ F] {μ : MeasureTheory.Measure ℂ}
  {Ω : TopologicalSpace.Opens ℂ} {u : ℂ → F} [FiniteDimensional ℂ F] [μ.IsAddHaarMeasure]
  (h : TauCeti.HasWeakConjWirtingerDerivOn μ Ω u 0) :
  ∃ v, DifferentiableOn ℂ v ↑Ω ∧ u =ᵐ[μ.restrict ↑Ω] v
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../../part-01/integral-currents-geometric-homology-and-minimiz/the-du-bois-reymond-lemma.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Weyl.html#TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq).

## Other forms

**Weyl's lemma for continuous functions.** Formalized in Tau Ceti as [`TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Weyl.html#TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn).

```lean
TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] {μ : MeasureTheory.Measure E}
  {Ω : TopologicalSpace.Opens E} {F : Type u_2} [NormedAddCommGroup F] [NormedSpace ℝ F] {w : E → F}
  [BorelSpace E] [μ.IsAddHaarMeasure] [FiniteDimensional ℝ F] (hu : ContinuousOn w ↑Ω) :
  InnerProductSpace.HarmonicOnNhd w ↑Ω ↔ TauCeti.WeaklyHarmonicOn μ Ω w
```

**Weyl's lemma with finite-dimensional coefficients.** Formalized in Tau Ceti as [`TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Weyl.html#TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq).

```lean
TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] {μ : MeasureTheory.Measure E}
  {Ω : TopologicalSpace.Opens E} {F : Type u_2} [NormedAddCommGroup F] [NormedSpace ℝ F] {w : E → F}
  [BorelSpace E] [μ.IsAddHaarMeasure] [FiniteDimensional ℝ F]
  (hw : TauCeti.WeaklyHarmonicOn μ Ω w) :
  ∃ v, InnerProductSpace.HarmonicOnNhd v ↑Ω ∧ w =ᵐ[μ.restrict ↑Ω] v
```

## Sources

- [Tau Ceti documentation: `TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Weyl.html#TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq)
- [Source of `TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq` in TauCeti/Analysis/Complex/Wirtinger/Weyl.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Wirtinger/Weyl.lean#L99)
