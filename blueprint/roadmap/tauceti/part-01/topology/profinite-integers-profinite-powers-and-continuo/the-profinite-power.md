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
- [Source of `TauCeti.zpowHat` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.lean#L80)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteArithmetic/STATUS.md)
