---
declaration: section
origin: cited
lean: MetaMathlibExt.goldenFactorialExponent, MetaMathlibExt.exists_goldenRatio_pow_ge_factorial, MetaMathlibExt.goldenFactorialExponent_mem, MetaMathlibExt.goldenFactorialExponent_le, MetaMathlibExt.goldenFactorialExponent_one, MetaMathlibExt.goldenFactorialExponent_two, MetaMathlibExt.alternatingSignFibonacci, MetaMathlibExt.alternatingSignFibonacci_add_two
statement: formalized
---

# Factorials bounded by powers of the golden ratio

21 results, 12 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html).

## Golden factorial exponent

For a natural number $n$, the golden factorial exponent
$\alpha(n)$ is the least positive integer $m$ with $n! \le \varphi^m$, where $\varphi$ is the golden
ratio. This is the sequence OEIS A214048.

Equivalently $\alpha(n)$ is the positive integer $m$ with $\varphi^{m-1} \le n! \le \varphi^m$; the
number $n!$ is never a power of $\varphi$ for $n \ge 2$, and $\alpha(1) = 1$.

## Sources

- Aleksandar Petojević, Marjana Gorjanac Ranitović, Dragan Rastovac and Milinko Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 2.2, definition (4).

Formalized by `MetaMathlibExt.goldenFactorialExponent`, a definition declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#golden-factorial-exponent).

## Every factorial is at most a positive power of the golden ratio

Let $\varphi$ be the
golden ratio. For every natural number $n$ there is an integer $m \ge 1$ with $n! \le \varphi^m$.

Thus the set of positive integers $m$ with $n! \le \varphi^m$, whose least element is the
golden factorial exponent of $n$, is nonempty.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 2.2, definition (4).

Formalized by `MetaMathlibExt.exists_goldenRatio_pow_ge_factorial`, a theorem declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#exists-golden-ratio-pow-ge-factorial).

## Defining property of the golden factorial exponent

Let $\varphi$ be the golden ratio
and, for a natural number $n$, let $\alpha(n)$ be the least positive integer $m$ with
$n! \le \varphi^m$. For every natural number $n$, $\alpha(n) \ge 1$ and
$n! \le \varphi^{\alpha(n)}$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 2.2, definition (4).

Formalized by `MetaMathlibExt.goldenFactorialExponent_mem`, a theorem declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#golden-factorial-exponent-mem).

## Minimality of the golden factorial exponent

Let $\varphi$ be the golden ratio and,
for a natural number $n$, let $\alpha(n)$ be the least positive integer $m$ with
$n! \le \varphi^m$. If $n$ and $m$ are natural numbers with $m \ge 1$ and $n! \le \varphi^m$,
then $\alpha(n) \le m$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 2.2, definition (4).

Formalized by `MetaMathlibExt.goldenFactorialExponent_le`, a theorem declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#golden-factorial-exponent-le).

## Golden factorial exponent of $1$

Let $\varphi$ be the golden ratio and, for a natural
number $n$, let $\alpha(n)$ be the least positive integer $m$ with $n! \le \varphi^m$. Then
$\alpha(1) = 1$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Table 3.

Formalized by `MetaMathlibExt.goldenFactorialExponent_one`, a theorem declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#golden-factorial-exponent-one).

## Golden factorial exponent of $2$

Let $\varphi$ be the golden ratio and, for a natural
number $n$, let $\alpha(n)$ be the least positive integer $m$ with $n! \le \varphi^m$. Then
$\alpha(2) = 2$.

This holds because $\varphi < 2 \le \varphi^2 = \varphi + 1$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Table 3.

Formalized by `MetaMathlibExt.goldenFactorialExponent_two`, a theorem declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#golden-factorial-exponent-two).

## Alternating-sign Fibonacci sequence

The alternating-sign Fibonacci sequence
(OEIS A181716) is the integer sequence $(d_m)_{m \ge 0}$ defined by $d_0 = 0$, $d_1 = 1$ and
$d_{m+2} = d_{m+1} + d_m + (-1)^{m+2}$ for every natural number $m$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 2.2 (definition before Lemma 3).

