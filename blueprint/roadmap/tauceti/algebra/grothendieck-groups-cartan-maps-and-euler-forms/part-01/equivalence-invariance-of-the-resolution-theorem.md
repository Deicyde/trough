---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.IsResolving.mapEquiv_comp_resolutionEquiv
statement: formalized
proof: formalized
---

# Equivalence invariance of the resolution theorem

An exact equivalence identifying two
resolving properties intertwines both the ambient exact `K₀` equivalence and the equivalence of
the resolving subcategories with their resolution-theorem comparisons.

```lean
TauCeti.ExactStructure.IsResolving.mapEquiv_comp_resolutionEquiv.{w, w', v, v', u, u'} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  {E : TauCeti.ExactStructure C} {P : CategoryTheory.ObjectProperty C} [E.IsResolving P]
  [CategoryTheory.EssentiallySmall.{w, v, u} C] {D : Type u'} [CategoryTheory.Category.{v', u'} D]
  [CategoryTheory.Preadditive D] [CategoryTheory.Limits.HasZeroObject D]
  [CategoryTheory.Limits.HasBinaryBiproducts D] [CategoryTheory.EssentiallySmall.{w', v', u'} D]
  {E' : TauCeti.ExactStructure D} {P' : CategoryTheory.ObjectProperty D} [E'.IsResolving P']
  (e : C ≌ D) [e.functor.Additive] [e.inverse.Additive] (hF : E.IsConflationExact E' e.functor)
  (hG : E'.IsConflationExact E e.inverse) (h : P'.inverseImage e.functor = P) :
  (TauCeti.ExactK0.mapEquiv e hF hG).toAddMonoidHom.comp
      (TauCeti.ExactStructure.IsResolving.resolutionEquiv E P).toAddMonoidHom =
    (TauCeti.ExactStructure.IsResolving.resolutionEquiv E' P').toAddMonoidHom.comp
      (TauCeti.ExactK0.mapEquiv (e.congrFullSubcategory h) ⋯ ⋯).toAddMonoidHom
```

## Depends on

- [The resolution theorem](the-resolution-theorem.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.IsResolving.mapEquiv_comp_resolutionEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Resolving.html#TauCeti.ExactStructure.IsResolving.mapEquiv_comp_resolutionEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.IsResolving.mapEquiv_comp_resolutionEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Resolving.html#TauCeti.ExactStructure.IsResolving.mapEquiv_comp_resolutionEquiv)
- [Source of `TauCeti.ExactStructure.IsResolving.mapEquiv_comp_resolutionEquiv` in TauCeti/CategoryTheory/GrothendieckGroup/Resolving.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/GrothendieckGroup/Resolving.lean#L400)
