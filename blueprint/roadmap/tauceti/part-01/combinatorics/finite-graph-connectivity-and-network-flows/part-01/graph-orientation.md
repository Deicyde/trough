---
declaration: structure
origin: cited
lean: Graph.Orientation
statement: formalized
---

# Graph.Orientation

An orientation of a multigraph chooses a tail and head for every actual edge, compatible
with that edge's incidence. Parallel edges retain separate choices, while a loop necessarily
has the same tail and head.

```lean
Graph.Orientation.{u, v} {V : Type u} {E : Type v} (G : Graph V E) : Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Graph.Orientation`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Basic.html#Graph.Orientation).

## Sources

- [Tau Ceti documentation: `Graph.Orientation`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Basic.html#Graph.Orientation)
- [Source of `Graph.Orientation` in TauCeti/Combinatorics/Graph/Orientation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Orientation/Basic.lean#L41)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
