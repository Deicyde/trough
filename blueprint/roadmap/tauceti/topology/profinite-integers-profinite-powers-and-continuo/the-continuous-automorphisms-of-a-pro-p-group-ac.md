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

## Proof depends on

- [TauCeti.profiniteFrattini](../profinite-and-pro-p-groups/part-01/tauceti-profinitefrattini.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.html#TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.html#TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini)
- [Source of `TauCeti.IsProP.isProP_ker_mapQuotient_proPFrattini` in TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.lean#L124)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
