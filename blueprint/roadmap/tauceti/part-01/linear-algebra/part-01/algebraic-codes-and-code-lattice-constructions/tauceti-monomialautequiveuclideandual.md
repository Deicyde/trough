---
declaration: def
origin: cited
lean: TauCeti.monomialAutEquivEuclideanDual
statement: formalized
---

# TauCeti.monomialAutEquivEuclideanDual

The monomial automorphism groups of a linear code and of its Euclidean dual are isomorphic,
by taking contragredients.

```lean
TauCeti.monomialAutEquivEuclideanDual.{u_2, u_4} {ι : Type u_2} {K : Type u_4} [Field K] [Fintype ι]
  [DecidableEq ι] (C : Submodule K (ι → K)) :
  ↥(TauCeti.monomialAut C) ≃* ↥(TauCeti.monomialAut C.euclideanDual)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.monomialAutEquivEuclideanDual`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Duality.html#TauCeti.monomialAutEquivEuclideanDual).

## Sources

- [Tau Ceti documentation: `TauCeti.monomialAutEquivEuclideanDual`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Duality.html#TauCeti.monomialAutEquivEuclideanDual)
- [Source of `TauCeti.monomialAutEquivEuclideanDual` in TauCeti/InformationTheory/Coding/Duality.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/InformationTheory/Coding/Duality.lean#L312)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AlgebraicCodingTheory/STATUS.md)
