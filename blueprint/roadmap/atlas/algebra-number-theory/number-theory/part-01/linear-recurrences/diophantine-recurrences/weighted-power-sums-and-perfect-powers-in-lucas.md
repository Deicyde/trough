---
declaration: section
origin: cited
lean: MetaMathlibExt.lucasU_root_pow, MetaMathlibExt.lucasV_eq_lucasU_succ_sub, MetaMathlibExt.lucasU_add_eq_mul_lucasV_sub, MetaMathlibExt.lucasV_sq_eq, MetaMathlibExt.lucasU_eq_sum_choose, MetaMathlibExt.lucasU_lucasV_alpha_bounds, MetaMathlibExt.lucasU_ratio_lower_bound, MetaMathlibExt.weighted_power_sum_log_bounds_of_neg
statement: formalized
---

# Weighted power sums and perfect powers in Lucas sequences

17 results, 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html).

## Powers of a root of the Lucas characteristic polynomial

Let $x$ and $y \neq 0$ be
integers and let $(U_n)$ be the Lucas sequence with parameters $(x, y)$, given by $U_0 = 0$,
$U_1 = 1$ and $U_{n+2} = x U_{n+1} - y U_n$. If $\alpha$ is a complex number with
$\alpha^2 - x\alpha + y = 0$, then $\alpha^n = \alpha U_n - y U_{n-1}$ for every $n \geq 1$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.1 (i), (ii).

Stated but not proved: `MetaMathlibExt.lucasU_root_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#lucas-u-root-pow).

## The companion Lucas sequence in terms of the fundamental one

Let $x$ and $y \neq 0$ be
integers and let $(U_n)$ and $(V_n)$ be the Lucas sequences with parameters $(x, y)$, given by
$U_0 = 0$, $U_1 = 1$, $V_0 = 2$, $V_1 = x$ and $W_{n+2} = x W_{n+1} - y W_n$ for $W = U, V$.
Then $V_n = U_{n+1} - y U_{n-1}$ for every $n \geq 1$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.1 (iii).

Stated but not proved: `MetaMathlibExt.lucasV_eq_lucasU_succ_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#lucas-v-eq-lucas-u-succ-sub).

## Addition formula for the Lucas sequence $U$

Let $x$ and $y \neq 0$ be integers and let
$(U_n)$ and $(V_n)$ be the Lucas sequences with parameters $(x, y)$, given by $U_0 = 0$, $U_1 = 1$,
$V_0 = 2$, $V_1 = x$ and $W_{n+2} = x W_{n+1} - y W_n$ for $W = U, V$. Then for all natural
numbers $n \leq m$, $U_{m+n} = U_m V_n - y^n U_{m-n}$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.1 (iv).

Stated but not proved: `MetaMathlibExt.lucasU_add_eq_mul_lucasV_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#lucas-u-add-eq-mul-lucas-v-sub).

## Square of the companion Lucas sequence

Let $x$ and $y \neq 0$ be integers and let
$(U_n)$ and $(V_n)$ be the Lucas sequences with parameters $(x, y)$, given by $U_0 = 0$, $U_1 = 1$,
$V_0 = 2$, $V_1 = x$ and $W_{n+2} = x W_{n+1} - y W_n$ for $W = U, V$. Then for every natural
number $n$, $V_n^2 = (x^2 - 4y) U_n^2 + 4 y^n$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.1 (vi).

Stated but not proved: `MetaMathlibExt.lucasV_sq_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#lucas-v-sq-eq).

## Binomial-sum formula for the Lucas sequence $U$

Let $x$ and $y \neq 0$ be integers and
let $(U_n)$ be the Lucas sequence with parameters $(x, y)$, given by $U_0 = 0$, $U_1 = 1$ and
$U_{n+2} = x U_{n+1} - y U_n$. Then for every $r \geq 1$,

$$
U_r = \sum_{i=0}^{\lfloor (r-1)/2 \rfloor} (-y)^i \binom{r-i-1}{i} x^{r-2i-1}.
$$

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.1 (vii).

