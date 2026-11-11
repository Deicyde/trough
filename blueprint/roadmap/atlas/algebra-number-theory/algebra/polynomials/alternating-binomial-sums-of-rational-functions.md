---
declaration: section
origin: cited
lean: MetaMathlibExt.X_sub_one_pow_dvd_alternating_sum_prod_X_pow_add_C, MetaMathlibExt.X_sub_one_pow_dvd_alternating_sum_prod_comp_X_pow
statement: formalized
---

# Alternating binomial sums of rational functions

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/alternating-binomial-sums-of-rational-functions/index.html).

## The factor $(x - 1)^n$ of an alternating binomial sum

For every real number $a$ and
every natural number $n$, the polynomial $(x - 1)^n$ divides, in $\mathbb{R}[x]$, the polynomial

$$H_n(x; a) = \sum_{i=0}^{n} (-1)^i \binom{n}{i} \prod_{0 \le k \le n,\ k \ne i} (x^k + a).$$

For $a \ne -1$ (the paper's condition), $H_n(x; a)$ is the numerator of
$G_n(x; a) = \sum_{i=0}^{n} (-1)^i \binom{n}{i} / (x^i + a)$ over the common denominator
$\prod_{k=0}^{n} (x^k + a)$; at $a = -1$ the factor $x^0 + a$ is zero and only the polynomial
statement remains.

## Sources

- Takashi Agoh, *An Intrinsic Factor of an Alternating Sum Involving Certain Rational Functions*, INTEGERS 26 (2026), Article A9, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.X_sub_one_pow_dvd_alternating_sum_prod_X_pow_add_C` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/AlternatingSumIntrinsicFactorWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/AlternatingSumIntrinsicFactorWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/alternating-binomial-sums-of-rational-functions/index.html#x-sub-one-pow-dvd-alternating-sum-prod-x).

## The factor $(x - 1)^n$ for polynomials with distinct real roots

Let $c$ be a real
number, let $s$ be a finite set of real numbers, and let $f(x) = c \prod_{r \in s} (x - r)$ in
$\mathbb{R}[x]$. For every natural number $n$, the polynomial $(x - 1)^n$ divides the polynomial

$$\sum_{i=0}^{n} (-1)^i \binom{n}{i} \prod_{0 \le k \le n,\ k \ne i} f(x^k).$$

For $c \ne 0$ and $1 \notin s$ (the paper's conditions), this polynomial is the numerator of
$Q_n(x; f) = \sum_{i=0}^{n} (-1)^i \binom{n}{i} / f(x^i)$ over the common denominator
$\prod_{k=0}^{n} f(x^k)$; for $c = 0$ or $1 \in s$ some $f(x^k)$ is zero and only the
polynomial statement remains.

## Sources

- Takashi Agoh, *An Intrinsic Factor of an Alternating Sum Involving Certain Rational Functions*, INTEGERS 26 (2026), Article A9, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.X_sub_one_pow_dvd_alternating_sum_prod_comp_X_pow` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/AlternatingSumIntrinsicFactorWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/AlternatingSumIntrinsicFactorWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/alternating-binomial-sums-of-rational-functions/index.html#x-sub-one-pow-dvd-alternating-sum-prod-c).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alternating binomial sums of rational functions](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/alternating-binomial-sums-of-rational-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials/alternating-binomial-sums-of-rational-functions)
