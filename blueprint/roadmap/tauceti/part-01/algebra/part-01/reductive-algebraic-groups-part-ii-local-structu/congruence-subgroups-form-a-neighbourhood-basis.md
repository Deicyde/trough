---
declaration: theorem
origin: cited
lean: TauCeti.HopfAlgebra.hasBasis_nhds_one_congruenceSubgroup
statement: formalized
proof: formalized
---

# Congruence subgroups form a neighbourhood basis of the identity

If ideals `J i` of `R`
form a basis of neighbourhoods of `0`, then for `H` of finite type over `k` the congruence
subgroups of the levels `J i` form a basis of neighbourhoods of the identity point in the point
topology.

```lean
TauCeti.HopfAlgebra.hasBasis_nhds_one_congruenceSubgroup.{u_1, u_2, u_3, u_4} {k : Type u_1}
  {H : Type u_2} {R : Type u_3} [CommSemiring k] [Semiring H] [HopfAlgebra k H] [CommRing R]
  [Algebra k R] [TopologicalSpace R] [IsTopologicalAddGroup R] [Algebra.FiniteType k H]
  {ι : Sort u_4} {p : ι → Prop} {J : ι → Ideal R} (hJ : (nhds 0).HasBasis p fun i => ↑(J i)) :
  (nhds 1).HasBasis p fun i => ↑(TauCeti.HopfAlgebra.congruenceSubgroup k H (J i))
```

## Depends on

- [TauCeti.PointTopology.instTopologicalSpaceWithConv](tauceti-pointtopology-insttopologicalspacewithco.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfAlgebra.hasBasis_nhds_one_congruenceSubgroup`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/Topology.html#TauCeti.HopfAlgebra.hasBasis_nhds_one_congruenceSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfAlgebra.hasBasis_nhds_one_congruenceSubgroup`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/Topology.html#TauCeti.HopfAlgebra.hasBasis_nhds_one_congruenceSubgroup)
- [Source of `TauCeti.HopfAlgebra.hasBasis_nhds_one_congruenceSubgroup` in TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/Topology.lean#L82)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
