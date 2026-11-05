---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.Real.tendsto_sum_one_div_prime_atTop, not_summable_one_div_on_primes
mathlib_file: Archive/Wiedijk100Theorems/SumOfPrimeReciprocalsDiverges.lean
---

# Divergence of the Prime Reciprocal Series

Mathlib records this with 2 declarations.

`Theorems100.Real.tendsto_sum_one_div_prime_atTop`.

```lean
Theorems100.Real.tendsto_sum_one_div_prime_atTop :
  Filter.Tendsto (fun n => ∑ p ∈ Finset.range n with Nat.Prime p, 1 / ↑p) Filter.atTop Filter.atTop
```

`not_summable_one_div_on_primes`: The sum over the reciprocals of the primes diverges.

```lean
not_summable_one_div_on_primes : ¬Summable ({p | Nat.Prime p}.indicator fun n => 1 / ↑n)
```

## Depends on

- [Bornology](../../overview/analysis/topological-vector-spaces/bornology.md)
- [Infinite sum](../../overview/topology/topological-algebra/infinite-sum.md)
- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Order (Real numbers)](../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuous function](../../overview/topology/general-topology/part-01/continuous-function.md)
- [Metric space](../../overview/topology/metric-spaces/metric-space.md)
- [Order topology](../../overview/topology/topological-algebra/order-topology.md)
- [The Infinitude of Primes](../part-01/the-infinitude-of-primes.md)
- [The Number of Subsets of a Set](../part-03/the-number-of-subsets-of-a-set.md)
- [Uniformly continuous function](../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Theorems100.Real.tendsto_sum_one_div_prime_atTop`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/SumOfPrimeReciprocalsDiverges.html#Theorems100.Real.tendsto_sum_one_div_prime_atTop)
- [Source of `Theorems100.Real.tendsto_sum_one_div_prime_atTop` in Archive/Wiedijk100Theorems/SumOfPrimeReciprocalsDiverges.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/SumOfPrimeReciprocalsDiverges.lean#L198)
- [Mathlib documentation: `not_summable_one_div_on_primes`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumPrimeReciprocals.html#not_summable_one_div_on_primes)
- [Source of `not_summable_one_div_on_primes` in Mathlib/NumberTheory/SumPrimeReciprocals.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/SumPrimeReciprocals.lean#L101)
- [Freek Wiedijk's 100 theorems, no. 81](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L415)
