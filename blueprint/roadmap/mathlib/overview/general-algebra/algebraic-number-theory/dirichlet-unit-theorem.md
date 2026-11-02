---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: NumberField.Units.exist_unique_eq_mul_prod
mathlib_file: Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean
---

# Dirichlet unit theorem

**Dirichlet Unit Theorem**. Any unit `x` of `𝓞 K` can be written uniquely as the product of
a root of unity and powers of the units of the fundamental system `fundSystem`.

```lean
NumberField.Units.exist_unique_eq_mul_prod.{u_1} (K : Type u_1) [Field K] [NumberField K]
  (x : (NumberField.RingOfIntegers K)ˣ) :
  ∃! ζe, x = ↑ζe.1 * ∏ i, NumberField.Units.fundSystem K i ^ ζe.2 i
```

## Depends on

- [Dirichlet's unit theorem](../../../thousand-plus/number-theory/part-02/dirichlets-unit-theorem.md)

## Sources

- [Mathlib documentation: `NumberField.Units.exist_unique_eq_mul_prod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.exist_unique_eq_mul_prod)
- [Source of `NumberField.Units.exist_unique_eq_mul_prod` in Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean#L504)
- [Mathlib overview: General algebra › Algebraic Number Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L158)
