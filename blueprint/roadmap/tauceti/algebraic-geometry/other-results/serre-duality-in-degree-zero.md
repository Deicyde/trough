---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyZeroDualEquivCohomologyOne_tensor_dual, TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual
statement: formalized
proof: formalized
---

# Serre duality in degree zero

The dual of `H⁰(X, L)` is linearly isomorphic to
`H¹(X, ω ⊗ L⁻¹)` for any representative `ω` of the canonical class.

```lean
TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyZeroDualEquivCohomologyOne_tensor_dual.{u}
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
  Nonempty
    (Module.Dual k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology L.obj 0) ≃ₗ[k]
      TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology (ω.tensorProduct L.dual).obj 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The duality theorem, in dimensions](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-duality-theorem-in-dimensions.md)
- [Riemann's theorem](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/riemanns-theorem.md)
- [The weak approximation theorem](../../field-theory/function-field/part-01/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyZeroDualEquivCohomologyOne_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.html#TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyZeroDualEquivCohomologyOne_tensor_dual).

## Other forms

**Serre duality for line bundles.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.html#TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual).

```lean
TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual.{u}
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
  Nonempty
    (Module.Dual k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology L.obj 1) ≃ₗ[k]
      TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology (ω.tensorProduct L.dual).obj 0)
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyZeroDualEquivCohomologyOne_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.html#TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyZeroDualEquivCohomologyOne_tensor_dual)
- [Source of `TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyZeroDualEquivCohomologyOne_tensor_dual` in TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.lean#L135)
