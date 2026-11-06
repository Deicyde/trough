# Minimal polynomial

Suppose `x : B`, where `B` is an `A`-algebra.

The minimal polynomial `minpoly A x` of `x`
is a monic polynomial with coefficients in `A` of smallest degree that has `x` as its root,
if such exists (`IsIntegral A x`) or zero otherwise.

For example, if `V` is a `𝕜`-vector space for some field `𝕜` and `f : V →ₗ[𝕜] V` then
the minimal polynomial of `f` is `minpoly 𝕜 f`.

```lean
minpoly.{u_1, u_2} (A : Type u_1) {B : Type u_2} [CommRing A] [Ring B] [Algebra A B] (x : B) :
  Polynomial A
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Polynomial in one indeterminate](../../general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Sources

- [Mathlib documentation: `minpoly`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Minpoly/Basic.html#minpoly)
- [Source of `minpoly` in Mathlib/FieldTheory/Minpoly/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/Minpoly/Basic.lean#L31)
- [Mathlib overview: Linear algebra › Endomorphism polynomials](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L195)
- [Mathlib undergraduate list: Linear algebra › Endomorphism polynomials](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L55)
