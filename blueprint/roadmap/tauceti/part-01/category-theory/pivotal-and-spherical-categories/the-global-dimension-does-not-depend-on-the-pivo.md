---
declaration: theorem
origin: cited
lean: TauCeti.globalDim_pivotalCategory_eq
statement: formalized
proof: formalized
---

# The global dimension does not depend on the pivotal structure

over an algebraically
closed field `k`, if the endomorphisms of each simple object are finite-dimensional, then any two
pivotal structures `P` and `Q` on `C` give the same global dimension.

```lean
TauCeti.globalDim_pivotalCategory_eq.{w, v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.RigidCategory C]
  [CategoryTheory.Preadditive C] [Fintype (TauCeti.SimpleClasses C)] (k : Type w) [Field k]
  [IsAlgClosed k] [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.Linear k C]
  [CategoryTheory.MonoidalLinear k C] [CategoryTheory.Limits.HasKernels C]
  [∀ (S : TauCeti.SimpleClasses C), FiniteDimensional k (S.repr ⟶ S.repr)]
  (P Q : TauCeti.PivotalCategory C) : TauCeti.globalDim C = TauCeti.globalDim C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Freyd–Yetter identity](the-freyd-yetter-identity.md)
- [Schur's lemma as an identification of algebras](../preadditive/schurs-lemma-as-an-identification-of-algebras.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.globalDim_pivotalCategory_eq`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/GlobalDim.html#TauCeti.globalDim_pivotalCategory_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.globalDim_pivotalCategory_eq`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/GlobalDim.html#TauCeti.globalDim_pivotalCategory_eq)
- [Source of `TauCeti.globalDim_pivotalCategory_eq` in TauCeti/CategoryTheory/Monoidal/Pivotal/GlobalDim.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Pivotal/GlobalDim.lean#L84)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PivotalSpherical/STATUS.md)
