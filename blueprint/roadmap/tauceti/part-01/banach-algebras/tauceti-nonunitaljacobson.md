---
declaration: def
origin: cited
lean: TauCeti.nonUnitalJacobson
statement: formalized
---

# TauCeti.nonUnitalJacobson

The Jacobson radical of a nonunital algebra, defined through its external unitization.

```lean
TauCeti.nonUnitalJacobson.{u_1, u_2} (R : Type u_1) (A : Type u_2) [CommRing R] [NonUnitalRing A]
  [_root_.Module R A] [IsScalarTower R A A] [SMulCommClass R A A] : TwoSidedIdeal A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.nonUnitalJacobson`](https://taucetiproject.org/docs/TauCeti/RingTheory/Jacobson/NonUnital.html#TauCeti.nonUnitalJacobson).

## Sources

- [Tau Ceti documentation: `TauCeti.nonUnitalJacobson`](https://taucetiproject.org/docs/TauCeti/RingTheory/Jacobson/NonUnital.html#TauCeti.nonUnitalJacobson)
- [Source of `TauCeti.nonUnitalJacobson` in TauCeti/RingTheory/Jacobson/NonUnital.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Jacobson/NonUnital.lean#L55)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachAlgebras/STATUS.md)
