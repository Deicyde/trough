---
declaration: section
origin: cited
lean: MetaMathlibExt.gammaBinom, MetaMathlibExt.gammaBinom_natCast, MetaMathlibExt.gammaBinom_zero_right, MetaMathlibExt.integral_cos_half_cpow, MetaMathlibExt.integral_sin_half_cpow, MetaMathlibExt.integral_cos_pow_zero_pi, MetaMathlibExt.integral_cos_half_cpow_mul_sin_half_cpow, MetaMathlibExt.integral_cos_pow_mul_sin_cpow
statement: formalized
---

# Knuth's old sum

66 results, 4 proved and 62 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html).

## Generalized binomial coefficient of complex arguments

For complex numbers $u$ and $v$, the
generalized binomial coefficient is

$$
\binom{u}{v} = \frac{\Gamma(u+1)}{\Gamma(v+1)\,\Gamma(u-v+1)},
$$

where $\Gamma$ is taken to be $0$ at the non-positive integers (its poles) and division by $0$
gives $0$. In particular $\binom{u}{v} = 0$ whenever $v$ or $u - v$ is a negative integer, and at
natural arguments $\binom{u}{v}$ is the ordinary binomial coefficient.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Section 2, equation (7).

Formalized by `MetaMathlibExt.gammaBinom`, a definition declared in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#gamma-binom).

## The generalized binomial coefficient at natural arguments

For all natural numbers $n$
and $k$, the generalized binomial coefficient of complex arguments at $(n, k)$, namely
$\Gamma(n+1)/(\Gamma(k+1)\,\Gamma(n-k+1))$, equals the ordinary binomial coefficient
$\binom{n}{k}$; in particular it is $0$ when $k > n$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Section 2 (definitions of the binomial and the generalized binomial coefficients).

Formalized by `MetaMathlibExt.gammaBinom_natCast`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#gamma-binom-nat-cast).

## The generalized binomial coefficient with lower argument zero

For every complex number $u$
with $\operatorname{Re} u > -1$, the generalized binomial coefficient of complex arguments
$\binom{u}{0} = \Gamma(u+1)/(\Gamma(1)\,\Gamma(u+1))$ equals $1$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Section 2, equation (7).

Formalized by `MetaMathlibExt.gammaBinom_zero_right`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#gamma-binom-zero-right).

## Integral of a complex power of $\cos(x/2)$ over $(0, \pi)$

For every complex number $u$
with $\operatorname{Re} u > -1$,

$$
\int_0^\pi \cos(x/2)^u \, dx = 2^{-u} \pi \binom{u}{u/2},
$$

where $\cos(x/2)^u$ is the principal complex power of the nonnegative real $\cos(x/2)$ and
$\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\,\Gamma(a-b+1))$ is the generalized binomial coefficient
of complex arguments.

This is the first equality of equation (8) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Lemma 1.

Stated but not proved: `MetaMathlibExt.integral_cos_half_cpow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#integral-cos-half-cpow).

## Integral of $\sin(x/2)$ to a complex power over $(0, \pi)$

For every complex number $u$
with $\operatorname{Re} u > -1$,

$$
\int_0^\pi \sin(x/2)^u \, dx = 2^{-u} \pi \binom{u}{u/2},
$$

where $\sin(x/2)^u$ is the principal complex power of the nonnegative real $\sin(x/2)$ and
$\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\,\Gamma(a-b+1))$ is the generalized binomial coefficient
of complex arguments.

This is the second equality of equation (8) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Lemma 1.

Stated but not proved: `MetaMathlibExt.integral_sin_half_cpow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#integral-sin-half-cpow).

## Integral of $\cos^m x$ over $(0, \pi)$

For every natural number $m$,
$\int_0^\pi \cos^m x \, dx$ equals $\pi \binom{m}{m/2} / 2^m$ if $m$ is even and $0$ if $m$ is
odd.

This is equation (9) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Lemma 1.

Stated but not proved: `MetaMathlibExt.integral_cos_pow_zero_pi` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#integral-cos-pow-zero-pi).

## Integral of $\cos^u(x/2)\sin^v(x/2)$ over $(0, \pi)$

For all complex numbers $u$ and $v$
with $\operatorname{Re} u > -1$ and $\operatorname{Re} v > -1$,

$$
\int_0^\pi \cos(x/2)^u \sin(x/2)^v \, dx =
2^{-u-v} \pi \binom{u}{u/2} \binom{v}{v/2} \binom{(u+v)/2}{u/2}^{-1},
$$

where the powers are principal complex powers of the nonnegative reals $\cos(x/2)$ and
$\sin(x/2)$, and $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\,\Gamma(a-b+1))$ is the generalized
binomial coefficient of complex arguments.

This is equation (10) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Lemma 1.

Stated but not proved: `MetaMathlibExt.integral_cos_half_cpow_mul_sin_half_cpow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#integral-cos-half-cpow-mul-sin-half-cpow).

## Integral of $\cos^m x \, \sin^v x$ over $(0, \pi)$

For every natural number $m$ and every
complex number $v$ with $\operatorname{Re} v > -1$, the integral
$\int_0^\pi \cos^m x \, \sin(x)^v \, dx$ equals
$2^{-m-v} \pi \binom{m}{m/2} \binom{v}{v/2} \binom{(m+v)/2}{m/2}^{-1}$ if $m$ is even and $0$
if $m$ is odd. Here $\sin(x)^v$ is the principal complex power of the nonnegative real $\sin x$
and $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\,\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex arguments.

This is equation (11) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Lemma 1.

Stated but not proved: `MetaMathlibExt.integral_cos_pow_mul_sin_cpow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#integral-cos-pow-mul-sin-cpow).

## Knuth's old sum (the Reed–Dawson identity)

For every natural number $n$, the sum
$\sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{2k}{k} 2^{-k}$ equals $2^{-n} \binom{n}{n/2}$ if $n$
is even and $0$ if $n$ is odd.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 1.

