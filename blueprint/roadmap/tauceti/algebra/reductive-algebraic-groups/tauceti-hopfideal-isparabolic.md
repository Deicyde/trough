---
declaration: def
origin: cited
lean: TauCeti.HopfIdeal.IsParabolic
statement: formalized
---

# TauCeti.HopfIdeal.IsParabolic

A Hopf ideal defines a **parabolic subgroup** when its base change to an algebraic closure
defines a smooth closed subgroup of the geometric fibre containing a Borel subgroup.

The order is contravariant: `I ≤ J` says that the subgroup cut out by `I` contains the subgroup
cut out by `J`.

```lean
TauCeti.HopfIdeal.IsParabolic.{u, v} (k : Type u) [Field k] (H : CommHopfAlgCat k)
  [Algebra.FiniteType k ↑H] (I : TauCeti.HopfIdeal k ↑H) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfIdeal.IsParabolic`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Parabolic/Basic.html#TauCeti.HopfIdeal.IsParabolic).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfIdeal.IsParabolic`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Parabolic/Basic.html#TauCeti.HopfIdeal.IsParabolic)
- [Source of `TauCeti.HopfIdeal.IsParabolic` in TauCeti/Algebra/AlgebraicGroup/Parabolic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Parabolic/Basic.lean#L243)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReductiveGroups/STATUS.md)
