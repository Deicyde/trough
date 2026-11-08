---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.abelJacobiMapOfDegree_app_pow_basePoint
statement: formalized
proof: formalized
---

# The Abel–Jacobi map of degree `d` sends `d • x₀_T` to the identity

`𝒪(d • x₀_T - d • x₀_T) = 𝒪`.

```lean
TauCeti.AlgebraicGeometry.abelJacobiMapOfDegree_app_pow_basePoint.{u}
  {S X : AlgebraicGeometry.Scheme} (f : X ⟶ S) [AlgebraicGeometry.IsProper f]
  [TauCeti.AlgebraicGeometry.RelativeDimensionLE 1 f]
  [AlgebraicGeometry.SmoothOfRelativeDimension 1 f] {x₀ : S ⟶ X}
  (hx₀ : CategoryTheory.CategoryStruct.comp x₀ f = CategoryTheory.CategoryStruct.id S) (d : ℕ)
  (T : (CategoryTheory.Over S)ᵒᵖ) :
  (CategoryTheory.ConcreteCategory.hom
        ((TauCeti.AlgebraicGeometry.abelJacobiMapOfDegree f hx₀ d).app T))
      {
        down :=
          ⟨(CategoryTheory.ConcreteCategory.hom ((TauCeti.AlgebraicGeometry.graphDivisor f).app T))
                (TauCeti.AlgebraicGeometry.basePoint hx₀ (Opposite.unop T)) ^
              d,
            ⋯⟩ } =
    1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.abelJacobiMapOfDegree_app_pow_basePoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Degree.html#TauCeti.AlgebraicGeometry.abelJacobiMapOfDegree_app_pow_basePoint).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.abelJacobiMapOfDegree_app_pow_basePoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Degree.html#TauCeti.AlgebraicGeometry.abelJacobiMapOfDegree_app_pow_basePoint)
- [Source of `TauCeti.AlgebraicGeometry.abelJacobiMapOfDegree_app_pow_basePoint` in TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Degree.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Degree.lean#L171)
