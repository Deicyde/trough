---
declaration: def
origin: cited
lean: TauCeti.DynkinType.rootLattice
statement: formalized
---

# The positive root lattice of a simply-laced Dynkin type

`t`: the integral lattice on
`Fin t.rank → ℚ` whose Gram matrix in the standard basis is the Cartan matrix `t.cartanMatrix`.
The standard coordinate vectors are the simple roots, in Bourbaki numbering.

```lean
TauCeti.DynkinType.rootLattice (t : TauCeti.DynkinType) (ht : t.IsSimplyLaced) :
  TauCeti.IntegralLattice (Fin t.rank → ℚ)
```

## Depends on

- [TauCeti.IntegralLattice](../../part-04/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.rootLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/Dynkin.html#TauCeti.DynkinType.rootLattice).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.rootLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/Dynkin.html#TauCeti.DynkinType.rootLattice)
- [Source of `TauCeti.DynkinType.rootLattice` in TauCeti/LinearAlgebra/IntegralLattice/RootLattice/Dynkin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/Dynkin.lean#L81)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