Stated but not proved: `MetaMathlibExt.lucasU_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#lucas-u-eq-sum-choose).

## Bounds on Lucas sequences by powers of the dominant root

Let $x$ and $y \neq 0$ be
integers with $x \geq 1$, $|y + 1| \leq x$ and $D = x^2 - 4y > 0$, let $(U_n)$ and $(V_n)$ be the
Lucas sequences with parameters $(x, y)$, given by $U_0 = 0$, $U_1 = 1$, $V_0 = 2$, $V_1 = x$
and $W_{n+2} = x W_{n+1} - y W_n$ for $W = U, V$, and put $\alpha = (x + \sqrt{D})/2$. Then for
every $n \geq 2$ we have $x \alpha^{n-2} \leq U_n$; if $y \leq 0$, then $U_n \leq \alpha^{n-1}$
and $x \alpha^{n-1} \leq V_n \leq \alpha^{n+1}/x$; and if $y \geq 0$, then
$U_n \leq \alpha^n/\sqrt{D}$ and $\alpha^n \leq V_n \leq \alpha^{n+1}/\sqrt{D}$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_alpha_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#lucas-u-lucas-v-alpha-bounds).

## Lower bounds for ratios of consecutive Lucas terms

Let $x$ and $y \neq 0$ be integers
with $x \geq 1$ and $|y + 1| \leq x$, and let $(U_n)$ be the Lucas sequence with parameters
$(x, y)$, given by $U_0 = 0$, $U_1 = 1$ and $U_{n+2} = x U_{n+1} - y U_n$. If $y < 0$, then
$U_n / U_{n-1} \geq x - xy/(x^2 - y)$ for every $n > 2$. If $y > 0$, then
$U_n / U_{n-1} \geq (x + \sqrt{x^2 - 4y})/2$ for every $n \geq 2$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.3.

Stated but not proved: `MetaMathlibExt.lucasU_ratio_lower_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#lucas-u-ratio-lower-bound).

## Logarithmic bounds for weighted Lucas power sums when $y < 0$

Let $x \ge 1$ and $y < 0$
be integers with $|y + 1| \le x$, let $(U_m)$ be the Lucas sequence with parameters $(x, y)$,
given by $U_0 = 0$, $U_1 = 1$ and $U_{m+2} = x U_{m+1} - y U_m$, and let
$\alpha = (x + \sqrt{x^2 - 4y})/2$. Let $k$ be a natural number and $n$, $p$, $q$ positive
integers with $\sum_{j=1}^k j U_j^p = U_n^q$. If $k \ge 2$, then
$\log_\alpha k + p \log_\alpha x + (k - 2)p < (n - 1)q$. If $k \ge 3$, then
$q \log_\alpha x + (n - 2)q < (k - 1)p + \log_\alpha k +
\log_\alpha\bigl(1 + (x^2 - 2y)/(x^{p-1}(x^3 - x^2 - 2xy + y))\bigr)$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.4.

Stated but not proved: `MetaMathlibExt.weighted_power_sum_log_bounds_of_neg` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#weighted-power-sum-log-bounds-of-neg).

## Logarithmic bounds for weighted Lucas power sums when $y > 0$

Let $x$ and $y > 0$ be
integers with $|y + 1| \le x$ and $D = x^2 - 4y > 0$, let $(U_m)$ be the Lucas sequence with
parameters $(x, y)$, given by $U_0 = 0$, $U_1 = 1$ and $U_{m+2} = x U_{m+1} - y U_m$, and let
$\alpha = (x + \sqrt{D})/2$. Let $k$ be a natural number and $n$, $p$, $q$ positive integers
with $\sum_{j=1}^k j U_j^p = U_n^q$. If $k \ge 2$, then
$\log_\alpha k + p \log_\alpha x + (k - 2)p < q(n - \log_\alpha \sqrt{D})$. If $k \ge 3$, then
$q \log_\alpha x + (n - 2)q < \log_\alpha k + p(k + 1 - \log_\alpha \sqrt{D}) -
\log_\alpha(\alpha^p - 1)$.

The hypothesis $D > 0$ is added to the statement of the paper: for $x = 2$, $y = 1$ one has
$\alpha = 1$, and $\log_\alpha$ is undefined.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.5.

Stated but not proved: `MetaMathlibExt.weighted_power_sum_log_bounds_of_pos` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#weighted-power-sum-log-bounds-of-pos).

## Valuation of $U_n$ at a prime dividing the discriminant

