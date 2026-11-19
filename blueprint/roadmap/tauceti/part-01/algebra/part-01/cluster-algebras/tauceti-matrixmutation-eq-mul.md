---
declaration: theorem
origin: cited
lean: TauCeti.matrixMutation_eq_mul
statement: formalized
proof: formalized
---

# TauCeti.matrixMutation_eq_mul

Signed factorization of extended matrix mutation. Only the selected mutable diagonal
entry must vanish; the other entries need not be skew-symmetrizable.

```lean
TauCeti.matrixMutation_eq_mul.{u_1, u_2} {I : Type u_1} {K : Type u_2} [DecidableEq I]
  [DecidableEq K] (row : K ↪ I) (B : Matrix I K ℤ) (k : K) (ε : ℤ) [Fintype I] [Fintype K]
  (hkk : B (row k) k = 0) (hε : ε = 1 ∨ ε = -1) :
  TauCeti.matrixMutation row B k =
    TauCeti.matrixMutationLeft row B k ε * B * TauCeti.matrixMutationRight row B k ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.matrixMutation_eq_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Factorization.html#TauCeti.matrixMutation_eq_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.matrixMutation_eq_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Factorization.html#TauCeti.matrixMutation_eq_mul)
- [Source of `TauCeti.matrixMutation_eq_mul` in TauCeti/Algebra/Cluster/ExchangeMatrix/Factorization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Cluster/ExchangeMatrix/Factorization.lean#L204)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
