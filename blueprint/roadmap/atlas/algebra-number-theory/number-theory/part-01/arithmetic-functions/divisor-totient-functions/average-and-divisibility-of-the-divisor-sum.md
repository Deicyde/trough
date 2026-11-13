---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.AmicableWanted.tendsto_density_not_dvd_sigma, MathlibExt.NumberTheory.AmicableWanted.sum_sigma_div_lt
statement: formalized
---

# Average and divisibility of the divisor sum

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/average-and-divisibility-of-the-divisor-sum/index.html).

## A fixed positive integer divides the divisor sum of almost every natural number

For
a natural number $l$ let $\sigma(l)$ denote the sum of the positive divisors of $l$, with
$\sigma(0) = 0$. Then for every positive integer $N$, the set of natural numbers $l$ such
that $N$ does not divide $\sigma(l)$ has natural density $0$.

## Sources

- Stoyan Dimitrov, "Generalizations of Amicable Numbers", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.AmicableWanted.tendsto_density_not_dvd_sigma` is written with `theorem_wanted` in [WantedExt/NumberTheory/AmicableWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AmicableWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/average-and-divisibility-of-the-divisor-sum/index.html#tendsto-density-not-dvd-sigma).

## Linear bound for the partial sums of the abundancy index

For a positive integer
$n$ let $\sigma(n)$ denote the sum of the positive divisors of $n$, and let
$\zeta(2) = \sum_{n=1}^{\infty} 1/n^2$. Then for every real number $x \ge 1$,

$$\sum_{n=1}^{\lfloor x \rfloor} \frac{\sigma(n)}{n} < \zeta(2)\, x.$$

## Sources

- Stoyan Dimitrov, "Generalizations of Amicable Numbers", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.AmicableWanted.sum_sigma_div_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/AmicableWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AmicableWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/average-and-divisibility-of-the-divisor-sum/index.html#sum-sigma-div-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Average and divisibility of the divisor sum](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/average-and-divisibility-of-the-divisor-sum/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/average-and-divisibility-of-the-divisor-sum)
