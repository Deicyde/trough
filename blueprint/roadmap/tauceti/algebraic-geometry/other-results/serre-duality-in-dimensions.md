---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub
statement: formalized
proof: formalized
---

# Serre duality, in dimensions

Assume `k` is integrally closed in `k(X)`. For every
canonical divisor `K` on the curve `X` (a divisor whose function-field divisor represents the
canonical class) and every Weil divisor `D`,
`dim_k H¹(X, 𝒪_X(D)) = dim_k H⁰(X, 𝒪_X(K - D))`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The duality theorem, in dimensions](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-duality-theorem-in-dimensions.md)
- [Riemann's theorem](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/riemanns-theorem.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/SerreDuality.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/SerreDuality.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub)
- [Source of `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_one_sheaf_eq_finrank_cohomology_zero_sheaf_sub` in TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/SerreDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/SerreDuality.lean#L196)
