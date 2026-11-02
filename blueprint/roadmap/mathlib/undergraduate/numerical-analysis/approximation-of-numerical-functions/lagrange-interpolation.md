---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Lagrange.interpolate
mathlib_file: Mathlib/LinearAlgebra/Lagrange.lean
---

# Lagrange interpolation

Lagrange interpolation: given a finset `s : Finset ι`, a nodal map `v : ι → F` injective on
`s` and a value function `r : ι → F`, `interpolate s v r` is the unique
polynomial of degree `< #s` that takes value `r i` on `v i` for all `i` in `s`.

```lean
Lagrange.interpolate.{u_1, u_2} {F : Type u_1} [Field F] {ι : Type u_2} [DecidableEq ι]
  (s : Finset ι) (v : ι → F) : (ι → F) →ₗ[F] Polynomial F
```

## Depends on

- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Sources

- [Mathlib documentation: `Lagrange.interpolate`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Lagrange.html#Lagrange.interpolate)
- [Source of `Lagrange.interpolate` in Mathlib/LinearAlgebra/Lagrange.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Lagrange.lean#L294)
- [Mathlib undergraduate list: Numerical Analysis › Approximation of numerical functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L666)
- [Mathlib undergraduate list: Numerical Analysis › Approximation of numerical functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L667)
