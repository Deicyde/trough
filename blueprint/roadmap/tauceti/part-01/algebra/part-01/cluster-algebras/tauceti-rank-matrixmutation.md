---
declaration: theorem
origin: cited
lean: TauCeti.rank_matrixMutation
statement: formalized
proof: formalized
---

# TauCeti.rank_matrixMutation

Mutation preserves rank after scalar change to any commutative ring. In particular,
choosing `R = ℚ` gives preservation of rational column rank.

```lean
TauCeti.rank_matrixMutation.{u_1, u_2, u_5} {I : Type u_1} {K : Type u_2} [DecidableEq I]
  [DecidableEq K] (row : K ↪ I) (B : Matrix I K ℤ) (k : K) [Fintype K] [Finite I] {R : Type u_5}
  [CommRing R] (hkk : B (row k) k = 0) :
  ((TauCeti.matrixMutation row B k).map ⇑(Int.castRingHom R)).rank =
    (B.map ⇑(Int.castRingHom R)).rank
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.matrixMutation_eq_mul](tauceti-matrixmutation-eq-mul.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.rank_matrixMutation`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Factorization.html#TauCeti.rank_matrixMutation).

## Sources

- [Tau Ceti documentation: `TauCeti.rank_matrixMutation`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Factorization.html#TauCeti.rank_matrixMutation)
- [Source of `TauCeti.rank_matrixMutation` in TauCeti/Algebra/Cluster/ExchangeMatrix/Factorization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Cluster/ExchangeMatrix/Factorization.lean#L228)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
