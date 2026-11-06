---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.inverse_triangle_sum
mathlib_file: Archive/Wiedijk100Theorems/InverseTriangleSum.lean
---

# Sum of the Reciprocals of the Triangular Numbers

**Sum of the Reciprocals of the Triangular Numbers**

```lean
Theorems100.inverse_triangle_sum (n : ℕ) :
  ∑ k ∈ Finset.range n, 2 / (↑k * (↑k + 1)) = if n = 0 then 0 else 2 - 2 / ↑n
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Rational number](../../overview/general-algebra/numbers/rational-number.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Field $\Q$ of rational numbers](../../undergraduate/ring-theory/field-theory/field-q-of-rational-numbers.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Theorems100.inverse_triangle_sum`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/InverseTriangleSum.html#Theorems100.inverse_triangle_sum)
- [Source of `Theorems100.inverse_triangle_sum` in Archive/Wiedijk100Theorems/InverseTriangleSum.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/InverseTriangleSum.lean#L29)
- [Freek Wiedijk's 100 theorems, no. 42](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L219)
