---
declaration: def
origin: cited
lean: TauCeti.restrictTotalDegreeEquivPolynomialsDegLE
statement: formalized
---

# TauCeti.restrictTotalDegreeEquivPolynomialsDegLE

Formal bounded-degree polynomials and the functions they represent are linearly
equivalent.

```lean
TauCeti.restrictTotalDegreeEquivPolynomialsDegLE.{u_1} (ι : Type u_1) (m : ℕ) :
  ↥(MvPolynomial.restrictTotalDegree ι ℝ m) ≃ₗ[ℝ] ↥(TauCeti.polynomialsDegLE ι m)
```

## Depends on

- [TauCeti.polynomialEvalₗ](tauceti-polynomialevall.md)
- [TauCeti.polynomialsDegLE](tauceti-polynomialsdegle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.restrictTotalDegreeEquivPolynomialsDegLE`](https://taucetiproject.org/docs/TauCeti/Analysis/MvPolynomial/PolynomialSpace.html#TauCeti.restrictTotalDegreeEquivPolynomialsDegLE).

## Sources

- [Tau Ceti documentation: `TauCeti.restrictTotalDegreeEquivPolynomialsDegLE`](https://taucetiproject.org/docs/TauCeti/Analysis/MvPolynomial/PolynomialSpace.html#TauCeti.restrictTotalDegreeEquivPolynomialsDegLE)
- [Source of `TauCeti.restrictTotalDegreeEquivPolynomialsDegLE` in TauCeti/Analysis/MvPolynomial/PolynomialSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/MvPolynomial/PolynomialSpace.lean#L87)
- [Tau Ceti roadmap status: Polynomial approximation in Sobolev spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SobolevPolynomialApproximation/STATUS.md)
