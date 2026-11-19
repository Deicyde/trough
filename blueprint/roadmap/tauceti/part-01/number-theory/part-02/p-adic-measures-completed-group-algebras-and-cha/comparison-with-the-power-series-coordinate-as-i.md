---
declaration: theorem
origin: cited
lean: TauCeti.Iwasawa.completedCoordinateEquiv_eq_powerSeriesCoordinate
statement: formalized
proof: formalized
---

# Comparison with the power-series coordinate, as isomorphisms

Over `O = ℤ_p`, the
isomorphism `completedCoordinateEquiv hp` is the power-series coordinate attached to the
topological generator `γ = 1` of `ℤ_p`.

```lean
TauCeti.Iwasawa.completedCoordinateEquiv_eq_powerSeriesCoordinate {p : ℕ} [Fact (Nat.Prime p)]
  (hp : ↑p ∈ IsLocalRing.maximalIdeal ℤ_[p]) :
  TauCeti.Iwasawa.completedCoordinateEquiv hp =
    TauCeti.completedGroupAlgebra.powerSeriesCoordinate ⋯ ⋯
```

## Depends on

- [The Iwasawa algebra is the completed group algebra of `ℤ_p`](the-iwasawa-algebra-is-the-completed-group-algeb.md)

## Proof depends on

- [TauCeti.FiniteQuotientTower](tauceti-finitequotienttower.md)
- [Van Dantzig's theorem](../../../../part-02/topology/algebra/part-02/van-dantzigs-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.completedCoordinateEquiv_eq_powerSeriesCoordinate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/CompletedCoordinate.html#TauCeti.Iwasawa.completedCoordinateEquiv_eq_powerSeriesCoordinate).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.completedCoordinateEquiv_eq_powerSeriesCoordinate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/CompletedCoordinate.html#TauCeti.Iwasawa.completedCoordinateEquiv_eq_powerSeriesCoordinate)
- [Source of `TauCeti.Iwasawa.completedCoordinateEquiv_eq_powerSeriesCoordinate` in TauCeti/RingTheory/Iwasawa/CompletedCoordinate.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Iwasawa/CompletedCoordinate.lean#L197)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
