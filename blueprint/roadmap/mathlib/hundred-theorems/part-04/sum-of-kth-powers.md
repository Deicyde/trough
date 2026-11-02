---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: sum_range_pow, sum_Ico_pow
mathlib_file: Mathlib/NumberTheory/Bernoulli.lean
---

# Sum of kth powers

Mathlib records this with 2 declarations.

`sum_range_pow`: **Faulhaber's theorem** relating the **sum of p-th powers** to the Bernoulli numbers:
$$\sum_{k=0}^{n-1} k^p = \sum_{i=0}^p B_i\binom{p+1}{i}\frac{n^{p+1-i}}{p+1}.$$
See https://proofwiki.org/wiki/Faulhaber%27s_Formula and [orosi2018faulhaber] for
the proof provided here.

```lean
sum_range_pow (n p : ℕ) :
  ∑ k ∈ Finset.range n, ↑k ^ p =
    ∑ i ∈ Finset.range (p + 1), bernoulli i * ↑((p + 1).choose i) * ↑n ^ (p + 1 - i) / (↑p + 1)
```

`sum_Ico_pow`: Alternate form of **Faulhaber's theorem**, relating the sum of p-th powers to the Bernoulli
numbers:
$$\sum_{k=1}^{n} k^p = \sum_{i=0}^p (-1)^iB_i\binom{p+1}{i}\frac{n^{p+1-i}}{p+1}.$$
Deduced from `sum_range_pow`.

```lean
sum_Ico_pow (n p : ℕ) :
  ∑ k ∈ Finset.Ico 1 (n + 1), ↑k ^ p =
    ∑ i ∈ Finset.range (p + 1), bernoulli' i * ↑((p + 1).choose i) * ↑n ^ (p + 1 - i) / (↑p + 1)
```

## Depends on

- [Bernoulli numbers](../../overview/general-algebra/number-theory/bernoulli-numbers.md)

## Proof depends on

- [Array](../../overview/data-structures/list-like-structures/array.md)
- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Euclidean domain](../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Field $\R$ of real numbers](../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Group](../../overview/general-algebra/group-theory/part-01/group.md)
- [Induced topology](../../overview/topology/general-topology/part-01/induced-topology.md)
- [Invertible elements](../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Linear map](../../overview/linear-algebra/fundamentals/linear-map.md)
- [Metric structure](../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Power series](../../overview/general-algebra/polynomials-and-power-series/power-series.md)
- [Product of rings](../../undergraduate/ring-theory/fundamentals/product-of-rings.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [The Binomial Theorem](../part-03/the-binomial-theorem.md)

## Sources

- [Mathlib documentation: `sum_range_pow`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Bernoulli.html#sum_range_pow)
- [Source of `sum_range_pow` in Mathlib/NumberTheory/Bernoulli.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Bernoulli.lean#L291)
- [Mathlib documentation: `sum_Ico_pow`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Bernoulli.html#sum_Ico_pow)
- [Source of `sum_Ico_pow` in Mathlib/NumberTheory/Bernoulli.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Bernoulli.lean#L356)
- [Freek Wiedijk's 100 theorems, no. 77](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L389)
