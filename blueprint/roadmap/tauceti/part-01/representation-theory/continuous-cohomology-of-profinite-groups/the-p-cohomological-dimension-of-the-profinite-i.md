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
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.zHat.cohomologicalDimensionAt_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.html#TauCeti.zHat.cohomologicalDimensionAt_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.zHat.cohomologicalDimensionAt_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.html#TauCeti.zHat.cohomologicalDimensionAt_eq_one)
- [Source of `TauCeti.zHat.cohomologicalDimensionAt_eq_one` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.lean#L197)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
