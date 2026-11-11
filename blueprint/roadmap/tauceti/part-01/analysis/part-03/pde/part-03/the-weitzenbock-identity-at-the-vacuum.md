---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.vacuumAdjoint_vacuumOperator, TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator
statement: formalized
proof: formalized
---

# The Weitzenböck identity at the vacuum

`L₀* L₀ = -Δ + 1 / 4`.

```lean
TauCeti.Vortex.vacuumAdjoint_vacuumOperator (x : SchwartzMap ℂ (EuclideanSpace ℝ (Fin 4))) :
  TauCeti.Vortex.vacuumAdjoint (TauCeti.Vortex.vacuumOperator x) =
    -Laplacian.laplacian x + (1 / 4) • x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.vacuumAdjoint_vacuumOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Basic.html#TauCeti.Vortex.vacuumAdjoint_vacuumOperator).

## Other forms

**The Weitzenböck identity at the vacuum on tempered fields.** Formalized in Tau Ceti as [`TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.html#TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator).

```lean
TauCeti.Vortex.temperedVacuumAdjoint_temperedVacuumOperator (x : Fin 4 → TemperedDistribution ℂ ℂ) :
  TauCeti.Vortex.temperedVacuumAdjoint (TauCeti.Vortex.temperedVacuumOperator x) = fun i =>
    -Laplacian.laplacian (x i) + (1 / 4) • x i
```

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.vacuumAdjoint_vacuumOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Basic.html#TauCeti.Vortex.vacuumAdjoint_vacuumOperator)
- [Source of `TauCeti.Vortex.vacuumAdjoint_vacuumOperator` in TauCeti/Analysis/PDE/Vortex/VacuumOperator/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Basic.lean#L214)
