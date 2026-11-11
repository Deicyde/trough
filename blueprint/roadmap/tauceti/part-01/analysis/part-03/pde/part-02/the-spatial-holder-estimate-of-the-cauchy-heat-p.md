---
declaration: theorem
origin: cited
lean: HolderWith.heatCauchyPotential
statement: formalized
proof: formalized
---

# The spatial Hölder estimate of the Cauchy heat potential

If `g` is continuous and
`α`-Hölder with constant `H`, then so is every time slice of its Cauchy potential, with the same
constant.

```lean
HolderWith.heatCauchyPotential.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {g : E → F} {H α : NNReal} (hg : HolderWith H α g)
  (hgc : Continuous g) (t : ℝ) : HolderWith H α (TauCeti.heatCauchyPotential g t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HolderWith.heatCauchyPotential`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.html#HolderWith.heatCauchyPotential).

## Sources

- [Tau Ceti documentation: `HolderWith.heatCauchyPotential`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.html#HolderWith.heatCauchyPotential)
- [Source of `HolderWith.heatCauchyPotential` in TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/HeatKernel/CauchyPotential.lean#L267)
