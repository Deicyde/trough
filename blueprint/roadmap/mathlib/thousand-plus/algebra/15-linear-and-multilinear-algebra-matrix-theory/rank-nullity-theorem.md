---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: LinearMap.rank_range_add_rank_ker
mathlib_file: Mathlib/LinearAlgebra/Dimension/RankNullity.lean
---

# Rank–nullity theorem

The **rank-nullity theorem**

```lean
LinearMap.rank_range_add_rank_ker.{u, u_1} {R : Type u_1} {M M₁ : Type u} [Ring R] [AddCommGroup M]
  [AddCommGroup M₁] [_root_.Module R M] [_root_.Module R M₁] [HasRankNullity.{u, u_1} R]
  (f : M →ₗ[R] M₁) : Module.rank R ↥f.range + Module.rank R ↥f.ker = Module.rank R M
```

## Depends on

- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Quotient space (Fundamentals)](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `LinearMap.rank_range_add_rank_ker`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dimension/RankNullity.html#LinearMap.rank_range_add_rank_ker)
- [Source of `LinearMap.rank_range_add_rank_ker` in Mathlib/LinearAlgebra/Dimension/RankNullity.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Dimension/RankNullity.lean#L81)
- [1000+ theorems list: Q303402](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L356)
- [1000+ theorems project: Q303402](https://1000-plus.github.io/all.html?length=-1#Q303402)
- [Wikipedia: Rank–nullity theorem](https://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem)
- [Wikidata: Q303402](https://www.wikidata.org/wiki/Q303402)