Formalized by `MetaMathlibExt.alternatingSignFibonacci`, a definition declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#alternating-sign-fibonacci).

## Recurrence of the alternating-sign Fibonacci sequence

For every natural number $m$,
the alternating-sign Fibonacci sequence $d$ satisfies $d_{m+2} = d_{m+1} + d_m + (-1)^{m+2}$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 2.2.

Formalized by `MetaMathlibExt.alternatingSignFibonacci_add_two`, a theorem declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#alternating-sign-fibonacci-add-two).

## First values of the alternating-sign Fibonacci sequence

The alternating-sign Fibonacci
sequence $d$ satisfies $d_0 = 0$, $d_1 = 1$, $d_2 = 2$, $d_3 = 2$ and $d_4 = 5$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Example 5.

Formalized by `MetaMathlibExt.alternatingSignFibonacci_small_values`, a theorem declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#alternating-sign-fibonacci-small-values).

## Kurepa's partial integral

For a natural number $n$ and a real number $x$, Kurepa's partial
integral is

$$K_n(x) = \int_0^x e^{-t} \sum_{k=0}^{n-1} t^k \, dt,$$

an oriented integral, so for $x < 0$ it is minus the integral over $[x, 0]$.

The paper writes it as $!n(x) = \int_0^x e^{-t} \frac{t^n - 1}{t - 1} \, dt$; the geometric sum
agrees with $\frac{t^n - 1}{t - 1}$ for $t \ne 1$, and the singularity at $t = 1$ is removable.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 1 (the function `!z(x)`) and Sections 3.1-3.3.

Formalized by `MetaMathlibExt.kurepaPartialIntegral`, a definition declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#kurepa-partial-integral).

## Kurepa's partial integral vanishes at zero

For every natural number $n$, Kurepa's partial
integral $K_n(x) = \int_0^x e^{-t} \sum_{k=0}^{n-1} t^k \, dt$ satisfies $K_n(0) = 0$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 1.

Formalized by `MetaMathlibExt.kurepaPartialIntegral_zero`, a theorem declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#kurepa-partial-integral-zero).

## Increment bounds for the golden factorial exponent

Let $\varphi$ be the golden ratio
and, for a natural number $n$, let $\alpha(n)$ be the least positive integer $m$ with
$n! \le \varphi^m$. For every natural number $n > 1$,

$$\alpha(n-1) + \lfloor \log_\varphi n \rfloor \le \alpha(n) \le
\alpha(n-1) + \lfloor \log_\varphi n \rfloor + 1.$$

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Lemma 2 (`jis-2024-24.5.7-lem-2`).

