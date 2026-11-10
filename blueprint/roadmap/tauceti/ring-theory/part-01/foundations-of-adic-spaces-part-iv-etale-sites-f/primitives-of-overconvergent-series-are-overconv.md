---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.primitive_mem_washnitzerAlgebra
statement: formalized
proof: formalized
---

# Primitives of overconvergent series are overconvergent

Over an ultrametric normed field
of characteristic zero, the termwise primitive with respect to `Xᵢ` of an overconvergent series is
overconvergent. See `MvPowerSeries.IsRestricted.primitive` for the radius-by-radius version.

```lean
TauCeti.Dagger.primitive_mem_washnitzerAlgebra.{u_1, u_2} {σ : Type u_1} {K : Type u_2}
  [NormedField K] [IsUltrametricDist K] [CharZero K] {f : MvPowerSeries σ K}
  (hf : f ∈ TauCeti.Dagger.washnitzerAlgebra σ K) (i : σ) :
  (MvPowerSeries.primitive i) f ∈ TauCeti.Dagger.washnitzerAlgebra σ K
```

## Depends on

- [TauCeti.Dagger.washnitzerAlgebra](tauceti-dagger-washnitzeralgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.primitive_mem_washnitzerAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.primitive_mem_washnitzerAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.primitive_mem_washnitzerAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.primitive_mem_washnitzerAlgebra)
- [Source of `TauCeti.Dagger.primitive_mem_washnitzerAlgebra` in TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean#L631)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
