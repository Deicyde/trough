---
declaration: theorem
origin: cited
lean: TauCeti.zHat.cohomologicalDimensionAt_eq_one
statement: formalized
proof: formalized
---

# The `p`-cohomological dimension of the profinite integers is one, for every prime `p`

```lean
TauCeti.zHat.cohomologicalDimensionAt_eq_one.{u} (p : ℕ) [Fact (Nat.Prime p)] :
  TauCeti.cohomologicalDimensionAt p ↑TauCeti.zHat.toProfinite.toTop = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dimension shifting in every positive degree](dimension-shifting-in-every-positive-degree.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.zHat.cohomologicalDimensionAt_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.html#TauCeti.zHat.cohomologicalDimensionAt_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.zHat.cohomologicalDimensionAt_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.html#TauCeti.zHat.cohomologicalDimensionAt_eq_one)
- [Source of `TauCeti.zHat.cohomologicalDimensionAt_eq_one` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.lean#L197)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
