---
declaration: theorem
origin: cited
lean: TopCat.singularCohomologyKunneth_bijective
statement: formalized
proof: formalized
---

# The Künneth theorem for cohomology

over a commutative semisimple ring `k`, for instance a
field, if the homology `Hₚ(X; k)` is finitely generated in degrees `p ≤ n`, the cohomology Künneth
map `⨁_{p + q = n} Hᵖ(X; k) ⊗ H^q(Y; k) ⟶ Hⁿ(X × Y; k)` is bijective.

```lean
TopCat.singularCohomologyKunneth_bijective.{w} {k : Type w} [CommRing k] (X Y : TopCat)
  [IsSemisimpleRing k] (n : ℕ)
  (hX :
    ∀ p ≤ n,
      Module.Finite k
        ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) p).obj
                (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))).obj
            X)) :
  Function.Bijective
    ⇑(CategoryTheory.ConcreteCategory.hom
        (X.singularCohomologyKunneth Y
          (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))
          (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k)) k
          (CategoryTheory.MonoidalCategoryStruct.leftUnitor
              (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))).hom
          n))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Eilenberg–Zilber theorem for singular chains](../singular/the-eilenberg-zilber-theorem-for-singular-chains.md)
- [The Künneth theorem for cubical homology](../singular/the-kunneth-theorem-for-cubical-homology.md)
- [The universal coefficient theorem over a field](the-universal-coefficient-theorem-over-a-field.md)

## Lean

Formalized in Tau Ceti as [`TopCat.singularCohomologyKunneth_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Kunneth.html#TopCat.singularCohomologyKunneth_bijective).

## Sources

- [Tau Ceti documentation: `TopCat.singularCohomologyKunneth_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Kunneth.html#TopCat.singularCohomologyKunneth_bijective)
- [Source of `TopCat.singularCohomologyKunneth_bijective` in TauCeti/AlgebraicTopology/Cohomology/Kunneth.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Cohomology/Kunneth.lean#L362)
