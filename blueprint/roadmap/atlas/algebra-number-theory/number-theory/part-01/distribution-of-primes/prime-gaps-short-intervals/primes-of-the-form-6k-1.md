---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.DistinctEisensteinPrimesWanted.exists_prime_modEq_five_between, MathlibExt.NumberTheory.DistinctEisensteinPrimesWanted.eq_sum_distinct_primes_modEq_five
statement: formalized
---

# Primes of the form 6k − 1

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-of-the-form-6k-1/index.html).

## Breusch's theorem for primes of the form $6k - 1$

For every natural number $x \ge 7$
there is a prime $p$ with $x < p < 2x$ and $p \equiv 5 \pmod 6$, that is, a prime of the form
$6k - 1$ strictly between $x$ and $2x$.

## Sources

- Elchin Hasanalizade, "Sums of Distinct Eisenstein Primes", Lemma 2 (citing Breusch).

Stated but not proved: `MathlibExt.NumberTheory.DistinctEisensteinPrimesWanted.exists_prime_modEq_five_between` is written with `theorem_wanted` in [WantedExt/NumberTheory/DistinctEisensteinPrimesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DistinctEisensteinPrimesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-of-the-form-6k-1/index.html#exists-prime-mod-eq-five-between).

## Makowski's theorem on sums of distinct primes of the form $6k - 1$

Every natural number
$n > 161$ is the sum of the elements of some finite set of primes $p$ with $p \equiv 5 \pmod 6$;
that is, $n$ is a sum of distinct primes of the form $6k - 1$.

## Sources

- Elchin Hasanalizade, "Sums of Distinct Eisenstein Primes", Lemma 3 (citing Makowski).

Stated but not proved: `MathlibExt.NumberTheory.DistinctEisensteinPrimesWanted.eq_sum_distinct_primes_modEq_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/DistinctEisensteinPrimesWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DistinctEisensteinPrimesWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-of-the-form-6k-1/index.html#eq-sum-distinct-primes-mod-eq-five).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primes of the form 6k − 1](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-of-the-form-6k-1/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-of-the-form-6k-1)
