---
declaration: structure
origin: cited
lean: Graph.EarDecomposition
statement: formalized
---

# Graph.EarDecomposition

A finite ear decomposition in `G`, indexed by its final graph `H`.

The stage sequence and successor equations determine the construction completely.  In
particular, a term of `G.EarDecomposition G` covers every actual vertex and edge of `G`.

```lean
Graph.EarDecomposition.{u, v} {α : Type u} {β : Type v} (G H : Graph α β) : Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Graph.EarDecomposition`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Ear/Basic.html#Graph.EarDecomposition).

## Sources

- [Tau Ceti documentation: `Graph.EarDecomposition`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Ear/Basic.html#Graph.EarDecomposition)
- [Source of `Graph.EarDecomposition` in TauCeti/Combinatorics/Graph/Connectivity/Ear/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Graph/Connectivity/Ear/Basic.lean#L558)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
