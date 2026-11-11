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
- [Source of `TauCeti.PlanarMatching.card_planarMatching` in TauCeti/Combinatorics/PlanarMatching/DyckWord.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/PlanarMatching/DyckWord.lean#L211)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
