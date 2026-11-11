---
declaration: theorem
origin: cited
lean: TauCeti.TopCat.normalSpace_of_isColimit
statement: formalized
proof: formalized
---

# TauCeti.TopCat.normalSpace_of_isColimit

The colimit of a sequence of normal spaces in `TopCat` whose transition maps are closed
embeddings is normal.

```lean
TauCeti.TopCat.normalSpace_of_isColimit.{u} {F : CategoryTheory.Functor ℕ TopCat}
  {c : CategoryTheory.Limits.Cocone F}
  (hF :
    ∀ (n : ℕ),
      Topology.IsClosedEmbedding
        ⇑(CategoryTheory.ConcreteCategory.hom (F.map (CategoryTheory.homOfLE ⋯))))
  (hc : CategoryTheory.Limits.IsColimit c) [∀ (n : ℕ), NormalSpace ↑(F.obj n)] : NormalSpace ↑c.pt
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TopCat.normalSpace_of_isColimit`](https://taucetiproject.org/docs/TauCeti/Topology/Category/TopCat/Normal.html#TauCeti.TopCat.normalSpace_of_isColimit).

## Sources

- [Tau Ceti documentation: `TauCeti.TopCat.normalSpace_of_isColimit`](https://taucetiproject.org/docs/TauCeti/Topology/Category/TopCat/Normal.html#TauCeti.TopCat.normalSpace_of_isColimit)
- [Source of `TauCeti.TopCat.normalSpace_of_isColimit` in TauCeti/Topology/Category/TopCat/Normal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Category/TopCat/Normal.lean#L152)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Orbifolds/STATUS.md)
