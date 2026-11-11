---
declaration: theorem
origin: cited
lean: Polynomial.isUnit_entireResultant_iff
statement: formalized
proof: formalized
---

# The entire resultant detects coprimality

For monic `P` and entire `F`, `Res(P, F)` is a
unit exactly when `P` and `F` are coprime in the ring of entire series.

```lean
Polynomial.isUnit_entireResultant_iff.{u_1} {R : Type u_1} [NormedCommRing R] [CompleteSpace R]
  [IsUltrametricDist R] [NormOneClass R] {P : Polynomial R} {F : PowerSeries R} (hP : P.Monic)
  (hF : F.IsEntire) : IsUnit (P.entireResultant F) ↔ IsCoprime ⟨↑P, ⋯⟩ ⟨F, ⋯⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass division estimate for a multiplicatively distinguished divisor](the-weierstrass-division-estimate-for-a-multipli.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.isUnit_entireResultant_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Resultant.html#Polynomial.isUnit_entireResultant_iff).

## Sources

- [Tau Ceti documentation: `Polynomial.isUnit_entireResultant_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Resultant.html#Polynomial.isUnit_entireResultant_iff)
- [Source of `Polynomial.isUnit_entireResultant_iff` in TauCeti/RingTheory/PowerSeries/Entire/Resultant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Entire/Resultant.lean#L226)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
