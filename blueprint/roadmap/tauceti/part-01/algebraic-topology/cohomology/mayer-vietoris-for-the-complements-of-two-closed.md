---
declaration: theorem
origin: cited
lean: TopCat.exists_singularCohomologyComplRestrict_eq_of_add_eq_zero
statement: formalized
proof: formalized
---

# Mayer–Vietoris for the complements of two closed sets, exactness at the middle term

if
`a ∈ Hⁿ(X, X ∖ S)` and `b ∈ Hⁿ(X, X ∖ T)` restrict to classes of `Hⁿ(X, X ∖ (S ∪ T))` with sum
zero, then `a` and `-b` are the restrictions of one class of `Hⁿ(X, X ∖ (S ∩ T))`. This is
`TopCat.singularCohomologyPairMayerVietoris_exact₂` for the pairs `(univ, X ∖ S)` and
`(univ, X ∖ T)`.

```lean
TopCat.exists_singularCohomologyComplRestrict_eq_of_add_eq_zero.{w, v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Limits.HasCoproducts C]
  [CategoryTheory.Abelian C] {R : C} {k : Type u_1} [Ring k] [CategoryTheory.Linear k C] {M : C}
  {X : TopCat} {S T : Set ↑X} (hS : IsClosed S) (hT : IsClosed T) {n : ℕ}
  (a : ↑((TopPair.ofSubset Sᶜ).singularCohomology R k M n))
  (b : ↑((TopPair.ofSubset Tᶜ).singularCohomology R k M n))
  (h :
    (CategoryTheory.ConcreteCategory.hom (TopCat.singularCohomologyComplRestrict R k M ⋯ n)) a +
        (CategoryTheory.ConcreteCategory.hom (TopCat.singularCohomologyComplRestrict R k M ⋯ n)) b =
      0) :
  ∃ z,
    (CategoryTheory.ConcreteCategory.hom (TopCat.singularCohomologyComplRestrict R k M ⋯ n)) z = a ∧
      (CategoryTheory.ConcreteCategory.hom (TopCat.singularCohomologyComplRestrict R k M ⋯ n)) z =
        -b
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.exists_singularCohomologyComplRestrict_eq_of_add_eq_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/MayerVietoris/Compl.html#TopCat.exists_singularCohomologyComplRestrict_eq_of_add_eq_zero).

## Sources

- [Tau Ceti documentation: `TopCat.exists_singularCohomologyComplRestrict_eq_of_add_eq_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/MayerVietoris/Compl.html#TopCat.exists_singularCohomologyComplRestrict_eq_of_add_eq_zero)
- [Source of `TopCat.exists_singularCohomologyComplRestrict_eq_of_add_eq_zero` in TauCeti/AlgebraicTopology/Cohomology/MayerVietoris/Compl.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cohomology/MayerVietoris/Compl.lean#L176)
