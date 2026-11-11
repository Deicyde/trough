---
declaration: def
origin: cited
lean: TauCeti.ContCohomology.explicitFiniteQuotientColimit0
statement: formalized
---

# The degree-zero finite-quotient colimit theorem

`H⁰(G, M)` is the colimit of
`H⁰(G ⧸ U, M^U)` over the open normal subgroups, through the inflation maps.

Every transition is an isomorphism, so the system is eventually constant and the whole-group
level — where the comparison leg is the equivalence
`TauCeti.ContCohomology.explicitInfl0Equiv` — already computes the colimit.

```lean
TauCeti.ContCohomology.explicitFiniteQuotientColimit0.{u, v} (G : Type u) [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (M : Type v) [AddCommGroup M] [DistribMulAction G M] :
  CategoryTheory.Limits.IsColimit (TauCeti.ContCohomology.explicitFiniteQuotientCocone0 G M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitFiniteQuotientColimit0`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/Colimit.html#TauCeti.ContCohomology.explicitFiniteQuotientColimit0).

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.explicitFiniteQuotientColimit0`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/Colimit.html#TauCeti.ContCohomology.explicitFiniteQuotientColimit0)
- [Source of `TauCeti.ContCohomology.explicitFiniteQuotientColimit0` in TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/ContCohomology/FiniteQuotient/Colimit.lean#L207)
