---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Pell.pell
mathlib_file: Mathlib/NumberTheory/PellMatiyasevic.lean
---

# Solutions to Pell's equation

The Pell sequences, i.e. the sequence of integer solutions to `x ^ 2 - d * y ^ 2 = 1`, where
`d = a ^ 2 - 1`, defined together in mutual recursion.

```lean
Pell.pell {a : ℕ} (a1 : 1 < a) : ℕ → ℕ × ℕ
```

## Depends on

- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Pell.pell`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/PellMatiyasevic.html#Pell.pell)
- [Source of `Pell.pell` in Mathlib/NumberTheory/PellMatiyasevic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/PellMatiyasevic.lean#L102)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L145)
