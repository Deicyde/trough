---
declaration: section
origin: cited
lean: MetaMathlibExt.totient_div_gg_and_sigma_div_ll_log_log, MetaMathlibExt.card_minFac_gt_le_div_log, MetaMathlibExt.card_cardFactors_ge_ten_log_log_le, MetaMathlibExt.card_divisors_sigma_gt_exp_sqrt_log_le, MetaMathlibExt.zero_set_card_le_exp_exp_exp, MetaMathlibExt.card_abs_le_dominant_root_pow_le_sqrt, MetaMathlibExt.card_totient_sigma_inequality_fails_le_div_log
statement: formalized
---

# Euler's function and divisor sums along linear recurrences

7 results, 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r/index.html).

## Lower bound for Euler's function and upper bound for the sum of divisors

Let $\varphi$
be Euler's totient function and $\sigma(n)$ the sum of the positive divisors of $n$. There is a
constant $C > 0$ such that $\varphi(n)/n \ge C/\log\log n$ for every integer $n \ge 3$, and there
is a constant $C'$ such that $\sigma(n)/n \le C' \log\log n$ for every integer $n \ge 3$.

## Sources

- Florian Luca and Makoko Campbell Manape, *On the Euler Function of Linearly Recurrence Sequences*, Fibonacci Quarterly 62 (2024), Article 62-4/luca09162024rev2, Lemma 1, quoted from Hardy and Wright, Theorems 323, 328 and 329.

Stated but not proved: `MetaMathlibExt.totient_div_gg_and_sigma_div_ll_log_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r/index.html#totient-div-gg-and-sigma-div-ll-log-log).

## Sieve bound for integers without small prime factors

Write $p(n)$ for the least prime
factor of an integer $n \ge 2$, and set $p(1) = 1$. There is a constant $C$ such that for all real
$x$ and $y$ with $2 \le y \le x$, the number of integers $1 \le n \le x$ with $p(n) > y$ is at
most $C x / \log y$.

## Sources

- Florian Luca and Makoko Campbell Manape, *On the Euler Function of Linearly Recurrence Sequences*, Fibonacci Quarterly 62 (2024), Article 62-4/luca09162024rev2, Lemma 2, quoted from Tenenbaum, page 397.

Stated but not proved: `MetaMathlibExt.card_minFac_gt_le_div_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r/index.html#card-min-fac-gt-le-div-log).

## Integers with many prime factors are rare

Let $\Omega(n)$ be the number of prime factors
of $n$ counted with multiplicity. There is a constant $C$ such that for every real $x \ge 10$, the
number of integers $1 \le n \le x$ with $\Omega(n) \ge 10 \log\log x$ is at most
$C x / (\log x)^2$.

## Sources

- Florian Luca and Makoko Campbell Manape, *On the Euler Function of Linearly Recurrence Sequences*, Fibonacci Quarterly 62 (2024), Article 62-4/luca09162024rev2, Lemma 3.

Stated but not proved: `MetaMathlibExt.card_cardFactors_ge_ten_log_log_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r/index.html#card-card-factors-ge-ten-log-log-le).

## Integers whose sum of divisors has many divisors

Let $\sigma(n)$ be the sum of the
positive divisors of $n$ and $\tau(m)$ the number of positive divisors of $m$. There is a constant
$C$ such that for every real $x \ge 10$, the number of integers $1 \le n \le x$ with
$\tau(\sigma(n)) > \exp(\sqrt{\log x})$ is at most $C x / (\log x)^2$.

## Sources

- Florian Luca and Makoko Campbell Manape, *On the Euler Function of Linearly Recurrence Sequences*, Fibonacci Quarterly 62 (2024), Article 62-4/luca09162024rev2, Lemma 4.

Stated but not proved: `MetaMathlibExt.card_divisors_sigma_gt_exp_sqrt_log_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r/index.html#card-divisors-sigma-gt-exp-sqrt-log-le).

## Schmidt's bound on the zeros of a linear recurrence

