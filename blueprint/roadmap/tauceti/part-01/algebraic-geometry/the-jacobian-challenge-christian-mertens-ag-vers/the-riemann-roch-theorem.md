---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus, TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_zero_sheaf_eq_relativeDegree_of_genus_eq_one, TauCeti.AlgebraicGeometry.InvertibleSheaf.eulerCharBelow_eq_relativeDegree_add_one_sub_genus, TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf
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

## Proof depends on

- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus).

## Other forms

**Riemann–Roch on a curve of genus one.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_zero_sheaf_eq_relativeDegree_of_genus_eq_one`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/GenusOne.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_zero_sheaf_eq_relativeDegree_of_genus_eq_one).

```lean
TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_zero_sheaf_eq_relativeDegree_of_genus_eq_one.{u}
  (k : Type u) [Field k] {X : AlgebraicGeometry.Scheme} [AlgebraicGeometry.IsIntegral X]
  [AlgebraicGeometry.IsNoetherian X]
  [∀ (y : TauCeti.AlgebraicGeometry.CodimensionOnePoint X),
      IsDiscreteValuationRing ↑(X.presheaf.stalk ↑y)]
  [hX : Fact (∀ (y : ↥X), Order.coheight y ≤ 1)] [X.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.IsProper (X ↘ AlgebraicGeometry.Spec ↧k)]
  [FiniteDimensional k
      (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
        (TauCeti.AlgebraicGeometry.InvertibleSheaf.trivial X).obj 1)]
  (hk : IsIntegrallyClosedIn k ↑X.functionField) (hg : AlgebraicGeometry.Scheme.genus k X = 1)
  {D : TauCeti.AlgebraicGeometry.SchemeWeilDivisor X}
  (hD :
    0 <
      (TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree (X ↘ AlgebraicGeometry.Spec ↧k))
        D) :
  ↑(Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology D.sheaf 0)) =
    (TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree (X ↘ AlgebraicGeometry.Spec ↧k)) D
```

**The Riemann–Roch theorem for a line bundle.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.InvertibleSheaf.eulerCharBelow_eq_relativeDegree_add_one_sub_genus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.html#TauCeti.AlgebraicGeometry.InvertibleSheaf.eulerCharBelow_eq_relativeDegree_add_one_sub_genus).

```lean
TauCeti.AlgebraicGeometry.InvertibleSheaf.eulerCharBelow_eq_relativeDegree_add_one_sub_genus.{u}
  {X : AlgebraicGeometry.Scheme} [AlgebraicGeometry.IsIntegral X]
  [AlgebraicGeometry.IsLocallyNoetherian X]
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
  {L : TauCeti.AlgebraicGeometry.InvertibleSheaf X}
  {D : TauCeti.AlgebraicGeometry.SchemeWeilDivisor X} (e : L.obj ≅ D.sheaf) :
  AlgebraicGeometry.Scheme.Modules.eulerCharBelow k X L.obj 2 =
    (TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree (X ↘ AlgebraicGeometry.Spec ↧k)) D +
        1 -
      ↑(AlgebraicGeometry.Scheme.genus k X)
```

**The Riemann–Roch theorem, in terms of the two cohomology dimensions.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf).

```lean
TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf.{u}
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
  ↑(Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology D.sheaf 0)) -
      ↑(Module.finrank k (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology D.sheaf 1)) =
    (TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree (X ↘ AlgebraicGeometry.Spec ↧k)) D +
        1 -
      ↑(AlgebraicGeometry.Scheme.genus k X)
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus)
- [Source of `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus` in TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.lean#L121)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/JacobianChallenge/STATUS.md)
