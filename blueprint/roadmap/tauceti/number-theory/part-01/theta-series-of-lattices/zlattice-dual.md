---
declaration: def
origin: cited
lean: ZLattice.dual
statement: formalized
---

# ZLattice.dual

The dual lattice of `L : Submodule ℤ E`: the vectors whose inner product with every vector of
`L` is an integer. It is Mathlib's `BilinForm.dualSubmodule` of the inner product.

```lean
ZLattice.dual.{u} {E : Type u} [NormedAddCommGroup E] [InnerProductSpace ℝ E] (L : Submodule ℤ E) :
  Submodule ℤ E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZLattice.dual`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Dual.html#ZLattice.dual).

## Sources

- [Tau Ceti documentation: `ZLattice.dual`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Dual.html#ZLattice.dual)
- [Source of `ZLattice.dual` in TauCeti/Algebra/Module/ZLattice/Dual.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/ZLattice/Dual.lean#L82)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
