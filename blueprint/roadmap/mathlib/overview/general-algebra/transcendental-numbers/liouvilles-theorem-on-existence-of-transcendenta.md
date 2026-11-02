---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: transcendental_liouvilleNumber
mathlib_file: Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleNumber.lean
---

# Liouville's theorem on existence of transcendental numbers

Mathlib states this as `transcendental_liouvilleNumber`.

```lean
transcendental_liouvilleNumber {m : ℕ} (hm : 2 ≤ m) : Transcendental ℤ (liouvilleNumber ↑m)
```

## Depends on

- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Transcendental elements](../../../undergraduate/ring-theory/field-theory/part-01/transcendental-elements.md)
- [Uniform space](../../topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Liouville’s Theorem and the Construction of Transcendental Numbers](../../../hundred-theorems/part-01/liouvilles-theorem-and-the-construction-of-trans.md)

## Sources

- [Mathlib documentation: `transcendental_liouvilleNumber`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleNumber.html#transcendental_liouvilleNumber)
- [Source of `transcendental_liouvilleNumber` in Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleNumber.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleNumber.lean#L191)
- [Mathlib overview: General algebra › Transcendental numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L154)
