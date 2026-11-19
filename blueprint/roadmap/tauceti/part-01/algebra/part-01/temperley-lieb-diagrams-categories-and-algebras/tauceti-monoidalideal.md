---
declaration: structure
origin: cited
lean: TauCeti.MonoidalIdeal
statement: formalized
---

# TauCeti.MonoidalIdeal

A **tensor ideal** of a monoidal preadditive category `C`: a two-sided morphism ideal which
is closed under whiskering by arbitrary objects on either side.

```lean
TauCeti.MonoidalIdeal.{v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.MonoidalCategory C] : Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MonoidalIdeal`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.html#TauCeti.MonoidalIdeal).

## Sources

- [Tau Ceti documentation: `TauCeti.MonoidalIdeal`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.html#TauCeti.MonoidalIdeal)
- [Source of `TauCeti.MonoidalIdeal` in TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.lean#L72)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TemperleyLieb/STATUS.md)
