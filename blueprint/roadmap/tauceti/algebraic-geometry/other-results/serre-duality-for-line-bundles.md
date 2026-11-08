---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual
statement: formalized
proof: formalized
---

# Serre duality for line bundles

The dual of `H¹(X, L)` is linearly isomorphic to
`H⁰(X, ω ⊗ L⁻¹)` for any representative `ω` of the canonical line-bundle class.
The existence statement does not select a canonical pairing.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The duality theorem, in dimensions](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-duality-theorem-in-dimensions.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.html#TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.html#TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual)
- [Source of `TauCeti.AlgebraicGeometry.InvertibleSheaf.nonempty_cohomologyOneDualEquivCohomologyZero_tensor_dual` in TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.lean#L102)