Let $x \ge 1$ and $y \ne 0$ be
coprime integers with $|y + 1| \le x$, let $(U_m)$ be the Lucas sequence with parameters $(x, y)$,
given by $U_0 = 0$, $U_1 = 1$ and $U_{m+2} = x U_{m+1} - y U_m$, and let $\ell$ be a prime
dividing $D = x^2 - 4y$. Write $\nu_\ell$ for the $\ell$-adic valuation of an integer, with
$\nu_\ell(0) = 0$. Then for every $n \ge 1$, $\nu_\ell(U_n) = \nu_\ell(n) + \nu_\ell(U_\ell) - 1$
if $\ell \mid n$, and $\nu_\ell(U_n) = 0$ if $\ell \nmid n$. Moreover, $\nu_\ell(U_\ell) = 1$ if
$\ell \ge 5$.

Coprimality of $x$ and $y$ (Sanna's standing hypothesis) is added to the statement of the paper:
without it, $x = 6$, $y = 3$ and $\ell = 3 \mid D = 24$ give $\nu_3(U_2) = \nu_3(6) = 1 \ne 0$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.6.

Stated but not proved: `MetaMathlibExt.padicValInt_lucasU_of_dvd_discr` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#padic-val-int-lucas-u-of-dvd-discr).

## A quadratic equation in the companion Lucas sequence

Let $x$ be a positive integer,
let $(V_n)$ be the companion Lucas sequence with parameters $(x, -1)$, given by $V_0 = 2$,
$V_1 = x$ and $V_{n+2} = x V_{n+1} + V_n$, and let $D = x^2 + 4$. Let $p, q, k$ be natural numbers
with $p$ odd and $q, k$ positive. If

$$
V_p k^2 + (V_p - 2) k - 1 = \pm D^{p-q} V_p^2
$$

in $\mathbb{Q}$, where the exponent $p - q$ may be negative, then $(p, q, k, x)$ is one of
$(1, 1, 1, 1)$, $(1, 1, 2, 1)$ and $(1, 1, 2, 5)$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2.7.

Stated but not proved: `MetaMathlibExt.lucasV_quadratic_eq_pm_discr_zpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#lucas-v-quadratic-eq-pm-discr-zpow).

## Solutions of $1 + 2x^p = U_n^q$ for Lucas sequences with $y = \pm 1$

Let $x$ be a
positive integer, let $y \in \{1, -1\}$, and let $(U_m)$ be the Lucas sequence with parameters
$(x, y)$, given by $U_0 = 0$, $U_1 = 1$ and $U_{m+2} = x U_{m+1} - y U_m$. For positive integers
$n$, $p$, $q$, the equation $1 + 2x^p = U_n^q$ holds if and only if $(n, p, q, x, y)$ is one of
$(4, p, 1, 1, -1)$, $(1 + 2^{p+1}, p, 1, 2, 1)$, $(3, 2, 2, 2, 1)$, $(3, 1, 1, 2, -1)$ and
$(5, 3, 1, 3, 1)$, where $p$ is arbitrary in the first two.

Since $U_1 = 1$ and $U_2 = x$, this is the case $k = 2$ of the equation
$\sum_{j=1}^k j U_j^p = U_n^q$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Theorem 1.1 and Proposition 3.1.

Stated but not proved: `MetaMathlibExt.one_add_two_mul_pow_eq_lucasU_pow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#one-add-two-mul-pow-eq-lucas-u-pow-iff).

## No solutions of $\sum_{j=1}^k j U_j^p = U_n^q$ when $y = -1$ and $x \ge 2$ or $y = 1$ and $x \ge 3$, with $k \ge 3$ and exponents at most $11$

**No solutions of $\sum_{j=1}^k j U_j^p = U_n^q$ when $y = -1$ and $x \ge 2$ or $y = 1$ and
$x \ge 3$, with $k \ge 3$ and exponents at most $11$.** Let $y \in \{1, -1\}$, let $x$ be an
integer with $x \ge 2$ if $y = -1$ and $x \ge 3$ if $y = 1$, and let $(U_m)$ be the Lucas sequence
with parameters $(x, y)$, given by $U_0 = 0$, $U_1 = 1$ and $U_{m+2} = x U_{m+1} - y U_m$. If $n$,
$p$, $q$ are positive integers with $p \le 11$ and $q \le 11$, and $k \ge 3$ is an integer, then
$\sum_{j=1}^k j U_j^p \ne U_n^q$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Theorem 1.1, second part.

Stated but not proved: `MetaMathlibExt.weighted_power_sum_ne_lucasU_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#weighted-power-sum-ne-lucas-u-pow).

## Remainder form of the weighted power-sum equation for Lucas sequences

Let $x$ be a
positive integer, let $y \in \{1, -1\}$, and let $(U_n)$ be the Lucas sequence with parameters
$(x, y)$, given by $U_0 = 0$, $U_1 = 1$ and $U_{n+2} = x U_{n+1} - y U_n$. Suppose
$D = x^2 - 4y > 0$ and put $\alpha = (x + \sqrt{D})/2$. Let $n, p, q$ be positive integers and
$k \geq 3$ an integer with

$$
\sum_{j=1}^{k} j \, U_j^p = U_n^q.
$$

Then there are real numbers $R_1, R_2$ with $|R_1| < k^2 \alpha^{k(p-2)}$,
$|R_2| < \alpha^{n(q-2)}$ and

$$
\frac{D^{(q-p)/2} (k\alpha^p - (k+1))}{(\alpha^p - 1)^2} \alpha^{p(k+1)} - \alpha^{qn} =
D^{q/2} R_2 - D^{q/2} R_1 - \frac{D^{(q-p)/2} \alpha^p}{(\alpha^p - 1)^2}.
$$

The remainders $R_1, R_2$ are only asserted to exist; the source defines them explicitly in its
proof.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Proposition 4.1.

Stated but not proved: `MetaMathlibExt.exists_remainders_weighted_power_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#exists-remainders-weighted-power-sum).

## Bound on the parameter in the weighted power-sum equation for Lucas sequences

Let $x$
be a positive integer, let $y \in \{1, -1\}$, and let $(U_n)$ be the Lucas sequence with
parameters $(x, y)$, given by $U_0 = 0$, $U_1 = 1$ and $U_{n+2} = x U_{n+1} - y U_n$.
If $n, p, q$ are positive integers and $k \geq 3$ is an integer with

$$
\sum_{j=1}^{k} j \, U_j^p = U_n^q,
$$

then $x \leq (k + 1)^2/4 + 1$.

The hypothesis $k \geq 3$ cannot be dropped entirely: for $k = 1$ and $y = -1$,
$(n, p, q, x) = (1, 1, 1, 5)$ is a solution and $5 > (1 + 1)^2/4 + 1 = 2$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 4.4.

Stated but not proved: `MetaMathlibExt.le_of_weighted_power_sum_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#le-of-weighted-power-sum-eq).

## Remainder bound for weighted Lucas power sums when $y = -1$

Let $x$ be a positive
integer, let $(U_m)$ be the Lucas sequence with parameters $(x, -1)$, given by $U_0 = 0$,
$U_1 = 1$ and $U_{m+2} = x U_{m+1} + U_m$, and let $D = x^2 + 4$ and $\alpha = (x + \sqrt{D})/2$.
If positive integers $n$, $p$, $q$ and an integer $k \ge 3$ satisfy
$\sum_{j=1}^k j U_j^p = U_n^q$, then the remainder $R_2 = U_n^q - \alpha^{nq}/D^{q/2}$ satisfies
$D^{q/2} |R_2| < k (D + 1/x)^{q+1} \alpha^{kp - 2k/q + 1}$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 4.2.

Stated but not proved: `MetaMathlibExt.remainder_bound_of_neg` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#remainder-bound-of-neg).

## Remainder bound for weighted Lucas power sums when $y = 1$

Let $x$ be a positive integer
with $D = x^2 - 4 > 0$, let $(U_m)$ be the Lucas sequence with parameters $(x, 1)$, given by
$U_0 = 0$, $U_1 = 1$ and $U_{m+2} = x U_{m+1} - U_m$, let $V_2 = x^2 - 2$ be the term of index $2$
of the companion Lucas sequence, and let $\alpha = (x + \sqrt{D})/2$. If positive integers $n$,
$p$, $q$ and an integer $k \ge 3$ satisfy $\sum_{j=1}^k j U_j^p = U_n^q$, then the remainder
$R_2 = U_n^q - \alpha^{nq}/D^{q/2}$ satisfies
$D^{q/2} |R_2| < k (V_2 + 1/x)^{q+1} \alpha^{kp - 2k/q + 1/2}$.

## Sources

- Benjamin Earp-Lynch, Simon Earp-Lynch, Omar Kihel and Puntani Pongsumpun, *Extension of the Equation ∑ j F_j^p = F_n^q to a Family of Lucas Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 4.3.

Stated but not proved: `MetaMathlibExt.remainder_bound_of_pos` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasWeightedPowerSumWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html#remainder-bound-of-pos).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted power sums and perfect powers in Lucas sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/weighted-power-sums-and-perfect-powers-in-lucas)
