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
- [Source of `TauCeti.IsKrullSchmidt` in TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Basic.lean#L188)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RepresentationTheory/STATUS.md)
