---
declaration: def
origin: cited
lean: TauCeti.FiniteRankBundleCore.det
statement: formalized
---

# TauCeti.FiniteRankBundleCore.det

The determinant line of a finite-rank core of rank `r`: its exterior power `⋀^r A` in the top
degree, with fibres the top exterior powers of the fibres of `A`.

```lean
TauCeti.FiniteRankBundleCore.det.{u, u_1} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {B : Type u}
  [TopologicalSpace B] (A : TauCeti.FiniteRankBundleCore 𝕜 B) : TauCeti.FiniteRankBundleCore 𝕜 B
```

## Depends on

- [TauCeti.FiniteRankBundleCore](../../../../part-02/topology/topological-k-theory-of-vector-bundles/tauceti-finiterankbundlecore.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteRankBundleCore.det`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/FiniteRank/ExteriorPower.html#TauCeti.FiniteRankBundleCore.det).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteRankBundleCore.det`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/FiniteRank/ExteriorPower.html#TauCeti.FiniteRankBundleCore.det)
- [Source of `TauCeti.FiniteRankBundleCore.det` in TauCeti/Topology/VectorBundle/FiniteRank/ExteriorPower.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/FiniteRank/ExteriorPower.lean#L240)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexManifolds/STATUS.md)
