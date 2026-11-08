---
declaration: theorem
origin: cited
lean: TauCeti.zHat.cohomologicalDimensionAt_eq_one
statement: formalized
proof: formalized
---

# TauCeti.zHat.cohomologicalDimensionAt_eq_one

**The `p`-cohomological dimension of the profinite integers is one**, for every prime `p`.

```lean
TauCeti.zHat.cohomologicalDimensionAt_eq_one.{u} (p : ℕ) [Fact (Nat.Prime p)] :
  TauCeti.cohomologicalDimensionAt p ↑TauCeti.zHat.toProfinite.toTop = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.ContCohomology.dimensionShiftIso](tauceti-contcohomology-dimensionshiftiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.zHat.cohomologicalDimensionAt_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.html#TauCeti.zHat.cohomologicalDimensionAt_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.zHat.cohomologicalDimensionAt_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.html#TauCeti.zHat.cohomologicalDimensionAt_eq_one)
- [Source of `TauCeti.zHat.cohomologicalDimensionAt_eq_one` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.lean#L197)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
