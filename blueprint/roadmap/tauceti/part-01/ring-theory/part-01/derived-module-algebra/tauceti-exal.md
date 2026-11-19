---
declaration: def
origin: cited
lean: TauCeti.Exal
statement: formalized
---

# TauCeti.Exal

`Exal_A(B, M)`: the isomorphism classes of square-zero extensions of the `A`-algebra `B` by
the `B`-module `M`, whose rings lie in the universe of `B` and `M`.

```lean
TauCeti.Exal.{u, v, t} (A : Type u) (B : Type v) (M : Type t) [CommRing A] [CommRing B]
  [Algebra A B] [AddCommGroup M] [_root_.Module B M] : Type (max (max (t + 1) u) (v + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Exal`](https://taucetiproject.org/docs/TauCeti/RingTheory/Extension/SquareZero/Basic.html#TauCeti.Exal).

## Sources

- [Tau Ceti documentation: `TauCeti.Exal`](https://taucetiproject.org/docs/TauCeti/RingTheory/Extension/SquareZero/Basic.html#TauCeti.Exal)
- [Source of `TauCeti.Exal` in TauCeti/RingTheory/Extension/SquareZero/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Extension/SquareZero/Basic.lean#L315)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
