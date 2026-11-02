---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: char_dvd_card_solutions_of_sum_lt
mathlib_file: Mathlib/FieldTheory/ChevalleyWarning.lean
---

# Chevalley–Warning theorem

The **Chevalley–Warning theorem**, finitary version.
Let `(f i)` be a finite family of multivariate polynomials
in finitely many variables (`X s`, `s : σ`) over a finite field of characteristic `p`.
Assume that the sum of the total degrees of the `f i` is less than the cardinality of `σ`.
Then the number of common solutions of the `f i` is divisible by `p`.

```lean
char_dvd_card_solutions_of_sum_lt.{u_1, u_2, u_3} {K : Type u_1} {σ : Type u_2} {ι : Type u_3}
  [Fintype K] [Field K] [Fintype σ] [DecidableEq σ] [DecidableEq K] (p : ℕ) [CharP K p]
  {s : Finset ι} {f : ι → MvPolynomial σ K} (h : ∑ i ∈ s, (f i).totalDegree < Fintype.card σ) :
  p ∣ Fintype.card { x // ∀ i ∈ s, (MvPolynomial.eval x) (f i) = 0 }
```

## Depends on

- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Polynomial in several indeterminates](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Ring morphism](../../../overview/general-algebra/rings/ring-morphism.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Cyclic group](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md)
- [Euler's totient function ($\varphi$)](../../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Quotient group](../../../overview/general-algebra/group-theory/part-01/quotient-group.md)
- [Quotient space (Basic definitions)](../../../undergraduate/group-theory/basic-definitions/quotient-space.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Roots of a polynomial](../../../overview/general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)

## Sources

- [Mathlib documentation: `char_dvd_card_solutions_of_sum_lt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/ChevalleyWarning.html#char_dvd_card_solutions_of_sum_lt)
- [Source of `char_dvd_card_solutions_of_sum_lt` in Mathlib/FieldTheory/ChevalleyWarning.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/ChevalleyWarning.lean#L105)
- [1000+ theorems list: Q720469](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L780)
- [1000+ theorems project: Q720469](https://1000-plus.github.io/?length=-1#Q720469)
- [Wikipedia: Chevalley–Warning theorem](https://en.wikipedia.org/wiki/Chevalley%E2%80%93Warning_theorem)
- [Wikidata: Q720469](https://www.wikidata.org/wiki/Q720469)
