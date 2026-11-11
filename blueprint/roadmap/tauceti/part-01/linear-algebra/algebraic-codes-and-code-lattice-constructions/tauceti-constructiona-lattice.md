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
- [Source of `TauCeti.ConstructionA.lattice` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Basic.lean#L54)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AlgebraicCodingTheory/STATUS.md)
