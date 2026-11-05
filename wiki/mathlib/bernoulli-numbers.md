---
article_id: af_70826eb9ef43a33808106beb
concept: bernoulli
---

The **Bernoulli numbers** $B_0, B_1, B_2, \dots$ are a sequence of
[rational numbers](trough:Rat) defined by a power series identity, beginning
$1, -\tfrac12, \tfrac16, 0, -\tfrac1{30}, 0, \tfrac1{42}, \dots$. They appear
throughout number theory and analysis: they give closed formulas for sums of
powers of consecutive integers, up to explicit factors they are the values of the
Riemann zeta function at the negative integers and at the positive even
integers, and their denominators and numerators carry arithmetic information
about primes.

## Definition

The Bernoulli numbers are the coefficients of the exponential generating function

$$\frac{t}{e^t - 1} = \sum_{n=0}^{\infty} B_n \frac{t^n}{n!}.$$

Since $(e^t - 1)/t$ has constant term $1$, it is invertible as a
[power series](trough:PowerSeries), so this defines every $B_n$. Equivalently,
[the series $\sum_n B_n t^n/n!$ multiplied by $e^t - 1$ equals $t$](lean:bernoulliPowerSeries_mul_exp_sub_one)
as formal power series. Comparing coefficients of $t^n/n!$ on both sides gives a recurrence that determines
[the Bernoulli numbers $B_n$](lean:bernoulli) one at a time: for every $n \ge 0$,
[the sum $\sum_{k=0}^{n-1} \binom{n}{k} B_k$ equals $1$ if $n = 1$ and $0$ otherwise](lean:sum_bernoulli).
Starting from $B_0 = 1$, the case $n = 2$ reads $B_0 + 2B_1 = 0$, the case $n = 3$
reads $B_0 + 3B_1 + 3B_2 = 0$, and so on.

### Two conventions

