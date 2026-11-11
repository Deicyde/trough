---
declaration: theorem
origin: cited
lean: TauCeti.IsMonomialEquivalent.hammingMinDist_eq
statement: formalized
proof: formalized
---

# TauCeti.IsMonomialEquivalent.hammingMinDist_eq

Monomially equivalent codes have the same minimum distance.

```lean
TauCeti.IsMonomialEquivalent.hammingMinDist_eq.{u_1, u_2, u_3} {R : Type u_3} {ι : Type u_1}
  {κ : Type u_2} [CommSemiring R] {C : Submodule R (ι → R)} {D : Submodule R (κ → R)} [Fintype ι]
  [Fintype κ] [DecidableEq R] (h : TauCeti.IsMonomialEquivalent C D) :
  (↑C).hammingMinDist = (↑D).hammingMinDist
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMonomialEquivalent.hammingMinDist_eq`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Equivalence.html#TauCeti.IsMonomialEquivalent.hammingMinDist_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMonomialEquivalent.hammingMinDist_eq`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Equivalence.html#TauCeti.IsMonomialEquivalent.hammingMinDist_eq)
- [Source of `TauCeti.IsMonomialEquivalent.hammingMinDist_eq` in TauCeti/InformationTheory/Coding/Equivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/InformationTheory/Coding/Equivalence.lean#L414)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AlgebraicCodingTheory/STATUS.md)
