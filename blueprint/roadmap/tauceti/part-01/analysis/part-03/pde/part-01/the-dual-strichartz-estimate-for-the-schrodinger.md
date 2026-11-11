---
declaration: theorem
origin: cited
lean: TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le
statement: formalized
proof: formalized
---

# The dual Strichartz estimate for the Schrödinger equation on the line, at the admissible pair `(4, ∞)`

There is `C` such that for every almost everywhere strongly measurable
`F : ℝ → L²(E, V)` on a one-dimensional space `E` for which `s ↦ S(-s) F(s)` is integrable,

`‖∫ S(-s) F(s) ds‖₂ ≤ C ‖F‖_{L^{4/3}_t L¹_x}`.

```lean
TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le.{u_1, u_2} {E : Type u_1} {V : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup V] [InnerProductSpace ℂ V] [CompleteSpace V]
  (hE : Module.finrank ℝ E = 1) :
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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hardy–Littlewood–Sobolev inequality](../../../../measure-theory/integral/part-01/the-hardy-littlewood-sobolev-inequality.md)
- [Hölder's inequality for the integral of a product](../../../../measure-theory/function/part-01/holders-inequality-for-the-integral-of-a-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Schrodinger/Strichartz.html#TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le)
- [Source of `TauCeti.exists_enorm_integral_schrodingerPropagator_neg_le` in TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Schrodinger/Strichartz.lean#L77)