Stated but not proved: `MetaMathlibExt.knuth_old_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#knuth-old-sum).

## Two-parameter generalization of Knuth's old sum

For all natural numbers $m$ and $n$ and
every real number $v > -1$,

$$
\sum_{k=0}^{n} \frac{(-1)^k \binom{n}{k}}{2^{k+m}} \binom{2k+2m+v}{(2k+2m+v)/2}
\binom{k+m+v}{v/2}^{-1}
$$

equals, if $n$ is even,

$$
\sum_{k=0}^{\lfloor m/2 \rfloor} \frac{\binom{m}{2k}}{2^{n+2k}} \binom{2k+n}{(2k+n)/2}
\binom{(2k+n+v)/2}{(2k+n)/2}^{-1}
$$

and, if $n$ is odd,

$$
-\sum_{k=1}^{\lfloor (m+1)/2 \rfloor} \frac{\binom{m}{2k-1}}{2^{n+2k-1}}
\binom{2k+n-1}{(2k+n-1)/2} \binom{(2k+n-1+v)/2}{(2k+n-1)/2}^{-1}.
$$

Here $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\,\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex arguments, which at natural arguments is the ordinary binomial coefficient.

This is equation (14) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 2.

Stated but not proved: `MetaMathlibExt.knuth_old_sum_gammaBinom_shift` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#knuth-old-sum-gamma-binom-shift).

## One-parameter generalization of Knuth's old sum

For every natural number $n$ and every
real number $v > -1$,

$$
\sum_{k=0}^{n} \frac{(-1)^k \binom{n}{k}}{2^k} \binom{2k+v}{(2k+v)/2} \binom{k+v}{v/2}^{-1}
$$

equals $\binom{n}{n/2} 2^{-n} \binom{(n+v)/2}{v/2}^{-1}$ if $n$ is even and $0$ if $n$ is odd.
Here $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\,\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex arguments, which at natural arguments is the ordinary binomial coefficient.

This is equation (15) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 1.

Stated but not proved: `MetaMathlibExt.knuth_old_sum_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#knuth-old-sum-gamma-binom).

## Even-index binomial sum with inverse generalized binomial coefficients

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex $u$, $w$, which for natural $u$, $w$ is the ordinary binomial coefficient.
For every natural number $n$ and every real $v > -1$,

$$
\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{1}{2^{2k}} \binom{2k}{k}
\binom{(2k+v)/2}{k}^{-1}
= \frac{1}{2^n} \binom{2n+v}{(2n+v)/2} \binom{n+v}{v/2}^{-1}.
$$

This is equation (16) of the source, the case $n = 0$ of its two-parameter identity (14), whose
parameter $m$ is called $n$ here.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 2.

Stated but not proved: `MetaMathlibExt.sum_choose_two_mul_inv_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-two-mul-inv-gamma-binom).

## Odd-index binomial sum with inverse generalized binomial coefficients

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex $u$, $w$, which for natural $u$, $w$ is the ordinary binomial coefficient.
For every natural number $n$ and every real $v > -1$,

$$
\sum_{k=1}^{\lceil n/2 \rceil} \binom{n}{2k-1} \frac{2^n}{2^{2k}} \binom{2k}{k}
\binom{(2k+v)/2}{k}^{-1}
= \frac{1}{2} \binom{2n+v+2}{(2n+v+2)/2} \binom{n+v+1}{v/2}^{-1} -
\binom{2n+v}{(2n+v)/2} \binom{n+v}{v/2}^{-1}.
$$

This is equation (17) of the source, the case $n = 1$ of its two-parameter identity (14), whose
parameter $m$ is called $n$ here.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 2.

Stated but not proved: `MetaMathlibExt.sum_choose_two_mul_sub_one_inv_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-two-mul-sub-one-inv-gamma-bin).

## Odd-index binomial sum with odd reciprocal weights

For every natural number $n$,

$$\sum_{k=1}^{\lceil n/2 \rceil} \frac{1}{2k+1} \binom{n}{2k-1} =
\frac{2^{n+1}}{n+2} - \frac{2^n}{n+1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 1.

Stated but not proved: `MetaMathlibExt.sum_choose_odd_div_two_mul_add_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-odd-div-two-mul-add-one).

## Odd-index binomial sum of Catalan numbers

Write $C_m = \binom{2m}{m}/(m+1)$ for the
$m$-th Catalan number. For every natural number $n$,

$$\sum_{k=1}^{\lceil n/2 \rceil} \binom{n}{2k-1} \frac{2^n}{2^{2k}} C_k =
\frac{1}{2} C_{n+2} - C_{n+1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 1.

Stated but not proved: `MetaMathlibExt.sum_choose_odd_two_pow_mul_catalan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-odd-two-pow-mul-catalan).

## Alternating binomial sum of $2^{k+m}/(k+m+1)$

For all natural numbers $m$ and $n$, the
rational number $S = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \frac{2^{k+m}}{k+m+1}$ satisfies

$$S = \sum_{k=0}^{\lfloor m/2 \rfloor} \frac{\binom{m}{2k}}{2k+n+1}$$

when $n$ is even, and

$$S = -\sum_{k=1}^{\lfloor (m+1)/2 \rfloor} \frac{\binom{m}{2k-1}}{2k+n}$$

when $n$ is odd.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 2.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_two_pow_div_add_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-choose-two-pow-div-add-o).

## Alternating convolution of central binomial coefficients

For every natural number
$n$, the integer $\sum_{k=0}^{n} (-1)^k \binom{2k}{k} \binom{2(n-k)}{n-k}$ equals
$2^n \binom{n}{n/2}$ when $n$ is even and $0$ when $n$ is odd.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 3.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_centralBinom_mul_centralBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-central-binom-mul-centra).

## Alternating convolution of generalized central binomial coefficients

For every
natural number $n$ and every real $v > -1$, the sum

$$
\sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{2k+v}{(2k+v)/2} \binom{2n-2k+v}{(2n-2k+v)/2}
\binom{n+v}{(2k+v)/2}^{-1}
$$

