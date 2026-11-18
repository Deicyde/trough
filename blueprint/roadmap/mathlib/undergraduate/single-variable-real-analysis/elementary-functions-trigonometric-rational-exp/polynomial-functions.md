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
- [Source of `Polynomial.eval` in Mathlib/Algebra/Polynomial/Eval/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Algebra/Polynomial/Eval/Defs.lean#L248)
- [Mathlib undergraduate list: Single Variable Real Analysis › Elementary functions (trigonometric, rational, $\exp$, $\log$, etc)](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L330)
