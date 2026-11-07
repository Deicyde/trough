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
- [Source of `TauCeti.puiseuxField.levelCoconeIsColimit` in TauCeti/RingTheory/LaurentSeries/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LaurentSeries/Colimit.lean#L159)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
