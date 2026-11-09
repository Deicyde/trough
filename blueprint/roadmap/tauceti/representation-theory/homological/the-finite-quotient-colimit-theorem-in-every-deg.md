---
declaration: def
origin: cited
lean: TauCeti.ContCohomology.continuousFiniteQuotientColimit
statement: formalized
---

# The finite-quotient colimit theorem in every degree

For a compact group `G` and a discrete
module `M` with continuous action, the inflation-and-inclusion cocone exhibits the canonical
continuous cohomology `Hⁿ(G, M)` as the colimit, in `TopModuleCat ℤ`, of the cohomology groups
`Hⁿ(G ⧸ U, M^U)` of the finite quotients over the open normal subgroups `U` of `G`.

```lean
TauCeti.ContCohomology.continuousFiniteQuotientColimit.{u} (G : Type u) [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (M : Type u) [AddCommGroup M] [TopologicalSpace M]
  [DiscreteTopology M] [DistribMulAction G M] [CompactSpace G] [ContinuousSMul G M] (n : ℕ) :
  CategoryTheory.Limits.IsColimit (TauCeti.ContCohomology.continuousFiniteQuotientCocone G M n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.continuousFiniteQuotientColimit`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/AllDegreeColimit.html#TauCeti.ContCohomology.continuousFiniteQuotientColimit).

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.continuousFiniteQuotientColimit`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/AllDegreeColimit.html#TauCeti.ContCohomology.continuousFiniteQuotientColimit)
- [Source of `TauCeti.ContCohomology.continuousFiniteQuotientColimit` in TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/AllDegreeColimit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/AllDegreeColimit.lean#L398)
