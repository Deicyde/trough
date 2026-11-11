---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.isSelfAdjoint_of_star_e
statement: formalized
proof: formalized
---

# TauCeti.TemperleyLieb.isSelfAdjoint_of_star_e

A conjugate-linear star structure on the two-strand Temperley–Lieb algebra fixing the
generator exists only for a self-adjoint loop value: applied to `e * e = δ • e` it gives
`δ • e = star δ • e`. In particular over `ℂ` the loop value must be real.

```lean
TauCeti.TemperleyLieb.isSelfAdjoint_of_star_e.{u_1} {R : Type u_1} [CommSemiring R] [StarRing R]
  {δ : R} [StarMul (TauCeti.TemperleyLieb R δ 2)] [StarModule R (TauCeti.TemperleyLieb R δ 2)]
  (i : Fin (2 - 1)) (he : star (TauCeti.TemperleyLieb.e δ i) = TauCeti.TemperleyLieb.e δ i) :
  IsSelfAdjoint δ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.isSelfAdjoint_of_star_e`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.isSelfAdjoint_of_star_e).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.isSelfAdjoint_of_star_e`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.isSelfAdjoint_of_star_e)
- [Source of `TauCeti.TemperleyLieb.isSelfAdjoint_of_star_e` in TauCeti/Algebra/TemperleyLieb/Star.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/TemperleyLieb/Star.lean#L196)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Subfactors/STATUS.md)
