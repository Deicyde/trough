---
declaration: instance
origin: cited
lean: CategoryTheory.Idempotents.DoldKan.laxMonoidalΓ
statement: formalized
---

# CategoryTheory.Idempotents.DoldKan.laxMonoidalΓ

**The lax monoidal structure of the Dold–Kan functor** `Γ` from chain complexes to
simplicial objects: it is the mate, along the Dold–Kan equivalence, of the Alexander–Whitney
oplax monoidal structure of the normalized chain functor `N`
(`CategoryTheory.Idempotents.DoldKan.Γ_ε` and `CategoryTheory.Idempotents.DoldKan.Γ_μ`).

```lean
CategoryTheory.Idempotents.DoldKan.laxMonoidalΓ.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.IsIdempotentComplete C] [CategoryTheory.Limits.HasFiniteCoproducts C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C] :
  CategoryTheory.Idempotents.DoldKan.Γ.LaxMonoidal
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Coassociativity of the Alexander–Whitney map](coassociativity-of-the-alexander-whitney-map.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Idempotents.DoldKan.laxMonoidalΓ`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DoldKan/Monoidal.html#CategoryTheory.Idempotents.DoldKan.laxMonoidal%CE%93).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Idempotents.DoldKan.laxMonoidalΓ`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DoldKan/Monoidal.html#CategoryTheory.Idempotents.DoldKan.laxMonoidal%CE%93)
- [Source of `CategoryTheory.Idempotents.DoldKan.laxMonoidalΓ` in TauCeti/AlgebraicTopology/DoldKan/Monoidal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/DoldKan/Monoidal.lean#L307)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
