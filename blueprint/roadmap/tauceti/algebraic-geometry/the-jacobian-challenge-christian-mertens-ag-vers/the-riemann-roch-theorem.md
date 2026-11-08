---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus, TauCeti.AlgebraicGeometry.InvertibleSheaf.eulerCharBelow_eq_relativeDegree_add_one_sub_genus, TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual, TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf, TauCeti.AlgebraicGeometry.twoChartModel.eulerCharBelow_sheaf_eq_degree_add_one_sub_genus, TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual, TauCeti.AlgebraicGeometry.SchemeWeilDivisor.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf
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

- [The abstract residue theorem (Stichtenoth, (1.45))](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-abstract-residue-theorem-stichtenoth-1-45.md)
- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Krull–Akizuki's length bound](../../ring-theory/other-results/part-01/krull-akizukis-length-bound.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [Serre duality for line bundles](../other-results/serre-duality-for-line-bundles.md)
- [Stichtenoth's transformation formula `res_{P,s}(z) = res_{P,t}(z · ds/dt)`](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/stichtenoths-transformation-formula-res-p-s-z-re.md)
- [TauCeti.Ring.IsJapanese](../../ring-theory/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.html#TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus).

## Other forms

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

**The Riemann–Roch theorem for line bundles, in Serre-duality form.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/SerreDuality.html#TauCeti.AlgebraicGeometry.InvertibleSheaf.finrank_cohomology_zero_sub_finrank_cohomology_zero_tensor_dual).

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

**The Riemann–Roch theorem on `X_F` in dimension form.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/Cohomology.html#TauCeti.AlgebraicGeometry.twoChartModel.finrank_cohomology_zero_sheaf_sub_finrank_cohomology_one_sheaf).

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

**The Riemann–Roch theorem with the sheaf of differentials.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Differentials/Canonical.html#TauCeti.AlgebraicGeometry.finrank_cohomology_zero_sub_finrank_cohomology_zero_differentials_tensor_dual).

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
- [Source of `TauCeti.AlgebraicGeometry.SchemeWeilDivisor.eulerCharBelow_sheaf_eq_relativeDegree_add_one_sub_genus` in TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/WeilDivisor/Scheme/RiemannRoch/Basic.lean#L121)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/JacobianChallenge/STATUS.md)
