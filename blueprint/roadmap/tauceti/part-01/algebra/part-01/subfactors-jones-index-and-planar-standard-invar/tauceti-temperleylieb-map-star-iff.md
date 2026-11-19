---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.map_star_iff
statement: formalized
proof: formalized
---

# TauCeti.TemperleyLieb.map_star_iff

An algebra map out of the Temperley–Lieb algebra preserves the analytic adjoint exactly when
it sends every generator to a self-adjoint element. So the presentation is also a presentation
as a star algebra.

```lean
TauCeti.TemperleyLieb.map_star_iff.{u_1, u_2} {R : Type u_1} [CommSemiring R] [StarRing R] {δ : R}
  {n : ℕ} [hδ : Fact (IsSelfAdjoint δ)] {A : Type u_2} [Semiring A] [StarRing A] [Algebra R A]
  [StarModule R A] {F : TauCeti.TemperleyLieb R δ n →ₐ[R] A} :
  (∀ (x : TauCeti.TemperleyLieb R δ n), F (star x) = star (F x)) ↔
    ∀ (i : Fin (n - 1)), IsSelfAdjoint (F (TauCeti.TemperleyLieb.e δ i))
```

## Depends on

- [TauCeti.TemperleyLieb.instStarRing](tauceti-temperleylieb-inststarring.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.map_star_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.map_star_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.map_star_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.map_star_iff)
- [Source of `TauCeti.TemperleyLieb.map_star_iff` in TauCeti/Algebra/TemperleyLieb/Star.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TemperleyLieb/Star.lean#L152)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Subfactors/STATUS.md)
