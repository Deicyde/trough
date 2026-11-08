---
declaration: def
origin: cited
lean: TauCeti.ExactStructure.resolutionEquiv
statement: formalized
---

# The resolution theorem for finite projective resolutions

When every object satisfying
`P` is `E`-projective, the inclusion of the full subcategory on `P` into the full subcategory of
objects admitting a finite `P`-resolution induces an isomorphism of exact Grothendieck groups.
Its inverse sends the class of an object to the alternating class of any finite `P`-resolution of
it, by `TauCeti.ExactStructure.resolutionEquiv_symm_of`.

```lean
TauCeti.ExactStructure.resolutionEquiv.{w, v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasZeroObject C]
  [CategoryTheory.Limits.HasBinaryBiproducts C] [CategoryTheory.LocallySmall.{w, v, u} C]
  {E : TauCeti.ExactStructure C} {P : CategoryTheory.ObjectProperty C}
  [CategoryTheory.ObjectProperty.EssentiallySmall.{w, v, u} P] [P.ContainsZero]
  [P.IsClosedUnderBinaryProducts] (hproj : P ≤ E.isProjective)
  [CategoryTheory.ObjectProperty.EssentiallySmall.{w, v, u} (E.admitsFiniteResolution P)] :
  TauCeti.ExactK0 (TauCeti.ExactStructure.fullSubcategory P ⋯) ≃+
    TauCeti.ExactK0 (TauCeti.ExactStructure.fullSubcategory (E.admitsFiniteResolution P) ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [Schanuel's lemma](../../../category-theory/exact/schanuels-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.resolutionEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/ProjectiveResolution.html#TauCeti.ExactStructure.resolutionEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.resolutionEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/ProjectiveResolution.html#TauCeti.ExactStructure.resolutionEquiv)
- [Source of `TauCeti.ExactStructure.resolutionEquiv` in TauCeti/CategoryTheory/GrothendieckGroup/ProjectiveResolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/GrothendieckGroup/ProjectiveResolution.lean#L375)
