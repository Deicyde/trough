---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree_add_one_sub_genus_le_finrank_cohomology_zero_sheaf
statement: formalized
proof: formalized
---

# Riemann's inequality

On a proper integral curve over a field `k` whose codimension-one
local rings are discrete valuation rings, with all global functions constant and with
`H¹(X, 𝒪_X)` finite-dimensional, `dim_k H⁰(X, 𝒪_X(D)) ≥ deg D + 1 - g`.

```lean
TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree_add_one_sub_genus_le_finrank_cohomology_zero_sheaf.{u}
  {X : AlgebraicGeometry.Scheme} [AlgebraicGeometry.IsIntegral X]
  [∀ (y : TauCeti.AlgebraicGeometry.CodimensionOnePoint X),
      IsDiscreteValuationRing ↑(X.presheaf.stalk ↑y)]
  (k : Type u) [Field k] [X.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.IsProper (X ↘ AlgebraicGeometry.Spec ↧k)]
  [FiniteDimensional k
      (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
        (TauCeti.AlgebraicGeometry.InvertibleSheaf.trivial X).obj 1)]
  (hX : ∀ (y : ↥X), Order.coheight y ≤ 1)
  (hφ : Function.Surjective ⇑(AlgebraicGeometry.Scheme.Modules.baseRingToGlobalSections k X))
  (D : TauCeti.AlgebraicGeometry.SchemeWeilDivisor X) :
  (TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree (X ↘ AlgebraicGeometry.Spec ↧k)) D +
        1 -
      ↑(AlgebraicGeometry.Scheme.genus k X) ≤
    ↑(Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology D.sheaf 0))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree_add_one_sub_genus_le_finrank_cohomology_zero_sheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree_add_one_sub_genus_le_finrank_cohomology_zero_sheaf).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree_add_one_sub_genus_le_finrank_cohomology_zero_sheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree_add_one_sub_genus_le_finrank_cohomology_zero_sheaf)
- [Source of `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree_add_one_sub_genus_le_finrank_cohomology_zero_sheaf` in TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.lean#L157)
