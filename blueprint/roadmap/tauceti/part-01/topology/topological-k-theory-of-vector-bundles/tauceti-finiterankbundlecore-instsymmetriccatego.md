---
declaration: instance
origin: cited
lean: TauCeti.FiniteRankBundleCore.instSymmetricCategory
statement: formalized
---

# TauCeti.FiniteRankBundleCore.instSymmetricCategory

The braiding `tensorComm` makes the monoidal category of finite-rank cores symmetric.

```lean
TauCeti.FiniteRankBundleCore.instSymmetricCategory.{u_1, u_2} {𝕜 : Type u_1} {B : Type u_2}
  [NontriviallyNormedField 𝕜] [TopologicalSpace B] :
  CategoryTheory.SymmetricCategory (TauCeti.FiniteRankBundleCore 𝕜 B)
```

## Depends on

- [TauCeti.FiniteRankBundleCore](tauceti-finiterankbundlecore.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteRankBundleCore.instSymmetricCategory`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/FiniteRank/Monoidal.html#TauCeti.FiniteRankBundleCore.instSymmetricCategory).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteRankBundleCore.instSymmetricCategory`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/FiniteRank/Monoidal.html#TauCeti.FiniteRankBundleCore.instSymmetricCategory)
- [Source of `TauCeti.FiniteRankBundleCore.instSymmetricCategory` in TauCeti/Topology/VectorBundle/FiniteRank/Monoidal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/FiniteRank/Monoidal.lean#L170)
- [Tau Ceti roadmap status: Topological K-theory of vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalKTheory/STATUS.md)
