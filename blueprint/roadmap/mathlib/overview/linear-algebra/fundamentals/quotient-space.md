# Quotient space (Fundamentals)

The quotient of a module `M` by a submodule `p ⊆ M`.

```lean
Submodule.hasQuotient.{u_1, u_2} {R : Type u_1} {M : Type u_2} [Ring R] [AddCommGroup M]
  [_root_.Module R M] : HasQuotient M (Submodule R M)
```

## Depends on

- [Integer](../../general-algebra/numbers/integer.md)
- [Module](module.md)
- [Ring](../../general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `Submodule.hasQuotient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Quotient/Defs.html#Submodule.hasQuotient)
- [Source of `Submodule.hasQuotient` in Mathlib/LinearAlgebra/Quotient/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/Quotient/Defs.lean#L53)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L173)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L10)