equals $2^n \binom{n}{n/2} \binom{v}{v/2} \binom{(n+v)/2}{v/2}^{-1}$ when $n$ is even and $0$
when $n$ is odd. Here $\binom{n}{k}$ and $\binom{n}{n/2}$ are ordinary binomial coefficients and
otherwise $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex numbers $a, b$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 5.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_gammaBinom_complement` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-choose-gamma-binom-compl).

## Convolution of generalized central binomial coefficients

For complex numbers $u$ and
$w$ write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\,\Gamma(u-w+1))$ for the generalized
binomial coefficient, which is the ordinary binomial coefficient at natural arguments. For
every natural number $n$ and every real number $v > -1$,

$$\sum_{k=0}^{n} \binom{n}{k} \binom{2k+v}{(2k+v)/2} \binom{2n-2k+v}{(2n-2k+v)/2}
\binom{n+v}{(2k+v)/2}^{-1} = 2^{2n} \binom{v}{v/2}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 6.

Stated but not proved: `MetaMathlibExt.sum_choose_gammaBinom_convolution` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-gamma-binom-convolution).

## Reciprocal binomial transform of a polynomial identity

Let $s, n, m, r$ be natural
numbers, $f, g : \mathbb{N} \to \mathbb{C}$ and $p, q : \mathbb{N} \to \mathbb{N}$ such that
$\sum_{k=s}^{n} f(k) (1+t)^{p(k)} = \sum_{k=m}^{r} g(k) t^{q(k)}$ for every complex $t$. Then
for all complex numbers $u, v$ with $\operatorname{Re} u > -1$ and $\operatorname{Re} v > -1$,

$$
\sum_{k=s}^{n} f(k) \binom{p(k)+u+v+1}{u+1}^{-1}
= \frac{u+1}{v+1} \sum_{k=m}^{r} (-1)^{q(k)} g(k) \binom{q(k)+u+v+1}{v+1}^{-1},
$$

where $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex numbers $a, b$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 7.

Stated but not proved: `MetaMathlibExt.sum_inv_gammaBinom_of_binomial_poly_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-inv-gamma-binom-of-binomial-poly-ide).

## Shifted central binomial transform of a polynomial identity

Let $s, n, m, r$ be
natural numbers, $f, g : \mathbb{N} \to \mathbb{C}$ and $p, q : \mathbb{N} \to \mathbb{N}$
such that $\sum_{k=s}^{n} f(k) (1+t)^{p(k)} = \sum_{k=m}^{r} g(k) t^{q(k)}$ for every
complex $t$, and let $u, v$ be complex numbers with $\operatorname{Re} v > -1$,
$\operatorname{Re}(2(u-p(j))+v) > -1$ for $s \le j \le n$ and
$\operatorname{Re}(2(u-q(j))+v) > -1$ for $m \le j \le r$. Then

$$
\sum_{k=s}^{n} f(k)\, 2^{2p(k)} \binom{2(u-p(k))+v}{(2(u-p(k))+v)/2}
\binom{u-p(k)+v}{v/2}^{-1}
= \binom{v}{v/2}^{-1} \sum_{k=m}^{r} g(k) \binom{2(u-q(k))+v}{(2(u-q(k))+v)/2}
\binom{2q(k)+v}{(2q(k)+v)/2} \binom{u+v}{(2q(k)+v)/2}^{-1},
$$

where $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex numbers $a, b$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 8.

Stated but not proved: `MetaMathlibExt.sum_gammaBinom_shift_of_binomial_poly_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-gamma-binom-shift-of-binomial-poly-i).

## Shifted central binomial transform of a polynomial identity, dual form

Let
$s, n, m, r$ be natural numbers, $f, g : \mathbb{N} \to \mathbb{C}$ and
$p, q : \mathbb{N} \to \mathbb{N}$ such that
$\sum_{k=s}^{n} f(k) (1+t)^{p(k)} = \sum_{k=m}^{r} g(k) t^{q(k)}$ for every complex $t$, and
let $u, v$ be complex numbers with $\operatorname{Re} v > -1$,
$\operatorname{Re}(2(u-p(j))+v) > -1$ for $s \le j \le n$ and
$\operatorname{Re}(2(u-q(j))+v) > -1$ for $m \le j \le r$. Then

$$
\sum_{k=m}^{r} (-1)^{q(k)} g(k)\, 2^{2q(k)} \binom{2(u-q(k))+v}{(2(u-q(k))+v)/2}
\binom{u-q(k)+v}{v/2}^{-1}
= \binom{v}{v/2}^{-1} \sum_{k=s}^{n} (-1)^{p(k)} f(k) \binom{2(u-p(k))+v}{(2(u-p(k))+v)/2}
\binom{2p(k)+v}{(2p(k)+v)/2} \binom{u+v}{(2p(k)+v)/2}^{-1},
$$

where $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex numbers $a, b$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 8.

Stated but not proved: `MetaMathlibExt.sum_gammaBinom_shift_of_binomial_poly_identity'` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-gamma-binom-shift-of-binomial-poly-i-2).

## Alternating reciprocal generalized-binomial sums from a polynomial identity

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\,\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex numbers $u$ and $w$. Let $s, n, m, r$ be natural numbers, let
$f, g \colon \mathbb{N} \to \mathbb{C}$ and $p, q \colon \mathbb{N} \to \mathbb{N}$ satisfy

$$\sum_{k=s}^{n} f(k)\,(1+t)^{p(k)} = \sum_{k=m}^{r} g(k)\, t^{q(k)}
\quad \text{for all } t \in \mathbb{C},$$

and let $u, v$ be complex numbers with $\operatorname{Re} v > -1$,
$\operatorname{Re} u - p(j) > -1$ for $s \le j \le n$ and $\operatorname{Re} u - q(j) > -1$ for
$m \le j \le r$. Then

$$\sum_{k=s}^{n} (-1)^{p(k)} f(k) \binom{u+v}{u-p(k)}^{-1}
= \frac{u+v+1}{v+1} \sum_{k=m}^{r} (-1)^{q(k)} g(k) \binom{u-q(k)+v+1}{v+1}^{-1}.$$

This is the paper's equation (34) corrected. The paper prints the last binomial as
$\binom{u-q(k)+1}{v+1}$; that is false (for the identity $1 = 1$, that is $f = g = 1$ and
$p = q = 0$, at $u = v = 1$ the left side is $1/2$ and the printed right side $3/2$), and the
paper's own proof (integration against $(1-x)^v$ with the Beta integral) gives the reading
stated here, which agrees with the printed one at $v = 0$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 9.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_inv_gammaBinom_of_binomial_poly_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-inv-gamma-binom-of-binom).

## Two-parameter generalized-binomial sums from a polynomial identity

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\,\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex numbers $u$ and $w$. Let $s, n, m, r$ be natural numbers, let
$f, g \colon \mathbb{N} \to \mathbb{C}$ and $p, q \colon \mathbb{N} \to \mathbb{N}$ satisfy