Stated but not proved: `MetaMathlibExt.goldenFactorialExponent_succ_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#golden-factorial-exponent-succ-bounds).

## Counting integers by their golden-ratio logarithm

Let $d$ be the integer sequence with
$d(0) = 0$, $d(1) = 1$ and $d(m) = d(m-1) + d(m-2) + (-1)^m$ for $m \ge 2$, and let $\varphi$ be
the golden ratio. For every integer $m \ge 1$, the number of positive integers $n$ with
$\lfloor \log_\varphi n \rfloor = m$ equals $d(m)$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Lemma 3 (`jis-2024-24.5.7-lem-3`).

Stated but not proved: `MetaMathlibExt.ncard_floor_logb_goldenRatio_eq_alternatingSignFibonacci` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#ncard-floor-logb-golden-ratio-eq-alterna).

## Existence of the Lambert sequences

Let $h(y) = y e^y$ be the Lambert map. For every
natural number $n \ge 4$ and every real number $c$ with $0 < c \le 1$ there is a real number
$a \ge n - 1$ with

$$h\left(-\frac{a}{n-1}\right) = -\frac{1}{n-1} \, c^{1/(n-1)}.$$

Equivalently, $a = -(n-1) \, W_{-1}\left(-\frac{1}{n-1} c^{1/(n-1)}\right)$, where $W_{-1}$ is the
lower real branch of the Lambert W function. With $c = 4/7$ this is the paper's $a_n$, and with
$c = 4/(7m)$ for an integer $m \ge 1$ it is the paper's $A_{n,m}$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 3.1 (the lower branch `W₋₁` defining `a n` and `A n m`).

Formalized by `MetaMathlibExt.exists_lambertSequence`, a theorem declared in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#exists-lambert-sequence).

## The golden factorial exponent exceeds the Lambert sequence

Let $n > 4$ be an integer, let
$h(y) = y e^y$ be the Lambert map, and let $a$ be a real number with $a \ge n - 1$ and

$$h\left(-\frac{a}{n-1}\right) = -\frac{1}{n-1}\left(\frac{4}{7}\right)^{1/(n-1)}.$$

Then $a < \alpha(n)$, where $\alpha(n)$ is the least positive integer $m$ with $n! \le \varphi^m$
and $\varphi$ is the golden ratio.

The two conditions on $a$ say exactly that
$a = -(n-1)\, W_{-1}\left(-\frac{1}{n-1}\left(\frac{4}{7}\right)^{1/(n-1)}\right)$, where $W_{-1}$
is the lower real branch of the Lambert $W$ function; this is the paper's $a(n)$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Theorem 6 (`jis-2024-24.5.7-thm-6`).

Stated but not proved: `MetaMathlibExt.lambertSequence_lt_goldenFactorialExponent` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#lambert-sequence-lt-golden-factorial-exp).

## A linear lower bound for the Lambert sequence

Let $n \ge 4$ be a natural number, write
$h(y) = y e^y$ for the Lambert map, and let $a$ be a real number with $a \ge n - 1$ such that

$$h\left(-\frac{a}{n - 1}\right) = -\frac{1}{n - 1} \left(\frac{4}{7}\right)^{1/(n - 1)}.$$

Then $2n - 4 < \frac{3}{4} a$.

These conditions determine $a$ uniquely: it is the paper's
$a_n = -(n - 1) W_{-1}\bigl(-\frac{1}{n - 1} (4/7)^{1/(n - 1)}\bigr)$, where $W_{-1}$ is the lower
real branch of the Lambert W function.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Lemma 8 (`jis-2024-24.5.7-lem-8`).

Stated but not proved: `MetaMathlibExt.two_mul_sub_four_lt_lambertSequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#two-mul-sub-four-lt-lambert-sequence).

## Partial exponential sums at the Lambert sequence

Let $n \ge 5$ and $k$ be natural numbers
with $k < n - 2$, let $h(y) = y e^y$ be the Lambert map, and let $a$ be a real number with
$a \ge n - 1$ and

$$h\left(-\frac{a}{n-1}\right) = -\frac{1}{n-1}\left(\frac{4}{7}\right)^{1/(n-1)}.$$

Then

$$\sum_{t=0}^{k} \frac{a^t}{t!} < \frac{a^{k+1}}{(k+1)!}.$$

The two conditions on $a$ say exactly that
$a = -(n-1)\, W_{-1}\left(-\frac{1}{n-1}\left(\frac{4}{7}\right)^{1/(n-1)}\right)$, where $W_{-1}$
is the lower real branch of the Lambert $W$ function; this is the paper's $a(n)$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Lemma 9 (`jis-2024-24.5.7-lem-9`).

Stated but not proved: `MetaMathlibExt.sum_pow_div_factorial_lt_lambertSequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#sum-pow-div-factorial-lt-lambert-sequenc).

## Lambert bounds for the left factorial

Let $n \ge 5$ be an integer, let
$!n = \sum_{k=0}^{n-1} k!$ be the left factorial, let
$K_n(x) = \int_0^x e^{-t} \sum_{k=0}^{n-1} t^k \, dt$ be Kurepa's partial integral, let
$h(y) = y e^y$ be the Lambert map, and let $a$ be a real number with $a \ge n - 1$ and

$$h\left(-\frac{a}{n-1}\right) = -\frac{1}{n-1}\left(\frac{4}{7}\right)^{1/(n-1)}.$$

Then $K_n(a) < {!n} < K_n(a) + 1$.

The two conditions on $a$ say exactly that
$a = -(n-1)\, W_{-1}\left(-\frac{1}{n-1}\left(\frac{4}{7}\right)^{1/(n-1)}\right)$, where $W_{-1}$
is the lower real branch of the Lambert $W$ function; this is the paper's $a(n)$, and $K_n(a)$
is its $b(n)$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Theorem 10 (`jis-2024-24.5.7-thm-10`).

Stated but not proved: `MetaMathlibExt.kurepaPartialIntegral_lambertSequence_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#kurepa-partial-integral-lambert-sequence).

