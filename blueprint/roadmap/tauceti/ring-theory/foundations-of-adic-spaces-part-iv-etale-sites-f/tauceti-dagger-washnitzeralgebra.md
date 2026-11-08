---
declaration: def
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra
statement: formalized
---

# TauCeti.Dagger.washnitzerAlgebra

The **Monsky–Washnitzer algebra** `R⟨X⟩†` of overconvergent power series: the series
restricted at some constant radius `ρ > 1`.

```lean
TauCeti.Dagger.washnitzerAlgebra.{u_1, u_2} (σ : Type u_1) (R : Type u_2) [NormedCommRing R]
  [IsUltrametricDist R] : Subalgebra R (MvPowerSeries σ R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.washnitzerAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.washnitzerAlgebra)
- [Source of `TauCeti.Dagger.washnitzerAlgebra` in TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean#L113)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
