---
declaration: def
origin: cited
lean: TauCeti.ArrowWalk.splitEquiv
statement: formalized
---

# TauCeti.ArrowWalk.splitEquiv

Lifting identifies the walks from `s` to `t` with the walks in the split network from the
entrance of `s` to the entrance (`b = false`) or exit (`b = true`) of `t`; the inverse is
projection.

```lean
TauCeti.ArrowWalk.splitEquiv.{u, v} {V : Type u} (Q : V → V → Type v) (s t : V) (b : Bool) :
  TauCeti.ArrowWalk Q s t ≃ TauCeti.ArrowWalk (TauCeti.SplitHom Q) (s, false) (t, b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ArrowWalk.splitEquiv`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/VertexSplitting.html#TauCeti.ArrowWalk.splitEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ArrowWalk.splitEquiv`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/VertexSplitting.html#TauCeti.ArrowWalk.splitEquiv)
- [Source of `TauCeti.ArrowWalk.splitEquiv` in TauCeti/Combinatorics/Network/VertexSplitting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/VertexSplitting.lean#L263)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
