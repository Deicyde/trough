---
declaration: def
origin: cited
lean: TauCeti.DynkinType.rootLatticeIsometryCheckerboard
statement: formalized
---

# The root lattice of type `Dₙ` is the checkerboard lattice

For `4 ≤ n`, the isometry
sends the `i`-th simple root to the `i`-th Bourbaki simple root of the Conway--Sloane coordinate
model `{x ∈ ℤⁿ | ∑ xᵢ even}`; both bases have Gram matrix `CartanMatrix.D n`.

```lean
TauCeti.DynkinType.rootLatticeIsometryCheckerboard (n : ℕ) (hn : 4 ≤ n)
  (ht : (TauCeti.DynkinType.D n).IsSimplyLaced) :
  ((TauCeti.DynkinType.D n).rootLattice ht).Isometry (TauCeti.IntegralLattice.checkerboardLattice n)
```

## Depends on

- [The positive root lattice of a simply-laced Dynkin type `t`](the-positive-root-lattice-of-a-simply-laced-dynk.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.rootLatticeIsometryCheckerboard`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/Dynkin.html#TauCeti.DynkinType.rootLatticeIsometryCheckerboard).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.rootLatticeIsometryCheckerboard`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/Dynkin.html#TauCeti.DynkinType.rootLatticeIsometryCheckerboard)
- [Source of `TauCeti.DynkinType.rootLatticeIsometryCheckerboard` in TauCeti/LinearAlgebra/IntegralLattice/RootLattice/Dynkin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/Dynkin.lean#L274)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
