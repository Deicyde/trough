---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.star_unique
statement: formalized
proof: formalized
---

# TauCeti.TemperleyLieb.star_unique

The analytic adjoint is the unique additive, product-reversing, conjugate-linear unital map
fixing every generator.

```lean
TauCeti.TemperleyLieb.star_unique.{u_1} {R : Type u_1} [CommSemiring R] [StarRing R] {δ : R} {n : ℕ}
  [hδ : Fact (IsSelfAdjoint δ)] {f : TauCeti.TemperleyLieb R δ n → TauCeti.TemperleyLieb R δ n}
  (map_add : ∀ (x y : TauCeti.TemperleyLieb R δ n), f (x + y) = f x + f y)
  (map_mul : ∀ (x y : TauCeti.TemperleyLieb R δ n), f (x * y) = f y * f x)
  (map_smul : ∀ (r : R) (x : TauCeti.TemperleyLieb R δ n), f (r • x) = star r • f x)
  (map_one : f 1 = 1)
  (map_e : ∀ (i : Fin (n - 1)), f (TauCeti.TemperleyLieb.e δ i) = TauCeti.TemperleyLieb.e δ i) :
  f = star
```

## Depends on

- [TauCeti.TemperleyLieb.instStarRing](tauceti-temperleylieb-inststarring.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.star_unique`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.star_unique).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.star_unique`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.star_unique)
- [Source of `TauCeti.TemperleyLieb.star_unique` in TauCeti/Algebra/TemperleyLieb/Star.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/TemperleyLieb/Star.lean#L134)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Subfactors/STATUS.md)
