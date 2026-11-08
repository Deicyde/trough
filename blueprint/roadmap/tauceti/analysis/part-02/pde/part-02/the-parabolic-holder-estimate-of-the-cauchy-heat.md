---
declaration: theorem
origin: cited
lean: TauCeti.holderWith_heatCauchyPotential
statement: formalized
proof: formalized
---

# The parabolic Hölder estimate of the Cauchy heat potential

If `g` is continuous and
`α`-Hölder with constant `H`, its Cauchy potential is `α`-Hölder on parabolic space-time, whose
distance is `‖x - x'‖ + √|t - s|`, with constant `H (1 + M_α)`. Here
`M_α = ∫ ‖y‖^α K_1(y) dy` is `TauCeti.heatKernelMoment`, which depends only on `α` and the
dimension. Continuity is automatic when `α > 0` (`HolderWith.continuous`).

```lean
TauCeti.holderWith_heatCauchyPotential.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {g : E → F} {H α : NNReal}
  (hg : HolderWith H α g) (hgc : Continuous g) :
  HolderWith (H * (1 + TauCeti.heatKernelMoment E α)) α fun p =>
    TauCeti.heatCauchyPotential g p.time p.space
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.holderWith_heatCauchyPotential`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.html#TauCeti.holderWith_heatCauchyPotential).

## Sources

- [Tau Ceti documentation: `TauCeti.holderWith_heatCauchyPotential`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.html#TauCeti.holderWith_heatCauchyPotential)
- [Source of `TauCeti.holderWith_heatCauchyPotential` in TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.lean#L220)
