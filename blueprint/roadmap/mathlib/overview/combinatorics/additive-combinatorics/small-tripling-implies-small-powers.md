# Small tripling implies small powers

If `A` is symmetric \(`A⁻¹ = A`\) and has small tripling, then `A` has small powers,
in the sense that `|A ^ m|` is at most `|A|` times a constant exponential in `m`.

See also `Finset.small_alternating_pow_of_small_tripling` for a version with a weaker constant but
which encompasses non-symmetric sets.

```lean
Finset.small_pow_of_small_tripling.{u_1} {G : Type u_1} [DecidableEq G] [Group G] {A : Finset G}
  {K : ℝ} {m : ℕ} (hm : 3 ≤ m) (hA : ↑(A ^ 3).card ≤ K * ↑A.card) (hAsymm : A⁻¹ = A) :
  ↑(A ^ m).card ≤ K ^ (m - 2) * ↑A.card
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Real number](../../general-algebra/numbers/real-number.md)

## Proof depends on

- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Finset.small_pow_of_small_tripling`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/SmallTripling.html#Finset.small_pow_of_small_tripling)
- [Source of `Finset.small_pow_of_small_tripling` in Mathlib/Combinatorics/Additive/SmallTripling.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/SmallTripling.lean#L167)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L548)
