# Polynomial functions

`eval x p` is the evaluation of the polynomial `p` at `x`

```lean
Polynomial.eval.{u} {R : Type u} [Semiring R] (x : R) (p : Polynomial R) : R
```

## Depends on

- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Ring morphism](../../../overview/general-algebra/rings/ring-morphism.md)

## Sources

- [Mathlib documentation: `Polynomial.eval`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Eval/Defs.html#Polynomial.eval)
- [Source of `Polynomial.eval` in Mathlib/Algebra/Polynomial/Eval/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/Eval/Defs.lean#L247)
- [Mathlib undergraduate list: Single Variable Real Analysis › Elementary functions (trigonometric, rational, $\exp$, $\log$, etc)](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L330)
