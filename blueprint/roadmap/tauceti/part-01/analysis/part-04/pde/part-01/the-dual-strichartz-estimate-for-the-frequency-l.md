---
declaration: theorem
origin: cited
lean: ContDiffBump.exists_enorm_integral_halfWavePropagator_neg_littlewoodPaley_le, TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le, TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le_of_finrank_eq_one
statement: formalized
proof: formalized
---

# The dual Strichartz estimate for the frequency-localized wave equation

Let `E` have
dimension `n`, let `ψⱼ` be the Littlewood–Paley cutoffs built from `φ`, and let `Pⱼ` be the `L²`
Fourier multiplier with symbol `ψⱼ`. Let `(q, r)` be sharp wave-admissible,
`2 / q + (n - 1) / r = (n - 1) / 2`, with `2 < q < ∞`, let `p` and `r'` be the Hölder conjugates
of `q` and `r`, and let `γ = n / 2 - n / r - 1 / q`. There is `C` such that for every `j ∈ ℤ` and
every almost everywhere strongly measurable `F : ℝ → L²(E)` for which `s ↦ W₊(-s) Pⱼ F(s)` is
integrable,

`‖∫ W₊(-s) Pⱼ F(s) ds‖₂ ≤ C 2^{jγ} ‖F‖_{L^p_t L^{r'}_x}`.

```lean
ContDiffBump.exists_enorm_integral_halfWavePropagator_neg_littlewoodPaley_le.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] (φ : ContDiffBump 0) {p q : NNReal} {r r' : ENNReal} [r'.HolderConjugate r]
  (hq : 2 < q) (hpq : p.HolderConjugate q)
  (hqr : 2 / ↑q + (↑(Module.finrank ℝ E) - 1) * r⁻¹.toReal = (↑(Module.finrank ℝ E) - 1) / 2) :
  ∃ C,
    ∀ (j : ℤ) (m : ↥(MeasureTheory.Lp ℂ ⊤ MeasureTheory.volume)),
      (↑↑m =ᵐ[MeasureTheory.volume] fun ξ => ↑(φ.littlewoodPaley j ξ)) →
        ∀ (F : ℝ → ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume)),
          MeasureTheory.AEStronglyMeasurable F MeasureTheory.volume →
            MeasureTheory.Integrable
                (fun s =>
                  (TauCeti.halfWavePropagator ℂ (-s))
                    ((MeasureTheory.Lp.fourierMultiplierCLM ℂ m) (F s)))
                MeasureTheory.volume →
              ‖∫ (s : ℝ),
                    (TauCeti.halfWavePropagator ℂ (-s))
                      ((MeasureTheory.Lp.fourierMultiplierCLM ℂ m) (F s))‖ₑ ≤
                ↑C *
                    ENNReal.ofReal
                      ((2 ^ j) ^
                        (↑(Module.finrank ℝ E) / 2 - ↑(Module.finrank ℝ E) * r⁻¹.toReal - (↑q)⁻¹)) *
                  MeasureTheory.eLpNorm
                    (fun s => MeasureTheory.eLpNorm (↑↑(F s)) r' MeasureTheory.volume) (↑p)
                    MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hardy–Littlewood–Sobolev inequality](../../../../measure-theory/integral/part-01/the-hardy-littlewood-sobolev-inequality.md)
- [Hölder's inequality for disjoint pieces](../../../../measure-theory/function/part-01/holders-inequality-for-disjoint-pieces.md)
- [Plancherel bound for Fourier multipliers](../../../part-03/fourier/part-01/plancherel-bound-for-fourier-multipliers.md)
- [The Riesz–Thorin interpolation theorem](../../../../measure-theory/integral/part-02/the-riesz-thorin-interpolation-theorem.md)
- [Young's inequality `L¹ ⋆ L² ⊆ L²`](../../../part-03/convolution/youngs-inequality-l1-l2-l2.md)

## Lean

Formalized in Tau Ceti as [`ContDiffBump.exists_enorm_integral_halfWavePropagator_neg_littlewoodPaley_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Wave/Strichartz.html#ContDiffBump.exists_enorm_integral_halfWavePropagator_neg_littlewoodPaley_le).

## Other forms

**The dual Strichartz estimate for the Schrödinger equation in every dimension `n`, at a non-endpoint admissible pair.** Formalized in Tau Ceti as [`TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le).

```lean
TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {p q : NNReal} {r r' : ENNReal} [r'.HolderConjugate r] (hq : 2 < q)
  (hpq : p.HolderConjugate q)
  (hqr : 2 / ↑q + ↑(Module.finrank ℝ E) * r⁻¹.toReal = ↑(Module.finrank ℝ E) / 2) :
  ∃ C,
    ∀ (F : ℝ → ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume)),
      MeasureTheory.AEStronglyMeasurable F MeasureTheory.volume →
        MeasureTheory.Integrable (fun s => (TauCeti.schrodingerPropagator ℂ (-s)) (F s))
            MeasureTheory.volume →
          ‖∫ (s : ℝ), (TauCeti.schrodingerPropagator ℂ (-s)) (F s)‖ₑ ≤
            ↑C *
              MeasureTheory.eLpNorm
                (fun s => MeasureTheory.eLpNorm (↑↑(F s)) r' MeasureTheory.volume) (↑p)
                MeasureTheory.volume
```

**The dual Strichartz estimate for the Schrödinger equation on the line, at the admissible pair `(4, ∞)`.** Formalized in Tau Ceti as [`TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le_of_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le_of_finrank_eq_one).

```lean
TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le_of_finrank_eq_one.{u_1, u_2}
  {E : Type u_1} {V : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup V]
  [InnerProductSpace ℂ V] [CompleteSpace V] (hE : Module.finrank ℝ E = 1) :
  ∃ C,
    ∀ (F : ℝ → ↥(MeasureTheory.Lp V 2 MeasureTheory.volume)),
      MeasureTheory.AEStronglyMeasurable F MeasureTheory.volume →
        MeasureTheory.Integrable (fun s => (TauCeti.schrodingerPropagator V (-s)) (F s))
            MeasureTheory.volume →
          ‖∫ (s : ℝ), (TauCeti.schrodingerPropagator V (-s)) (F s)‖ₑ ≤
            ↑C *
              MeasureTheory.eLpNorm
                (fun s => MeasureTheory.eLpNorm (↑↑(F s)) 1 MeasureTheory.volume) (↑(4 / 3))
                MeasureTheory.volume
```

## Sources

- [Tau Ceti documentation: `ContDiffBump.exists_enorm_integral_halfWavePropagator_neg_littlewoodPaley_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Wave/Strichartz.html#ContDiffBump.exists_enorm_integral_halfWavePropagator_neg_littlewoodPaley_le)
- [Source of `ContDiffBump.exists_enorm_integral_halfWavePropagator_neg_littlewoodPaley_le` in TauCeti/Analysis/PDE/Wave/Strichartz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Wave/Strichartz.lean#L371)
