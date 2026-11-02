---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.Prime.sq_add_sq
mathlib_file: Mathlib/NumberTheory/SumTwoSquares.lean
---

# Sum of two squares

**Fermat's theorem on the sum of two squares**. Every prime not congruent to 3 mod 4 is the sum
of two squares. Also known as **Fermat's Christmas theorem**.

```lean
Nat.Prime.sq_add_sq {p : ℕ} [Fact (Nat.Prime p)] (hp : p % 4 ≠ 3) : ∃ a b, a ^ 2 + b ^ 2 = p
```

## Depends on

- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [Associative algebra over a commutative ring](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Bezout’s Theorem](../../../hundred-theorems/part-03/bezouts-theorem.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic of a ring](../field-theory/characteristic-of-a-ring.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Cyclic group](../group-theory/part-01/cyclic-group.md)
- [Euler's totient function ($\varphi$)](../divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Frobenius morphism](../field-theory/frobenius-morphism.md)
- [Greatest common divisor](../divisibility-in-integral-domains/greatest-common-divisor.md)
- [Invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Isomorphism with $K^n$](../../linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Local ring](../rings/local-ring.md)
- [Noetherian ring](../rings/noetherian-ring.md)
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Product of rings](../../../undergraduate/ring-theory/fundamentals/product-of-rings.md)
- [Quotient group](../group-theory/part-01/quotient-group.md)
- [Quotient space (Basic definitions)](../../../undergraduate/group-theory/basic-definitions/quotient-space.md)
- [Roots of a polynomial](../polynomials-and-power-series/roots-of-a-polynomial.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Nat.Prime.sq_add_sq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.Prime.sq_add_sq)
- [Source of `Nat.Prime.sq_add_sq` in Mathlib/NumberTheory/SumTwoSquares.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/SumTwoSquares.lean#L34)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L142)
- [Freek Wiedijk's 100 theorems, no. 20](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L99)
- [1000+ theorems list: Q914517](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1070)
- [1000+ theorems project: Q914517](https://1000-plus.github.io/?length=-1#Q914517)
- [Wikipedia: Fermat's theorem on sums of two squares](https://en.wikipedia.org/wiki/Fermat's_theorem_on_sums_of_two_squares)
- [Wikidata: Q914517](https://www.wikidata.org/wiki/Q914517)
