---
declaration: def
origin: cited
lean: TauCeti.integralAntipodeEquiv
statement: formalized
---

# TauCeti.integralAntipodeEquiv

A bijective antipode identifies the left and right integral submodules.

```lean
TauCeti.integralAntipodeEquiv.{u_1, u_2} {R : Type u_1} {H : Type u_2} [CommSemiring R] [Semiring H]
  [HopfAlgebra R H] (hS : Function.Bijective ⇑(HopfAlgebraStruct.antipode R)) :
  ↥(TauCeti.leftIntegral R H) ≃ₗ[R] ↥(TauCeti.rightIntegral R H)
```

## Depends on

- [TauCeti.leftIntegral](tauceti-leftintegral.md)
- [TauCeti.rightIntegral](tauceti-rightintegral.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integralAntipodeEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/Basic.html#TauCeti.integralAntipodeEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.integralAntipodeEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/Basic.html#TauCeti.integralAntipodeEquiv)
- [Source of `TauCeti.integralAntipodeEquiv` in TauCeti/Algebra/HopfAlgebra/Integral/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/HopfAlgebra/Integral/Basic.lean#L153)
- [Tau Ceti roadmap status: Hopfological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HopfologicalAlgebra/STATUS.md)
