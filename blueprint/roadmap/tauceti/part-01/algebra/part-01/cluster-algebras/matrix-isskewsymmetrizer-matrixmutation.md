---
declaration: theorem
origin: cited
lean: Matrix.IsSkewSymmetrizer.matrixMutation
statement: formalized
proof: formalized
---

# Matrix.IsSkewSymmetrizer.matrixMutation

A skew-symmetrizer of a square matrix is a skew-symmetrizer of each of its mutations.

```lean
Matrix.IsSkewSymmetrizer.matrixMutation.{u_3} {K : Type u_3} [DecidableEq K] {B : Matrix K K ℤ}
  {s : K → ℤ} (h : B.IsSkewSymmetrizer s) (k : K) :
  (TauCeti.matrixMutation (Function.Embedding.refl K) B k).IsSkewSymmetrizer s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.IsSkewSymmetrizer.matrixMutation`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.html#Matrix.IsSkewSymmetrizer.matrixMutation).

## Sources

- [Tau Ceti documentation: `Matrix.IsSkewSymmetrizer.matrixMutation`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.html#Matrix.IsSkewSymmetrizer.matrixMutation)
- [Source of `Matrix.IsSkewSymmetrizer.matrixMutation` in TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.lean#L226)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
