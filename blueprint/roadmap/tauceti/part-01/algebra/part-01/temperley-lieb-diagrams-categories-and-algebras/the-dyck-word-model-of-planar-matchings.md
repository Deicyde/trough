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
- [Source of `TauCeti.PlanarMatching.dyckWordEquiv` in TauCeti/Combinatorics/PlanarMatching/DyckWord.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/PlanarMatching/DyckWord.lean#L223)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
