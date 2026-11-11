---
declaration: structure
origin: cited
lean: TauCeti.ExchangeMatrix
statement: formalized
---

# TauCeti.ExchangeMatrix

An *exchange matrix* along the embedding `row : K ↪ I` of the mutable indices `K` into the
index type `I`: an integer matrix with rows indexed by `I` and columns by `K`, together with a
chosen symmetrizer of its *principal block*, the square matrix formed by the mutable rows.

The rows outside the range of `row` are the frozen rows; no condition is imposed on them. A
square exchange matrix, with no frozen rows, is an exchange matrix along
`Function.Embedding.refl K`.

```lean
TauCeti.ExchangeMatrix.{u_1, u_4} {I : Type u_1} {K : Type u_4} (row : K ↪ I) : Type (max u_1 u_4)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ExchangeMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Basic.html#TauCeti.ExchangeMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.ExchangeMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Basic.html#TauCeti.ExchangeMatrix)
- [Source of `TauCeti.ExchangeMatrix` in TauCeti/Algebra/Cluster/ExchangeMatrix/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Cluster/ExchangeMatrix/Basic.lean#L151)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
