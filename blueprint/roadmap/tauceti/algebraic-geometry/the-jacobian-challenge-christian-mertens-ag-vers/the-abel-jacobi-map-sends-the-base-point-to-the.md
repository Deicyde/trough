---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.abelJacobiMap_app_basePoint
statement: formalized
proof: formalized
---

# The Abel–Jacobi map sends the base point to the identity

`𝒪(x₀_T - x₀_T) = 𝒪`.

```lean
TauCeti.AlgebraicGeometry.abelJacobiMap_app_basePoint.{u} {S X : AlgebraicGeometry.Scheme}
  (f : X ⟶ S) [AlgebraicGeometry.IsSeparated f] [AlgebraicGeometry.SmoothOfRelativeDimension 1 f]
  {x₀ : S ⟶ X} (hx₀ : CategoryTheory.CategoryStruct.comp x₀ f = CategoryTheory.CategoryStruct.id S)
  (T : (CategoryTheory.Over S)ᵒᵖ) :
  (CategoryTheory.ConcreteCategory.hom ((TauCeti.AlgebraicGeometry.abelJacobiMap f hx₀).app T))
      { down := TauCeti.AlgebraicGeometry.basePoint hx₀ (Opposite.unop T) } =
    1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.abelJacobiMap_app_basePoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Jacobi.html#TauCeti.AlgebraicGeometry.abelJacobiMap_app_basePoint).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.abelJacobiMap_app_basePoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Jacobi.html#TauCeti.AlgebraicGeometry.abelJacobiMap_app_basePoint)
- [Source of `TauCeti.AlgebraicGeometry.abelJacobiMap_app_basePoint` in TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Jacobi.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Jacobi.lean#L109)
