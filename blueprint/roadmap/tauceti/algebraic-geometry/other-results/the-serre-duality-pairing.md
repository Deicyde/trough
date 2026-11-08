---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.SchemeWeilDivisor.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne, TauCeti.AlgebraicGeometry.twoChartModel.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne, TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub
statement: formalized
proof: formalized
---

# The Serre duality pairing

Under `SchemeWeilDivisor.cohomologyOneDualEquivCohomologyZero`,
a section `s` of `𝒪_X(K - D)`, with underlying rational function `f`, is the linear form on
`H¹(X, 𝒪_X(D))` sending the class of a repartition `a` to `ω(f · a)`.

Not `@[simp]`: `SchemeWeilDivisor.repartitionToCohomologyOne_apply` already rewrites the class of a
repartition on the left-hand side, so this rule would not be in simp-normal form.

```lean
TauCeti.AlgebraicGeometry.SchemeWeilDivisor.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne.{u}
  {k : Type u} [Field k] {X : AlgebraicGeometry.Scheme} [X.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.IsIntegral X]
  [∀ (x : TauCeti.AlgebraicGeometry.CodimensionOnePoint X),
      IsDiscreteValuationRing ↑(X.presheaf.stalk ↑x)]
  [X.IsSeparated]
  (hex : AlgebraicGeometry.ValuativeCriterion.Existence (X ↘ AlgebraicGeometry.Spec ↧k))
  (hdim : ∀ (x : ↥X), Order.coheight x ≤ 1) [AlgebraicGeometry.IsNoetherian X]
  (hF : TauCeti.IsFunctionField k ↑X.functionField) (hk : IsIntegrallyClosedIn k ↑X.functionField)
  {ω : Module.Dual k ↥(TauCeti.repartitionSpace k ↑X.functionField)} (hω : ω ≠ 0)
  {K : TauCeti.AlgebraicGeometry.SchemeWeilDivisor X}
  (hK :
    IsGreatest {E | ω ∈ TauCeti.weilDifferentialFiltration E}
      ((TauCeti.AlgebraicGeometry.SchemeWeilDivisor.equivFunctionFieldDivisor hex hdim) K))
  (D : TauCeti.AlgebraicGeometry.SchemeWeilDivisor X)
  (s : TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology (K - D).sheaf 0)
  (a : ↥(TauCeti.repartitionSpace k ↑X.functionField)) :
  ((TauCeti.AlgebraicGeometry.SchemeWeilDivisor.cohomologyOneDualEquivCohomologyZero hex hdim hF hk
            hω hK D).symm
        s)
      ((TauCeti.AlgebraicGeometry.SchemeWeilDivisor.repartitionToCohomologyOne hex hdim D) a) =
    ω
      (((TauCeti.repartitionMul hF)
          ((TauCeti.AlgebraicGeometry.Scheme.rationalFunctionsEquiv ⊤)
            ((CategoryTheory.ConcreteCategory.hom
                (AlgebraicGeometry.Scheme.Modules.Hom.app (K - D).sheafι ⊤))
              ((TauCeti.AlgebraicGeometry.Scheme.Modules.cohomologyZeroEquiv (K - D).sheaf) s))))
        a)
```

## Depends on

- [The duality theorem, in dimensions](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-duality-theorem-in-dimensions.md)

## Proof depends on

- [Krull–Akizuki's length bound](../../ring-theory/other-results/part-01/krull-akizukis-length-bound.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [TauCeti.Ring.IsJapanese](../../ring-theory/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.SchemeWeilDivisor.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/SerreDuality.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne).

## Other forms

**The Serre duality pairing on `X_F` in terms of `F`.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.twoChartModel.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.html#TauCeti.AlgebraicGeometry.twoChartModel.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne).

```lean
TauCeti.AlgebraicGeometry.twoChartModel.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne.{u}
  {k F : Type u} [Field k] [Field F] [Algebra k F] {hF : TauCeti.IsFunctionField k F} {x : F}
  {hx : x ≠ 0} (hxt : Transcendental k x) (hk : IsIntegrallyClosedIn k F)
  {ω : Module.Dual k ↥(TauCeti.repartitionSpace k F)} (hω : ω ≠ 0)
  {K : TauCeti.AlgebraicGeometry.SchemeWeilDivisor (TauCeti.AlgebraicGeometry.twoChartModel hF hx)}
  (hK :
    IsGreatest {E | ω ∈ TauCeti.weilDifferentialFiltration E}
      ((TauCeti.AlgebraicGeometry.twoChartModel.equivDivisor hxt) K))
  (D : TauCeti.AlgebraicGeometry.SchemeWeilDivisor (TauCeti.AlgebraicGeometry.twoChartModel hF hx))
  (s : TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology (K - D).sheaf 0)
  (a : ↥(TauCeti.repartitionSpace k F)) :
  ((TauCeti.AlgebraicGeometry.twoChartModel.cohomologyOneDualEquivCohomologyZero hxt hk hω hK
            D).symm
        s)
      ((TauCeti.AlgebraicGeometry.twoChartModel.repartitionToCohomologyOne hxt D) a) =
    ω
      (((TauCeti.repartitionMul hF)
          ↑((TauCeti.AlgebraicGeometry.twoChartModel.cohomologyZeroEquivRiemannRochSpace hxt
                (K - D))
              s))
        a)
```

**Serre duality, in dimensions.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/SerreDuality.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub).

```lean
TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub.{u}
  {k : Type u} [Field k] {X : AlgebraicGeometry.Scheme} [X.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.IsIntegral X]
  [∀ (x : TauCeti.AlgebraicGeometry.CodimensionOnePoint X),
      IsDiscreteValuationRing ↑(X.presheaf.stalk ↑x)]
  [X.IsSeparated]
  (hex : AlgebraicGeometry.ValuativeCriterion.Existence (X ↘ AlgebraicGeometry.Spec ↧k))
  (hdim : ∀ (x : ↥X), Order.coheight x ≤ 1) [AlgebraicGeometry.IsNoetherian X]
  (hF : TauCeti.IsFunctionField k ↑X.functionField) (hk : IsIntegrallyClosedIn k ↑X.functionField)
  {K : TauCeti.AlgebraicGeometry.SchemeWeilDivisor X}
  (hK :
    (TauCeti.Place.orderSystem hF).divisorClass
        ((TauCeti.AlgebraicGeometry.SchemeWeilDivisor.equivFunctionFieldDivisor hex hdim) K) =
      TauCeti.canonicalClass hF hk)
  (D : TauCeti.AlgebraicGeometry.SchemeWeilDivisor X) :
  Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology D.sheaf 1) =
    Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology (K - D).sheaf 0)
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/SerreDuality.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne)
- [Source of `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.cohomologyOneDualEquivCohomologyZero_symm_apply_repartitionToCohomologyOne` in TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/SerreDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/SerreDuality.lean#L131)
