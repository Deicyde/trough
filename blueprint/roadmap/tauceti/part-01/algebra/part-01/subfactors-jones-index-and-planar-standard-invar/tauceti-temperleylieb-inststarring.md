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
- [Source of `TauCeti.TemperleyLieb.instStarRing` in TauCeti/Algebra/TemperleyLieb/Star.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TemperleyLieb/Star.lean#L108)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Subfactors/STATUS.md)
