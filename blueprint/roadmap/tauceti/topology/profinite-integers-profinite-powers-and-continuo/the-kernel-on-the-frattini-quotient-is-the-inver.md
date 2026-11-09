---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.range_pi_mapQuotient_ker_proPFrattini
statement: formalized
proof: formalized
---

# The kernel on the Frattini quotient is the inverse limit of the finite kernels

For a
topologically finitely generated pro-`p` group `G`, the coordinates on the quotients `G ⧸ N` by the
topologically characteristic open normal subgroups `N ≤ proPFrattini p G` identify the kernel of
`ContinuousAut G →* MulAut (G ⧸ proPFrattini p G)` with the families of automorphisms `σ N` of
the finite `p`-groups `G ⧸ N` that act trivially on the Frattini quotients of `G ⧸ N` and are
compatible with the quotient maps `G ⧸ N → G ⧸ M` for `N ≤ M`. The coordinate map is injective
and a topological embedding by `ContinuousAut.isEmbedding_pi_mapQuotient_ker_proPFrattini`.

```lean
TauCeti.IsProP.range_pi_mapQuotient_ker_proPFrattini.{u_1} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] {p : ℕ}
  [Fact (Nat.Prime p)] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) :
  (Set.range fun φ N => (TauCeti.ContinuousAut.mapQuotient ⋯) ↑φ) =
    {σ |
      (∀
          (N :
            { N //
              TauCeti.IsTopCharacteristic G ↑N.toOpenSubgroup ∧
                ↑N.toOpenSubgroup ≤ TauCeti.proPFrattini p G }),
          σ N ∈ (MulAut.mapQuotient (frattini (G ⧸ ↑(↑N).toOpenSubgroup))).ker) ∧
        ∀
          ⦃N M :
            { N //
              TauCeti.IsTopCharacteristic G ↑N.toOpenSubgroup ∧
                ↑N.toOpenSubgroup ≤ TauCeti.proPFrattini p G }⦄
          (hle : ↑N ≤ ↑M) (q : G ⧸ ↑(↑N).toOpenSubgroup),
          (TauCeti.QuotientGroup.mapOfLE hle) ((σ N) q) =
            (σ M) ((TauCeti.QuotientGroup.mapOfLE hle) q)}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.profiniteFrattini](../profinite-and-pro-p-groups/part-01/tauceti-profinitefrattini.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.range_pi_mapQuotient_ker_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.html#TauCeti.IsProP.range_pi_mapQuotient_ker_proPFrattini).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.range_pi_mapQuotient_ker_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.html#TauCeti.IsProP.range_pi_mapQuotient_ker_proPFrattini)
- [Source of `TauCeti.IsProP.range_pi_mapQuotient_ker_proPFrattini` in TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.lean#L204)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
