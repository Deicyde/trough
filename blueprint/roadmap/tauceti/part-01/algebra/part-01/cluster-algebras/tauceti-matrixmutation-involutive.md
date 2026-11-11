---
declaration: theorem
origin: cited
lean: TauCeti.matrixMutation_involutive
statement: formalized
proof: formalized
---

# TauCeti.matrixMutation_involutive

Mutation in a fixed direction is an involution.

```lean
TauCeti.matrixMutation_involutive.{u_1, u_3} {I : Type u_1} {K : Type u_3} [DecidableEq I]
  [DecidableEq K] (row : K ↪ I) (k : K) :
  Function.Involutive fun B => TauCeti.matrixMutation row B k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.matrixMutation_involutive`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.html#TauCeti.matrixMutation_involutive).

## Sources

- [Tau Ceti documentation: `TauCeti.matrixMutation_involutive`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.html#TauCeti.matrixMutation_involutive)
- [Source of `TauCeti.matrixMutation_involutive` in TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Cluster/ExchangeMatrix/Mutation.lean#L133)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
