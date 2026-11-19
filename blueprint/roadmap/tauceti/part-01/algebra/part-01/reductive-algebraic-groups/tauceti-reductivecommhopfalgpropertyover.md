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
- [Source of `TauCeti.reductiveCommHopfAlgPropertyOver` in TauCeti/Algebra/AlgebraicGroup/Reductive/Over.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/Reductive/Over.lean#L43)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroups/STATUS.md)
