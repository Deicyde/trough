---
declaration: theorem
origin: cited
lean: TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le_of_integrable
statement: formalized
proof: formalized
---

# The inhomogeneous Strichartz estimate for the Schrödinger equation

**The inhomogeneous Strichartz estimate for the Schrödinger equation** in every dimension `n`,
in weak form, for two non-endpoint admissible pairs: `2 < q, q₁ < ∞` with `2 / q + n / r = n / 2`
and `2 / q₁ + n / r₁ = n / 2`, where `p`, `p₁`, `r'` and `r₁'` are the Hölder conjugates of `q`,
`q₁`, `r` and `r₁`. There is `C` such that for all almost everywhere strongly measurable
`F, G : ℝ → L²(E)` for which `s ↦ S(-s) F(s)` and `t ↦ S(-t) G(t)` are integrable,

`|∫ ∫_{s < t} ⟪S(t - s) F(s), G(t)⟫ ds dt| ≤ C ‖F‖_{L^{p₁}_t L^{r₁'}_x} ‖G‖_{L^p_t L^{r'}_x}`.

This is the Duhamel estimate
`‖∫_{s < t} S(t - s) F(s) ds‖_{L^q_t L^r_x} ≤ C ‖F‖_{L^{p₁}_t L^{r₁'}_x}` tested against `G`; for
`F` vanishing on negative times the inner integral runs over `(0, t)`. The integrability
hypotheses are qualitative: `C` does not depend on them. For a single pair,
`TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le` gives the
bound without them.

```lean
TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le_of_integrable.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {p q p₁ q₁ : NNReal} {r r' r₁ r₁' : ENNReal}
  [r'.HolderConjugate r] [r₁'.HolderConjugate r₁] (hq : 2 < q) (hpq : p.HolderConjugate q)
  (hqr : 2 / ↑q + ↑(Module.finrank ℝ E) * r⁻¹.toReal = ↑(Module.finrank ℝ E) / 2) (hq₁ : 2 < q₁)
  (hpq₁ : p₁.HolderConjugate q₁)
  (hqr₁ : 2 / ↑q₁ + ↑(Module.finrank ℝ E) * r₁⁻¹.toReal = ↑(Module.finrank ℝ E) / 2) :
  ∃ C,
    ∀ (F G : ℝ → ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume)),
      MeasureTheory.AEStronglyMeasurable F MeasureTheory.volume →
        MeasureTheory.AEStronglyMeasurable G MeasureTheory.volume →
          MeasureTheory.Integrable (fun s => (TauCeti.schrodingerPropagator ℂ (-s)) (F s))
              MeasureTheory.volume →
            MeasureTheory.Integrable (fun t => (TauCeti.schrodingerPropagator ℂ (-t)) (G t))
                MeasureTheory.volume →
              ‖∫ (t : ℝ),
                    ∫ (s : ℝ) in Set.Iio t,
                      inner ℂ ((TauCeti.schrodingerPropagator ℂ (t - s)) (F s)) (G t)‖ₑ ≤
                ↑C *
                    MeasureTheory.eLpNorm
                      (fun s => MeasureTheory.eLpNorm (↑↑(F s)) r₁' MeasureTheory.volume) (↑p₁)
                      MeasureTheory.volume *
                  MeasureTheory.eLpNorm
                    (fun t => MeasureTheory.eLpNorm (↑↑(G t)) r' MeasureTheory.volume) (↑p)
                    MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Christ–Kiselev lemma, in bilinear form](../../../../measure-theory/integral/part-01/the-christ-kiselev-lemma-in-bilinear-form.md)
- [The dual Strichartz estimate for the frequency-localized wave equation](../part-01/the-dual-strichartz-estimate-for-the-frequency-l.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le_of_integrable`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le_of_integrable).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le_of_integrable`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le_of_integrable)
- [Source of `TauCeti.exists_enorm_integral_setIntegral_Iio_inner_schrodingerPropagator_sub_le_of_integrable` in TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean#L309)
