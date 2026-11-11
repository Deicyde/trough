---
declaration: def
origin: cited
lean: TauCeti.puiseuxField.levelCoconeIsColimit
statement: formalized
---

# TauCeti.puiseuxField.levelCoconeIsColimit

The Puiseux field is the colimit of the ramified Laurent levels in `CommAlgCat K`.

Equivalently, every compatible family of `K`-algebra maps from the levels factors uniquely
through the bounded-denominator Puiseux series field.

```lean
TauCeti.puiseuxField.levelCoconeIsColimit.{u_1} {K : Type u_1} [Field K] :
  CategoryTheory.Limits.IsColimit (TauCeti.puiseuxField.levelCocone K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.puiseuxField.levelCoconeIsColimit`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Colimit.html#TauCeti.puiseuxField.levelCoconeIsColimit).

## Sources

- [Tau Ceti documentation: `TauCeti.puiseuxField.levelCoconeIsColimit`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Colimit.html#TauCeti.puiseuxField.levelCoconeIsColimit)
- [Source of `TauCeti.puiseuxField.levelCoconeIsColimit` in TauCeti/RingTheory/LaurentSeries/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/Colimit.lean#L159)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
