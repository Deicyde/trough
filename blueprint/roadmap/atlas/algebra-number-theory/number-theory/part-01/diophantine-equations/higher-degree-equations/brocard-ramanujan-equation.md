---
declaration: section
origin: cited
lean: MetaMathlibExt.brocardRamanujan_powerFree_finite, MetaMathlibExt.brocardRamanujan_sevenFree_subset, MetaMathlibExt.brocardRamanujan_fewPrimeFactors_finite, MetaMathlibExt.brocardRamanujan_primePow_subset, MetaMathlibExt.le_exp_of_dvd_factorial, MetaMathlibExt.le_rpow_mul_pow_of_dvd_factorial, MetaMathlibExt.brocardRamanujan_polynomial_powerFree_mul_fewPrimeFactors_finite
statement: formalized
---

# Brocard–Ramanujan equation

7 results, 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation/index.html).

## Brocard–Ramanujan solutions with $x - 1$ or $x + 1$ power-free are finite

For every
natural number $k \ge 2$, there are only finitely many pairs of natural numbers $(n, x)$ with
$n! + 1 = x^2$ such that $x - 1$ or $x + 1$ is $k$-free.

## Sources

- Abderrahim Makki Naciri, *On the Brocard-Ramanujan Equation with 7-Free Integers and Prime Powers*, INTEGERS 25 (2025), Article A71, Theorem 1(i), first sentence.

Stated but not proved: `MetaMathlibExt.brocardRamanujan_powerFree_finite` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation/index.html#brocard-ramanujan-power-free-finite).

## Brocard–Ramanujan solutions with $x - 1$ or $x + 1$ seven-free

If natural numbers $n$
and $x$ satisfy $n! + 1 = x^2$ and $x - 1$ or $x + 1$ is $7$-free, then $(n, x)$ is one of
$(4, 5)$, $(5, 11)$ and $(7, 71)$.

## Sources

- Abderrahim Makki Naciri, *On the Brocard-Ramanujan Equation with 7-Free Integers and Prime Powers*, INTEGERS 25 (2025), Article A71, Theorem 1(i), second sentence.

Stated but not proved: `MetaMathlibExt.brocardRamanujan_sevenFree_subset` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation/index.html#brocard-ramanujan-seven-free-subset).

## Brocard–Ramanujan solutions with $x - 1$ or $x + 1$ having few prime factors are finite

For every natural number $l \ge 2$, there are only finitely many pairs of natural numbers
$(n, x)$ with $n! + 1 = x^2$ such that $x - 1$ or $x + 1$ has fewer than $l$ distinct prime
divisors.

## Sources

- Abderrahim Makki Naciri, *On the Brocard-Ramanujan Equation with 7-Free Integers and Prime Powers*, INTEGERS 25 (2025), Article A71, Theorem 1(ii), first sentence.

Stated but not proved: `MetaMathlibExt.brocardRamanujan_fewPrimeFactors_finite` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation/index.html#brocard-ramanujan-few-prime-factors-fini).

## Brocard–Ramanujan solutions with $x - 1$ or $x + 1$ a prime power

If natural numbers
$n$ and $x$ satisfy $n! + 1 = x^2$ and $x - 1$ or $x + 1$ is a prime power, then
$(n, x) = (4, 5)$.

## Sources

- Abderrahim Makki Naciri, *On the Brocard-Ramanujan Equation with 7-Free Integers and Prime Powers*, INTEGERS 25 (2025), Article A71, Theorem 1(ii), second sentence.

Stated but not proved: `MetaMathlibExt.brocardRamanujan_primePow_subset` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation/index.html#brocard-ramanujan-prime-pow-subset).

## Divisors of a factorial bounded by their largest prime exponent

Let $n \ge 1$ and let
$x$ be a positive integer dividing $n!$. Write $K(x)$ for the largest exponent in the prime
factorization of $x$, with $K(1) = 0$. Then $x \le \exp(3 n K(x) / 2)$.

## Sources

- Abderrahim Makki Naciri, *On the Brocard-Ramanujan Equation with 7-Free Integers and Prime Powers*, INTEGERS 25 (2025), Article A71, Lemma 1.

Stated but not proved: `MetaMathlibExt.le_exp_of_dvd_factorial` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation/index.html#le-exp-of-dvd-factorial).

## Divisors of a factorial bounded by their number of prime factors

Let $n \ge 1$ and let
$x$ be a positive integer dividing $n!$, and write $\omega(x)$ for the number of distinct prime
divisors of $x$. Then for every positive integer $a$,
$x \le n^{n/a} (a \, \omega(x) + 1)^{n \, \omega(x)}$, where $n^{n/a}$ is a real power.

## Sources

- Abderrahim Makki Naciri, *On the Brocard-Ramanujan Equation with 7-Free Integers and Prime Powers*, INTEGERS 25 (2025), Article A71, Lemma 2.

Stated but not proved: `MetaMathlibExt.le_rpow_mul_pow_of_dvd_factorial` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation/index.html#le-rpow-mul-pow-of-dvd-factorial).

## Finitely many Brocard–Ramanujan solutions of polynomial shape

Let $k \ge 2$, $l \ge 2$
and $m \ge 1$ be natural numbers and let $P \in \mathbb{Z}[X_1, \ldots, X_m]$. Write
$F_k P_l$ for the set of products $y z$ of a $k$-free number $y$ and a positive integer $z$
with fewer than $l$ distinct prime divisors. Then there are only finitely many pairs $(n, x)$
of a natural number $n$ and an integer $x$ such that $n! + 1 = x^2$ and
$x = x_1 \cdots x_m P(x_1, \ldots, x_m) + 1$ or $x = x_1 \cdots x_m P(x_1, \ldots, x_m) - 1$
for some $x_1, \ldots, x_m \in F_k P_l$.

Here $x$ ranges over the integers, since negating $x$ does not preserve the shape
$x_1 \cdots x_m P(x_1, \ldots, x_m) \pm 1$.

## Sources

- Abderrahim Makki Naciri, *On the Brocard-Ramanujan Equation with 7-Free Integers and Prime Powers*, INTEGERS 25 (2025), Article A71, Theorem 2.

Stated but not proved: `MetaMathlibExt.brocardRamanujan_polynomial_powerFree_mul_fewPrimeFactors_finite` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanPowerFreeWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation/index.html#brocard-ramanujan-polynomial-power-free).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Brocard–Ramanujan equation](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/brocard-ramanujan-equation)
