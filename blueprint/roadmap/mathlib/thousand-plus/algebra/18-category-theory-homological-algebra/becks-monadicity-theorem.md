# Beck's monadicity theorem

**Beck's monadicity theorem**: if `G` has a left adjoint and creates coequalizers of `G`-split
pairs, then it is monadic.
This is the converse of `createsGSplitCoequalizersOfMonadic`.

```lean
CategoryTheory.Monad.monadicOfCreatesGSplitCoequalizers.{v₁, u₁, u₂} {C : Type u₁} {D : Type u₂}
  [CategoryTheory.Category.{v₁, u₁} C] [CategoryTheory.Category.{v₁, u₂} D]
  {G : CategoryTheory.Functor D C} {F : CategoryTheory.Functor C D} (adj : F ⊣ G)
  [CategoryTheory.Monad.CreatesColimitOfIsSplitPair G] : CategoryTheory.MonadicRightAdjoint G
```

## Depends on

- [Adjunction](../../../overview/general-algebra/category-theory/adjunction.md)
- [Isomorphism](../../../overview/general-algebra/category-theory/isomorphism.md)
- [Monad](../../../overview/general-algebra/category-theory/monad.md)
- [Small category](../../../overview/general-algebra/category-theory/small-category.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Monad.monadicOfCreatesGSplitCoequalizers`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Monad/Monadicity.html#CategoryTheory.Monad.monadicOfCreatesGSplitCoequalizers)
- [Source of `CategoryTheory.Monad.monadicOfCreatesGSplitCoequalizers` in Mathlib/CategoryTheory/Monad/Monadicity.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/CategoryTheory/Monad/Monadicity.lean#L345)
- [1000+ theorems list: Q4878586](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L2881)
- [1000+ theorems project: Q4878586](https://1000-plus.github.io/all.html?length=-1#Q4878586)
- [Wikipedia: Beck's monadicity theorem](https://en.wikipedia.org/wiki/Beck's_monadicity_theorem)
- [Wikidata: Q4878586](https://www.wikidata.org/wiki/Q4878586)
