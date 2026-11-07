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
- [Source of `TauCeti.groupCohomology.averagingHomotopy` in TauCeti/RepresentationTheory/Homological/GroupCohomology/Averaging.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/Averaging.lean#L183)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Orbifolds/STATUS.md)
