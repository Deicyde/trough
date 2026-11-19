---
declaration: theorem
origin: cited
lean: CategoryTheory.ShortComplex.ShortExact.extClass_baerSum
statement: formalized
proof: formalized
---

# CategoryTheory.ShortComplex.ShortExact.extClass_baerSum

The pullback and pushout Baer sum represents addition of the native extension
classes, in every abelian category with `HasExt`.

```lean
CategoryTheory.ShortComplex.ShortExact.extClass_baerSum.{w, v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [CategoryTheory.HasExt C]
  {S : CategoryTheory.ShortComplex C} (hS : S.ShortExact) {E : C} {i : S.X₁ ⟶ E} {p : E ⟶ S.X₃}
  {w : CategoryTheory.CategoryStruct.comp i p = 0}
  (hT : { X₁ := S.X₁, X₂ := E, X₃ := S.X₃, f := i, g := p, zero := w }.ShortExact) :
  ⋯.extClass = hS.extClass + hT.extClass
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.ShortComplex.ShortExact.extClass_baerSum`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Ext/BaerSum.html#CategoryTheory.ShortComplex.ShortExact.extClass_baerSum).

## Sources

- [Tau Ceti documentation: `CategoryTheory.ShortComplex.ShortExact.extClass_baerSum`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Ext/BaerSum.html#CategoryTheory.ShortComplex.ShortExact.extClass_baerSum)
- [Source of `CategoryTheory.ShortComplex.ShortExact.extClass_baerSum` in TauCeti/Algebra/Homology/Ext/BaerSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/Ext/BaerSum.lean#L135)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
