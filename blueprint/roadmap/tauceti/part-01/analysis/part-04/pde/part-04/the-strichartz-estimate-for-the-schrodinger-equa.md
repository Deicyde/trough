---
declaration: theorem
origin: cited
lean: TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le, ContDiffBump.exists_enorm_integral_inner_halfWavePropagator_littlewoodPaley_le, TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le_of_finrank_eq_one
statement: formalized
proof: formalized
---

# The Strichartz estimate for the Schrödinger equation

**The Strichartz estimate for the Schrödinger equation** in every dimension `n`, in weak
form, at a non-endpoint admissible pair: `2 < q < ∞` and `2 / q + n / r = n / 2`, with `p` and
`r'` the Hölder conjugates of `q` and `r`. There is `C` such that for every `f ∈ L²(E)` and every
almost everywhere strongly measurable `G : ℝ → L²(E)` for which `t ↦ S(-t) G(t)` is integrable,

`|∫ ⟪S(t) f, G(t)⟫ dt| ≤ C ‖f‖₂ ‖G‖_{L^p_t L^{r'}_x}`.

This is `‖S(t) f‖_{L^q_t L^r_x} ≤ C ‖f‖₂` tested against `G`.

```lean
TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {p q : NNReal} {r r' : ENNReal} [r'.HolderConjugate r] (hq : 2 < q)
  (hpq : p.HolderConjugate q)
  (hqr : 2 / ↑q + ↑(Module.finrank ℝ E) * r⁻¹.toReal = ↑(Module.finrank ℝ E) / 2) :
  ∃ C,
    ∀ (f : ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume))
      (G : ℝ → ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume)),
      MeasureTheory.AEStronglyMeasurable G MeasureTheory.volume →
        MeasureTheory.Integrable (fun t => (TauCeti.schrodingerPropagator ℂ (-t)) (G t))
            MeasureTheory.volume →
          ‖∫ (t : ℝ), inner ℂ ((TauCeti.schrodingerPropagator ℂ t) f) (G t)‖ₑ ≤
            ↑C * ‖f‖ₑ *
              MeasureTheory.eLpNorm
                (fun t => MeasureTheory.eLpNorm (↑↑(G t)) r' MeasureTheory.volume) (↑p)
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

Formalized in Tau Ceti as [`TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le).

## Other forms

**The Strichartz estimate for the frequency-localized wave equation, in weak form.** Formalized in Tau Ceti as [`ContDiffBump.exists_enorm_integral_inner_halfWavePropagator_littlewoodPaley_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Wave/Strichartz.html#ContDiffBump.exists_enorm_integral_inner_halfWavePropagator_littlewoodPaley_le).

```lean
ContDiffBump.exists_enorm_integral_inner_halfWavePropagator_littlewoodPaley_le.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] (φ : ContDiffBump 0) {p q : NNReal} {r r' : ENNReal} [r'.HolderConjugate r]
  (hq : 2 < q) (hpq : p.HolderConjugate q)
  (hqr : 2 / ↑q + (↑(Module.finrank ℝ E) - 1) * r⁻¹.toReal = (↑(Module.finrank ℝ E) - 1) / 2) :
  ∃ C,
    ∀ (j : ℤ) (m : ↥(MeasureTheory.Lp ℂ ⊤ MeasureTheory.volume)),
      (↑↑m =ᵐ[MeasureTheory.volume] fun ξ => ↑(φ.littlewoodPaley j ξ)) →
        ∀ (f : ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume))
          (G : ℝ → ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume)),
          MeasureTheory.AEStronglyMeasurable G MeasureTheory.volume →
            MeasureTheory.Integrable
                (fun t =>
                  (TauCeti.halfWavePropagator ℂ (-t))
                    ((MeasureTheory.Lp.fourierMultiplierCLM ℂ m) (G t)))
                MeasureTheory.volume →
              ‖∫ (t : ℝ),
                    inner ℂ
                      ((TauCeti.halfWavePropagator ℂ t)
                        ((MeasureTheory.Lp.fourierMultiplierCLM ℂ m) f))
                      (G t)‖ₑ ≤
                ↑C *
                      ENNReal.ofReal
                        ((2 ^ j) ^
                          (↑(Module.finrank ℝ E) / 2 - ↑(Module.finrank ℝ E) * r⁻¹.toReal -
                            (↑q)⁻¹)) *
                    ‖f‖ₑ *
                  MeasureTheory.eLpNorm
                    (fun t => MeasureTheory.eLpNorm (↑↑(G t)) r' MeasureTheory.volume) (↑p)
                    MeasureTheory.volume
```

**The Strichartz estimate for the Schrödinger equation on the line, at the admissible pair `(4, ∞)`, in weak form.** Formalized in Tau Ceti as [`TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le_of_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le_of_finrank_eq_one).

```lean
TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le_of_finrank_eq_one.{u_1, u_2}
  {E : Type u_1} {V : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup V]
  [InnerProductSpace ℂ V] [CompleteSpace V] (hE : Module.finrank ℝ E = 1) :
  ∃ C,
    ∀ (f : ↥(MeasureTheory.Lp V 2 MeasureTheory.volume))
      (G : ℝ → ↥(MeasureTheory.Lp V 2 MeasureTheory.volume)),
      MeasureTheory.AEStronglyMeasurable G MeasureTheory.volume →
        MeasureTheory.Integrable (fun t => (TauCeti.schrodingerPropagator V (-t)) (G t))
            MeasureTheory.volume →
          ‖∫ (t : ℝ), inner ℂ ((TauCeti.schrodingerPropagator V t) f) (G t)‖ₑ ≤
            ↑C * ‖f‖ₑ *
              MeasureTheory.eLpNorm
                (fun t => MeasureTheory.eLpNorm (↑↑(G t)) 1 MeasureTheory.volume) (↑(4 / 3))
                MeasureTheory.volume
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le)
- [Source of `TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le` in TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean#L277)
