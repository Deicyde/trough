---
declaration: theorem
origin: cited
lean: TauCeti.finrank_polynomialsDegLE
statement: formalized
proof: formalized
---

# TauCeti.finrank_polynomialsDegLE

The dimension of polynomial functions of total degree at most `m` is the number of
monomials of that degree or less.

```lean
TauCeti.finrank_polynomialsDegLE.{u_1} (ι : Type u_1) [Fintype ι] (m : ℕ) :
  Module.finrank ℝ ↥(TauCeti.polynomialsDegLE ι m) = (m + Fintype.card ι).choose (Fintype.card ι)
```

## Depends on

- [TauCeti.polynomialsDegLE](tauceti-polynomialsdegle.md)

## Proof depends on

- [TauCeti.restrictTotalDegreeEquivPolynomialsDegLE](tauceti-restricttotaldegreeequivpolynomialsdegle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_polynomialsDegLE`](https://taucetiproject.org/docs/TauCeti/Analysis/MvPolynomial/PolynomialSpace.html#TauCeti.finrank_polynomialsDegLE).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_polynomialsDegLE`](https://taucetiproject.org/docs/TauCeti/Analysis/MvPolynomial/PolynomialSpace.html#TauCeti.finrank_polynomialsDegLE)
- [Source of `TauCeti.finrank_polynomialsDegLE` in TauCeti/Analysis/MvPolynomial/PolynomialSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/MvPolynomial/PolynomialSpace.lean#L148)
- [Tau Ceti roadmap status: Polynomial approximation in Sobolev spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SobolevPolynomialApproximation/STATUS.md)
