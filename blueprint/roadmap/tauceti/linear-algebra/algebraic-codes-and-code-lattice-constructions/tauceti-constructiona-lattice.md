---
declaration: def
origin: cited
lean: TauCeti.ConstructionA.lattice
statement: formalized
---

# TauCeti.ConstructionA.lattice

The rational carrier of Construction A: the integer vectors reducing to the additive code
`C` modulo `m`.

```lean
TauCeti.ConstructionA.lattice.{u_1} {ι : Type u_1} (m : ℕ) (C : AddSubgroup (ι → ZMod m)) :
  Submodule ℤ (ι → ℚ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ConstructionA.lattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Basic.html#TauCeti.ConstructionA.lattice).

## Sources

- [Tau Ceti documentation: `TauCeti.ConstructionA.lattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Basic.html#TauCeti.ConstructionA.lattice)
- [Source of `TauCeti.ConstructionA.lattice` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Basic.lean#L54)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AlgebraicCodingTheory/STATUS.md)
