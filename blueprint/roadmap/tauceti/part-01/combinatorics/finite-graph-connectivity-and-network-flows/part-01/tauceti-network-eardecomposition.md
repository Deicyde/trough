---
declaration: structure
origin: cited
lean: TauCeti.Network.EarDecomposition
statement: formalized
---

# TauCeti.Network.EarDecomposition

A finite directed ear decomposition of the subnetwork `T`. It starts at one vertex and records
the subnetwork after every prefix, together with the ear adjoined at each successor stage.

```lean
TauCeti.Network.EarDecomposition.{u, w, u_1} {K : Type w} {V : Type u} [LE K]
  {N : TauCeti.Network K V} (T : N.Subnetwork) : Type (max u u_1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Network.EarDecomposition`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Ear/Basic.html#TauCeti.Network.EarDecomposition).

## Sources

- [Tau Ceti documentation: `TauCeti.Network.EarDecomposition`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Ear/Basic.html#TauCeti.Network.EarDecomposition)
- [Source of `TauCeti.Network.EarDecomposition` in TauCeti/Combinatorics/Network/Ear/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Network/Ear/Basic.lean#L237)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
