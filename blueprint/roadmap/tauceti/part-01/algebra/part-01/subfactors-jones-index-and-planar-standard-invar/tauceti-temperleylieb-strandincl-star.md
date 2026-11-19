---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.strandIncl_star
statement: formalized
proof: formalized
---

# TauCeti.TemperleyLieb.strandIncl_star

Adding a straight strand commutes with the analytic adjoint.

```lean
TauCeti.TemperleyLieb.strandIncl_star.{u_1} {R : Type u_1} [CommSemiring R] [StarRing R] {δ : R}
  {n : ℕ} [hδ : Fact (IsSelfAdjoint δ)] (x : TauCeti.TemperleyLieb R δ (n + 1)) :
  TauCeti.TemperleyLieb.strandIncl (star x) = star (TauCeti.TemperleyLieb.strandIncl x)
```

## Depends on

- [TauCeti.TemperleyLieb.instStarRing](tauceti-temperleylieb-inststarring.md)

## Proof depends on

- [TauCeti.TemperleyLieb.map_star_iff](tauceti-temperleylieb-map-star-iff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.strandIncl_star`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.strandIncl_star).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.strandIncl_star`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Star.html#TauCeti.TemperleyLieb.strandIncl_star)
- [Source of `TauCeti.TemperleyLieb.strandIncl_star` in TauCeti/Algebra/TemperleyLieb/Star.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TemperleyLieb/Star.lean#L169)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Subfactors/STATUS.md)
