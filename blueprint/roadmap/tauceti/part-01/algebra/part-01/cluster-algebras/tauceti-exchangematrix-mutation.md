---
declaration: def
origin: cited
lean: TauCeti.ExchangeMatrix.mutation
statement: formalized
---

# TauCeti.ExchangeMatrix.mutation

The *mutation* of an exchange matrix in direction `k`: the underlying matrix is mutated and
the symmetrizer is kept.

```lean
TauCeti.ExchangeMatrix.mutation.{u_1, u_3} {I : Type u_1} {K : Type u_3} [DecidableEq I]
  [DecidableEq K] {row : K ↪ I} (B : TauCeti.ExchangeMatrix row) (k : K) :
  TauCeti.ExchangeMatrix row
```

## Depends on

- [TauCeti.ExchangeMatrix](tauceti-exchangematrix.md)

## Proof depends on

- [Matrix.IsSkewSymmetrizer.matrixMutation](matrix-isskewsymmetrizer-matrixmutation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExchangeMatrix.mutation`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.html#TauCeti.ExchangeMatrix.mutation).

## Sources

- [Tau Ceti documentation: `TauCeti.ExchangeMatrix.mutation`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.html#TauCeti.ExchangeMatrix.mutation)
- [Source of `TauCeti.ExchangeMatrix.mutation` in TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.lean#L258)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
