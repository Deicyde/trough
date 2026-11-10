---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.memSobolev_temperedVacuumOperator_iff
statement: formalized
proof: formalized
---

# The vacuum operator restricts to a bijection `H^s → H^{s-1}`

a tempered field `x` lies in
`H^s` if and only if `L₀ x` lies in `H^{s-1}`. Since `L₀` is bijective on tempered fields
(`temperedVacuumOperatorEquiv`), it restricts to a bijection from `H^s` onto `H^{s-1}`, for every
real `s`.

```lean
TauCeti.Vortex.memSobolev_temperedVacuumOperator_iff {x : Fin 4 → TemperedDistribution ℂ ℂ}
  {s : ℝ} :
  (∀ (i : Fin 4),
      TemperedDistribution.MemSobolev (s - 1) 2 (TauCeti.Vortex.temperedVacuumOperator x i)) ↔
    ∀ (i : Fin 4), TemperedDistribution.MemSobolev s 2 (x i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TemperedDistribution.laplacianResolvent](tempereddistribution-laplacianresolvent.md)
- [The vacuum operator is invertible on tempered fields](the-vacuum-operator-is-invertible-on-tempered-fi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.memSobolev_temperedVacuumOperator_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.html#TauCeti.Vortex.memSobolev_temperedVacuumOperator_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.memSobolev_temperedVacuumOperator_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.html#TauCeti.Vortex.memSobolev_temperedVacuumOperator_iff)
- [Source of `TauCeti.Vortex.memSobolev_temperedVacuumOperator_iff` in TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Vortex/VacuumOperator/Sobolev.lean#L344)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
