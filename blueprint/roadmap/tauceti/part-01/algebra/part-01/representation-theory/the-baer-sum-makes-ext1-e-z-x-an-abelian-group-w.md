---
declaration: instance
origin: cited
lean: TauCeti.ExactStructure.Ext1.instAddCommGroup
statement: formalized
---

# The Baer sum makes `Ext¹_E(Z, X)` an abelian group, with the class of the split conflation as zero

The multiples of a class are its cobase changes along the multiples of `𝟙 X`, so that the
`ℕ`- and `ℤ`-module structures agree definitionally with those of an `R`-linear category.

```lean
TauCeti.ExactStructure.Ext1.instAddCommGroup.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasZeroObject C]
  [CategoryTheory.Limits.HasBinaryBiproducts C] {E : TauCeti.ExactStructure C} {X Z : C} :
  AddCommGroup (E.Ext1 Z X)
```

## Depends on

- [TauCeti.ExactStructure.Ext1](tauceti-exactstructure-ext1.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.Ext1.instAddCommGroup`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/YonedaExt/BaerSum.html#TauCeti.ExactStructure.Ext1.instAddCommGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.Ext1.instAddCommGroup`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/YonedaExt/BaerSum.html#TauCeti.ExactStructure.Ext1.instAddCommGroup)
- [Source of `TauCeti.ExactStructure.Ext1.instAddCommGroup` in TauCeti/CategoryTheory/Exact/YonedaExt/BaerSum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Exact/YonedaExt/BaerSum.lean#L290)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RepresentationTheory/STATUS.md)
