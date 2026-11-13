---
declaration: section
origin: cited
lean: MetaMathlibExt.shortIntervalDivisorCount, MetaMathlibExt.shortIntervalDivisorCount_le_card_divisors, MetaMathlibExt.letendreXi, MetaMathlibExt.letendreXi_of_le_sq, MetaMathlibExt.letendreXi_of_small_theta_large_eta, MetaMathlibExt.prod_zpow_le_lcm_zpow_mul_prod_gcd, MetaMathlibExt.exists_perm_prefix_sum_le, MetaMathlibExt.card_le_of_avoids_residues_primePow
statement: formalized
---

# Divisors in short intervals

17 results, 5 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html).

## Number of divisors in a short interval

For a natural number $n$ and real numbers $X$
and $Y$, Letendre's $D_n(X, Y)$ is the number of positive divisors $d$ of $n$ with
$X \le d \le X + Y$. Here $0$ is taken to have no divisors, so $D_0(X, Y) = 0$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Section 1 (definition of `D_n(X, Y)`).

Formalized by `MetaMathlibExt.shortIntervalDivisorCount`, a definition declared in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#short-interval-divisor-count).

## Trivial bound for the short-interval divisor count

For every natural number $n$ and
all real numbers $X$ and $Y$, the number $D_n(X, Y)$ of positive divisors of $n$ in
$[X, X + Y]$ is at most the number $\tau(n)$ of positive divisors of $n$. Here $0$ is taken to
have no divisors, so $D_0(X, Y) = \tau(0) = 0$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Section 1 (definition of `D_n(X, Y)`).

Formalized by `MetaMathlibExt.shortIntervalDivisorCount_le_card_divisors`, a theorem declared in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#short-interval-divisor-count-le-card-div).

## Letendre's saving exponent

For real numbers $\theta$ and $\eta$, Letendre's saving
exponent $\xi(\theta, \eta)$ is defined as follows. If $\eta \le \theta^2$, then
$\xi(\theta, \eta) = 1$. Otherwise, if $\theta \le 1/2$, then $\xi(\theta, \eta) = \theta^2/\eta$
when $2\eta \le \theta$ and $\xi(\theta, \eta) = 4(\theta - \eta)$ when $2\eta > \theta$; and if
$\theta > 1/2$, then $\xi(\theta, \eta) = (1 - \theta)^2/((1 - \theta)^2 + \eta - \theta^2)$ when
$2\eta \le 3\theta - 1$ and $\xi(\theta, \eta) = 4(\theta - \eta)$ when $2\eta > 3\theta - 1$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Theorem 1, display (2).

Formalized by `MetaMathlibExt.letendreXi`, a definition declared in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#letendre-xi).

## Letendre's exponent equals $1$ when $\eta \le \theta^2$

For all real numbers $\theta$ and
$\eta$ with $\eta \le \theta^2$, Letendre's saving exponent satisfies $\xi(\theta, \eta) = 1$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Theorem 1, display (2).

Formalized by `MetaMathlibExt.letendreXi_of_le_sq`, a theorem declared in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#letendre-xi-of-le-sq).

## Letendre's exponent for $\theta^2 < \eta$, $\theta \le 1/2$ and $\theta < 2\eta$

For all
real numbers $\theta$ and $\eta$ with $\theta^2 < \eta$, $\theta \le 1/2$ and $\theta < 2\eta$,
Letendre's saving exponent satisfies $\xi(\theta, \eta) = 4(\theta - \eta)$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Theorem 1, display (2).

Formalized by `MetaMathlibExt.letendreXi_of_small_theta_large_eta`, a theorem declared in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#letendre-xi-of-small-theta-large-eta).

## Cohen's lcm–gcd inequality

Let $k$ be a natural number, let $d_1, \dots, d_k$ be
positive integers and let $t$ be an integer. Then, as an inequality of rational numbers,

$$\prod_{i=1}^{k} d_i^{\,t} \le \operatorname{lcm}(d_1, \dots, d_k)^{t(t+1)/2}
\prod_{1 \le i < j \le k} \gcd(d_i, d_j),$$

where the exponent $t(t+1)/2$ is an integer.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Lemma 1.

Stated but not proved: `MetaMathlibExt.prod_zpow_le_lcm_zpow_mul_prod_gcd` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#prod-zpow-le-lcm-zpow-mul-prod-gcd).

## Reordering so that prefix sums compare

Let $k$ be a natural number and let
$x_1, \dots, x_k$ and $y_1, \dots, y_k$ be real numbers with $\sum_i x_i \le \sum_i y_i$. Then
there is a permutation $\sigma$ of $\{1, \dots, k\}$ such that
$\sum_{i \le s} x_{\sigma(i)} \le \sum_{i \le s} y_{\sigma(i)}$ for every $s$ with $0 \le s \le k$.

