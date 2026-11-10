---
declaration: theorem
origin: cited
lean: TauCeti.Iwasawa.iwasawaCoordinate_injective
statement: formalized
proof: formalized
---

# The level coordinates separate points

over a noetherian `O`, the product
`O⟦T⟧ → ∏ₙ O[ℤ/pⁿ]` of the level maps is injective.

```lean
TauCeti.Iwasawa.iwasawaCoordinate_injective.{u_1} {p : ℕ} [Fact (Nat.Prime p)] {O : Type u_1}
  [CommRing O] [IsLocalRing O] (hp : ↑p ∈ IsLocalRing.maximalIdeal O)
  [IsAdicComplete (IsLocalRing.maximalIdeal O) O] [IsNoetherianRing O] :
  Function.Injective ⇑(TauCeti.Iwasawa.iwasawaCoordinate hp)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Iwasawa.ker_levelCoordinate](tauceti-iwasawa-ker-levelcoordinate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.iwasawaCoordinate_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/LevelCoordinate.html#TauCeti.Iwasawa.iwasawaCoordinate_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.iwasawaCoordinate_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/LevelCoordinate.html#TauCeti.Iwasawa.iwasawaCoordinate_injective)
- [Source of `TauCeti.Iwasawa.iwasawaCoordinate_injective` in TauCeti/RingTheory/Iwasawa/LevelCoordinate.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Iwasawa/LevelCoordinate.lean#L364)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
