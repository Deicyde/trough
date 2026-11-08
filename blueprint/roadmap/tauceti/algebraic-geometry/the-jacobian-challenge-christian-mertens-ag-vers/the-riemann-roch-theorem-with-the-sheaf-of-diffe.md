---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual
statement: formalized
proof: formalized
---

# The Riemann–Roch theorem with the sheaf of differentials

Over an exact constant field,
every line bundle `L` satisfies

`dim H⁰(X, L) - dim H⁰(X, Ω_{X/k} ⊗ L⁻¹) = deg L + 1 - g`,

where `deg L = χ(L) - χ(𝒪_X)` is the Euler-characteristic degree and `g = dim H¹(X, 𝒪_X)`.

```lean
TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual.{u}
  {k : Type u} [Field k] {X : AlgebraicGeometry.Scheme} [X.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.IsIntegral X] [AlgebraicGeometry.IsNoetherian X] [X.IsSeparated]
  [∀ (y : TauCeti.AlgebraicGeometry.CodimensionOnePoint X),
      IsDiscreteValuationRing ↑(X.presheaf.stalk ↑y)]
  [TauCeti.AlgebraicGeometry.SheafOfModules.isInvertible X
      (AlgebraicGeometry.Scheme.relativeDifferentials k X)]
  (hF : TauCeti.IsFunctionField k ↑X.functionField) (hk : IsIntegrallyClosedIn k ↑X.functionField)
  (hdim : ∀ (y : ↥X), Order.coheight y ≤ 1)
  (hex : AlgebraicGeometry.ValuativeCriterion.Existence (X ↘ AlgebraicGeometry.Spec ↧k))
  (L : TauCeti.AlgebraicGeometry.InvertibleSheaf X) :
  ↑(Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology L.obj 0)) -
      ↑(Module.finrank k
          (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
            (TauCeti.AlgebraicGeometry.InvertibleSheaf.tensorProduct
                { obj := AlgebraicGeometry.Scheme.relativeDifferentials k X, property := ⋯ }
                L.dual).obj
            0)) =
    TauCeti.AlgebraicGeometry.InvertibleSheaf.eulerDegree k L + 1 -
      ↑(AlgebraicGeometry.Scheme.genus k X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The abstract residue theorem (Stichtenoth, (1.45))](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-abstract-residue-theorem-stichtenoth-1-45.md)
- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Riemann's theorem](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [The Riemann–Roch theorem for line bundles, in Serre-duality form](../other-results/the-riemann-roch-theorem-for-line-bundles-in-ser.md)
- [Stichtenoth's transformation formula](../../field-theory/function-field/part-01/stichtenoths-transformation-formula.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Differentials/Canonical.html#TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Differentials/Canonical.html#TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual)
- [Source of `TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual` in TauCeti/AlgebraicGeometry/Modules/Differentials/Canonical.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Modules/Differentials/Canonical.lean#L280)
