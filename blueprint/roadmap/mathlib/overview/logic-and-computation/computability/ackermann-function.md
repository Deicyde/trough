# Ackermann function

The two-argument Ackermann function, defined so that

- `ack 0 n = n + 1`
- `ack (m + 1) 0 = ack m 1`
- `ack (m + 1) (n + 1) = ack m (ack (m + 1) n)`.

This is of interest as both a fast-growing function, and as an example of a recursive function that
isn't primitive recursive.

```lean
ack : ℕ → ℕ → ℕ
```

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `ack`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/Ackermann.html#ack)
- [Source of `ack` in Mathlib/Computability/Ackermann.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/Ackermann.lean#L58)
- [Mathlib overview: Logic and computation › Computability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L605)
