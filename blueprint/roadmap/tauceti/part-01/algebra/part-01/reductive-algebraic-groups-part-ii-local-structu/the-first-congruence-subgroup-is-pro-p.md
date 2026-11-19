---
declaration: theorem
origin: cited
lean: TauCeti.HopfAlgebra.isProP_congruenceSubgroup
statement: formalized
proof: formalized
---

# The first congruence subgroup is pro-`p`

If the topology of `R` is `I`-adic, `(p : R) ∈ I`
and `H` is of finite type over `k`, then the congruence subgroup of level `I`, with its subspace
topology, is pro-`p`: each of its quotients by an open normal subgroup is a `p`-group.

```lean
TauCeti.HopfAlgebra.isProP_congruenceSubgroup.{u_1, u_2, u_3} {k : Type u_1} {H : Type u_2}
  {R : Type u_3} [CommSemiring k] [Semiring H] [HopfAlgebra k H] [CommRing R] [Algebra k R]
  [TopologicalSpace R] [Algebra.FiniteType k H] {I : Ideal R} (hI : IsAdic I) {p : ℕ}
  (hp : ↑p ∈ I) : TauCeti.IsProP p ↥(TauCeti.HopfAlgebra.congruenceSubgroup k H I)
```

## Depends on

- [TauCeti.PointTopology.instTopologicalSpaceWithConv](tauceti-pointtopology-insttopologicalspacewithco.md)

## Proof depends on

- [Congruence subgroups form a neighbourhood basis of the identity](congruence-subgroups-form-a-neighbourhood-basis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfAlgebra.isProP_congruenceSubgroup`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/ProP.html#TauCeti.HopfAlgebra.isProP_congruenceSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfAlgebra.isProP_congruenceSubgroup`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/ProP.html#TauCeti.HopfAlgebra.isProP_congruenceSubgroup)
- [Source of `TauCeti.HopfAlgebra.isProP_congruenceSubgroup` in TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/ProP.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/ProP.lean#L106)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
