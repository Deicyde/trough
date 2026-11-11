---
declaration: def
origin: cited
lean: TauCeti.infiniteGrassmannian.isColimit
statement: formalized
---

# TauCeti.infiniteGrassmannian.isColimit

The infinite Grassmannian is the colimit in `TopCat` of the finite Grassmannians along
ambient stabilization.

```lean
TauCeti.infiniteGrassmannian.isColimit.{u_2} (𝕜 : Type u_2) [Field 𝕜] [TopologicalSpace 𝕜] (k : ℕ) :
  CategoryTheory.Limits.IsColimit (TauCeti.infiniteGrassmannian.cocone 𝕜 k)
```

## Depends on

- [TauCeti.finiteGrassmannian](tauceti-finitegrassmannian.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.infiniteGrassmannian.isColimit`](https://taucetiproject.org/docs/TauCeti/Topology/Grassmannian/Infinite.html#TauCeti.infiniteGrassmannian.isColimit).

## Sources

- [Tau Ceti documentation: `TauCeti.infiniteGrassmannian.isColimit`](https://taucetiproject.org/docs/TauCeti/Topology/Grassmannian/Infinite.html#TauCeti.infiniteGrassmannian.isColimit)
- [Source of `TauCeti.infiniteGrassmannian.isColimit` in TauCeti/Topology/Grassmannian/Infinite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Grassmannian/Infinite.lean#L258)
- [Tau Ceti roadmap status: Topological K-theory of vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalKTheory/STATUS.md)