No positivity of the $x_i$ or $y_i$ is assumed.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Lemma 2.

Stated but not proved: `MetaMathlibExt.exists_perm_prefix_sum_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#exists-perm-prefix-sum-le).

## Arithmetic large sieve with prime-power moduli

Let $N \ge 1$ be an integer and let $M$
be a finite set of integers contained in $[a, a + N)$ for some integer $a$. Let $S$ be a finite
set of primes and, for each $p \in S$, let $\beta_p \ge 1$ be an integer and let $\Omega_p$ be a
set of fewer than $p^{\beta_p}$ integers in $[0, p^{\beta_p})$ such that no $m \in M$ has its
remainder modulo $p^{\beta_p}$ in $\Omega_p$. Then for every real $Q \ge 1$,

$$|M| \le \frac{N + Q^2}{\sum_{1 \le q \le Q} h(q)},$$

where $q$ runs over the integers in $[1, Q]$ and $h(q) = \prod_{p \mid q} h_p(q)$, the product
over the prime factors $p$ of $q$ of $h_p(q) = |\Omega_p| / (p^{\beta_p} - |\Omega_p|)$ if
$p \in S$ and $p^{\beta_p}$ exactly divides $q$, and $h_p(q) = 0$ otherwise (so $h(1) = 1$).

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Lemma 3.

Stated but not proved: `MetaMathlibExt.card_le_of_avoids_residues_primePow` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#card-le-of-avoids-residues-prime-pow).

## Counting $x$ with $x^2 + p^v u$ not a square modulo $p^{v+1}$

Let $p \ge 3$ be a prime
and let $u$ be an integer not divisible by $p$. For $v \ge 0$ let $S_v$ be the number of integers
$0 \le x < p^{v+1}$ for which there is no integer $y$ with
$x^2 + p^v u \equiv y^2 \pmod{p^{v+1}}$. Then $2 S_0 = p - \left(\frac{-u}{p}\right)$, where
$\left(\frac{-u}{p}\right)$ is the Legendre symbol, $S_1 = p$, and $S_v = p S_{v-2}$ for every
$v \ge 2$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Lemma 4.

Stated but not proved: `MetaMathlibExt.card_unsolvable_sq_add_primePow` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#card-unsolvable-sq-add-prime-pow).

## Divisors in windows of length $n^{\theta^2 - \varepsilon}$

For a natural number $n$ and
real numbers $X$, $Y$, let $D_n(X, Y)$ be the number of divisors $d$ of $n$ with
$X \le d \le X + Y$. There is an absolute constant $C$ such that for every integer $n \ge 1$ and
all real numbers $\theta$, $\varepsilon$ with $0 < \theta < 1$ and $0 < \varepsilon < \theta^2$,
$D_n(n^\theta, n^{\theta^2 - \varepsilon}) \le
C \left(\theta(1 - \theta)/\varepsilon + 1/(\theta(1 - \theta))\right)$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Proposition 1.

Stated but not proved: `MetaMathlibExt.exists_shortIntervalDivisorCount_le_of_window_theta_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#exists-short-interval-divisor-count-le-o).

## Letendre's exponent as the largest admissible exponent

Let $\theta$ and $\eta$ be real
numbers with $\theta^2 \le \eta < \theta$. Then Letendre's saving exponent $\xi(\theta, \eta)$ is
the largest real number $A$ with $0 < A \le 1$ such that

$$\left(\frac{\theta - t}{\alpha}\right)^2 - \frac{\eta - t}{\alpha} \ge 0$$

for all real numbers $\alpha$ and $t$ with $0 < \alpha \le A$ and $0 \le t \le 1 - \alpha$.

On this range $\xi(\theta, \eta)$ equals the paper's $\alpha(\theta, \eta)$ of display (4). The cap
$A \le 1$ reflects $\alpha$ being an exponent ($a = n^\alpha \le n$); without it the set of such
$A$ is unbounded when $\eta = \theta^2$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Proposition 2.

Stated but not proved: `MetaMathlibExt.isGreatest_letendreXi` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#is-greatest-letendre-xi).

## Exponents with a margin in Letendre's inequality

Let $\xi(\theta, \eta)$ denote Letendre's
saving exponent, and let $\theta$, $\eta$ and $\delta$ be real numbers with $0 \le \delta \le 1$,
$\eta < \theta < 1$ and $0 < \theta^2 - (\theta(1 - \theta))^2 \delta \le \eta$. Then there is a
real number $A > 0$ with $\xi(\theta, \eta) - \delta \le A \le \xi(\theta, \eta)$ such that
$((\theta - t)/\alpha)^2 - (\eta - t)/\alpha \ge (\theta(1 - \theta))^2 \delta$ for all real
numbers $\alpha$ and $t$ with $0 < \alpha \le A$ and $0 \le t \le 1 - \alpha$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Proposition 3.

