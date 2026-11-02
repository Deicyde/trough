---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.bertrand
mathlib_file: Mathlib/NumberTheory/Bertrand.lean
---

# Bertrand’s Postulate

**Alias** of `Nat.exists_prime_lt_and_le_two_mul`.

---

**Bertrand's Postulate**: For any positive natural number, there is a prime which is greater than
it, but no more than twice as large.

```lean
Nat.bertrand (n : ℕ) (hn0 : n ≠ 0) : ∃ p, Nat.Prime p ∧ n < p ∧ p ≤ 2 * n
```

## Depends on

- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [$C^k$ function](../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Algebra of endomorphisms of a vector space](../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Cantor’s Theorem](../part-04/cantors-theorem.md)
- [Cardinal](../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../overview/topology/general-topology/part-01/closed-map.md)
- [Completion of an abelian topological group](../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Continuity (Complex-valued series)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/continuity.md)
- [Continuity of monotone functions](../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of-r/continuity-of-monotone-functions.md)
- [Convex function](../../overview/analysis/convexity/convex-function.md)
- [Derivative of the inverse of a function (Analysis)](../../overview/analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Derivative of the inverse of a function (Single Variable Real Analysis)](../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Existence of bases](../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Field $\C$ of complex numbers](../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Finite product of metric spaces](../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Intermediate value theorem](../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Kernel of a linear map](../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Limit point](../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Matrix exponential](../../undergraduate/linear-algebra/exponential/matrix-exponential.md)
- [Pointwise convergence](../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Power functions](../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)
- [Schroeder-Bernstein Theorem](../part-02/schroeder-bernstein-theorem.md)
- [Sequential space](../../overview/topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../part-04/sum-of-a-geometric-series.md)
- [Sum of subspaces](../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Binomial Theorem](../part-03/the-binomial-theorem.md)
- [The Fundamental Theorem of Arithmetic](../part-04/the-fundamental-theorem-of-arithmetic.md)
- [The Mean Value Theorem](../part-04/the-mean-value-theorem.md)
- [The Number of Subsets of a Set](../part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `Nat.bertrand`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Bertrand.html#Nat.bertrand)
- [Source of `Nat.bertrand` in Mathlib/NumberTheory/Bertrand.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Bertrand.lean#L243)
- [Freek Wiedijk's 100 theorems, no. 98](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L506)
- [1000+ theorems list: Q632546](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L647)
- [1000+ theorems project: Q632546](https://1000-plus.github.io/?length=-1#Q632546)
- [Wikipedia: Bertrand's postulate](https://en.wikipedia.org/wiki/Bertrand's_postulate)
- [Wikidata: Q632546](https://www.wikidata.org/wiki/Q632546)
