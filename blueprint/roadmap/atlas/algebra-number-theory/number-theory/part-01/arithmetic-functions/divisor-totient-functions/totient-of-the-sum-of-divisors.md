---
declaration: section
origin: cited
lean: MetaMathlibExt.card_free_of_prime_set_le_exp_neg_sum_inv, MetaMathlibExt.card_not_dvd_sigma_le, MetaMathlibExt.card_totient_sigma_ge_mul_le, MetaMathlibExt.card_totient_sigma_ge_div_isBigO, MetaMathlibExt.card_totient_sigma_gt_div_log_five_isBigO
statement: formalized
---

# Totient of the sum of divisors

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/totient-of-the-sum-of-divisors/index.html).

## Pollack–Pomerance sieve bound

There is an absolute constant $C > 0$ such that for every
set $P$ of primes and every real $x > 1$, the number of integers $n$ with $1 \le n \le x$ that
are divisible by no prime in $P$ is at most $C x \exp(-A_P(x))$, where
$A_P(x) = \sum_{p \in P,\ p \le x} 1/p$.

## Sources

- Anup B. Dixit and Saunak Bhattacharjee, *On the Distribution of φ(σ(n))*, INTEGERS 24 (2024), Article A65, Lemma 1, quoting Pollack and Pomerance, Lemma 3.

Stated but not proved: `MetaMathlibExt.card_free_of_prime_set_le_exp_neg_sum_inv` is written with `theorem_wanted` in [WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/totient-of-the-sum-of-divisors/index.html#card-free-of-prime-set-le-exp-neg-sum-in).

## Integers whose sum of divisors is not divisible by $p$

There is an absolute constant
$C > 0$ such that for every prime $p$ and every real $x \ge e^p$, the number of integers $n$ with
$1 \le n \le x$ for which $p$ does not divide the sum of divisors $\sigma(n)$ is at most
$C x (\log \log x / \log x)^{1/(p-1)}$.

## Sources

- Anup B. Dixit and Saunak Bhattacharjee, *On the Distribution of φ(σ(n))*, INTEGERS 24 (2024), Article A65, Lemma 3.

Stated but not proved: `MetaMathlibExt.card_not_dvd_sigma_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/totient-of-the-sum-of-divisors/index.html#card-not-dvd-sigma-le).

## Upper bound for the number of $n$ with $\varphi(\sigma(n)) \ge c n$

Write $\log_k$ for
the $k$-fold iterated natural logarithm, so $\log_3 x = \log \log \log x$, and let $\varphi$ be
Euler's totient function and $\sigma$ the sum of divisors. For every real $c > 0$ there is a
constant $C$ such that for all sufficiently large $x$, the number of integers $n$ with
$1 \le n \le x$ and $\varphi(\sigma(n)) \ge c n$ is at most

$$
\frac{\pi^2 x}{6 c \log_4 x} +
C \, \frac{x \log_3 x}{(\log x)^{1/\log_3 x} \log_4 x}.
$$

The bound is only claimed for large $x$ since it needs $\log_4 x > 0$, that is, $x > e^{e^e}$.

## Sources

- Anup B. Dixit and Saunak Bhattacharjee, *On the Distribution of φ(σ(n))*, INTEGERS 24 (2024), Article A65, Theorem 1.

Stated but not proved: `MetaMathlibExt.card_totient_sigma_ge_mul_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/totient-of-the-sum-of-divisors/index.html#card-totient-sigma-ge-mul-le).

## How often $\varphi(\sigma(n)) \ge n / f(n)$

Write $\log_k$ for the $k$-fold iterated
natural logarithm, so $\log_3 x = \log \log \log x$, and let $\varphi$ be Euler's totient function
and $\sigma$ the sum of divisors. Let $f$ be a real function that is positive and non-decreasing
on $(0, \infty)$ with $f(x) = o(\log_4 x)$ as $x \to \infty$, and let $P_f(x)$ be the number of
integers $n$ with $1 \le n \le x$ and $\varphi(\sigma(n)) \ge n / f(n)$. Then, as $x \to \infty$,

$$
P_f(x) = O\left(\frac{x f(x)}{\log_4 x} +
\frac{x \log_3 x}{(\log x)^{1/\log_3 x} \log_4 x}\right)
$$

and $P_f(x) = o(x)$.

## Sources

- Anup B. Dixit and Saunak Bhattacharjee, *On the Distribution of φ(σ(n))*, INTEGERS 24 (2024), Article A65, Theorem 2.

Stated but not proved: `MetaMathlibExt.card_totient_sigma_ge_div_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/totient-of-the-sum-of-divisors/index.html#card-totient-sigma-ge-div-is-big-o).

## Exceptions to $\varphi(\sigma(n)) \le n / \log_5 n$

Write $\log_k$ for the $k$-fold
iterated natural logarithm, and let $\varphi$ be Euler's totient function and $\sigma$ the sum of
divisors. The number of integers $n$ with $1 \le n \le x$ and $\varphi(\sigma(n)) > n / \log_5 n$
is $O(x \log_5 x / \log_4 x)$ as $x \to \infty$.

The finitely many small $n$ for which $\log_5 n$ is not a positive real are absorbed by the
$O$-term.

## Sources

- Anup B. Dixit and Saunak Bhattacharjee, *On the Distribution of φ(σ(n))*, INTEGERS 24 (2024), Article A65, Corollary 1.

Stated but not proved: `MetaMathlibExt.card_totient_sigma_gt_div_log_five_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TotientSigmaDistributionWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/totient-of-the-sum-of-divisors/index.html#card-totient-sigma-gt-div-log-five-is-bi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Totient of the sum of divisors](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/totient-of-the-sum-of-divisors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/totient-of-the-sum-of-divisors)
