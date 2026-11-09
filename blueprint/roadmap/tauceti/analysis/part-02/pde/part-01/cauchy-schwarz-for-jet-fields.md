---
declaration: theorem
origin: cited
lean: TauCeti.PDE.integral_norm_jetField_mul_le
statement: formalized
proof: formalized
---

# Cauchy--Schwarz for jet fields

The integral of the product of the jet norms of two
Sobolev functions is at most the product of their `W^{1,2}` norms. This is the estimate that
turns the pointwise operator-norm bound on the energy integrand into boundedness of the energy
form.

```lean
TauCeti.PDE.integral_norm_jetField_mul_le.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  (u v : ↥(TauCeti.W1p mu Omega 2)) :
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
      ‖TauCeti.PDE.jetField u x‖ * ‖TauCeti.PDE.jetField v x‖ ∂mu ≤
    ‖u‖ * ‖v‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.integral_norm_jetField_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.integral_norm_jetField_mul_le).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.integral_norm_jetField_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.integral_norm_jetField_mul_le)
- [Source of `TauCeti.PDE.integral_norm_jetField_mul_le` in TauCeti/Analysis/PDE/EnergyForm/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/EnergyForm/Sobolev.lean#L381)
