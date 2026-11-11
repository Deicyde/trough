---
declaration: def
origin: cited
lean: ChainComplex.regradeEquivalence
statement: formalized
---

# ChainComplex.regradeEquivalence

The equivalence of categories `ChainComplex C ℤ ≌ CochainComplex C ℤ` regrading a chain
complex `K` into the cochain complex with `C^k = K_(n-k)` and the same differential. Its body is
exposed so that statements about its functor, inverse, unit and counit, such as
`regradeEquivalence_unitIso_hom_app_f` and `regradeIsoShift`, type-check with `C^k = K_(n-k)`
definitionally.

```lean
ChainComplex.regradeEquivalence.{v_1, u_1} (C : Type u_1) [CategoryTheory.Category.{v_1, u_1} C]
  [CategoryTheory.Limits.HasZeroMorphisms C] (n : ℤ) : ChainComplex C ℤ ≌ CochainComplex C ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ChainComplex.regradeEquivalence`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Embedding/Regrade.html#ChainComplex.regradeEquivalence).

## Sources

- [Tau Ceti documentation: `ChainComplex.regradeEquivalence`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Embedding/Regrade.html#ChainComplex.regradeEquivalence)
- [Source of `ChainComplex.regradeEquivalence` in TauCeti/Algebra/Homology/Embedding/Regrade.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/Embedding/Regrade.lean#L102)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