Some authors use instead the numbers $B_n^+ = (-1)^n B_n$, whose generating function
is $t/(1 - e^{-t}) = t e^t/(e^t - 1)$; the only difference is the sign of the term
of index $1$, since $B_1^+ = \tfrac12$ while
[$B_n^+ = B_n$ for every $n \ne 1$](lean:bernoulli_eq_bernoulli'_of_ne_one). The
convention $B_1 = -\tfrac12$ is the one used in this article.

## Examples

The first values are
[$B_0 = 1$](lean:bernoulli_zero), [$B_1 = -\tfrac12$](lean:bernoulli_one) and
[$B_2 = \tfrac16$](lean:bernoulli_two). Continuing,

$$B_4 = -\tfrac1{30},\quad B_6 = \tfrac1{42},\quad B_8 = -\tfrac1{30},\quad
B_{10} = \tfrac5{66},\quad B_{12} = -\tfrac{691}{2730},\quad B_{14} = \tfrac76.$$

## Properties

- **Odd indices.** The function $t/(e^t - 1) + t/2 = (t/2)\coth(t/2)$ is even, so
  all odd-indexed coefficients except the first vanish:
  [$B_n = 0$ for every odd $n > 1$](lean:bernoulli_eq_zero_of_odd).
- **Sums of powers.** For natural numbers $n$ and $p$,
  [Faulhaber's formula](lean:sum_range_pow) expresses the
  [sum of $p$th powers](trough:sum_range_pow) as a
  polynomial in $n$ of degree $p + 1$ (with the convention $0^0 = 1$):

  $$\sum_{k=0}^{n-1} k^p = \frac{1}{p+1}\sum_{i=0}^{p} \binom{p+1}{i} B_i\, n^{p+1-i}.$$

  For $p = 2$ this gives $0^2 + 1^2 + \dots + (n-1)^2 = n^3/3 - n^2/2 + n/6$. [With
  the numbers $B_i^+$ in place of $B_i$, the same right-hand side gives the sum
  $1^p + 2^p + \dots + n^p$](lean:sum_Ico_pow).
- **Zeta values at even integers.** For every integer $k \ge 1$, the value
  $\zeta(2k) = \sum_{m \ge 1} m^{-2k}$ of the Riemann zeta function
  [is a rational multiple of $\pi^{2k}$ given by](lean:riemannZeta_two_mul_nat)

  $$\zeta(2k) = (-1)^{k+1}\frac{2^{2k-1}\pi^{2k} B_{2k}}{(2k)!}.$$

  The case $k = 1$ is [the sum of the reciprocals of the squares](trough:hasSum_zeta_two),
  [$\zeta(2) = \pi^2/6$](lean:riemannZeta_two). Since $\zeta(2k) > 0$, the sign of
  $B_{2k}$ is $(-1)^{k+1}$, so $B_2, B_4, B_6, \dots$ are all nonzero and alternate
  in sign, and since $\zeta(2k)$ tends to $1$, their absolute values grow roughly like
  $2\,(2k)!/(2\pi)^{2k}$.
- **Zeta values at negative integers.** For every natural number $k$,
  [$\zeta(-k) = (-1)^k B_{k+1}/(k+1)$](lean:riemannZeta_neg_nat_eq_bernoulli). For
  example $\zeta(0) = -\tfrac12$ and $\zeta(-1) = -\tfrac1{12}$, while
  $\zeta(-2k) = 0$ for $k \ge 1$ because $B_{2k+1} = 0$.
- **Denominators.** The
  [von Staudt–Clausen theorem](trough:Bernoulli.vonStaudt_clausen) states that for
  every $k \ge 1$
  [the following number is an integer](lean:Bernoulli.vonStaudt_clausen):

  $$B_{2k} + \sum_{p \text{ prime},\ (p-1) \mid 2k} \frac1p.$$

  Consequently, for $k \ge 1$ and a [prime](trough:Prime) $p$ with $p - 1$ dividing
  $2k$, [$p$ divides the denominator of $B_{2k}$](lean:Bernoulli.dvd_den_bernoulli)
  but [$p^2$ does not](lean:Bernoulli.not_sq_dvd_den_bernoulli), and, since $B_{2k}$
  differs from an integer by the sum of the $1/p$, no other prime divides it. So the denominator of $B_{2k}$ is the product of the primes $p$ with
  $(p - 1) \mid 2k$; in particular it is always divisible by $6$.

## Bernoulli polynomials

The Bernoulli numbers are the constant terms of the
[Bernoulli polynomials](lean:Polynomial.bernoulli)

$$B_n(x) = \sum_{i=0}^{n} \binom{n}{i} B_i\, x^{n-i},$$

a family of [polynomials](trough:Polynomial) with rational coefficients:
[$B_n(0) = B_n$](lean:Polynomial.bernoulli_eval_zero), while
[$B_n(1) = B_n^+$](lean:Polynomial.bernoulli_eval_one). For $n \ge 1$ and every rational $x$,
[$B_n(x + 1) = B_n(x) + n x^{n-1}$](lean:Polynomial.bernoulli_eval_one_add), which
turns sums of powers into differences of values of $B_{p+1}$. The polynomials also
give the values at the negative integers of the Hurwitz zeta function $\zeta(s, x)$,
which for $0 < x \le 1$ is the meromorphic continuation of
$\sum_{m \ge 0} (m + x)^{-s}$: for every integer $k \ge 1$ and $0 < x \le 1$,
[$\zeta(-k, x) = -B_{k+1}(x)/(k+1)$](lean:HurwitzZeta.hurwitzZeta_neg_nat).
Taking $x = 1$ recovers the values of the Riemann zeta function.

## In Mathlib

Mathlib defines the numbers $B_n^+$ first, by the recursion
$B_n^+ = 1 - \sum_{k=0}^{n-1} \binom{n}{k} B_k^+/(n - k + 1)$, and then sets
$B_n = (-1)^n B_n^+$; both are rational numbers; the unprimed name denotes the
numbers $B_n$ with $B_1 = -\tfrac12$ used here, and the primed name the numbers
$B_n^+$. The generating function identity is stated for formal
power series with coefficients in any commutative algebra over the rationals, and
there is a matching identity for $B_n^+$ with right-hand side $t e^t$. In the
von Staudt–Clausen theorem the sum runs over the primes below $2k + 2$, which for
$k \ge 1$ is no restriction, and for $k = 0$ makes the sum empty, so the statement
holds for every $k$ since $B_0 = 1$. The facts about denominators assume
$k \ge 1$, a prime $p$ and $(p - 1) \mid 2k$. The zeta values are stated for the
Riemann zeta function on the complex numbers, with the even-integer formula
assuming $k \ne 0$. The Hurwitz zeta formula is stated for $0 \le x \le 1$ and
assumes $k \ne 0$.

## Depends on

- [Rational number](trough:Rat)
- [Power series](trough:PowerSeries)
- [Exponential](trough:Real.exp)
