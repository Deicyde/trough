---
declaration: theorem
origin: cited
lean: TopCat.lerayHirschProd_bijective
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

## Lean

Formalized in Tau Ceti as [`TopCat.lerayHirschProd_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/LerayHirsch/Product.html#TopCat.lerayHirschProd_bijective).

## Sources

- [Tau Ceti documentation: `TopCat.lerayHirschProd_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/LerayHirsch/Product.html#TopCat.lerayHirschProd_bijective)
- [Source of `TopCat.lerayHirschProd_bijective` in TauCeti/AlgebraicTopology/Cohomology/LerayHirsch/Product.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/LerayHirsch/Product.lean#L255)
