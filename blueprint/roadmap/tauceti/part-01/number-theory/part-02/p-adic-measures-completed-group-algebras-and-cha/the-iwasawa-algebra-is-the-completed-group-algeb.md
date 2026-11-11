---
declaration: def
origin: cited
lean: TauCeti.Iwasawa.completedCoordinateEquiv
statement: formalized
---

# The Iwasawa algebra is the completed group algebra of `ℤ_p`

For a noetherian local ring
`O`, complete for its maximal ideal, in which `p` is not a unit, the `O`-algebra isomorphism
`O⟦T⟧ ≃ₐ[O] O[[ℤ_p]]` sending `T` to `γ - 1`, for the topological generator `γ = 1` of `ℤ_p`.

```lean
TauCeti.Iwasawa.completedCoordinateEquiv.{u_1} {p : ℕ} [Fact (Nat.Prime p)] {O : Type u_1}
  [CommRing O] [IsLocalRing O] (hp : ↑p ∈ IsLocalRing.maximalIdeal O)
  [IsAdicComplete (IsLocalRing.maximalIdeal O) O] [IsNoetherianRing O] :
  PowerSeries O ≃ₐ[O] TauCeti.completedGroupAlgebra O (Multiplicative ℤ_[p])
```

## Depends on

- [TauCeti.FiniteQuotientTower](tauceti-finitequotienttower.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.completedCoordinateEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/CompletedCoordinate.html#TauCeti.Iwasawa.completedCoordinateEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.completedCoordinateEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/CompletedCoordinate.html#TauCeti.Iwasawa.completedCoordinateEquiv)
- [Source of `TauCeti.Iwasawa.completedCoordinateEquiv` in TauCeti/RingTheory/Iwasawa/CompletedCoordinate.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Iwasawa/CompletedCoordinate.lean#L159)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
