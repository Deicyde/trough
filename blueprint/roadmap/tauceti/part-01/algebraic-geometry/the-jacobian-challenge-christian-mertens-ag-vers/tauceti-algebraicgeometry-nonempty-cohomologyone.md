---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.nonempty_cohomologyOneDualEquivCohomologyZero_differentials_tensor_dual
statement: formalized
proof: formalized
---

# TauCeti.AlgebraicGeometry.nonempty_cohomologyOneDualEquivCohomologyZero_differentials_tensor_dual

Over an exact constant field, the dual of `H¹(X, L)` is linearly equivalent to
`H⁰(X, Ω_{X/k} ⊗ L⁻¹)`, by the identification of the differential line bundle with the canonical
bundle. This asserts only the existence of a noncanonical linear equivalence, not a natural
duality pairing.

```lean
TauCeti.AlgebraicGeometry.nonempty_cohomologyOneDualEquivCohomologyZero_differentials_tensor_dual.{u}
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
  Nonempty
    (Module.Dual k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology L.obj 1) ≃ₗ[k]
      TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
        (TauCeti.AlgebraicGeometry.InvertibleSheaf.tensorProduct
            { obj := AlgebraicGeometry.Scheme.relativeDifferentials k X, property := ⋯ } L.dual).obj
        0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The abstract residue theorem (Stichtenoth, (1.45))](../../field-theory/function-field/part-01/the-abstract-residue-theorem-stichtenoth-1-45.md)
- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [Serre duality in degree zero](../other-results/serre-duality-in-degree-zero.md)
- [Stichtenoth's transformation formula](../../field-theory/function-field/part-02/stichtenoths-transformation-formula.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.nonempty_cohomologyOneDualEquivCohomologyZero_differentials_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Differentials/Canonical.html#TauCeti.AlgebraicGeometry.nonempty_cohomologyOneDualEquivCohomologyZero_differentials_tensor_dual).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.nonempty_cohomologyOneDualEquivCohomologyZero_differentials_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Differentials/Canonical.html#TauCeti.AlgebraicGeometry.nonempty_cohomologyOneDualEquivCohomologyZero_differentials_tensor_dual)
- [Source of `TauCeti.AlgebraicGeometry.nonempty_cohomologyOneDualEquivCohomologyZero_differentials_tensor_dual` in TauCeti/AlgebraicGeometry/Modules/Differentials/Canonical.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Modules/Differentials/Canonical.lean#L244)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/JacobianChallenge/STATUS.md)