$$\sum_{k=s}^{n} f(k)\,(1+t)^{p(k)} = \sum_{k=m}^{r} g(k)\, t^{q(k)}
\quad \text{for all } t \in \mathbb{C},$$

and let $u, v$ be complex numbers with $\operatorname{Re} u > -1$ and $\operatorname{Re} v > -1$.
Then

$$\sum_{k=s}^{n} \frac{f(k)}{2^{2p(k)}} \binom{v}{v/2} \binom{2p(k)+u}{(2p(k)+u)/2}
\binom{(2p(k)+u+v)/2}{v/2}^{-1}
= \sum_{k=m}^{r} \frac{(-1)^{q(k)} g(k)}{2^{2q(k)}} \binom{u}{u/2}
\binom{2q(k)+v}{(2q(k)+v)/2} \binom{(2q(k)+u+v)/2}{u/2}^{-1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 10.

Stated but not proved: `MetaMathlibExt.sum_two_param_gammaBinom_of_binomial_poly_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-two-param-gamma-binom-of-binomial-po).

## Central binomial transform of a polynomial identity, even exponents at even indices

Let $s, n, m, r$ be natural numbers, $f, g : \mathbb{N} \to \mathbb{C}$ and
$p, q : \mathbb{N} \to \mathbb{N}$ such that
$\sum_{k=s}^{n} f(k) (1+t)^{p(k)} = \sum_{k=m}^{r} g(k) t^{q(k)}$ for every complex $t$.
Suppose that $q(2j)$ is even whenever $m \le 2j \le r$ and $q(2j+1)$ is odd whenever
$m \le 2j+1 \le r$. Then for every complex $v$ with $\operatorname{Re} v > -1$,

$$
\sum_{k=s}^{n} \frac{f(k)}{2^{p(k)}} \binom{2p(k)+v}{(2p(k)+v)/2} \binom{p(k)+v}{v/2}^{-1}
= \sum_{k=\lfloor (m+1)/2 \rfloor}^{\lfloor r/2 \rfloor} \frac{g(2k)}{2^{q(2k)}}
\binom{q(2k)}{q(2k)/2} \binom{(q(2k)+v)/2}{v/2}^{-1},
$$

where $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex numbers $a, b$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 11, part 1.

Stated but not proved: `MetaMathlibExt.sum_gammaBinom_of_binomial_poly_identity_q_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-gamma-binom-of-binomial-poly-identit).

## Central binomial sums from a polynomial identity: right exponents odd at even indices

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex $u$, $w$. Let $s, n, m, r$ be natural numbers, let $f, g$ be
complex-valued functions and $p, q$ natural-number-valued functions on the natural numbers, and
suppose that for every complex $t$,

$$
\sum_{k=s}^{n} f(k) (1+t)^{p(k)} = \sum_{k=m}^{r} g(k) t^{q(k)}.
$$

Suppose also that $q(2j)$ is odd whenever $m \le 2j \le r$, and $q(2j+1)$ is even whenever
$m \le 2j+1 \le r$. Then for every complex $v$ with $\operatorname{Re} v > -1$,

$$
\sum_{k=s}^{n} \frac{f(k)}{2^{p(k)}} \binom{2p(k)+v}{(2p(k)+v)/2} \binom{p(k)+v}{v/2}^{-1}
= \sum_{k=\lfloor (m+2)/2 \rfloor}^{\lfloor (r+1)/2 \rfloor} \frac{g(2k-1)}{2^{q(2k-1)}}
\binom{q(2k-1)}{q(2k-1)/2} \binom{(q(2k-1)+v)/2}{v/2}^{-1}.
$$

This is equation (37) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 11, part 1.

Stated but not proved: `MetaMathlibExt.sum_gammaBinom_of_binomial_poly_identity_q_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-gamma-binom-of-binomial-poly-identit-2).

## Central binomial sums from a polynomial identity: left exponents even at even indices

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex $u$, $w$. Let $s, n, m, r$ be natural numbers, let $f, g$ be
complex-valued functions and $p, q$ natural-number-valued functions on the natural numbers, and
suppose that for every complex $t$,

$$
\sum_{k=s}^{n} f(k) (1+t)^{p(k)} = \sum_{k=m}^{r} g(k) t^{q(k)}.
$$

Suppose also that $p(2j)$ is even whenever $s \le 2j \le n$, and $p(2j+1)$ is odd whenever
$s \le 2j+1 \le n$. Then for every complex $v$ with $\operatorname{Re} v > -1$,

$$
\sum_{k=m}^{r} \frac{(-1)^{q(k)} g(k)}{2^{q(k)}} \binom{2q(k)+v}{(2q(k)+v)/2}
\binom{q(k)+v}{v/2}^{-1}
= \sum_{k=\lfloor (s+1)/2 \rfloor}^{\lfloor n/2 \rfloor} \frac{(-1)^{p(2k)} f(2k)}{2^{p(2k)}}
\binom{p(2k)}{p(2k)/2} \binom{(p(2k)+v)/2}{v/2}^{-1}.
$$

This is equation (38) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 11, part 2.

Stated but not proved: `MetaMathlibExt.sum_gammaBinom_of_binomial_poly_identity_p_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-gamma-binom-of-binomial-poly-identit-3).

## Central binomial sums from a polynomial identity: left exponents odd at even indices

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex $u$, $w$. Let $s, n, m, r$ be natural numbers, let $f, g$ be
complex-valued functions and $p, q$ natural-number-valued functions on the natural numbers, and
suppose that for every complex $t$,

$$
\sum_{k=s}^{n} f(k) (1+t)^{p(k)} = \sum_{k=m}^{r} g(k) t^{q(k)}.
$$

Suppose also that $p(2j)$ is odd whenever $s \le 2j \le n$, and $p(2j+1)$ is even whenever
$s \le 2j+1 \le n$. Then for every complex $v$ with $\operatorname{Re} v > -1$,

$$
\sum_{k=m}^{r} \frac{(-1)^{q(k)} g(k)}{2^{q(k)}} \binom{2q(k)+v}{(2q(k)+v)/2}
\binom{q(k)+v}{v/2}^{-1}
= \sum_{k=\lfloor (s+2)/2 \rfloor}^{\lfloor (n+1)/2 \rfloor}
\frac{(-1)^{p(2k-1)} f(2k-1)}{2^{p(2k-1)}}
\binom{p(2k-1)}{p(2k-1)/2} \binom{(p(2k-1)+v)/2}{v/2}^{-1}.
$$

