---
declaration: def
origin: cited
lean: TauCeti.ExchangeMatrix.principalExtension
statement: formalized
---

# TauCeti.ExchangeMatrix.principalExtension

The principal extension of a square exchange matrix, obtained by appending an identity
block of frozen rows.

```lean
TauCeti.ExchangeMatrix.principalExtension.{u_1} {K : Type u_1} [DecidableEq K]
  (B : TauCeti.ExchangeMatrix (Function.Embedding.refl K)) :
  TauCeti.ExchangeMatrix Function.Embedding.inl
```

## Depends on

- [TauCeti.ExchangeMatrix](tauceti-exchangematrix.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExchangeMatrix.principalExtension`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Compatibility.html#TauCeti.ExchangeMatrix.principalExtension).

## Sources

- [Tau Ceti documentation: `TauCeti.ExchangeMatrix.principalExtension`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Compatibility.html#TauCeti.ExchangeMatrix.principalExtension)
- [Source of `TauCeti.ExchangeMatrix.principalExtension` in TauCeti/Algebra/Cluster/ExchangeMatrix/Compatibility.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Cluster/ExchangeMatrix/Compatibility.lean#L152)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
