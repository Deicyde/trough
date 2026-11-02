---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MvPolynomial.uniqueFactorizationMonoid
mathlib_file: Mathlib/RingTheory/Polynomial/UniqueFactorization.lean
---

# $A[{X_i}]$ is a UFD when $A$ is a UFD

Mathlib states this as `MvPolynomial.uniqueFactorizationMonoid`.

```lean
MvPolynomial.uniqueFactorizationMonoid.{u, v} (σ : Type v) {D : Type u} [CommRing D]
  [UniqueFactorizationMonoid D] : UniqueFactorizationMonoid (MvPolynomial σ D)
```

## Depends on

- [Polynomial in several indeterminates](polynomial-in-several-indeterminates.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Proof depends on

- [$A\[X\]$ has gcd and lcm if $A$ does](a-x-has-gcd-and-lcm-if-a-does.md)
- [Associative algebra over a commutative ring](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Group](../group-theory/part-01/group.md)
- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/polynomial-functions.md)
- [Prime ideal](../ideals-and-quotients/prime-ideal.md)

## Sources

- [Mathlib documentation: `MvPolynomial.uniqueFactorizationMonoid`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/UniqueFactorization.html#MvPolynomial.uniqueFactorizationMonoid)
- [Source of `MvPolynomial.uniqueFactorizationMonoid` in Mathlib/RingTheory/Polynomial/UniqueFactorization.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Polynomial/UniqueFactorization.lean#L128)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L103)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L147)
