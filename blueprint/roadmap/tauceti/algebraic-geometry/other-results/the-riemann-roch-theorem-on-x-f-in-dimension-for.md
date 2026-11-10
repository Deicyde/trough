---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf, TauCeti.AlgebraicGeometry.twoChartModel.eulerCharBelow_sheaf_eq_degree_add_one_sub_genus
statement: formalized
proof: formalized
---

# The Riemann–Roch theorem on `X_F` in dimension form

when `k` is integrally closed in `F`,
`dim_k H⁰(X_F, 𝒪(D)) - dim_k H¹(X_F, 𝒪(D)) = deg D + 1 - g(F)`.

```lean
TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf.{u}
  {k F : Type u} [Field k] [Field F] [Algebra k F] {hF : TauCeti.IsFunctionField k F} {x : F}
  {hx : x ≠ 0} (hxt : Transcendental k x) (hk : IsIntegrallyClosedIn k F)
  (D :
    TauCeti.AlgebraicGeometry.SchemeWeilDivisor (TauCeti.AlgebraicGeometry.twoChartModel hF hx)) :
  ↑(Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology D.sheaf 0)) -
      ↑(Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology D.sheaf 1)) =
    TauCeti.Divisor.degree ((TauCeti.AlgebraicGeometry.twoChartModel.equivDivisor hxt) D) + 1 -
      ↑(TauCeti.genus k F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-01/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/riemanns-theorem.md)
- [TauCeti.Ring.IsJapanese](../../ring-theory/part-01/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.html#TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf).

## Other forms

**The Riemann–Roch theorem on `X_F` in Euler-characteristic form.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.twoChartModel.eulerCharBelow_sheaf_eq_degree_add_one_sub_genus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.html#TauCeti.AlgebraicGeometry.twoChartModel.eulerCharBelow_sheaf_eq_degree_add_one_sub_genus).

```lean
TauCeti.AlgebraicGeometry.twoChartModel.eulerCharBelow_sheaf_eq_degree_add_one_sub_genus.{u}
  {k F : Type u} [Field k] [Field F] [Algebra k F] {hF : TauCeti.IsFunctionField k F} {x : F}
  {hx : x ≠ 0} (hxt : Transcendental k x) (hk : IsIntegrallyClosedIn k F)
  (D :
    TauCeti.AlgebraicGeometry.SchemeWeilDivisor (TauCeti.AlgebraicGeometry.twoChartModel hF hx)) :
  AlgebraicGeometry.Scheme.Modules.eulerCharBelow k (TauCeti.AlgebraicGeometry.twoChartModel hF hx)
      D.sheaf 2 =
    TauCeti.Divisor.degree ((TauCeti.AlgebraicGeometry.twoChartModel.equivDivisor hxt) D) + 1 -
      ↑(TauCeti.genus k F)
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.html#TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf)
- [Source of `TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf` in TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.lean#L520)
