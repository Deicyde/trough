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
- [Source of `Graph.EarDecomposition` in TauCeti/Combinatorics/Graph/Connectivity/Ear/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Connectivity/Ear/Basic.lean#L364)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
