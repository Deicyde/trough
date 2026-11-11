---
declaration: theorem
origin: cited
lean: TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn, TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq
statement: formalized
proof: formalized
---

# Weyl's lemma for continuous functions

A function continuous on the open set `Ω` is
harmonic on `Ω` if and only if it is weakly harmonic there: `∫ Δφ • u ∂μ = 0` for every test
function `φ ∈ 𝓓(Ω)`.

```lean
TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] {μ : MeasureTheory.Measure E}
  {Ω : TopologicalSpace.Opens E} {F : Type u_2} [NormedAddCommGroup F] [NormedSpace ℝ F] {w : E → F}
  [BorelSpace E] [μ.IsAddHaarMeasure] [FiniteDimensional ℝ F] (hu : ContinuousOn w ↑Ω) :
  InnerProductSpace.HarmonicOnNhd w ↑Ω ↔ TauCeti.WeaklyHarmonicOn μ Ω w
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../../part-02/distribution/the-du-bois-reymond-lemma.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Weyl.html#TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn).

## Other forms

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

- [Tau Ceti documentation: `TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Weyl.html#TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn)
- [Source of `TauCeti.harmonicOnNhd_iff_weaklyHarmonicOn` in TauCeti/Analysis/InnerProductSpace/Harmonic/Weyl.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Harmonic/Weyl.lean#L442)
