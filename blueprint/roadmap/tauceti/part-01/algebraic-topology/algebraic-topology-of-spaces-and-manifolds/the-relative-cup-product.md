---
declaration: def
origin: cited
lean: TopCat.singularRelativeCup
statement: formalized
---

# The relative cup product

**The relative cup product** `Hᵖ(X, U; R, M) × H^q(X, V; S, N) ⟶ Hⁿ(X, U ∪ V; T, L)` for
subsets `U` and `V` of `X` which are open in `U ∪ V`, and `p + q = n`: the cup product along the
relative Alexander–Whitney diagonal `TopCat.relativeAlexanderWhitneyDiagonal U V u` and the pairing
`μ : M ⊗ N ⟶ L`, which lands in the cohomology of the chains of `X` relative to its singular
simplices lying in `U` or in `V`, followed by the inverse of the small-chain isomorphism with the
cohomology of `(X, U ∪ V)` (`TopCat.homologyMap_cochainComplexMap_singularRelativeCup`).

```lean
TopCat.singularRelativeCup.{w, v, u, u_1} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Abelian C] [CategoryTheory.Limits.HasCoproducts C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C] {R S T M N L : C}
  (k : Type u_1) [CommRing k] [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  {X : TopCat} (u : T ⟶ CategoryTheory.MonoidalCategoryStruct.tensorObj R S)
  (μ : CategoryTheory.MonoidalCategoryStruct.tensorObj M N ⟶ L) (U V : Set ↑X)
  (hU : IsOpen (Subtype.val ⁻¹' U)) (hV : IsOpen (Subtype.val ⁻¹' V)) (p q n : ℕ) (h : p + q = n) :
  ↑((TopPair.ofSubset U).singularCohomology R k M p) →ₗ[k]
    ↑((TopPair.ofSubset V).singularCohomology S k N q) →ₗ[k]
      ↑((TopPair.ofSubset (U ∪ V)).singularCohomology T k L n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.singularRelativeCup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Cup/Relative.html#TopCat.singularRelativeCup).

## Sources

- [Tau Ceti documentation: `TopCat.singularRelativeCup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Cup/Relative.html#TopCat.singularRelativeCup)
- [Source of `TopCat.singularRelativeCup` in TauCeti/AlgebraicTopology/Cohomology/Cup/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/Cup/Relative.lean#L302)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
