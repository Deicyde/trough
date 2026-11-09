---
declaration: def
origin: cited
lean: TauCeti.ExactStructure.IsResolving.resolutionEquiv
statement: formalized
---

# The resolution theorem

For a resolving property `P` of an exact category, the inclusion
of the full subcategory on `P` induces an isomorphism of exact Grothendieck groups. Its inverse
sends the class of an object to the alternating class of any finite `P`-resolution of it, by
`TauCeti.ExactStructure.IsResolving.resolutionEquiv_symm_of`.

```lean
TauCeti.ExactStructure.IsResolving.resolutionEquiv.{w, v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  (E : TauCeti.ExactStructure C) (P : CategoryTheory.ObjectProperty C) [E.IsResolving P]
  [CategoryTheory.EssentiallySmall.{w, v, u} C] :
  TauCeti.ExactK0 (E.resolvingSubcategory P) ≃+ TauCeti.ExactK0 E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.IsResolving.resolutionEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Resolving.html#TauCeti.ExactStructure.IsResolving.resolutionEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.IsResolving.resolutionEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Resolving.html#TauCeti.ExactStructure.IsResolving.resolutionEquiv)
- [Source of `TauCeti.ExactStructure.IsResolving.resolutionEquiv` in TauCeti/CategoryTheory/GrothendieckGroup/Resolving.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/GrothendieckGroup/Resolving.lean#L304)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