Stated but not proved: `MetaMathlibExt.exists_alpha_with_margin` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#exists-alpha-with-margin).

## Letendre's bound for divisors in short intervals

For a natural number $n$ and real numbers
$X$, $Y$, let $D_n(X, Y)$ be the number of divisors $d$ of $n$ with $X \le d \le X + Y$, let
$\tau(n)$ be the number of divisors of $n$, let $V(n)$ be the largest exponent in the prime
factorization of $n$, and let $\xi(\theta, \eta)$ be Letendre's saving exponent. There is an
absolute constant $C$ such that for all real numbers $\theta$, $\eta$ with $0 < \eta < \theta < 1$
and every integer $n \ge 2$,
$D_n(n^\theta, n^\eta) \le C \tau(n)^{1 - \xi(\theta, \eta)} V(n) \log \tau(n) /
(\theta(1 - \theta))$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Theorem 1.

Stated but not proved: `MetaMathlibExt.exists_shortIntervalDivisorCount_le_letendre` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#exists-short-interval-divisor-count-le-l).

## Arbitrarily large integers with a divisor in a short window

Let $\theta$ and $\varepsilon$
be real numbers with $0 < \theta < 1$ and $0 < \varepsilon < \theta$. Then for every natural
number $N$ there is a natural number $n \ge N$ with at least one divisor $d$ satisfying
$n^\theta \le d \le n^\theta + n^{\theta - \varepsilon}$.

This is the nontrivial form of the statement that a constant bounding the number of such divisors
for all $n \ge 1$ is at least $1$; that weaker statement already follows from $n = 1$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Proposition 4.

Stated but not proved: `MetaMathlibExt.exists_large_shortIntervalDivisorCount_pos` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#exists-large-short-interval-divisor-coun).

## Lower bound for constants bounding divisors in short windows

There is an absolute
constant $c > 0$ with the following property. Let $\theta$, $\varepsilon$ and $k$ be real numbers
with $0 < \theta < 1$ and $0 < \varepsilon < \theta$, and suppose that for every integer $n \ge 1$
the number of divisors $d$ of $n$ with $n^\theta \le d \le n^\theta + n^{\theta - \varepsilon}$ is
at most $k$. Then $c \sqrt{\varepsilon} \, (\theta(1 - \theta))^{3/2} \,
\left(1 / (\theta^\theta (1 - \theta)^{1 - \theta})\right)^{1/\varepsilon} \le k$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Theorem 2.

Stated but not proved: `MetaMathlibExt.exists_lower_bound_conjecture_constant` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#exists-lower-bound-conjecture-constant).

## Letendre's square-root bound for divisors in short intervals

For a natural number $n$
and real numbers $X$, $Y$, let $D_n(X, Y)$ be the number of divisors $d$ of $n$ with
$X \le d \le X + Y$, let $\tau(n)$ be the number of divisors of $n$, and let $\xi(\theta, \eta)$
be Letendre's saving exponent. There is an absolute constant $C$ such that for all real numbers
$\theta$, $\eta$ with $0 < \eta < \theta < 1$ and every integer $n \ge 2$,
$D_n(n^\theta, n^\eta) \le C \tau(n)^{1 - \xi(\theta, \eta)/2}
\sqrt{\log \tau(n) / (\theta(1 - \theta))}$.

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Corollary 1 (journal version).

Stated but not proved: `MetaMathlibExt.exists_shortIntervalDivisorCount_le_sqrt_letendre` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#exists-short-interval-divisor-count-le-s).

## Divisors near $\sqrt{an/b}$

Let $a$ and $b$ be coprime positive integers. For a natural
number $n$ and real numbers $X$, $Y$, let $D_n(X, Y)$ be the number of divisors $d$ of $n$ with
$X \le d \le X + Y$, and let $\omega(m)$ be the number of distinct prime factors of $m$. There is
a constant $C$, depending on $a$ and $b$, such that for all integers $n \ge 1$ and $i \ge 1$,
writing $x_0 = \sqrt{an/b}$ and $w = \omega(4abn)$,

$$D_n\bigl(x_0, \sqrt{i x_0 / b}\bigr) \le C \min\bigl(i, \; i/w + w (\log w)^2\bigr).$$

## Sources

- Patrick Letendre, *Divisors of an Integer in a Short Interval*, INTEGERS 26 (2026), Article A115, Proposition 5 (journal version).

Stated but not proved: `MetaMathlibExt.exists_shortIntervalDivisorCount_sqrt_window_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorsShortIntervalWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html#exists-short-interval-divisor-count-sqrt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Divisors in short intervals](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisors-in-short-intervals)
