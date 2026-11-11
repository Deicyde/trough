---
declaration: def
origin: cited
lean: TauCeti.ContCohomology.explicitFiniteQuotientColimit1
statement: formalized
---

# The degree-one finite-quotient colimit theorem

`H¹(G, M)` is the colimit of the
finite-level first cohomology groups `H¹(G ⧸ U, M^U)`, through the inflation maps.

```lean
TauCeti.ContCohomology.explicitFiniteQuotientColimit1.{u, v} (G : Type u) [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (M : Type v) [AddCommGroup M] [DistribMulAction G M]
  [TopologicalSpace M] [IsTopologicalAddGroup M] [DiscreteTopology M] [CompactSpace G]
  [TotallyDisconnectedSpace G] [ContinuousSMul G M] :
  CategoryTheory.Limits.IsColimit (TauCeti.ContCohomology.explicitFiniteQuotientCocone1 G M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitFiniteQuotientColimit1`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/Colimit.html#TauCeti.ContCohomology.explicitFiniteQuotientColimit1).

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.explicitFiniteQuotientColimit1`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/Colimit.html#TauCeti.ContCohomology.explicitFiniteQuotientColimit1)
- [Source of `TauCeti.ContCohomology.explicitFiniteQuotientColimit1` in TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/Colimit.lean#L569)
