---
declaration: def
origin: cited
lean: TauCeti.residualUpdate
statement: formalized
---

# TauCeti.residualUpdate

The *residual update* of `f` by a residual assignment `r`: the value on each arrow `e` is
`f e + r e⁺ - r e⁻`, where `e⁺ = Sum.inl e` and `e⁻ = Sum.inr e` are its residual copies.

```lean
TauCeti.residualUpdate.{u, v, w} {V : Type u} {Q : V → V → Type v} {K : Type w} [AddCommGroup K]
  (f : TauCeti.Assignment Q K) (r : TauCeti.Assignment (TauCeti.ResidualHom Q) K) :
  TauCeti.Assignment Q K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.residualUpdate`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Residual.html#TauCeti.residualUpdate).

## Sources

- [Tau Ceti documentation: `TauCeti.residualUpdate`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Residual.html#TauCeti.residualUpdate)
- [Source of `TauCeti.residualUpdate` in TauCeti/Combinatorics/Network/Residual.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Network/Residual.lean#L180)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
