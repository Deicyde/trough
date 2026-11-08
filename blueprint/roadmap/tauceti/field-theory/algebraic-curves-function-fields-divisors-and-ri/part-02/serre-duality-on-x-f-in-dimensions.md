---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub
statement: formalized
proof: formalized
---

# Serre duality on `X_F`, in dimensions

for every divisor `K` on `X_F` whose image in `F`
represents `canonicalClass hF hk`, `dim_k H¹(X_F, 𝒪(D)) = dim_k H⁰(X_F, 𝒪(K - D))`.

```lean
TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub.{u}
  {k F : Type u} [Field k] [Field F] [Algebra k F] {hF : TauCeti.IsFunctionField k F} {x : F}
  {hx : x ≠ 0} (hxt : Transcendental k x) (hk : IsIntegrallyClosedIn k F)
  {K : TauCeti.AlgebraicGeometry.SchemeWeilDivisor (TauCeti.AlgebraicGeometry.twoChartModel hF hx)}
  (hK :
    (TauCeti.Place.orderSystem hF).divisorClass
        ((TauCeti.AlgebraicGeometry.twoChartModel.equivDivisor hxt) K) =
      TauCeti.canonicalClass hF hk)
  (D :
    TauCeti.AlgebraicGeometry.SchemeWeilDivisor (TauCeti.AlgebraicGeometry.twoChartModel hF hx)) :
  Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology D.sheaf 1) =
    Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology (K - D).sheaf 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Krull–Akizuki's length bound](../../../ring-theory/other-results/part-01/krull-akizukis-length-bound.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [The Serre duality pairing](../../../algebraic-geometry/other-results/the-serre-duality-pairing.md)
- [TauCeti.Ring.IsJapanese](../../../ring-theory/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.html#TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.html#TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub)
- [Source of `TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub` in TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.lean#L404)
