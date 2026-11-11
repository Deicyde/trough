---
declaration: theorem
origin: cited
lean: TauCeti.exists_holderWith_iteratedFDeriv_two_heatDuhamelPotential
statement: formalized
proof: formalized
---

# The Hölder estimate for the Hessian of the Duhamel potential

For `0 < α < 1` there is a
constant `C`, depending only on `α` and the dimension, such that the Hessian `D² w(t, ·)` is
`α`-Hölder with constant `C H` whenever `f` is jointly measurable and essentially bounded on
`(0, t) × E` and `f(s, ·)` is `α`-Hölder with constant `H` for almost every `0 < s < t`. Neither
the bound on `f` nor the time `t` enters the estimate.

```lean
TauCeti.exists_holderWith_iteratedFDeriv_two_heatDuhamelPotential.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {α : NNReal}
  (hα₀ : 0 < α) (hα₁ : α < 1) :
  ∃ C,
    ∀ {f : ℝ → E → F} {M t : ℝ} {H : NNReal},
      MeasureTheory.StronglyMeasurable (Function.uncurry f) →
        (∀ᵐ (s : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo 0 t), ∀ᵐ (y : E), ‖f s y‖ ≤ M) →
          (∀ᵐ (s : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo 0 t), HolderWith H α (f s)) →
            0 < t → HolderWith (C * H) α (iteratedFDeriv ℝ 2 (TauCeti.heatDuhamelPotential f t))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder bounds on the derivatives of a heat convolution](holder-bounds-on-the-derivatives-of-a-heat-convo.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_holderWith_iteratedFDeriv_two_heatDuhamelPotential`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/Basic.html#TauCeti.exists_holderWith_iteratedFDeriv_two_heatDuhamelPotential).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_holderWith_iteratedFDeriv_two_heatDuhamelPotential`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/Basic.html#TauCeti.exists_holderWith_iteratedFDeriv_two_heatDuhamelPotential)
- [Source of `TauCeti.exists_holderWith_iteratedFDeriv_two_heatDuhamelPotential` in TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/Basic.lean#L562)
