---
declaration: theorem
origin: cited
lean: TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le
statement: formalized
proof: formalized
---

# The Strichartz estimate for the Schrödinger equation on the line, at the admissible pair `(4, ∞)`, in weak form

There is `C` such that for every `f ∈ L²(E, V)` on a one-dimensional space
`E` and every almost everywhere strongly measurable `G : ℝ → L²(E, V)` for which
`t ↦ S(-t) G(t)` is integrable,

`|∫ ⟪S(t) f, G(t)⟫ dt| ≤ C ‖f‖₂ ‖G‖_{L^{4/3}_t L¹_x}`.

This is `‖S(t) f‖_{L⁴_t L^∞_x} ≤ C ‖f‖₂` tested against `G`.

```lean
TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le.{u_1, u_2} {E : Type u_1}
  {V : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup V] [InnerProductSpace ℂ V]
  [CompleteSpace V] (hE : Module.finrank ℝ E = 1) :
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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hardy–Littlewood–Sobolev inequality](../../../../measure-theory/integral/part-01/the-hardy-littlewood-sobolev-inequality.md)
- [Hölder's inequality for the integral of a product](../../../../measure-theory/function/part-01/holders-inequality-for-the-integral-of-a-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le)
- [Source of `TauCeti.exists_enorm_integral_inner_schrodingerPropagator_le` in TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean#L98)