This is equation (39) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 11, part 2.

Stated but not proved: `MetaMathlibExt.sum_gammaBinom_of_binomial_poly_identity_p_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-gamma-binom-of-binomial-poly-identit-4).

## Central binomial transform of a polynomial identity with exponents $k$

Let
$s, n, m, r$ be natural numbers and $f, g : \mathbb{N} \to \mathbb{C}$ such that
$\sum_{k=s}^{n} f(k) (1+t)^{k} = \sum_{k=m}^{r} g(k) t^{k}$ for every complex $t$. Then for
every real $v > -1$,

$$
\sum_{k=s}^{n} \frac{f(k)}{2^{k}} \binom{2k+v}{(2k+v)/2} \binom{k+v}{v/2}^{-1}
= \sum_{k=\lfloor (m+1)/2 \rfloor}^{\lfloor r/2 \rfloor} \frac{g(2k)}{2^{2k}} \binom{2k}{k}
\binom{(2k+v)/2}{v/2}^{-1},
$$

where $\binom{2k}{k}$ is the central binomial coefficient and otherwise
$\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex numbers $a, b$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 3.

Stated but not proved: `MetaMathlibExt.sum_gammaBinom_of_poly_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-gamma-binom-of-poly-identity).

## Alternating companion of a generalized-binomial sum from a polynomial identity in $1+t$

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\,\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex numbers $u$ and $w$. Let $s, n, m, r$ be natural numbers and let
$f, g \colon \mathbb{N} \to \mathbb{C}$ satisfy

$$\sum_{k=s}^{n} f(k)\,(1+t)^k = \sum_{k=m}^{r} g(k)\, t^k \quad \text{for all } t \in \mathbb{C}.$$

Then for every real number $v > -1$,

$$\sum_{k=m}^{r} g(k)\, \frac{(-1)^k}{2^k} \binom{2k+v}{(2k+v)/2} \binom{k+v}{v/2}^{-1}
= \sum_{k=\lfloor (s+1)/2 \rfloor}^{\lfloor n/2 \rfloor} \frac{f(2k)}{2^{2k}} \binom{2k}{k}
\binom{(2k+v)/2}{v/2}^{-1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 3.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_gammaBinom_of_poly_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-gamma-binom-of-poly-iden).

## Polynomial identity for reciprocal generalized binomial coefficients

For every natural
number $n$ and all complex numbers $u, v, x$ with $\operatorname{Re} u > -1$ and
$\operatorname{Re} v > -1$,

$$
\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \binom{k+u+v+1}{u+1}^{-1} (1-x)^{n-k}
= \frac{u+1}{v+1} \sum_{k=0}^{n} (-1)^{k} \binom{n}{k} \binom{k+u+v+1}{v+1}^{-1} x^{n-k},
$$

where $\binom{n}{k}$ is the ordinary binomial coefficient and otherwise
$\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex numbers $a, b$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 12.

Stated but not proved: `MetaMathlibExt.sum_inv_gammaBinom_one_sub_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-inv-gamma-binom-one-sub-pow).

## Generalized central binomial polynomial identity, alternating form

Let $\binom{a}{b}$
denote the generalized binomial coefficient $\Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$. For every
natural number $n$, every real $v > -1$ and every complex $x$,

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} 2^{-k} \binom{2k+v}{(2k+v)/2} \binom{k+v}{v/2}^{-1}
(1-x)^{n-k} = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} 2^{-2k} \binom{2k}{k}
\binom{(2k+v)/2}{k}^{-1} x^{n-2k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 13.

Stated but not proved: `MetaMathlibExt.knuth_poly_gammaBinom_one_sub_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#knuth-poly-gamma-binom-one-sub-pow).

## Alternating polynomial identity in $1 - x$ with weights $2^k/(k+1)$

For every natural
number $n$ and every complex number $x$,

$$
\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \frac{2^k}{k+1} (1-x)^{n-k}
= \sum_{k=0}^{\lfloor n/2 \rfloor} \frac{1}{2k+1} \binom{n}{2k} x^{n-2k}.
$$

This is equation (45) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 4.

Stated but not proved: `MetaMathlibExt.sum_choose_two_pow_div_succ_one_sub_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-two-pow-div-succ-one-sub-pow).

## A polynomial identity for weighted central binomial coefficients

For every natural
number $n$ and every complex number $x$,

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \frac{1}{(k+2) 2^k} \binom{2k+2}{k+1} (1-x)^{n-k} =
\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{1}{(k+1) 2^{2k}} \binom{2k}{k} x^{n-2k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 4.

Stated but not proved: `MetaMathlibExt.sum_choose_centralBinom_succ_one_sub_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-central-binom-succ-one-sub-po).

## A two-parameter polynomial identity for generalized central binomial coefficients

Write $\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\,\Gamma(a-b+1))$ for the generalized binomial
coefficient of complex numbers $a, b$. For every natural number $n$ and all complex numbers
$u, v, x$ with $\operatorname{Re} u > -1$ and $\operatorname{Re} v > -1$,

$$
\binom{v}{v/2} \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} 2^{-2k} \binom{2k+u}{(2k+u)/2}
\binom{(2k+u+v)/2}{v/2}^{-1} (1-x)^{n-k}
= \binom{u}{u/2} \sum_{k=0}^{n} (-1)^{k} \binom{n}{k} 2^{-2k} \binom{2k+v}{(2k+v)/2}
\binom{(2k+u+v)/2}{u/2}^{-1} x^{n-k}.
$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 14.

Stated but not proved: `MetaMathlibExt.two_param_poly_gammaBinom_one_sub_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 549](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L549). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#two-param-poly-gamma-binom-one-sub-pow).

## Reflection symmetry of the central binomial polynomial sum

For every natural number $n$
and every complex $x$,

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{2k}{k} 2^{-2k} \binom{n}{k} (1-x)^{n-k} =
\sum_{k=0}^{n} (-1)^k \binom{2k}{k} 2^{-2k} \binom{n}{k} x^{n-k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 5.

Stated but not proved: `MetaMathlibExt.sum_centralBinom_choose_one_sub_pow_symm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-central-binom-choose-one-sub-pow-sym).

