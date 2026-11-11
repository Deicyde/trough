---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual
statement: formalized
proof: formalized
---

# The Riemann–Roch theorem for line bundles, in Serre-duality form

For every line bundle
`L` and every representative `ω` of the canonical class,

`dim H⁰(X, L) - dim H⁰(X, ω ⊗ L⁻¹) = deg L + 1 - g`,

where `deg L = χ(L) - χ(𝒪_X)` is the Euler-characteristic degree and `g = dim H¹(X, 𝒪_X)`. No
rational point is needed: it is the integral closedness of `k` in `k(X)` that makes
`H⁰(X, 𝒪_X)` one-dimensional.

```lean
TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual.{u}
  {k : Type u} [Field k] {X : AlgebraicGeometry.Scheme} [X.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.IsIntegral X] [AlgebraicGeometry.IsNoetherian X]
  [∀ (x : TauCeti.AlgebraicGeometry.CodimensionOnePoint X),
      IsDiscreteValuationRing ↑(X.presheaf.stalk ↑x)]
  [X.IsSeparated]
  (hex : AlgebraicGeometry.ValuativeCriterion.Existence (X ↘ AlgebraicGeometry.Spec ↧k))
  (hdim : ∀ (x : ↥X), Order.coheight x ≤ 1) (hF : TauCeti.IsFunctionField k ↑X.functionField)
  (hk : IsIntegrallyClosedIn k ↑X.functionField) (L ω : TauCeti.AlgebraicGeometry.InvertibleSheaf X)
  (hω :
    TauCeti.AlgebraicGeometry.LineBundleClass.mk ω =
      TauCeti.AlgebraicGeometry.LineBundleClass.mk
        (TauCeti.AlgebraicGeometry.InvertibleSheaf.canonicalBundle hex hdim hF hk)) :
  ↑(Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology L.obj 0)) -
      ↑(Module.finrank k
          (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology (ω.tensorProduct L.dual).obj 0)) =
    TauCeti.AlgebraicGeometry.InvertibleSheaf.eulerDegree k L + 1 -
      ↑(AlgebraicGeometry.Scheme.genus k X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Serre duality in degree zero](serre-duality-in-degree-zero.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.html#TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.html#TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual)
- [Source of `TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual` in TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.lean#L196)
