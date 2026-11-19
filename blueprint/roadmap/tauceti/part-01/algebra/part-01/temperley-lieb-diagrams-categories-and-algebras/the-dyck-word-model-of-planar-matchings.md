---
declaration: def
origin: cited
lean: TauCeti.PlanarMatching.dyckWordEquiv
statement: formalized
---

# The Dyck-word model of planar matchings

Recording at each boundary point whether its arc
opens or closes there is an equivalence between the planar matchings of `2 * n` points and the
Dyck words of semilength `n`.

```lean
TauCeti.PlanarMatching.dyckWordEquiv (n : ℕ) :
  TauCeti.PlanarMatching (2 * n) ≃ { p // p.semilength = n }
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Catalan count](the-catalan-count.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PlanarMatching.dyckWordEquiv`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PlanarMatching/DyckWord.html#TauCeti.PlanarMatching.dyckWordEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.PlanarMatching.dyckWordEquiv`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PlanarMatching/DyckWord.html#TauCeti.PlanarMatching.dyckWordEquiv)
- [Source of `TauCeti.PlanarMatching.dyckWordEquiv` in TauCeti/Combinatorics/PlanarMatching/DyckWord.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/PlanarMatching/DyckWord.lean#L223)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TemperleyLieb/STATUS.md)
