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
- [Source of `TauCeti.puiseuxField.levelCoconeIsColimit` in TauCeti/RingTheory/LaurentSeries/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/LaurentSeries/Colimit.lean#L159)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
