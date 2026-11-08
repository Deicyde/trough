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

- [Dimension shifting in every positive degree, `Hⁱ⁺¹(G, M) ≅ Hⁱ(G, Coind_1^G M ⧸ M)` for `i ≥ 1` and a compact group `G`, as an isomorphism of Mathlib's canonical continuous cohomology](dimension-shifting-in-every-positive-degree-hi-1.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.zHat.cohomologicalDimensionAt_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.html#TauCeti.zHat.cohomologicalDimensionAt_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.zHat.cohomologicalDimensionAt_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.html#TauCeti.zHat.cohomologicalDimensionAt_eq_one)
- [Source of `TauCeti.zHat.cohomologicalDimensionAt_eq_one` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ZHat/CohomologicalDimension.lean#L197)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
