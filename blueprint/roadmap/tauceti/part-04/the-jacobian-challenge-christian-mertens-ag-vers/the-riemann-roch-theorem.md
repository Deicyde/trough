---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus
statement: formalized
proof: formalized
---

# The Riemann–Roch theorem

On a proper integral curve over a field `k` whose
codimension-one local rings are discrete valuation rings, with a `k`-rational point and with
`H¹(X, 𝒪_X)` finite-dimensional, every Weil divisor `D` satisfies

`χ(𝒪_X(D)) = deg D + 1 - g`,

where `χ(M) = dim H⁰(X, M) - dim H¹(X, M)`, `deg D = Σ_y D(y) [κ(y) : k]` and `g` is the
genus.

```lean
TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus.{u}
  {X : AlgebraicGeometry.Scheme} [AlgebraicGeometry.IsIntegral X]
  [∀ (y : TauCeti.AlgebraicGeometry.CodimensionOnePoint X),
      IsDiscreteValuationRing ↑(X.presheaf.stalk ↑y)]
  (k : Type u) [Field k] [X.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.IsProper (X ↘ AlgebraicGeometry.Spec ↧k)]
  [FiniteDimensional k
      (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
        (TauCeti.AlgebraicGeometry.InvertibleSheaf.trivial X).obj 1)]
  (hX : ∀ (y : ↥X), Order.coheight y ≤ 1) {s : AlgebraicGeometry.Spec ↧k ⟶ X}
  (hs :
    CategoryTheory.CategoryStruct.comp s (X ↘ AlgebraicGeometry.Spec ↧k) =
      CategoryTheory.CategoryStruct.id (AlgebraicGeometry.Spec ↧k))
  (D : TauCeti.AlgebraicGeometry.SchemeWeilDivisor X) :
  AlgebraicGeometry.Scheme.Modules.eulerCharBelow k X D.sheaf 2 =
    (TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree (X ↘ AlgebraicGeometry.Spec ↧k)) D +
        1 -
      ↑(AlgebraicGeometry.Scheme.genus k X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus)
- [Source of `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus` in TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.lean#L121)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/JacobianChallenge/STATUS.md)