## Reflection symmetry of the Catalan polynomial sum

Let $C_m = \binom{2m}{m}/(m+1)$
denote the $m$-th Catalan number. For every natural number $n$ and every complex $x$,

$$\sum_{k=0}^{n} (-1)^{n-k} 2^{-2k} \binom{n}{k} C_{k+1} (1-x)^{n-k} =
\sum_{k=0}^{n} (-1)^k 2^{-2k} \binom{n}{k} C_{k+1} x^{n-k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 5.

Stated but not proved: `MetaMathlibExt.sum_catalan_succ_choose_one_sub_pow_symm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-catalan-succ-choose-one-sub-pow-symm).

## Generalized central binomial polynomial identity, Bernstein form

Let $\binom{a}{b}$
denote the generalized binomial coefficient $\Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$. For every
natural number $n$, every real $v > -1$ and every complex $x$,

$$\sum_{k=0}^{n} \binom{n}{k} 2^{-k} \binom{2k+v}{(2k+v)/2} \binom{k+v}{v/2}^{-1} (1-x)^k
x^{n-k} = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} 2^{-2k} \binom{2k}{k}
\binom{(2k+v)/2}{k}^{-1} (1-x)^{2k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 15.

Stated but not proved: `MetaMathlibExt.knuth_poly_gammaBinom_mul_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#knuth-poly-gamma-binom-mul-pow).

## Central binomial polynomial identity, Bernstein form

For every natural number $n$ and
every complex $x$,

$$\sum_{k=0}^{n} \binom{n}{k} 2^{-k} \binom{2k}{k} (1-x)^k x^{n-k} =
\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} 2^{-2k} \binom{2k}{k} (1-x)^{2k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 6.

Stated but not proved: `MetaMathlibExt.sum_choose_centralBinom_one_sub_pow_mul_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-central-binom-one-sub-pow-mul).

## Polynomial identity in $x$ and $1 - x$ with weights $2^k/(k+1)$

For every natural
number $n$ and every complex number $x$,

$$
\sum_{k=0}^{n} \binom{n}{k} \frac{2^k}{k+1} (1-x)^k x^{n-k}
= \sum_{k=0}^{\lfloor n/2 \rfloor} \frac{1}{2k+1} \binom{n}{2k} (1-x)^{2k}.
$$

This is equation (53) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 6.

Stated but not proved: `MetaMathlibExt.sum_choose_two_pow_div_succ_one_sub_pow_mul_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-two-pow-div-succ-one-sub-pow-2).

## Catalan polynomial identity, Bernstein form

Let $C_m = \binom{2m}{m}/(m+1)$ denote the
$m$-th Catalan number. For every natural number $n$ and every complex $x$,

$$\sum_{k=0}^{n} \binom{n}{k} 2^{-k} C_{k+1} (1-x)^k x^{n-k} =
\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} 2^{-2k} C_k (1-x)^{2k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Corollary 6.

Stated but not proved: `MetaMathlibExt.sum_choose_catalan_succ_one_sub_pow_mul_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 625](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L625). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-catalan-succ-one-sub-pow-mul).

## Alternating sum of reciprocal generalized binomial coefficients

For every natural
number $n$ and all complex numbers $u, v$ with $\operatorname{Re} u > -1$ and
$\operatorname{Re} v > -1$,

$$
\sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{k+u+v+1}{u+1}^{-1}
= \frac{u+1}{v+1} \binom{n+u+v+1}{v+1}^{-1},
$$

where $\binom{n}{k}$ is the ordinary binomial coefficient and otherwise
$\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$ is the generalized binomial
coefficient of complex numbers $a, b$.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 16.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_inv_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 638](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L638). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-choose-inv-gamma-binom).

## One-parameter extension of the alternating sum of $\binom{n}{k} 2^{n-2k} \binom{2k}{k}$

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\,\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex numbers $u$ and $w$. For every natural number $n$ and every real
number $v > -1$, the following identity holds in $\mathbb{C}$:

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} \frac{2^n}{2^{2k}} \binom{2k+v}{(2k+v)/2}
\binom{k+v}{v/2}^{-1}
= \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{1}{2^{2k}} \binom{2k}{k}
\binom{(2k+v)/2}{k}^{-1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 17.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_two_pow_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-choose-two-pow-gamma-bin).

## Binomial transform of generalized central binomial ratios

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex $u$, $w$, which for natural $u$, $w$ is the ordinary binomial coefficient.
For every natural number $n$ and every real $v > -1$,

$$
\sum_{k=0}^{n} \binom{n}{k} \frac{1}{2^k} \binom{2k+v}{(2k+v)/2} \binom{k+v}{v/2}^{-1}
= \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{2^n}{2^{4k}} \binom{2k}{k}
\binom{(2k+v)/2}{k}^{-1}.
$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 17.

Stated but not proved: `MetaMathlibExt.sum_choose_two_pow_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 662](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L662). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-two-pow-gamma-binom).

## Alternating sum of $\binom{n}{k} 2^{n-2k} \binom{2k}{k}$

For every natural number $n$,
the following identity holds in $\mathbb{Q}$:

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} \frac{2^n}{2^{2k}} \binom{2k}{k}
= \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{1}{2^{2k}} \binom{2k}{k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 3.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_two_pow_centralBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 674](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L674). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-choose-two-pow-central-b).

## Even-index against odd-index reciprocal binomial sums

For every natural number
$n \ge 1$,

$$\sum_{k=0}^{\lfloor n/2 \rfloor} \frac{1}{2k+1} \binom{n}{2k} =
\frac{2^{n-1}}{2^n - 1} \sum_{k=1}^{\lceil n/2 \rceil} \frac{1}{k} \binom{n}{2k-1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 3.

Stated but not proved: `MetaMathlibExt.sum_choose_even_div_eq_sum_choose_odd_div` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-even-div-eq-sum-choose-odd-di).

## Alternating binomial sum of Catalan numbers

For every natural number $n$, in the
rational numbers

$$
\sum_{k=0}^{n} (-1)^k \binom{n}{k} \frac{2k+1}{k+2} \cdot \frac{2^{n+1}}{2^{2k}} C_k
= \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{C_k}{2^{2k}},
$$

