---
declaration: theorem
origin: cited
lean: Matrix.rank_add_rank_le_rank_mul_add_card
statement: formalized
proof: formalized
---

# Sylvester's rank inequality

for an `m × n` matrix `A` and an `n × o` matrix `B` over a
field, `rank A + rank B ≤ rank (A * B) + n`. Equivalently, multiplying by `A` lowers the rank of
`B` by at most the nullity of `A`.

```lean
Matrix.rank_add_rank_le_rank_mul_add_card.{u_1, u_2, u_3, u_4} {K : Type u_1} [Field K]
  {m : Type u_2} {n : Type u_3} [Fintype n] {o : Type u_4} [Fintype o] (A : Matrix m n K)
  (B : Matrix n o K) : A.rank + B.rank ≤ (A * B).rank + Fintype.card n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.rank_add_rank_le_rank_mul_add_card`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Rank.html#Matrix.rank_add_rank_le_rank_mul_add_card).

## Sources

- [Tau Ceti documentation: `Matrix.rank_add_rank_le_rank_mul_add_card`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Rank.html#Matrix.rank_add_rank_le_rank_mul_add_card)
- [Source of `Matrix.rank_add_rank_le_rank_mul_add_card` in TauCeti/LinearAlgebra/Matrix/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/Rank.lean#L337)
