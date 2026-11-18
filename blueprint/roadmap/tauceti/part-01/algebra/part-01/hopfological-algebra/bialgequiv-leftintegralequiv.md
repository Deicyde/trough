---
declaration: def
origin: cited
lean: BialgEquiv.leftIntegralEquiv
statement: formalized
---

# BialgEquiv.leftIntegralEquiv

Restrict a bialgebra isomorphism to the left integral submodules.

```lean
BialgEquiv.leftIntegralEquiv.{u_1, u_2, u_3} {R : Type u_1} {H : Type u_2} {K : Type u_3}
  [CommSemiring R] [Semiring H] [Semiring K] [Bialgebra R H] [Bialgebra R K] (e : H ≃ₐc[R] K) :
  ↥(TauCeti.leftIntegral R H) ≃ₗ[R] ↥(TauCeti.leftIntegral R K)
```

## Depends on

- [TauCeti.leftIntegral](tauceti-leftintegral.md)

## Lean

Formalized in Tau Ceti as [`BialgEquiv.leftIntegralEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/Basic.html#BialgEquiv.leftIntegralEquiv).

## Sources

- [Tau Ceti documentation: `BialgEquiv.leftIntegralEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/Basic.html#BialgEquiv.leftIntegralEquiv)
- [Source of `BialgEquiv.leftIntegralEquiv` in TauCeti/Algebra/HopfAlgebra/Integral/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/HopfAlgebra/Integral/Basic.lean#L212)
- [Tau Ceti roadmap status: Hopfological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HopfologicalAlgebra/STATUS.md)