where $C_k = \binom{2k}{k}/(k+1)$ is the $k$-th Catalan number.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 3.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_two_pow_catalan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 692](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L692). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-choose-two-pow-catalan).

## Even-index binomial sum equal to a scaled central binomial coefficient

For every
natural number $n$,

$$\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{1}{2^{2k}} \binom{2k}{k} =
\frac{1}{2^n} \binom{2n}{n}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 4.

Stated but not proved: `MetaMathlibExt.sum_choose_even_centralBinom_div_four_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 701](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-even-central-binom-div-four-p).

## Even-index binomial sum with odd reciprocal weights

For every natural number $n$,

$$\sum_{k=0}^{\lfloor n/2 \rfloor} \frac{1}{2k+1} \binom{n}{2k} = \frac{2^n}{n+1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 4.

Stated but not proved: `MetaMathlibExt.sum_choose_even_div_two_mul_add_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 709](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L709). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-even-div-two-mul-add-one).

## Even-index binomial sum of weighted central binomial coefficients

Write
$C_m = \binom{2m}{m}/(m+1)$ for the $m$-th Catalan number. For every natural number $n$,

$$\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{1}{(k+1) 2^{2k}} \binom{2k}{k} =
\frac{2}{2^n (n+2)} (2n+1) C_n.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 4.

Stated but not proved: `MetaMathlibExt.sum_choose_even_centralBinom_div_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 716](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L716). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-even-central-binom-div-succ).

## Even-index expansion of a weighted central binomial sum

For every natural number $n$,

$$\sum_{k=0}^{n} \binom{n}{k} 2^{-k} \binom{2k}{k} =
\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} 2^{n-4k} \binom{2k}{k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 5.

Stated but not proved: `MetaMathlibExt.sum_choose_centralBinom_div_two_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 725](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L725). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-central-binom-div-two-pow).

## Even-index and odd-index binomial sums weighted by powers of $2$

For every natural
number $n$,

$$\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{2^{n-2k+1} - 2^{2k+1}}{2k+1} =
\sum_{k=1}^{\lceil n/2 \rceil} \binom{n}{2k-1} \frac{2^{2k-1}}{k}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 5.

Stated but not proved: `MetaMathlibExt.sum_choose_even_two_pow_sub_div` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 734](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L734). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-even-two-pow-sub-div).

## Binomial transform of weighted Catalan numbers

Write $C_m = \binom{2m}{m}/(m+1)$ for the
$m$-th Catalan number. For every natural number $n$,

$$\sum_{k=0}^{n} \binom{n}{k} \frac{2k+1}{k+2} \cdot \frac{2}{2^k} C_k =
\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{2^n}{2^{4k}} C_k.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 5.

Stated but not proved: `MetaMathlibExt.sum_choose_two_mul_add_one_div_catalan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-two-mul-add-one-div-catalan).

## One-parameter extension of the alternating sum of $\binom{n}{k} \binom{2k}{k}$

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\,\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex numbers $u$ and $w$. For every natural number $n$ and every real
number $v > -1$, the following identity holds in $\mathbb{C}$:

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \binom{2k+v}{(2k+v)/2} \binom{k+v}{v/2}^{-1}
= \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \binom{2k}{k} \binom{(2k+v)/2}{k}^{-1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 18.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_sub_choose_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 752](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L752). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-sub-choose-gamma-binom).

## Alternating sum of $\binom{n}{k} \binom{2k}{k}$

For every natural number $n$,

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \binom{2k}{k}
= \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{k} \binom{n-k}{k}$$

as integers.

Both sides are the central trinomial coefficient.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 6.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_sub_choose_centralBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-sub-choose-central-binom).

## Alternating sum of $\binom{n}{k} 2^{2k}/(k+1)$

For every natural number $n$, the
following identity holds in $\mathbb{Q}$:

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \frac{2^{2k}}{k+1}
= \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \frac{2^{2k}}{2k+1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 6.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_sub_choose_four_pow_div_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 772](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L772). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-sub-choose-four-pow-div).

## Alternating sum of $\binom{n}{k} \frac{2(2k+1)}{k+2} C_k$

Let
$C_k = \frac{1}{k+1}\binom{2k}{k}$ denote the $k$-th Catalan number. For every natural number
$n$, the following identity holds in $\mathbb{Q}$:

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \frac{2(2k+1)}{k+2}\, C_k
= \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} C_k.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 6.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_sub_choose_catalan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 780](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L780). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-neg-one-pow-sub-choose-catalan).

## Even-index identity for generalized central binomial coefficients

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex $u$, $w$, which for natural $u$, $w$ is the ordinary binomial coefficient.
For every natural number $n$ and every real $v > -1$,

$$
\sum_{k=0}^{n} \binom{2n}{2k} \binom{2(n-k)}{n-k} \binom{2k+v}{(2k+v)/2}
\binom{(2n+v)/2}{n-k}^{-1}
= \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} 2^{2n-2k} \binom{2k}{k}
\binom{2k+v}{(2k+v)/2} \binom{(4k+v)/2}{k}^{-1}.
$$

This is equation (56) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 19.

Stated but not proved: `MetaMathlibExt.sum_choose_two_mul_gammaBinom_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 791](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L791). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-two-mul-gamma-binom-even).

## Odd-index identity for generalized central binomial coefficients

Write $\binom{u}{w} = \Gamma(u+1)/(\Gamma(w+1)\Gamma(u-w+1))$ for the generalized binomial
coefficient of complex $u$, $w$, which for natural $u$, $w$ is the ordinary binomial coefficient.
For every natural number $n$ and every real $v > -1$,

$$
\sum_{k=1}^{n} \binom{2n}{2k-1} \binom{2(n-k+1)}{n-k+1} \binom{2k-1+v}{(2k-1+v)/2}
\binom{(2n+v+1)/2}{n-k+1}^{-1}
= \sum_{k=1}^{\lceil n/2 \rceil} \binom{n}{2k-1} 2^{2n+1-2k} \binom{2k}{k}
\binom{2k-1+v}{(2k-1+v)/2} \binom{(4k+v-1)/2}{k}^{-1}.
$$

This is equation (57) of the source.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 19.

