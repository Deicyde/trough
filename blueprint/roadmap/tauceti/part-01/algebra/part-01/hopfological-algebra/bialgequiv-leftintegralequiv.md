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
- [Source of `BialgEquiv.leftIntegralEquiv` in TauCeti/Algebra/HopfAlgebra/Integral/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/HopfAlgebra/Integral/Basic.lean#L212)
- [Tau Ceti roadmap status: Hopfological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HopfologicalAlgebra/STATUS.md)
