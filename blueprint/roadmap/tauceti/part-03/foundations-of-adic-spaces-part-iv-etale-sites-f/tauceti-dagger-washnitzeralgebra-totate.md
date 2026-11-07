---
declaration: def
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.toTate
statement: formalized
---

# TauCeti.Dagger.washnitzerAlgebra.toTate

The inclusion of the Monsky–Washnitzer algebra into the unit-radius Tate algebra `R{X/1}`,
through which `W` carries the Gauss norm.

```lean
TauCeti.Dagger.washnitzerAlgebra.toTate.{u_1, u_2} (σ : Type u_1) (R : Type u_2) [NormedCommRing R]
  [IsUltrametricDist R] :
  ↥(TauCeti.Dagger.washnitzerAlgebra σ R) →ₐ[R] ↥(MvPowerSeries.IsRestricted.subring fun x => 1)
```

## Depends on

- [TauCeti.Dagger.washnitzerAlgebra](tauceti-dagger-washnitzeralgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.toTate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.washnitzerAlgebra.toTate).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.toTate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.washnitzerAlgebra.toTate)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.toTate` in TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean#L293)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