Stated but not proved: `MetaMathlibExt.sum_choose_two_mul_sub_one_gammaBinom_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 807](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L807). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#sum-choose-two-mul-sub-one-gamma-binom-o).

## Waring-type sum of generalized central binomial coefficients

Write
$\binom{a}{b} = \Gamma(a+1)/(\Gamma(b+1)\,\Gamma(a-b+1))$ for the generalized binomial
coefficient. For every integer $n \ge 1$ and every real number $v > -1$,

$$
\sum_{k=0}^{\lfloor n/2 \rfloor} (-1)^k \frac{n}{n-k} \binom{n-k}{k} 2^{-4k}
\binom{2k+v}{(2k+v)/2} =
\binom{2n+v}{(2n+v)/2} \binom{v}{v/2} \, 2^{1-2n} \binom{n+v}{v/2}^{-1}.
$$

The paper states this for every non-negative integer $n$, but at $n = 0$ the factor
$n/(n-k)$ is $0/0$, and the paper derives the identity from Waring's formula, which it
states for positive $n$ only.

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Theorem 20.

Stated but not proved: `MetaMathlibExt.waring_sum_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 826](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L826). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#waring-sum-gamma-binom).

## Simons-type identity for generalized central binomial coefficients

Let $\binom{a}{b}$
denote the generalized binomial coefficient $\Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$. For every
natural number $n$ and every real $v > -1$,

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} 2^{-k} \binom{n+k}{k} \binom{2k+v}{(2k+v)/2}
\binom{k+v}{v/2}^{-1} = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} 2^{-2k} \binom{n+2k}{2k}
\binom{2k}{k} \binom{(2k+v)/2}{v/2}^{-1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 7.

Stated but not proved: `MetaMathlibExt.simons_sum_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 839](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L839). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#simons-sum-gamma-binom).

## Two-parameter Simons-type symmetry

Let $\binom{a}{b}$ denote the generalized binomial
coefficient $\Gamma(a+1)/(\Gamma(b+1)\Gamma(a-b+1))$. For every natural number $n$ and all real
$u > -1$ and $v > -1$,

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} 2^{-2k} \binom{n+k}{k} \binom{v}{v/2}
\binom{2k+u}{(2k+u)/2} \binom{(2k+u+v)/2}{v/2}^{-1} = \sum_{k=0}^{n} (-1)^k \binom{n}{k}
2^{-2k} \binom{n+k}{k} \binom{u}{u/2} \binom{2k+v}{(2k+v)/2} \binom{(2k+u+v)/2}{u/2}^{-1}.$$

## Sources

- Kunle Adegoke, *A Short Proof of Knuth's Old Sum, Generalizations and Related Sums*, INTEGERS 26 (2026), Article A19, Proposition 8.

Stated but not proved: `MetaMathlibExt.simons_two_param_gammaBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean, line 854](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KnuthOldSumWanted.lean#L854). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#simons-two-param-gamma-binom).

## Weight in Knuth's old sum

For a natural number $m$, the weight $w(m)$ is the rational
number $(4^m + 2^m)/2$, which equals $(2^m + 1) 2^{m-1}$.

It is the number of words of length $m$ over a four-letter alphabet in which a fixed letter
occurs an even number of times.

Formalized by `MathlibExt.Combinatorics.KnuthOldSumWanted.knuthOldSumWeight`, a definition declared in [WantedExt/Combinatorics/KnuthOldSumWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KnuthOldSumWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#knuth-old-sum-weight).

## Counting words with an even number of $a$'s

For every natural number $n$, the number of
words of length $n$ over the four-letter alphabet $\{a, b, c, d\}$ in which the letter $a$ occurs
an even number of times is $(4^n + 2^n)/2$.

## Sources

- Akalu Tefera and Aklilu Zeleke, "Combinatorial Identities Inspired by Knuth's Old Sum", Lemma 1.

Stated but not proved: `MathlibExt.Combinatorics.KnuthOldSumWanted.card_evenACount_words` is written with `theorem_wanted` in [WantedExt/Combinatorics/KnuthOldSumWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KnuthOldSumWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#card-even-acount-words).

## Tefera–Zeleke identity with binomial quotients

Let $n$ and $j$ be natural numbers, let
$N = n + 2j + 1$, and let $w(m) = (4^m + 2^m)/2$ be the weight in Knuth's old sum. Then, in the
rational numbers,

$$\sum_{k=0}^{n} \binom{N}{n-k} w(n-k) (-1)^k
= \binom{N}{n} \sum_{k=0}^{n} \frac{\binom{n}{k}}{\binom{2j+1+k}{2j+1}} w(n-k) (-1)^k.$$

This is Equation (1) of the paper, whose weight $(2^m + 1) 2^{m-1}$ is written here as
$(4^m + 2^m)/2$.

## Sources

- Akalu Tefera and Aklilu Zeleke, "Combinatorial Identities Inspired by Knuth's Old Sum", Theorem 1.

Stated but not proved: `MathlibExt.Combinatorics.KnuthOldSumWanted.knuthOldSum_eq_mul_sum_div` is written with `theorem_wanted` in [WantedExt/Combinatorics/KnuthOldSumWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KnuthOldSumWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#knuth-old-sum-eq-mul-sum-div).

## Tefera–Zeleke identity with powers of $2$, $3$ and $4$

Let $n$ and $j$ be natural numbers,
let $N = n + 2j + 1$, and let $w(m) = (4^m + 2^m)/2$ be the weight in Knuth's old sum. Then, in the
rational numbers,

$$\sum_{k=0}^{n} \binom{N}{n-k} w(n-k) (-1)^k
= \sum_{k=0}^{n} \binom{2j+k}{k} \frac{2^k + 4^k 3^{n-k}}{2}.$$

This is Equation (2) of the paper, which prints the weight as $(2^m + 1) 2^{m-1}$ and the terms
on the right as $\binom{2j+k}{k} 2^{k-1} (1 + 2^k 3^{n-k})$.

## Sources

- Akalu Tefera and Aklilu Zeleke, "Combinatorial Identities Inspired by Knuth's Old Sum", Theorem 2.

Stated but not proved: `MathlibExt.Combinatorics.KnuthOldSumWanted.knuthOldSum_eq_sum_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/KnuthOldSumWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KnuthOldSumWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html#knuth-old-sum-eq-sum-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Knuth's old sum](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/knuth-s-old-sum)
