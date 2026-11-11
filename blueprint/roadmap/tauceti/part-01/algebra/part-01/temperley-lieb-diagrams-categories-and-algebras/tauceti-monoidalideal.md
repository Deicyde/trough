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
- [Source of `TauCeti.MonoidalIdeal` in TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.lean#L72)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
