---
declaration: theorem
origin: cited
lean: TauCeti.norm_heatCauchyPotential_sub_heatCauchyPotential_le, TauCeti.exists_holderOnWith_iteratedFDeriv_two_heatDuhamelPotential
statement: formalized
proof: formalized
---

# The temporal Hölder estimate of the Cauchy heat potential

If `g` is continuous and
`α`-Hölder with constant `H`, its Cauchy potential `u` satisfies
`‖u(t, x) - u(s, x)‖ ≤ H M_α |t - s|^(α/2)`, where `M_α = ∫ ‖y‖^α K_1(y) dy` is
`TauCeti.heatKernelMoment`.

```lean
TauCeti.norm_heatCauchyPotential_sub_heatCauchyPotential_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {g : E → F} {H α : NNReal}
  (hg : HolderWith H α g) (hgc : Continuous g) (t s : ℝ) (x : E) :
  ‖TauCeti.heatCauchyPotential g t x - TauCeti.heatCauchyPotential g s x‖ ≤
    ↑H * ↑(TauCeti.heatKernelMoment E α) * |t - s| ^ (↑α / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder bounds on the derivatives of a heat convolution](../part-01/holder-bounds-on-the-derivatives-of-a-heat-convo.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_heatCauchyPotential_sub_heatCauchyPotential_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.html#TauCeti.norm_heatCauchyPotential_sub_heatCauchyPotential_le).

## Other forms

**The temporal Hölder estimate for the Hessian of the Duhamel potential.** Formalized in Tau Ceti as [`TauCeti.exists_holderOnWith_iteratedFDeriv_two_heatDuhamelPotential`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/Basic.html#TauCeti.exists_holderOnWith_iteratedFDeriv_two_heatDuhamelPotential).

```lean
TauCeti.exists_holderOnWith_iteratedFDeriv_two_heatDuhamelPotential.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  {α : NNReal} (hα₀ : 0 < α) (hα₂ : α < 2) :
  ∃ C,
    ∀ {f : ℝ → E → F} {M T : ℝ} {H : NNReal},
      MeasureTheory.StronglyMeasurable (Function.uncurry f) →
        (∀ᵐ (s : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo 0 T), ∀ᵐ (y : E), ‖f s y‖ ≤ M) →
          (∀ᵐ (s : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo 0 T), HolderWith H α (f s)) →
            ∀ (x : E),
              HolderOnWith (C * H) (α / 2)
                (fun t => iteratedFDeriv ℝ 2 (TauCeti.heatDuhamelPotential f t) x) (Set.Icc 0 T)
```

## Sources

- [Tau Ceti documentation: `TauCeti.norm_heatCauchyPotential_sub_heatCauchyPotential_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.html#TauCeti.norm_heatCauchyPotential_sub_heatCauchyPotential_le)
- [Source of `TauCeti.norm_heatCauchyPotential_sub_heatCauchyPotential_le` in TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.lean#L277)
