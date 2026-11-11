---
declaration: def
origin: cited
lean: TopCat.isColimitCompactSupportCohomologyOpensCocone
statement: formalized
---

# Cohomology with compact supports of a directed open union

If a Hausdorff space `X` is the
union of a directed family of open sets `U i`, then `Hⁿ_c(X)` is the colimit of the groups
`Hⁿ_c(U i)` along the extensions.

```lean
TopCat.isColimitCompactSupportCohomologyOpensCocone.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Limits.HasCoproducts C]
  [CategoryTheory.Abelian C] {R : C} {k : Type v} [Ring k] [CategoryTheory.Linear k C] {M : C}
  {X : TopCat} [T2Space ↑X] {J : Type v} [Preorder J] [IsDirected J fun x1 x2 => x1 ≤ x2]
  [Nonempty J] {V : J → TopologicalSpace.Opens ↑X} (hV : Monotone V) (hcover : ⨆ j, V j = ⊤)
  (n : ℕ) :
  CategoryTheory.Limits.IsColimit
    (CategoryTheory.Limits.Cocone.whisker hV.functor
      (TopCat.compactSupportCohomologyOpensCocone R k M X n))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative small-chain theorem for cochains](../cohomology/the-relative-small-chain-theorem-for-cochains.md)

## Lean

Formalized in Tau Ceti as [`TopCat.isColimitCompactSupportCohomologyOpensCocone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/DirectedUnion.html#TopCat.isColimitCompactSupportCohomologyOpensCocone).

## Sources

- [Tau Ceti documentation: `TopCat.isColimitCompactSupportCohomologyOpensCocone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/DirectedUnion.html#TopCat.isColimitCompactSupportCohomologyOpensCocone)
- [Source of `TopCat.isColimitCompactSupportCohomologyOpensCocone` in TauCeti/AlgebraicTopology/Cohomology/CompactSupport/DirectedUnion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/DirectedUnion.lean#L149)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
