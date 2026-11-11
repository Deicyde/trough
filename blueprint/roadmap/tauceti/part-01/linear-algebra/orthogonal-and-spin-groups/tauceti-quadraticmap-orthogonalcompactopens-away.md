---
declaration: abbrev
origin: cited
lean: TauCeti.QuadraticMap.OrthogonalCompactOpens.awayAdelicSpin
statement: formalized
---

# TauCeti.QuadraticMap.OrthogonalCompactOpens.awayAdelicSpin

The Spin group `Spin(V)(𝔸^S)` of the adeles away from `S`: the restricted product over the
primes outside `S` of the local Spin groups relative to the reference subgroups `U.spin p`.

```lean
TauCeti.QuadraticMap.OrthogonalCompactOpens.awayAdelicSpin.{u_1} {V : Type u_1} [AddCommGroup V]
  [_root_.Module ℚ V] {Q : QuadraticForm ℚ V} (U : TauCeti.QuadraticMap.OrthogonalCompactOpens Q)
  (S : Set Nat.Primes) : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.QuadraticMap.OrthogonalCompactOpens.awayAdelicSpin`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/AwayAdelic.html#TauCeti.QuadraticMap.OrthogonalCompactOpens.awayAdelicSpin).

## Sources

- [Tau Ceti documentation: `TauCeti.QuadraticMap.OrthogonalCompactOpens.awayAdelicSpin`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/AwayAdelic.html#TauCeti.QuadraticMap.OrthogonalCompactOpens.awayAdelicSpin)
- [Source of `TauCeti.QuadraticMap.OrthogonalCompactOpens.awayAdelicSpin` in TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/AwayAdelic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/AwayAdelic.lean#L120)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalSpinGroups/STATUS.md)
