---
declaration: class
origin: cited
lean: TauCeti.IsKrullSchmidt
statement: formalized
---

# A Krull-Schmidt category

every object is isomorphic to a finite biproduct of objects with
local endomorphism rings.

```lean
TauCeti.IsKrullSchmidt.{v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasFiniteBiproducts C] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsKrullSchmidt`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Basic.html#TauCeti.IsKrullSchmidt).

## Sources

- [Tau Ceti documentation: `TauCeti.IsKrullSchmidt`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Basic.html#TauCeti.IsKrullSchmidt)
- [Source of `TauCeti.IsKrullSchmidt` in TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Basic.lean#L191)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RepresentationTheory/STATUS.md)
