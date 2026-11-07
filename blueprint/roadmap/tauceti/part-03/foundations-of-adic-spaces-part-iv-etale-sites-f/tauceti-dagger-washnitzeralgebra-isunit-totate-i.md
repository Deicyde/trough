---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.isUnit_toTate_iff
statement: formalized
proof: formalized
---

# TauCeti.Dagger.washnitzerAlgebra.isUnit\_toTate\_iff

An overconvergent series is a unit of the Tate algebra iff it is a unit of the
Monsky–Washnitzer algebra: the inverse of an overconvergent series is overconvergent.

```lean
TauCeti.Dagger.washnitzerAlgebra.isUnit_toTate_iff.{u_1, u_2} {σ : Type u_1} {K : Type u_2}
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K]
  (f : ↥(TauCeti.Dagger.washnitzerAlgebra σ K)) :
  IsUnit ((TauCeti.Dagger.washnitzerAlgebra.toTate σ K) f) ↔ IsUnit f
```

## Depends on

- [TauCeti.Dagger.washnitzerAlgebra](tauceti-dagger-washnitzeralgebra.md)
- [TauCeti.Dagger.washnitzerAlgebra.toTate](tauceti-dagger-washnitzeralgebra-totate.md)

## Proof depends on

- [Units of the Monsky–Washnitzer algebra](units-of-the-monsky-washnitzer-algebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.isUnit_toTate_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.washnitzerAlgebra.isUnit_toTate_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.isUnit_toTate_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.washnitzerAlgebra.isUnit_toTate_iff)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.isUnit_toTate_iff` in TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean#L592)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
