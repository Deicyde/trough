---
declaration: theorem
origin: cited
lean: TopCat.lerayHirschProd_bijective, TopCat.lerayHirschProdOfClasses_bijective
statement: formalized
proof: formalized
---

# The Leray–Hirsch theorem for a product

over a commutative ring `k`, if the homology
`Hₚ(F; k)` is projective in every degree and finitely generated in degrees `p ≤ n`, for instance
over a field when `F` has finite CW type, and `b p` is a basis of `Hᵖ(F; k)` for every `p`, the
Leray–Hirsch map
`⨁_{p + q = n} ⨁_{i : ι p} H^q(X; k) ⟶ Hⁿ(X × F; k)`, `(a_{p,i}) ↦ ∑ pr₁^* a_{p,i} ⌣ pr₂^* b_{p,i}`,
is bijective.

```lean
TopCat.lerayHirschProd_bijective.{w} {k : Type w} [CommRing k] (X : TopCat) {F : TopCat} {n : ℕ}
  {ι : ℕ → Type w} [(p : ℕ) → DecidableEq (ι p)]
  (b :
    (p : ℕ) →
      Module.Basis (ι p) k
        ↑(TopCat.singularCohomology (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))
            k (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k)) F p))
  [∀ (p : ℕ),
      CategoryTheory.Projective
        (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) p).obj
              (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))).obj
          F)]
  (hF :
    ∀ p ≤ n,
      Module.Finite k
        ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) p).obj
                (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))).obj
            F)) :
  Function.Bijective ⇑(X.lerayHirschProd F n b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Künneth theorem for cohomology](the-kunneth-theorem-for-cohomology.md)
- [The universal coefficient theorem over a field](the-universal-coefficient-theorem-over-a-field.md)

## Lean

Formalized in Tau Ceti as [`TopCat.lerayHirschProd_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/LerayHirsch/Product.html#TopCat.lerayHirschProd_bijective).

## Other forms

**The Leray–Hirsch theorem for a product with fibrewise basis classes.** Formalized in Tau Ceti as [`TopCat.lerayHirschProdOfClasses_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/LerayHirsch/FiberwiseBasis.html#TopCat.lerayHirschProdOfClasses_bijective).

```lean
TopCat.lerayHirschProdOfClasses_bijective.{w} {k : Type w} [CommRing k] (X : TopCat) {F : TopCat}
  {ι : ℕ → Type w} [(p : ℕ) → DecidableEq (ι p)]
  [∀ (p : ℕ),
      CategoryTheory.Projective
        (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) p).obj
              (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))).obj
          F)]
  (n : ℕ)
  (c :
    (p : ℕ) →
      ι p →
        ↑(TopCat.singularCohomology (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))
            k (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))
            (CategoryTheory.MonoidalCategoryStruct.tensorObj X F) p))
  (hι : ∀ p ≤ n, Finite (ι p))
  (hF :
    ∀ p ≤ n,
      Module.Finite k
        ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) p).obj
                (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))).obj
            F))
  (hc :
    ∀ (x : ↑X) (p : ℕ),
      (LinearIndependent k fun i =>
          (CategoryTheory.ConcreteCategory.hom
              (TopCat.singularCohomologyMap (X.prodFiberInclusion F x) p))
            (c p i)) ∧
        ⊤ ≤
          Submodule.span k
            (Set.range fun i =>
              (CategoryTheory.ConcreteCategory.hom
                  (TopCat.singularCohomologyMap (X.prodFiberInclusion F x) p))
                (c p i))) :
  Function.Bijective ⇑(X.lerayHirschProdOfClasses F n c)
```

## Sources

- [Tau Ceti documentation: `TopCat.lerayHirschProd_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/LerayHirsch/Product.html#TopCat.lerayHirschProd_bijective)
- [Source of `TopCat.lerayHirschProd_bijective` in TauCeti/AlgebraicTopology/Cohomology/LerayHirsch/Product.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cohomology/LerayHirsch/Product.lean#L255)
