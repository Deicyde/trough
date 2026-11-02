---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Padic
mathlib_file: Mathlib/NumberTheory/Padics/PadicNumbers.lean
---

# $p$-adic number

The `p`-adic numbers `ℚ_[p]` are the Cauchy completion of `ℚ` with respect to the `p`-adic norm.

```lean
Padic (p : ℕ) [Fact (Nat.Prime p)] : Type
```

## Depends on

- [Field $\Q$ of rational numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-rational-numbers.md)
- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)

## Sources

- [Mathlib documentation: `Padic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic)
- [Source of `Padic` in Mathlib/NumberTheory/Padics/PadicNumbers.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Padics/PadicNumbers.lean#L542)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L28)
