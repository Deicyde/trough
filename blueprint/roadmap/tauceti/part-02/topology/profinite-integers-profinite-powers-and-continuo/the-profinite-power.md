---
declaration: def
origin: cited
lean: TauCeti.zpowHat
statement: formalized
---

# The profinite power

**The profinite power** `x ^ᶻ a` of an element `x` of a profinite group by a profinite integer
`a`: the value at `a`, read multiplicatively, of the continuous homomorphism `zHat.lift x` from
the profinite integers to `G` that sends the generator to `x`.

```lean
TauCeti.zpowHat.{u, v} {G : Type v} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (x : G)
  (a : Additive ↑TauCeti.zHat.toProfinite.toTop) : G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zpowHat`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.html#TauCeti.zpowHat).

## Sources

- [Tau Ceti documentation: `TauCeti.zpowHat`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.html#TauCeti.zpowHat)
- [Source of `TauCeti.zpowHat` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.lean#L80)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteArithmetic/STATUS.md)
