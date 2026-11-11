---
declaration: theorem
origin: cited
lean: TauCeti.PointTopology.isOpenEmbedding_integralPoints
statement: formalized
proof: formalized
---

# TauCeti.PointTopology.isOpenEmbedding_integralPoints

The integral points of a finite type algebra form an open subspace of the points over `E`.

```lean
TauCeti.PointTopology.isOpenEmbedding_integralPoints.{u_1, u_2} {E : Type u_1} {A : Type u_2}
  [CommRing E] [ValuativeRel E] [Semiring A] [Algebra (↥(ValuativeRel.valuation E).integer) A]
  [TopologicalSpace E] [IsValuativeTopology E]
  [Algebra.FiniteType (↥(ValuativeRel.valuation E).integer) A] :
  Topology.IsOpenEmbedding fun x => (Algebra.ofId (↥(ValuativeRel.valuation E).integer) E).comp x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PointTopology.isOpenEmbedding_integralPoints`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/IntegralPoints.html#TauCeti.PointTopology.isOpenEmbedding_integralPoints).

## Sources

- [Tau Ceti documentation: `TauCeti.PointTopology.isOpenEmbedding_integralPoints`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/IntegralPoints.html#TauCeti.PointTopology.isOpenEmbedding_integralPoints)
- [Source of `TauCeti.PointTopology.isOpenEmbedding_integralPoints` in TauCeti/Topology/Algebra/PointTopology/IntegralPoints.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/PointTopology/IntegralPoints.lean#L87)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
