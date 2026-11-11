---
declaration: instance
origin: cited
lean: TauCeti.TemperleyLieb.instStarRing
statement: formalized
---

# TauCeti.TemperleyLieb.instStarRing

For a self-adjoint loop value, the analytic adjoint on the Temperley–Lieb algebra: the
conjugate-linear, product-reversing involution fixing every generator.

```lean
TauCeti.TemperleyLieb.instStarRing.{u_1} {R : Type u_1} [CommSemiring R] [StarRing R] {δ : R}
  {n : ℕ} [hδ : Fact (IsSelfAdjoint δ)] : StarRing (TauCeti.TemperleyLieb R δ n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.instStarRing`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.instStarRing).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.instStarRing`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.instStarRing)
- [Source of `TauCeti.TemperleyLieb.instStarRing` in TauCeti/Algebra/TemperleyLieb/Star.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/TemperleyLieb/Star.lean#L108)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Subfactors/STATUS.md)
