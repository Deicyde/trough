---
declaration: theorem
origin: cited
lean: TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le, ContDiffBump.exists_enorm_integral_setIntegral_Iio_inner_halfWavePropagator_sub_littlewoodPaley_le
statement: formalized
proof: formalized
---

# The retarded Strichartz estimate for the Schrödinger equation

**The retarded Strichartz estimate for the Schrödinger equation** in every dimension `n`, in
weak form, at a non-endpoint admissible pair: `2 < q < ∞` and `2 / q + n / r = n / 2`, with `p`
and `r'` the Hölder conjugates of `q` and `r`. There is `C` such that for all almost everywhere
strongly measurable `F, G : ℝ → L²(E)`,

`|∫ ∫_{s < t} ⟪S(t - s) F(s), G(t)⟫ ds dt| ≤ C ‖F‖_{L^p_t L^{r'}_x} ‖G‖_{L^p_t L^{r'}_x}`.

This is the Duhamel estimate `‖∫_{s < t} S(t - s) F(s) ds‖_{L^q_t L^r_x} ≤ C ‖F‖_{L^p_t L^{r'}_x}`
tested against `G`; for `F` vanishing on negative times the inner integral runs over `(0, t)`.

```lean
TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {p q : NNReal} {r r' : ENNReal} [r'.HolderConjugate r]
  (hq : 2 < q) (hpq : p.HolderConjugate q)
  (hqr : 2 / ↑q + ↑(Module.finrank ℝ E) * r⁻¹.toReal = ↑(Module.finrank ℝ E) / 2) :
  ∃ C,
    ∀ (F G : ℝ → ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume)),
      MeasureTheory.AEStronglyMeasurable F MeasureTheory.volume →
        MeasureTheory.AEStronglyMeasurable G MeasureTheory.volume →
          ‖∫ (t : ℝ),
                ∫ (s : ℝ) in Set.Iio t,
                  inner ℂ ((TauCeti.schrodingerPropagator ℂ (t - s)) (F s)) (G t)‖ₑ ≤
            ↑C *
                MeasureTheory.eLpNorm
                  (fun s => MeasureTheory.eLpNorm (↑↑(F s)) r' MeasureTheory.volume) (↑p)
                  MeasureTheory.volume *
              MeasureTheory.eLpNorm
                (fun t => MeasureTheory.eLpNorm (↑↑(G t)) r' MeasureTheory.volume) (↑p)
                MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The bilinear Strichartz estimate for the frequency-localized wave equation](../part-01/the-bilinear-strichartz-estimate-for-the-frequen.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le).

## Other forms

**The retarded Strichartz estimate for the frequency-localized wave equation, in weak form.** Formalized in Tau Ceti as [`ContDiffBump.exists_enorm_integral_setIntegral_Iio_inner_halfWavePropagator_sub_littlewoodPaley_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Wave/Strichartz.html#ContDiffBump.exists_enorm_integral_setIntegral_Iio_inner_halfWavePropagator_sub_littlewoodPaley_le).

```lean
ContDiffBump.exists_enorm_integral_setIntegral_Iio_inner_halfWavePropagator_sub_littlewoodPaley_le.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] (φ : ContDiffBump 0) {p q : NNReal} {r r' : ENNReal}
  [r'.HolderConjugate r] (hq : 2 < q) (hpq : p.HolderConjugate q)
  (hqr : 2 / ↑q + (↑(Module.finrank ℝ E) - 1) * r⁻¹.toReal = (↑(Module.finrank ℝ E) - 1) / 2) :
  ∃ C,
    ∀ (j : ℤ) (m : ↥(MeasureTheory.Lp ℂ ⊤ MeasureTheory.volume)),
      (↑↑m =ᵐ[MeasureTheory.volume] fun ξ => ↑(φ.littlewoodPaley j ξ)) →
        ∀ (F G : ℝ → ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume)),
          MeasureTheory.AEStronglyMeasurable F MeasureTheory.volume →
            MeasureTheory.AEStronglyMeasurable G MeasureTheory.volume →
              ‖∫ (t : ℝ),
                    ∫ (s : ℝ) in Set.Iio t,
                      inner ℂ
                        ((TauCeti.halfWavePropagator ℂ (t - s))
                          ((MeasureTheory.Lp.fourierMultiplierCLM ℂ m)
                            ((MeasureTheory.Lp.fourierMultiplierCLM ℂ m) (F s))))
                        (G t)‖ₑ ≤
                ↑C *
                      ENNReal.ofReal
                        ((2 ^ j) ^
                          (2 *
                            (↑(Module.finrank ℝ E) / 2 - ↑(Module.finrank ℝ E) * r⁻¹.toReal -
                              (↑q)⁻¹))) *
                    MeasureTheory.eLpNorm
                      (fun s => MeasureTheory.eLpNorm (↑↑(F s)) r' MeasureTheory.volume) (↑p)
                      MeasureTheory.volume *
                  MeasureTheory.eLpNorm
                    (fun t => MeasureTheory.eLpNorm (↑↑(G t)) r' MeasureTheory.volume) (↑p)
                    MeasureTheory.volume
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le)
- [Source of `TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le` in TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean#L233)
