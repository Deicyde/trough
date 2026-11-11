---
declaration: def
origin: cited
lean: TauCeti.groupCohomology.averagingHomotopy
statement: formalized
---

# The averaging contraction

The identity of the complex of inhomogeneous cochains is
homotopic to the averaging projection onto the invariants placed in degree `0`, through the
homotopy whose component from degree `n + 1` to degree `n` is `(-1)^(n+1)` times the average
over the last argument (`TauCeti.groupCohomology.averagingHomotopy_hom_succ`).

```lean
TauCeti.groupCohomology.averagingHomotopy.{u} {k G : Type u} [CommRing k] [Group G] [Fintype G]
  [Invertible ↑(Fintype.card G)] (A : Rep.{u, u, u} k G) :
  Homotopy (CategoryTheory.CategoryStruct.id (groupCohomology.inhomogeneousCochains A))
    (TauCeti.groupCohomology.averageCochainMap A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.groupCohomology.averagingHomotopy`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Averaging.html#TauCeti.groupCohomology.averagingHomotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.groupCohomology.averagingHomotopy`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Averaging.html#TauCeti.groupCohomology.averagingHomotopy)
- [Source of `TauCeti.groupCohomology.averagingHomotopy` in TauCeti/RepresentationTheory/Homological/GroupCohomology/Averaging.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/GroupCohomology/Averaging.lean#L183)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Orbifolds/STATUS.md)
