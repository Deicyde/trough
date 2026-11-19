---
declaration: def
origin: cited
lean: TauCeti.leftIntegral
statement: formalized
---

# TauCeti.leftIntegral

The submodule of left integrals, including zero. A nonzero integral need not have
nonzero counit.

```lean
TauCeti.leftIntegral.{u_1, u_2} (R : Type u_1) (H : Type u_2) [CommSemiring R] [Semiring H]
  [Bialgebra R H] : Submodule R H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.leftIntegral`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/Basic.html#TauCeti.leftIntegral).

## Sources

- [Tau Ceti documentation: `TauCeti.leftIntegral`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/Basic.html#TauCeti.leftIntegral)
- [Source of `TauCeti.leftIntegral` in TauCeti/Algebra/HopfAlgebra/Integral/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/HopfAlgebra/Integral/Basic.lean#L42)
- [Tau Ceti roadmap status: Hopfological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HopfologicalAlgebra/STATUS.md)
