---
declaration: def
origin: cited
lean: TauCeti.GradedExactStructure.laurentResolutionEquiv, TauCeti.GradedExactStructure.IsResolving.laurentResolutionEquiv
statement: formalized
---

# The graded resolution theorem

Let `P` be a class of `E`-projectives containing a zero
object, closed under binary biproducts, and stable under the grading shift. Then the inclusion of
`P` into the objects of finite `P`-dimension induces an isomorphism of graded Grothendieck groups
as `ℤ[q,q⁻¹]`-modules. Its inverse sends the class of an object to its Euler class, by
`TauCeti.GradedExactStructure.laurentResolutionEquiv_symm_of`.

```lean
TauCeti.GradedExactStructure.laurentResolutionEquiv.{w, v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  (E : TauCeti.GradedExactStructure C) [CategoryTheory.LocallySmall.{w, v, u} C]
  {P : CategoryTheory.ObjectProperty C} [CategoryTheory.ObjectProperty.EssentiallySmall.{w, v, u} P]
  [P.ContainsZero] [P.IsClosedUnderBinaryProducts]
  [CategoryTheory.ObjectProperty.EssentiallySmall.{w, v, u} (E.admitsFiniteResolution P)]
  (hproj : P ≤ E.isProjective) (hshift : P.inverseImage E.shift.functor = P) :
  TauCeti.LaurentK0 (E.fullSubcategory P ⋯ hshift) ≃ₗ[LaurentPolynomial ℤ]
    TauCeti.LaurentK0 (E.fullSubcategory (E.admitsFiniteResolution P) ⋯ ⋯)
```

## Depends on

- [The resolution theorem](../../algebra/grothendieck-groups-cartan-maps-and-euler-forms/the-resolution-theorem.md)
- [The resolution theorem for finite projective resolutions](the-resolution-theorem-for-finite-projective-res.md)

## Proof depends on

- [The dual Noether isomorphism](../exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GradedExactStructure.laurentResolutionEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Laurent/Resolution.html#TauCeti.GradedExactStructure.laurentResolutionEquiv).

## Other forms

**The graded resolution theorem for a resolving subcategory.** Formalized in Tau Ceti as [`TauCeti.GradedExactStructure.IsResolving.laurentResolutionEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Laurent/Resolving/Basic.html#TauCeti.GradedExactStructure.IsResolving.laurentResolutionEquiv).

```lean
TauCeti.GradedExactStructure.IsResolving.laurentResolutionEquiv.{w, v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  [CategoryTheory.EssentiallySmall.{w, v, u} C] (E : TauCeti.GradedExactStructure C)
  (P : CategoryTheory.ObjectProperty C) [E.IsResolving P]
  (hshift : P.inverseImage E.shift.functor = P) :
  TauCeti.LaurentK0 (E.fullSubcategory P ⋯ hshift) ≃ₗ[LaurentPolynomial ℤ] TauCeti.LaurentK0 E
```

## Sources

- [Tau Ceti documentation: `TauCeti.GradedExactStructure.laurentResolutionEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Laurent/Resolution.html#TauCeti.GradedExactStructure.laurentResolutionEquiv)
- [Source of `TauCeti.GradedExactStructure.laurentResolutionEquiv` in TauCeti/CategoryTheory/GrothendieckGroup/Laurent/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/GrothendieckGroup/Laurent/Resolution.lean#L118)
