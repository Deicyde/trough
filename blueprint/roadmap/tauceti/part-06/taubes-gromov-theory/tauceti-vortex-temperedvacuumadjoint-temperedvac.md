---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator
statement: formalized
proof: formalized
---

# TauCeti.Vortex.temperedVacuumAdjoint\_temperedVacuumOperator

**The Weitzenböck identity at the vacuum** on tempered fields: `L₀* L₀ = -Δ + 1 / 4`.

```lean
TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator (x : Fin 4 → TemperedDistribution ℂ ℂ) :
  TauCeti.Vortex.temperedVacuumAdjoint (TauCeti.Vortex.temperedVacuumOperator x) = fun i =>
    -Laplacian.laplacian (x i) + (1 / 4) • x i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.html#TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.html#TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator)
- [Source of `TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator` in TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.lean#L193)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
