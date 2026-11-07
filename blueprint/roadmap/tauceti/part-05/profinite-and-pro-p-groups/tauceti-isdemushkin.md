---
declaration: structure
origin: cited
lean: TauCeti.IsDemushkin
statement: formalized
---

# TauCeti.IsDemushkin

**The Demushkin predicate** (Labute, p. 106), for a prime `p` and a topological group `G`: a
pro-`p` group whose `H¹(G, 𝔽_p)` is finite-dimensional, whose `H²(G, 𝔽_p)` is one-dimensional, and
on which the cup product `H¹(G, 𝔽_p) × H¹(G, 𝔽_p) → H²(G, 𝔽_p)` is nondegenerate on both sides.
The primality of `p` is a hypothesis of the predicate. Profiniteness is not: no field mentions
`CompactSpace G` or `TotallyDisconnectedSpace G`, so Lean leaves those section instances out of
the structure, and the predicate is also defined for topological groups that are not profinite.
The presentation results below assume both; on profinite groups, its intended mathematical
domain, this is Labute's notion. The pro-`p` hypothesis is a field, so that no theorem about
Demushkin groups applies to a group that satisfies only the cohomological clauses. Finite
generation is a consequence, `IsDemushkin.isTopologicallyFinitelyGenerated`, and is not assumed.

```lean
TauCeti.IsDemushkin.{u} (p : ℕ) [Fact (Nat.Prime p)] (G : Type u) [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Basic.html#TauCeti.IsDemushkin).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Basic.html#TauCeti.IsDemushkin)
- [Source of `TauCeti.IsDemushkin` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Basic.lean#L74)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
