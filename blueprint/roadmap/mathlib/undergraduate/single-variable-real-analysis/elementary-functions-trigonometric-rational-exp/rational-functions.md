# Rational functions

Evaluate a rational function `p` given a ring hom `f` from the scalar field
to the target and a value `x` for the variable in the target.

Fractions are reduced by clearing common denominators before evaluating:
`eval id 1 ((X^2 - 1) / (X - 1)) = eval id 1 (X + 1) = 2`, not `0 / 0 = 0`.

```lean
RatFunc.eval.{u} {K : Type u} [Field K] {L : Type u} [Field L] (f : K →+* L) (a : L)
  (p : RatFunc K) : L
```

## Depends on

- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Greatest common divisor](../../../overview/general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Least common multiple](../../../overview/general-algebra/divisibility-in-integral-domains/least-common-multiple.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Rational fraction fields with one indeterminate over a field](../../ring-theory/field-theory/rational-fraction-fields-with-one-indeterminate.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)

## Sources

- [Mathlib documentation: `RatFunc.eval`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/RatFunc/AsPolynomial.html#RatFunc.eval)
- [Source of `RatFunc.eval` in Mathlib/FieldTheory/RatFunc/AsPolynomial.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/RatFunc/AsPolynomial.lean#L139)
- [Mathlib undergraduate list: Single Variable Real Analysis › Elementary functions (trigonometric, rational, $\exp$, $\log$, etc)](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L331)
