---
declaration: theorem
origin: cited
lean: SSet.kanComplex_of_group, SSet.kanComplex_of_addGroup
statement: formalized
proof: formalized
---

# Moore's theorem

a simplicial set whose sets of simplices are groups, with simplicial
operators group homomorphisms, is a Kan complex.

```lean
SSet.kanComplex_of_group.{u} {X : _root_.SSet} [(n : SimplexCategoryᵒᵖ) → Group (X.obj n)]
  (hX :
    ∀ ⦃m n : SimplexCategoryᵒᵖ⦄ (f : m ⟶ n) (x y : X.obj m),
      (CategoryTheory.ConcreteCategory.hom (X.map f)) (x * y) =
        (CategoryTheory.ConcreteCategory.hom (X.map f)) x *
          (CategoryTheory.ConcreteCategory.hom (X.map f)) y) :
  X.KanComplex
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SSet.kanComplex_of_group`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/KanComplex/SimplicialGroup/Basic.html#SSet.kanComplex_of_group).

## Other forms

**Moore's theorem for additive groups.** Formalized in Tau Ceti as [`SSet.kanComplex_of_addGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/KanComplex/SimplicialGroup/Basic.html#SSet.kanComplex_of_addGroup).

```lean
SSet.kanComplex_of_addGroup.{u} {X : _root_.SSet} [(n : SimplexCategoryᵒᵖ) → AddGroup (X.obj n)]
  (hX :
    ∀ ⦃m n : SimplexCategoryᵒᵖ⦄ (f : m ⟶ n) (x y : X.obj m),
      (CategoryTheory.ConcreteCategory.hom (X.map f)) (x + y) =
        (CategoryTheory.ConcreteCategory.hom (X.map f)) x +
          (CategoryTheory.ConcreteCategory.hom (X.map f)) y) :
  X.KanComplex
```

## Sources

- [Tau Ceti documentation: `SSet.kanComplex_of_group`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/KanComplex/SimplicialGroup/Basic.html#SSet.kanComplex_of_group)
- [Source of `SSet.kanComplex_of_group` in TauCeti/AlgebraicTopology/SimplicialSet/KanComplex/SimplicialGroup/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/SimplicialSet/KanComplex/SimplicialGroup/Basic.lean#L185)
