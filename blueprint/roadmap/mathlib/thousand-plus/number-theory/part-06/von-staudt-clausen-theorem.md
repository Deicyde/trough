---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Bernoulli.vonStaudt_clausen
mathlib_file: Mathlib/NumberTheory/Bernoulli.lean
---

# Von Staudt–Clausen theorem

**von Staudt-Clausen theorem:** For any natural number $k$, the sum
$$B_{2k} + \sum_{p - 1 \mid 2k} \frac{1}{p}$$ is an integer.

```lean
Bernoulli.vonStaudt_clausen (k : ℕ) :
  bernoulli (2 * k) + ∑ p ∈ Finset.range (2 * k + 2) with Nat.Prime p ∧ p - 1 ∣ 2 * k, 1 / ↑p ∈
    Set.range Int.cast
```

## Depends on

- [Bernoulli numbers](../../../overview/general-algebra/number-theory/bernoulli-numbers.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [Bezout’s Theorem](../../../hundred-theorems/part-03/bezouts-theorem.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in.md)
- [Cyclic group](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md)
- [Euler's totient function ($\varphi$)](../../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function.md)
- [Greatest common divisor](../../../overview/general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Least common multiple](../../../overview/general-algebra/divisibility-in-integral-domains/least-common-multiple.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Quotient group](../../../overview/general-algebra/group-theory/part-01/quotient-group.md)
- [Quotient space](../../../undergraduate/group-theory/basic-definitions/quotient-space.md)
- [Roots of a polynomial](../../../overview/general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Subring](../../../overview/general-algebra/rings/subring.md)
- [Sum of kth powers](../../../hundred-theorems/part-04/sum-of-kth-powers.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Bernoulli.vonStaudt_clausen`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Bernoulli.html#Bernoulli.vonStaudt_clausen)
- [Source of `Bernoulli.vonStaudt_clausen` in Mathlib/NumberTheory/Bernoulli.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Bernoulli.lean#L666)
- [1000+ theorems list: Q3527230](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2565)
- [1000+ theorems project: Q3527230](https://1000-plus.github.io/?length=-1#Q3527230)
- [Wikipedia: Von Staudt–Clausen theorem](https://en.wikipedia.org/wiki/Von_Staudt%E2%80%93Clausen_theorem)
- [Wikidata: Q3527230](https://www.wikidata.org/wiki/Q3527230)
