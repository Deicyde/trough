---
declaration: def
origin: cited
lean: TauCeti.reductiveCommHopfAlgPropertyOver
statement: formalized
---

# TauCeti.reductiveCommHopfAlgPropertyOver

A finite-type affine group scheme over a commutative ring is reductive when it is smooth
and all of its geometric fibers are connected reductive groups.

```lean
TauCeti.reductiveCommHopfAlgPropertyOver.{u} (R : Type u) [CommRing R] :
  CategoryTheory.ObjectProperty (TauCeti.FiniteTypeCommHopfAlgCat R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.reductiveCommHopfAlgPropertyOver`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Reductive/Over.html#TauCeti.reductiveCommHopfAlgPropertyOver).

## Sources

- [Tau Ceti documentation: `TauCeti.reductiveCommHopfAlgPropertyOver`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Reductive/Over.html#TauCeti.reductiveCommHopfAlgPropertyOver)
- [Source of `TauCeti.reductiveCommHopfAlgPropertyOver` in TauCeti/Algebra/AlgebraicGroup/Reductive/Over.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Reductive/Over.lean#L43)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroups/STATUS.md)