## Left factorial bounds at the golden factorial exponent

For every integer $n \ge 1$, let
$!n = \sum_{k=0}^{n-1} k!$ be the left factorial, let
$K_n(x) = \int_0^x e^{-t} \sum_{k=0}^{n-1} t^k \, dt$ be Kurepa's partial integral, and let
$\alpha(n)$ be the least positive integer $m$ with $n! \le \varphi^m$, where $\varphi$ is the
golden ratio. Then $\beta(n) = K_n(\alpha(n))$ satisfies $\beta(n) < {!n} < \beta(n) + 1$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Theorem 12 (`jis-2024-24.5.7-thm-12`).

Stated but not proved: `MetaMathlibExt.kurepaPartialIntegral_goldenFactorialExponent_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#kurepa-partial-integral-golden-factorial).

## Two-parameter Lambert bounds for the left factorial

Let $n \ge 5$ and $m \ge 1$ be
integers, let $!n = \sum_{k=0}^{n-1} k!$ be the left factorial, let
$K_n(x) = \int_0^x e^{-t} \sum_{k=0}^{n-1} t^k \, dt$ be Kurepa's partial integral, let
$h(y) = y e^y$ be the Lambert map, and let $A$ be a real number with $A \ge n - 1$ and

$$h\left(-\frac{A}{n-1}\right) = -\frac{1}{n-1}\left(\frac{4}{7m}\right)^{1/(n-1)}.$$

Then $K_n(A) < {!n} < K_n(A) + \frac{1}{m}$.

The two conditions on $A$ say exactly that
$A = -(n-1)\, W_{-1}\left(-\frac{1}{n-1}\left(\frac{4}{7m}\right)^{1/(n-1)}\right)$, where $W_{-1}$
is the lower real branch of the Lambert $W$ function; this is the paper's $A(n, m)$, and
$K_n(A)$ is its $B(n, m)$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Theorem 14 (`jis-2024-24.5.7-thm-14`).

Stated but not proved: `MetaMathlibExt.kurepaPartialIntegral_lambertSequence_two_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#kurepa-partial-integral-lambert-sequence-2).

## Floor formulas for the left factorial

Let $!n = \sum_{k=0}^{n-1} k!$ be the left
factorial, let $K_n(x) = \int_0^x e^{-t} \sum_{k=0}^{n-1} t^k \, dt$ be Kurepa's partial integral,
let $h(y) = y e^y$ be the Lambert map, and let $\alpha(n)$ be the least positive integer $m$ with
$n! \le \varphi^m$, where $\varphi$ is the golden ratio. Then the following hold.
(i) For every integer $n \ge 1$, $\lfloor K_n(\alpha(n)) \rfloor + 1 = {!n}$.
(ii) For every integer $n > 4$ and every real $a \ge n - 1$ with
$h(-\frac{a}{n-1}) = -\frac{1}{n-1} (\frac{4}{7})^{1/(n-1)}$, we have
$\lfloor K_n(a) \rfloor + 1 = {!n}$.
(iii) For all integers $n > 4$ and $m \ge 1$ and every real $A \ge n - 1$ with
$h(-\frac{A}{n-1}) = -\frac{1}{n-1} (\frac{4}{7m})^{1/(n-1)}$, we have
$\lfloor K_n(A) + \frac{1}{m} \rfloor = {!n}$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Corollary 15 (`jis-2024-24.5.7-cor-15`).

Stated but not proved: `MetaMathlibExt.leftFactorial_eq_floor_kurepaPartialIntegral` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoldenRatioLeftFactorialLambertWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html#left-factorial-eq-floor-kurepa-partial-i).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Factorials bounded by powers of the golden ratio](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/factorials-bounded-by-powers-of-the-golden-ratio)