Let $(U_n)_{n \ge 1}$ be a sequence
of complex numbers satisfying $U_{m+k} = c_0 U_m + c_1 U_{m+1} + \dots + c_{k-1} U_{m+k-1}$ for
all $m \ge 1$, with complex coefficients $c_i$, where the order $k$ of this recurrence is minimal
among all linear recurrences with complex coefficients satisfied by $(U_n)_{n \ge 1}$, and
$k \ge 2$. Suppose the recurrence is nondegenerate: no root of its characteristic polynomial
$X^k - c_{k-1} X^{k-1} - \dots - c_0$ is $0$, and no quotient of two distinct roots is a root of
unity. Then $U_n = 0$ for only finitely many $n \ge 1$, and there are at most
$\exp(\exp(\exp(3k \log k)))$ such $n$.

## Sources

- Florian Luca and Makoko Campbell Manape, *On the Euler Function of Linearly Recurrence Sequences*, Fibonacci Quarterly 62 (2024), Article 62-4/luca09162024rev2, Theorem 3, quoted from Schmidt.

Stated but not proved: `MetaMathlibExt.zero_set_card_le_exp_exp_exp` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r/index.html#zero-set-card-le-exp-exp-exp).

## Few small values of a nondegenerate integer linear recurrence

Let $(U_n)_{n \ge 1}$ be a
sequence of integers satisfying $U_{m+k} = c_0 U_m + c_1 U_{m+1} + \dots + c_{k-1} U_{m+k-1}$ for
all $m \ge 1$, with integer coefficients $c_i$, where the order $k$ of this recurrence is minimal
among all linear recurrences with integer coefficients satisfied by $(U_n)_{n \ge 1}$. Suppose the
recurrence is nondegenerate: no complex root of its characteristic polynomial
$X^k - c_{k-1} X^{k-1} - \dots - c_0$ is $0$, and no quotient of two distinct complex roots is a
root of unity. Suppose also that the characteristic polynomial has at least two distinct complex
roots, and let $\alpha_1$ be a complex root of maximal modulus. Then there are a real $c$ with
$0 < c < 1/3$ and real constants $x_0$ and $C$ such that for every real $x \ge x_0$, the number of
integers $1 \le n \le x$ with $|U_n| \le |\alpha_1|^{n(1 - x^{-c})}$ is at most $C \sqrt{x}$.

## Sources

- Florian Luca and Makoko Campbell Manape, *On the Euler Function of Linearly Recurrence Sequences*, Fibonacci Quarterly 62 (2024), Article 62-4/luca09162024rev2, Lemma 5.

Stated but not proved: `MetaMathlibExt.card_abs_le_dominant_root_pow_le_sqrt` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r/index.html#card-abs-le-dominant-root-pow-le-sqrt).

## Euler's function and the sum of divisors along a linear recurrence

Let
$(U_n)_{n \ge 1}$ be a sequence of integers satisfying
$U_{m+k} = c_0 U_m + c_1 U_{m+1} + \dots + c_{k-1} U_{m+k-1}$ for all $m \ge 1$, with integer
coefficients $c_i$, where the order $k$ of this recurrence is minimal among all linear recurrences
with integer coefficients satisfied by $(U_n)_{n \ge 1}$. Suppose the recurrence is nondegenerate:
no complex root of its characteristic polynomial $X^k - c_{k-1} X^{k-1} - \dots - c_0$ is $0$, and
no quotient of two distinct complex roots is a root of unity. Suppose also that there is no
polynomial $P$ with rational coefficients such that $|U_n| = P(n)$ for all sufficiently large $n$.
Let $\varphi$ be Euler's totient function and $\sigma(m)$ the sum of the positive divisors of $m$,
with $\varphi(0) = \sigma(0) = 0$. Then there are real constants $x_0$ and $C$ such that for every
real $x \ge x_0$, the number of integers $1 \le n \le x$ with $\varphi(|U_n|) < |U_{\varphi(n)}|$
is at most $C x / \log x$, and the number of integers $1 \le n \le x$ with
$|U_{\sigma(n)}| < \sigma(|U_n|)$ is at most $C x / \log x$.

## Sources

- Florian Luca and Makoko Campbell Manape, *On the Euler Function of Linearly Recurrence Sequences*, Fibonacci Quarterly 62 (2024), Article 62-4/luca09162024rev2, Theorem 1.

Stated but not proved: `MetaMathlibExt.card_totient_sigma_inequality_fails_le_div_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/EulerFunctionLinearRecurrenceWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r/index.html#card-totient-sigma-inequality-fails-le-d).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler's function and divisor sums along linear recurrences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/euler-s-function-and-divisor-sums-along-linear-r)
