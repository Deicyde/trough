---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.abelJacobiMap_app_injective_of_genus_pos
statement: formalized
proof: formalized
---

# The Abel–Jacobi map of a curve of positive genus separates points over every field extension

Let `X` be a smooth proper geometrically connected curve of genus `g ≥ 1` over a
field `k`, with a rational point `x₀`. For every field extension `K / k`, two `K`-points of `X`
with the same class `𝒪(Γₓ - x₀)` in `Pic(X_K) / Pic(Spec K)` are equal. Taking `K`
algebraically closed, the Abel–Jacobi map is injective on geometric points.

```lean
TauCeti.AlgebraicGeometry.abelJacobiMap_app_injective_of_genus_pos.{u} {k : Type u} [Field k]
  {X : AlgebraicGeometry.Scheme} [X.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.IsProper (X ↘ AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.SmoothOfRelativeDimension 1 (X ↘ AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.GeometricallyConnected (X ↘ AlgebraicGeometry.Spec ↧k)]
  {x₀ : AlgebraicGeometry.Spec ↧k ⟶ X}
  (hx₀ :
    CategoryTheory.CategoryStruct.comp x₀ (X ↘ AlgebraicGeometry.Spec ↧k) =
      CategoryTheory.CategoryStruct.id (AlgebraicGeometry.Spec ↧k))
  (hg : 0 < AlgebraicGeometry.Scheme.genus k X) (K : Type u) [Field K] [Algebra k K] :
  Function.Injective
    ⇑(CategoryTheory.ConcreteCategory.hom
        ((TauCeti.AlgebraicGeometry.abelJacobiMap (X ↘ AlgebraicGeometry.Spec ↧k) hx₀).app
          (Opposite.op
            (CategoryTheory.Over.mk
              (AlgebraicGeometry.Spec.map (CommRingCat.ofHom (algebraMap k K)))))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [Serre's vanishing theorem on affine opens](../other-results/serres-vanishing-theorem-on-affine-opens.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)
- [Weierstrass gap theorem (Stichtenoth, Theorem 1.6.8)](../../field-theory/function-field/part-02/weierstrass-gap-theorem-stichtenoth-theorem-1-6.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.abelJacobiMap_app_injective_of_genus_pos`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/PointSeparation.html#TauCeti.AlgebraicGeometry.abelJacobiMap_app_injective_of_genus_pos).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.abelJacobiMap_app_injective_of_genus_pos`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/PointSeparation.html#TauCeti.AlgebraicGeometry.abelJacobiMap_app_injective_of_genus_pos)
- [Source of `TauCeti.AlgebraicGeometry.abelJacobiMap_app_injective_of_genus_pos` in TauCeti/AlgebraicGeometry/PicardFunctor/Abel/PointSeparation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/PointSeparation.lean#L108)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/JacobianChallenge/STATUS.md)
