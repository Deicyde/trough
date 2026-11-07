---
declaration: def
origin: cited
lean: TauCeti.Vortex.temperedVacuumOperatorEquiv
statement: formalized
---

# The vacuum operator is invertible on tempered fields

`L₀` as a continuous linear
automorphism of the fields of tempered distributions. Its inverse is `L₀⁻¹ = L₀* (-Δ + 1 / 4)⁻¹`
(`temperedVacuumOperatorEquiv_symm_apply`).

```lean
TauCeti.Vortex.temperedVacuumOperatorEquiv :
  (Fin 4 → TemperedDistribution ℂ ℂ) ≃L[ℂ] Fin 4 → TemperedDistribution ℂ ℂ
```

## Depends on

- [TemperedDistribution.laplacianResolvent](tempereddistribution-laplacianresolvent.md)

## Proof depends on

- [TauCeti.Vortex.temperedVacuumAdjoint\_temperedVacuumOperator](tauceti-vortex-temperedvacuumadjoint-temperedvac.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.temperedVacuumOperatorEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.html#TauCeti.Vortex.temperedVacuumOperatorEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.temperedVacuumOperatorEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.html#TauCeti.Vortex.temperedVacuumOperatorEquiv)
- [Source of `TauCeti.Vortex.temperedVacuumOperatorEquiv` in TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.lean#L241)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
