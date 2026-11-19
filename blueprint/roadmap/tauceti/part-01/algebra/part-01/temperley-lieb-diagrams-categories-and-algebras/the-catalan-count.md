---
declaration: theorem
origin: cited
lean: TauCeti.PlanarMatching.card_planarMatching
statement: formalized
proof: formalized
---

# The Catalan count

There are `catalan n` planar matchings of `2 * n` points.

```lean
TauCeti.PlanarMatching.card_planarMatching (n : ℕ) :
  Nat.card (TauCeti.PlanarMatching (2 * n)) = catalan n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PlanarMatching.card_planarMatching`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PlanarMatching/DyckWord.html#TauCeti.PlanarMatching.card_planarMatching).

## Sources

- [Tau Ceti documentation: `TauCeti.PlanarMatching.card_planarMatching`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PlanarMatching/DyckWord.html#TauCeti.PlanarMatching.card_planarMatching)
- [Source of `TauCeti.PlanarMatching.card_planarMatching` in TauCeti/Combinatorics/PlanarMatching/DyckWord.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/PlanarMatching/DyckWord.lean#L211)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TemperleyLieb/STATUS.md)
