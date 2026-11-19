---
declaration: theorem
origin: cited
lean: TauCeti.ContinuousAut.isOpen_ker_mapQuotient_proPFrattini
statement: formalized
proof: formalized
---

# TauCeti.ContinuousAut.isOpen_ker_mapQuotient_proPFrattini

For a topologically finitely generated compact group, the continuous automorphisms acting
trivially on the pro-`p` Frattini quotient form an open subgroup for the congruence topology: the
pro-`p` Frattini subgroup is open and topologically characteristic.

```lean
TauCeti.ContinuousAut.isOpen_ker_mapQuotient_proPFrattini.{u_1} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  (hG : TauCeti.IsTopologicallyFinitelyGenerated G) (p : ℕ) :
  IsOpen ↑(TauCeti.ContinuousAut.mapQuotient ⋯).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContinuousAut.isOpen_ker_mapQuotient_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.html#TauCeti.ContinuousAut.isOpen_ker_mapQuotient_proPFrattini).

## Sources

- [Tau Ceti documentation: `TauCeti.ContinuousAut.isOpen_ker_mapQuotient_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.html#TauCeti.ContinuousAut.isOpen_ker_mapQuotient_proPFrattini)
- [Source of `TauCeti.ContinuousAut.isOpen_ker_mapQuotient_proPFrattini` in TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/ContinuousAut/ProP.lean#L82)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteArithmetic/STATUS.md)
