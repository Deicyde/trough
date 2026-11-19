---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini
statement: formalized
proof: formalized
---

# The continuous automorphisms of a pro-`p` group acting trivially on its Frattini quotient form a pro-`p` group

For a compact pro-`p` group `G`, the kernel of
`ContinuousAut G →* MulAut (G ⧸ proPFrattini p G)` is pro-`p` for the congruence topology.

```lean
TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini.{u_1} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] {p : ℕ} [Fact (Nat.Prime p)]
  (hG : TauCeti.IsProP p G) : TauCeti.IsProP p ↥(TauCeti.ContinuousAut.mapQuotient ⋯).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.html#TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.html#TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini)
- [Source of `TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini` in TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.lean#L124)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteArithmetic/STATUS.md)
