---
declaration: def
origin: cited
lean: TauCeti.ExactStructure.Ext1
statement: formalized
---

# TauCeti.ExactStructure.Ext1

`Ext¹_E(Z, X)`, the **Yoneda `Ext¹`** of the exact category: the set of Yoneda equivalence
classes of conflations `X ⟶ Y ⟶ Z` of `E`.

```lean
TauCeti.ExactStructure.Ext1.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasZeroObject C]
  [CategoryTheory.Limits.HasBinaryBiproducts C] (E : TauCeti.ExactStructure C) (Z X : C) :
  Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.Ext1`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/YonedaExt/Basic.html#TauCeti.ExactStructure.Ext1).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.Ext1`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/YonedaExt/Basic.html#TauCeti.ExactStructure.Ext1)
- [Source of `TauCeti.ExactStructure.Ext1` in TauCeti/CategoryTheory/Exact/YonedaExt/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Exact/YonedaExt/Basic.lean#L327)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RepresentationTheory/STATUS.md)
