---
declaration: section
origin: cited
lean: MetaMathlibExt.lurothDigit, MetaMathlibExt.lurothMap, MetaMathlibExt.lurothDigitSeq, MetaMathlibExt.lurothDigit_one, MetaMathlibExt.lurothDigit_half, MetaMathlibExt.lurothMap_one, MetaMathlibExt.lurothMap_half, MetaMathlibExt.lurothMap_zero
statement: formalized
---

# Lüroth series

50 results, 27 proved and 23 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html).

## First Lüroth digit

For a real number $x$, the first Lüroth digit of $x$ is the natural
number $d_1(x) = \lfloor 1/x \rfloor + 1$, where $\lfloor \cdot \rfloor$ is the floor truncated
at $0$ and $1/0 = 0$. For $x \in (0, 1]$ this is the usual digit and is at least $2$; for
$x \le 0$ and for $x > 1$ it equals $1$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Section 2.

Formalized by `MetaMathlibExt.lurothDigit`, a definition declared in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-digit).

## Lüroth map

For a real number $x$ with first Lüroth digit $d = d_1(x)$, the Lüroth
map is $L(x) = d(d - 1)x - (d - 1)$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Section 2.

Formalized by `MetaMathlibExt.lurothMap`, a definition declared in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-map).

## Lüroth digits

For a real number $x$ and $n \ge 1$, the $n$-th Lüroth digit of $x$ is
$d_n(x) = d_1(L^{n-1}(x))$, where $d_1$ is the first Lüroth digit, $L$ is the Lüroth map and
$L^{n-1}$ is its $(n-1)$-fold iterate ($L^0$ is the identity).

The digit sequence is indexed from $0$: its term of index $k$ is $d_1(L^k(x)) = d_{k+1}(x)$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Section 2.

Formalized by `MetaMathlibExt.lurothDigitSeq`, a definition declared in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-digit-seq).

## First Lüroth digit of 1

The first Lüroth digit of $1$ is $d_1(1) = 2$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Section 2 (definition of `d₁`).

Formalized by `MetaMathlibExt.lurothDigit_one`, a theorem declared in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-digit-one).

## First Lüroth digit of 1/2

The first Lüroth digit of $1/2$ is $d_1(1/2) = 3$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Section 2 (definition of `d₁`).

Formalized by `MetaMathlibExt.lurothDigit_half`, a theorem declared in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-digit-half).

## The Lüroth map fixes 1

The Lüroth map $L$ satisfies $L(1) = 1$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Section 2 (definition of `L`).

Formalized by `MetaMathlibExt.lurothMap_one`, a theorem declared in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-map-one).

## The Lüroth map at 1/2

The Lüroth map $L$ sends $1/2$ to $1$: $L(1/2) = 1$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Section 2 (definition of `L`).

Formalized by `MetaMathlibExt.lurothMap_half`, a theorem declared in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-map-half).

## The Lüroth map fixes 0

The Lüroth map $L$ satisfies $L(0) = 0$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Section 2 (definition of `L`).

Formalized by `MetaMathlibExt.lurothMap_zero`, a theorem declared in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-map-zero).

## The Lüroth map shifts the digits

For every real number $x$ and every $n \ge 1$, the
$n$-th Lüroth digit of $L(x)$, where $L$ is the Lüroth map, is the $(n+1)$-st Lüroth digit of
$x$: $d_n(L(x)) = d_{n+1}(x)$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Section 2 (definition of `d_n`).

Formalized by `MetaMathlibExt.lurothDigitSeq_succ`, a theorem declared in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-digit-seq-succ).

## Measure of Lüroth cylinders

Write $d_k(x)$ for the $k$-th Lüroth digit of $x$. For every
$n \in \mathbb{N}$ and all natural numbers $c_1, \dots, c_n$, the set
$\{x \in (0, 1] : d_j(x) = c_j \text{ for } 1 \le j \le n\}$ has Lebesgue measure
$\prod_{j=1}^{n} \frac{1}{c_j (c_j - 1)}$, with the convention $1/0 = 0$; in particular both
sides vanish when some $c_j < 2$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Proposition 1, (10).

Stated but not proved: `MetaMathlibExt.volume_lurothCylinder` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#volume-luroth-cylinder).

## Borel–Bernstein theorem for Lüroth digits

Let $(\Psi(n))_{n \ge 0}$ be a sequence of
positive reals, write $d_k(x)$ for the $k$-th Lüroth digit of $x$, and let $E$ be the set of
$x \in (0, 1]$ such that $d_{n+1}(x) \ge \Psi(n)$ for infinitely many $n$. If
$\sum_{n \ge 0} 1 / \Psi(n) < \infty$ then $E$ has Lebesgue measure $0$, and if
$\sum_{n \ge 0} 1 / \Psi(n) = \infty$ then $E$ has Lebesgue measure $1$.

The paper quotes this result from Jager and de Vroedt (its reference [3]).

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Theorem 1.

Stated but not proved: `MetaMathlibExt.volume_lurothDigit_ge_zero_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#volume-luroth-digit-ge-zero-one).

## Zero-one law for weighted products of consecutive Lüroth digits

Let $m \ge 1$, let
$t_0, \dots, t_{m-1}$ be positive reals, let $T = \max_i t_i$ and let $\ell$ be the number of
indices $j$ with $t_j = T$. Let $(\Psi(n))_{n \ge 0}$ be a sequence of positive reals for which
there is $c > 1$ with $\Psi(n) \ge c$ for all sufficiently large $n$ (equivalently,
$\liminf_n \Psi(n) > 1$). Write $d_k(x)$ for the $k$-th Lüroth digit of $x$ and let $E$ be the
set of $x \in (0, 1]$ such that $\prod_{i=0}^{m-1} d_{n+i+1}(x)^{t_i} \ge \Psi(n)$ for
infinitely many $n$. If the series $\sum_{n \ge 0} (\log \Psi(n))^{\ell - 1} / \Psi(n)^{1/T}$
converges then $E$ has Lebesgue measure $0$, and if it diverges then $E$ has Lebesgue
measure $1$.

The paper quotes this result from Brown-Sarre, Robert and Hussain (its reference [2]).

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Theorem 2, with `T` and `ℓ(t)` from (2).

Stated but not proved: `MetaMathlibExt.volume_lurothWeightedProduct_ge_zero_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#volume-luroth-weighted-product-ge-zero-o).

## Zero-one law for functions of consecutive Lüroth digits

Let $m \in \mathbb{N}$, let $F$
be a real-valued function on $m$-tuples of natural numbers and let $(\Psi(n))_{n \ge 0}$ be a
real sequence. For $y \in \mathbb{R}$ put

$$H(y) = \sum_{a} \prod_{i=1}^{m} \frac{1}{a_i (a_i - 1)} \in [0, \infty],$$

the sum running over the $a = (a_1, \dots, a_m) \in \mathbb{N}^m$ with every $a_i \ge 2$ and
$F(a) \ge y$. Write $d_k(x)$ for the $k$-th Lüroth digit of $x$ and let $E$ be the set of
$x \in (0, 1]$ such that $F(d_{n+1}(x), \dots, d_{n+m}(x)) \ge \Psi(n)$ for infinitely many
$n$. If $\sum_{n \ge 0} H(\Psi(n)) < \infty$ then $E$ has Lebesgue measure $0$, and if
$\sum_{n \ge 0} H(\Psi(n)) = \infty$ then $E$ has Lebesgue measure $1$.

Unlike the paper, $F$ and $\Psi$ need not be positive.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Theorem 3, with `H` from (4).

Stated but not proved: `MetaMathlibExt.volume_lurothConsecutiveDigits_zero_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#volume-luroth-consecutive-digits-zero-on).

## Integral zero-one law for functions of consecutive Lüroth digits

Let $m \in \mathbb{N}$
and let $F : \mathbb{R}^m \to \mathbb{R}$ be a measurable function that is positive on
$[2, \infty)^m$ and non-decreasing there for the coordinatewise order. Let $M \in \mathbb{R}$
satisfy $F(x) \le M F(\lfloor x_1 \rfloor, \dots, \lfloor x_m \rfloor)$ for every
$x \in [2, \infty)^m$, and for $y \in \mathbb{R}$ put

$$G(y) = \int_{\{x \in [2, \infty)^m : F(x) \ge y\}} \prod_{i=1}^{m} \frac{1}{x_i^2} \, dx.$$

Let $(\Psi(n))_{n \ge 0}$ be a real sequence, write $d_k(x)$ for the $k$-th Lüroth digit of
$x$, and let $E$ be the set of $x \in (0, 1]$ such that
$F(d_{n+1}(x), \dots, d_{n+m}(x)) \ge \Psi(n)$ for infinitely many $n$. If
$\sum_{n \ge 0} G(\Psi(n)) < \infty$ then $E$ has Lebesgue measure $0$, and if
$\sum_{n \ge 0} G(M \Psi(n)) = \infty$ then $E$ has Lebesgue measure $1$.

Here $M$ is any constant with this property (the paper takes the supremum; a larger $M$ only
weakens the divergence condition). Unlike the paper, $\Psi$ need not be positive.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Theorem 4, with (6) and `G` from (7).

Stated but not proved: `MetaMathlibExt.volume_lurothConsecutiveDigits_zero_one_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#volume-luroth-consecutive-digits-zero-on-2).

## Borel–Cantelli dichotomy for Lüroth cylinder events

Let $m \in \mathbb{N}$, let
$(S_n)_{n \ge 0}$ be a sequence of sets of $m$-tuples of natural numbers, write $d_k(x)$ for
the $k$-th Lüroth digit of $x$ and $\lambda$ for Lebesgue measure. Put
$A_n = \{x \in (0, 1] : (d_1(x), \dots, d_m(x)) \in S_n\}$ (a union of cylinders of level $m$)
and let $E$ be the set of $x \in (0, 1]$ such that $(d_{n+1}(x), \dots, d_{n+m}(x)) \in S_n$
for infinitely many $n$. If $\sum_{n \ge 0} \lambda(A_n) < \infty$ then $\lambda(E) = 0$, and
if $\sum_{n \ge 0} \lambda(A_n) = \infty$ then $\lambda(E) = 1$.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Theorem 5.

Stated but not proved: `MetaMathlibExt.volume_limsup_lurothPreimage_zero_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#volume-limsup-luroth-preimage-zero-one).

## Upper bound for the measure of a Lüroth digit superlevel set

Let $m \in \mathbb{N}$, let
$F : \mathbb{R}^m \to \mathbb{R}$ be non-decreasing on $[2, \infty)^m$ for the coordinatewise
order, let $y \in \mathbb{R}$, and write $d_k(x)$ for the $k$-th Lüroth digit of $x$. Then the
Lebesgue measure of $\{x \in (0, 1] : F(d_1(x), \dots, d_m(x)) \ge y\}$ is at most

$$3^m \int_{\{x \in [2, \infty)^m : F(x) \ge y\}} \prod_{i=1}^{m} \frac{1}{x_i^2} \, dx.$$

The paper states this bound for $y = \Psi(n)$ under the hypotheses of its Theorem 4; only
the monotonicity of $F$ is used.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Theorem 6.

Stated but not proved: `MetaMathlibExt.volume_lurothDigits_ge_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#volume-luroth-digits-ge-le).

## Lower bound for the measure of large Lüroth digit values

Let $m$ be a natural number,
let $D = [2, \infty)^m$, let $F : \mathbb{R}^m \to \mathbb{R}$ satisfy $F(x) > 0$ for every
$x \in D$, and let $M$ be a real number with
$F(x) \le M\,F(\lfloor x_1 \rfloor, \ldots, \lfloor x_m \rfloor)$ for every $x \in D$ (the
paper's condition (6)). Put
$G(y) = \int_{\{x \in D \,:\, F(x) \ge y\}} \prod_{i=1}^m x_i^{-2}\,dx$ for real $y$, let
$\lambda$ be Lebesgue measure on $\mathbb{R}$ and let $d_1(x), d_2(x), \ldots$ be the Lüroth
digits of $x$. Then for every real $y$,

$$G(My) \le \lambda\{x \in (0, 1] : F(d_1(x), \ldots, d_m(x)) \ge y\}.$$

The paper states it only at the values of the sequence in its Theorem 4, under that theorem's
hypotheses, which also require $F$ to be measurable and non-decreasing; only positivity and
condition (6) are assumed here.

## Sources

- Dmitry Kleinbock and Yuqing Zhang, *Metrical Properties of Functions of Consecutive Digits in Lüroth Series*, INTEGERS 24 (2024), Article A67, Theorem 7.

Stated but not proved: `MetaMathlibExt.le_volume_lurothDigits_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothConsecutiveDigitsWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#le-volume-luroth-digits-ge).

## Well approximable numbers

For a function $\psi : \mathbb{N} \to \mathbb{R}$, the set
$W(\psi)$ of $\psi$-well approximable numbers consists of the real numbers $x \in [0, 1)$ such
that for infinitely many natural numbers $q$ there is an integer $p$ with
$|x - p/q| < \psi(q)/q$.

The fractions $p/q$ need not be in lowest terms, unlike Mathlib's well approximable sets,
which use points of exact additive order $q$. The value $\psi(0)$ is irrelevant.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (1).

Formalized by `MetaMathlibExt.wellApproximableSet`, a definition declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#well-approximable-set).

## Well approximable numbers lie in $(0, 1)$

For every function
$\psi : \mathbb{N} \to \mathbb{R}$, every point of the set $W(\psi)$ of $\psi$-well approximable
numbers lies in the interval $[0, 1)$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (1).

Formalized by `MetaMathlibExt.wellApproximableSet_subset_Ico`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#well-approximable-set-subset-ico).

## Lower order at infinity

For $\psi : \mathbb{N} \to \mathbb{R}$, the lower order at infinity
of $1/\psi$ is

$$\tau_\psi = \liminf_{q \to \infty} \max\left(-\frac{\log \psi(q)}{\log q},\, 0\right),$$

with the liminf taken in $[0, \infty]$. Here $\log x$ means $\log |x|$ for $x \ne 0$ and
$\log 0 = 0$, and the ratio is read as $0$ when $\log q = 0$. For $\psi$ with values in $(0, 1]$
the ratio is nonnegative once $q \ge 2$, so the truncation at $0$ has no effect there, and
$\tau_\psi$ may be infinite.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (11).

Formalized by `MetaMathlibExt.lowerOrderAtInfinity`, a definition declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#lower-order-at-infinity).

## Upper order at infinity

For a function $\psi$ from the natural numbers to the reals, the
upper order at infinity of $\psi$ is the element

$$\bar\tau_\psi = \limsup_{q \to \infty} \max\left(0, \frac{-\log \psi(q)}{\log q}\right)$$

of $[0, \infty]$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (11).

Formalized by `MetaMathlibExt.upperOrderAtInfinity`, a definition declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#upper-order-at-infinity).

## The order ratio of $q^{-\tau}$

For every real $\tau$ and all sufficiently large natural
numbers $q$, $\max(0, -\log((q^{\tau})^{-1})/\log q) = \max(0, \tau)$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (11).

Formalized by `MetaMathlibExt.orderRatio_rpow_inv`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#order-ratio-rpow-inv).

## Lower order at infinity of a power function

For a real number $\tau$, let
$\psi : \mathbb{N} \to \mathbb{R}$ be given by $\psi(q) = q^{-\tau}$ (the value at $q = 0$ does not
matter). Then the lower order at infinity of $1/\psi$ is $\tau_\psi = \max(\tau, 0)$, an element of
$[0, \infty]$; in particular $\tau_\psi = \tau$ when $\tau \ge 0$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, remark after Theorem 7.

Formalized by `MetaMathlibExt.lowerOrderAtInfinity_rpow_inv`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#lower-order-at-infinity-rpow-inv).

## Upper order at infinity of $q^{-\tau}$

For every real $\tau$, the upper order at infinity
of $q \mapsto (q^{\tau})^{-1}$ is $\max(0, \tau)$; in particular it is $\tau$ when $\tau \ge 0$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, remark after Theorem 7.

Formalized by `MetaMathlibExt.upperOrderAtInfinity_rpow_inv`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#upper-order-at-infinity-rpow-inv).

## Khintchine's theorem

Let $\psi : \mathbb{N} \to \mathbb{R}$ be non-increasing on all of
$\mathbb{N}$ (including $\psi(0) \ge \psi(1)$) with $0 \le \psi(q) \le 1/2$ for every $q$. If the
series $\sum_q \psi(q)$ converges, then the set $W(\psi)$ of $\psi$-well approximable numbers has
Lebesgue measure $0$; if the series diverges, then $W(\psi)$ has Lebesgue measure $1$.

The value $\psi(0)$ affects neither $W(\psi)$ nor the convergence of the series, so the
condition at $0$ costs nothing: extend by $\psi(0) = \psi(1)$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 1 (Khintchine).

Stated but not proved: `MetaMathlibExt.volume_wellApproximableSet_khintchine` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#volume-well-approximable-set-khintchine).

## Jarník–Besicovitch theorem

For a real number $\tau \ge 1$, let $W(\tau)$ be the set of
$x \in [0, 1)$ such that for infinitely many natural numbers $q$ there is an integer $p$ with
$|x - p/q| < q^{-(1+\tau)}$; this is the set of $\psi$-well approximable numbers for
$\psi(q) = q^{-\tau}$. Then the Hausdorff dimension of $W(\tau)$ is $2/(1 + \tau)$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 2 (Jarník; Besicovitch).

Stated but not proved: `MetaMathlibExt.dimH_wellApproximableSet_rpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#dim-h-well-approximable-set-rpow).

## Dodson's theorem

Let $\psi$ be a non-increasing function from the natural numbers to
$(0, 1/2]$, let $W(\psi)$ be the set of $x \in [0, 1)$ such that for infinitely many $q$ there
is an integer $p$ with $|x - p/q| < \psi(q)/q$, and let
$\tau_\psi = \liminf_{q \to \infty} (-\log \psi(q) / \log q)$, taken in $[0, \infty]$, be the
lower order at infinity of $1/\psi$. If $\tau_\psi \ge 1$, then the Hausdorff dimension of
$W(\psi)$ is $2/(1 + \tau_\psi)$, read as $0$ when $\tau_\psi = \infty$.

The paper allows $\psi(q) = 0$; here $\psi$ is assumed positive, so that $\log \psi(q)$ is
defined. Without the hypothesis $\tau_\psi \ge 1$ the formula fails: the constant
$\psi = 1/4$ has $\tau_\psi = 0$ and $\dim_H W(\psi) = 1$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 3 (Dodson).

Stated but not proved: `MetaMathlibExt.dimH_wellApproximableSet_dodson` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#dim-h-well-approximable-set-dodson).

## Lüroth denominators

For a sequence of natural numbers $d_0, d_1, d_2, \dots$ (numbered from
$0$), the $n$-th Lüroth denominator is

$$Q_n = d_n \prod_{j=0}^{n-1} d_j (d_j - 1), \qquad n \ge 0.$$

With digits numbered from $1$, as in the paper, this is the paper's $Q_{n+1}$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (8).

Formalized by `MetaMathlibExt.lurothDenominator`, a definition declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-denominator).

## Lüroth convergents

For a sequence of natural numbers $d_0, d_1, d_2, \dots$ (numbered from
$0$) with Lüroth denominators $Q_0, Q_1, Q_2, \dots$, the $n$-th Lüroth convergent is the rational
number

$$x_n = \sum_{k=0}^{n} \frac{1}{Q_k}, \qquad n \ge 0,$$

where a term with $Q_k = 0$ is read as $0$. With digits numbered from $1$, as in the paper, this is
the paper's $x_{n+1} = P_{n+1}/Q_{n+1}$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Section 2.

Formalized by `MetaMathlibExt.lurothConvergent`, a definition declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-convergent).

## The Lüroth digits of 1

Every Lüroth digit of $1$ equals $2$, that is,
$1 = [2, 2, 2, \dots]$ in Lüroth notation.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Section 2.

Formalized by `MetaMathlibExt.lurothDigitSeq_one`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-digit-seq-one).

## The Lüroth orbit of $27/71$ has period two

The Lüroth map $T$ sends $27/71$ to $20/71$
and sends $20/71$ to $27/71$; in particular $T(T(27/71)) = 27/71$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Section 2 (example).

Formalized by `MetaMathlibExt.lurothMap_lurothMap_27_71`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-map-luroth-map-27-71).

## Recurrence for Lüroth denominators

For every sequence of natural numbers
$d_0, d_1, d_2, \dots$ with Lüroth denominators $Q_0, Q_1, Q_2, \dots$ and every $n \ge 0$,

$$Q_{n+1} = Q_n (d_n - 1) d_{n+1}.$$

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (8).

Formalized by `MetaMathlibExt.lurothDenominator_succ`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-denominator-succ).

## Lüroth denominators of the constant digit sequence 2

If $d_j = 2$ for every $j \ge 0$,
then the Lüroth denominators are $Q_n = 2^{n+1}$ for every $n \ge 0$ (digits numbered from $0$;
this is the paper's $Q_{n+1} = 2^{n+1}$).

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (8).

Formalized by `MetaMathlibExt.lurothDenominator_two`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-denominator-two).

## Recurrence for Lüroth convergents

For every sequence of natural numbers
$d_0, d_1, d_2, \dots$ with Lüroth denominators $Q_n$ and Lüroth convergents $x_n$, and every
$n \ge 0$, $x_{n+1} = x_n + 1/Q_{n+1}$, where $1/Q_{n+1}$ is read as $0$ if $Q_{n+1} = 0$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Section 2.

Formalized by `MetaMathlibExt.lurothConvergent_succ`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-convergent-succ).

## Lüroth well approximable numbers

For a function $\psi$ from the natural numbers to the
reals, $L(\psi)$ is the set of $x \in (0, 1]$ such that $|x - c_n(x)| < \psi(Q_n(x))/Q_n(x)$ for
infinitely many $n$, where $Q_n(x)$ and $c_n(x)$ are the $n$-th Lüroth denominator and the $n$-th
Lüroth convergent of the Lüroth digit sequence of $x$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Section 2.

Formalized by `MetaMathlibExt.lurothWellApproximableSet`, a definition declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-well-approximable-set).

## Lüroth well approximable numbers lie in $(0, 1)$

For every function $\psi$ from the
natural numbers to the reals, the set $L(\psi)$ of Lüroth $\psi$-well approximable numbers is
contained in $(0, 1]$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Section 2.

Formalized by `MetaMathlibExt.lurothWellApproximableSet_subset_Ioc`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-well-approximable-set-subset-ioc).

## Lüroth convergent triples

The set $S$ consists of the triples $(c_n(y), Q_n(y), d_n(y))$
for $y \in (0, 1]$ and $n \ge 0$, where $d_0(y), d_1(y), \dots$ are the Lüroth digits of $y$
(indexed from $0$), $Q_n(y) = d_n(y) \prod_{j < n} d_j(y)(d_j(y) - 1)$ is the $n$-th Lüroth
denominator of this digit sequence, and $c_n(y) = \sum_{k \le n} 1/Q_k(y)$ is its $n$-th Lüroth
convergent. The first entry is the rational number $c_n(y)$, the second the natural number
$Q_n(y)$ and the third the digit $d_n(y)$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (16).

Formalized by `MetaMathlibExt.lurothTripleSet`, a definition declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-triple-set).

## A Lüroth triple from the expansion of $1$

Let $S$ be the set of triples
$(P_n(y)/Q_n(y), Q_n(y), d_n(y))$ for $y \in (0, 1]$ and $n \ge 0$, where $P_n(y)/Q_n(y)$ is the
$n$-th Lüroth convergent of $y$, $Q_n(y)$ its Lüroth denominator and $d_n(y)$ its $n$-th Lüroth
digit (indexed from $0$). Then $(1/2, 2, 2) \in S$: it is the triple of the first convergent of
$1 = [2, 2, 2, \ldots]$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, equation (16).

Formalized by `MetaMathlibExt.half_two_two_mem_lurothTripleSet`, a theorem declared in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#half-two-two-mem-luroth-triple-set).

## Lüroth convergents approximate from below

Let $x \in (0, 1]$ have Lüroth digits
$d_0, d_1, d_2, \dots$ (numbered from $0$), Lüroth denominators $Q_0, Q_1, Q_2, \dots$ and Lüroth
convergents $x_0, x_1, x_2, \dots$. Then for every $n \ge 0$,

$$0 < x - x_n \le \frac{1}{(d_n - 1) Q_n}.$$

In the paper's numbering from $1$ these are $d_{n+1}$, $Q_{n+1}$ and $x_{n+1} = P_{n+1}/Q_{n+1}$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Proposition 1.

Stated but not proved: `MetaMathlibExt.lurothConvergent_lt_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-convergent-lt-le).

## Mass transference principle for intervals

Let $(c_n)$ and $(r_n)$ be real sequences with
$r_n \ge 0$ for every $n$ and $r_n \to 0$, and let $I_n = [c_n - r_n, c_n + r_n]$. Assume that
$I_n \subseteq [0, 1]$ for every $n$, let $0 < s < 1$, and let $I_n^s = [c_n - r_n^s, c_n + r_n^s]$.
If $[0, 1] \cap \limsup_{n \to \infty} I_n^s$ has Lebesgue measure $1$, then the $s$-dimensional
Hausdorff measure of $\limsup_{n \to \infty} I_n$ is infinite and the Hausdorff dimension of
$\limsup_{n \to \infty} I_n$ is at least $s$.

The endpoints $s = 0$ and $s = 1$ admitted by the printed statement are excluded. For $s = 0$, the
intervals $I_n = [1/2 - 1/(n+2), 1/2 + 1/(n+2)]$ satisfy the hypothesis, but $\limsup I_n$ is the
single point $1/2$, whose $0$-dimensional Hausdorff measure is $1$. For $s = 1$, the
$1$-dimensional Hausdorff measure of a subset of $[0, 1]$ is at most $1$. The paper's proof treats
$0 < s < 1$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Proposition 3.

Stated but not proved: `MetaMathlibExt.hausdorffMeasure_limsup_closedBall_of_volume` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#hausdorff-measure-limsup-closed-ball-of).

## Recognising Lüroth convergents

For $y \in (0, 1]$ and $n \ge 0$ let $P_n(y)/Q_n(y)$ be
the $n$-th Lüroth convergent of $y$, $Q_n(y)$ its Lüroth denominator and $d_n(y)$ the $n$-th
Lüroth digit of $y$, and let $S$ be the set of all triples $(P_n(y)/Q_n(y), Q_n(y), d_n(y))$ for
$y \in (0, 1]$ and $n \ge 0$. If $x \in (0, 1]$ and $(P/Q, Q, d) \in S$ satisfy
$0 < x - P/Q \le 1/((d - 1) Q)$, then $P/Q$ is a Lüroth convergent of $x$, that is,
$P/Q = P_n(x)/Q_n(x)$ for some $n$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Proposition 4.

Stated but not proved: `MetaMathlibExt.exists_lurothConvergent_eq_of_mem_lurothTripleSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#exists-luroth-convergent-eq-of-mem-lurot).

## Lüroth $q^{-\tau}$-well approximable numbers as a limsup over convergent triples

Let
$\tau \ge 0$ and let $L(\tau)$ be the set of Lüroth $\psi$-well approximable numbers for
$\psi(q) = q^{-\tau}$. For a triple $t = (c, Q, d)$ in the set $S$ of Lüroth convergent triples, put
$B_t = (c, c + Q^{-(1+\tau)}) \cap (c, c + 1/((d - 1)Q)]$. Then $L(\tau)$ consists of the real
numbers $x$ that lie in $B_t$ for infinitely many $t \in S$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Proposition 5.

Stated but not proved: `MetaMathlibExt.lurothWellApproximableSet_rpow_eq_limsup` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-well-approximable-set-rpow-eq-lim).

## Lüroth well approximable numbers as a limsup over convergent triples

Let $\psi$ be a
function from the natural numbers to $(0, 1]$ whose lower order at infinity $\tau_\psi$ is greater
than $1$. Then the set $L(\psi)$ of Lüroth $\psi$-well approximable numbers consists of the real
numbers $x$ for which there are infinitely many triples $(c, Q, d)$ in the set $S$ of Lüroth
convergent triples with $c < x < c + \psi(Q)/Q$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Proposition 7.

Stated but not proved: `MetaMathlibExt.lurothWellApproximableSet_eq_limsup` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#luroth-well-approximable-set-eq-limsup).

## Tan–Zhou theorem (Lüroth analogue of Khintchine's theorem)

Let $\psi$ be a non-increasing
function from the natural numbers (including $0$) to $(0, 1]$, and let $L(\psi)$ be the set of
Lüroth $\psi$-well approximable numbers. If the series $\sum_{q \ge 1} -\psi(q) \log \psi(q) / q$
converges, then $L(\psi)$ has Lebesgue measure $0$; if it diverges, then $L(\psi)$ has Lebesgue
measure $1$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 4 (Tan and Zhou).

Stated but not proved: `MetaMathlibExt.volume_lurothWellApproximableSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#volume-luroth-well-approximable-set).

## Cao–Wu–Zhang theorem

For $x \in (0, 1]$ let $P_n(x)/Q_n(x)$ be the $n$-th Lüroth
convergent of $x$, with Lüroth denominator $Q_n(x)$. For a real number $\tau \ge 1$ let $L(\tau)$
be the set of $x \in (0, 1]$ such that $|x - P_n(x)/Q_n(x)| < Q_n(x)^{-\tau}/Q_n(x)$ for
infinitely many $n$, that is, the set of Lüroth $\psi$-well approximable numbers for
$\psi(q) = q^{-\tau}$. Then the Hausdorff dimension of $L(\tau)$ is $1/(1 + \tau)$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 5 (Cao, Wu, and Zhang).

Stated but not proved: `MetaMathlibExt.dimH_lurothWellApproximableSet_rpow_of_one_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#dim-h-luroth-well-approximable-set-rpow).

## Hausdorff dimension and measure of Lüroth well approximable sets for powers

For
$x \in (0, 1]$ let $P_n(x)/Q_n(x)$ be the $n$-th Lüroth convergent of $x$, with Lüroth
denominator $Q_n(x)$. For a real number $\tau \ge 0$ let $L(\tau)$ be the set of $x \in (0, 1]$
such that $|x - P_n(x)/Q_n(x)| < Q_n(x)^{-\tau}/Q_n(x)$ for infinitely many $n$, that is, the set
of Lüroth $\psi$-well approximable numbers for $\psi(q) = q^{-\tau}$. Then the Hausdorff dimension
of $L(\tau)$ is $1/(1 + \tau)$, and if $\tau > 0$, the $1/(1 + \tau)$-dimensional Hausdorff
measure of $L(\tau)$ is infinite.

The source also states the measure claim at $\tau = 0$, where it fails: $L(0)$ is contained in
$(0, 1]$, so its $1$-dimensional Hausdorff measure is at most $1$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 6.

Stated but not proved: `MetaMathlibExt.dimH_hausdorffMeasure_lurothWellApproximableSet_rpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#dim-h-hausdorff-measure-luroth-well-appr).

## Dimension bounds for Lüroth well approximable sets

Let $\psi$ be a function from the
natural numbers to $(0, 1]$. Let $L(\psi)$ be the set of $x \in (0, 1]$ such that
$|x - P_n(x)/Q_n(x)| < \psi(Q_n(x))/Q_n(x)$ for infinitely many $n$, where $P_n(x)/Q_n(x)$ is the
$n$-th Lüroth convergent of $x$ and $Q_n(x)$ its Lüroth denominator. Let
$\tau_\psi = \liminf_{q \to \infty} (-\log \psi(q) / \log q)$ and
$\bar\tau_\psi = \limsup_{q \to \infty} (-\log \psi(q) / \log q)$, taken in $[0, \infty]$, be the
lower and upper orders at infinity of $1/\psi$. Then
$1/(1 + \bar\tau_\psi) \le \dim_H L(\psi) \le 1/(1 + \tau_\psi)$, where $1/\infty = 0$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 7.

Stated but not proved: `MetaMathlibExt.dimH_lurothWellApproximableSet_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#dim-h-luroth-well-approximable-set-bound).

## Dimension bounds for Lüroth well approximable sets via denominators

Let $\psi$ be a
function from the natural numbers to $(0, 1]$. Let $L(\psi)$ be the set of $x \in (0, 1]$ such
that $|x - P_n(x)/Q_n(x)| < \psi(Q_n(x))/Q_n(x)$ for infinitely many $n$, where $P_n(x)/Q_n(x)$
is the $n$-th Lüroth convergent of $x$ and $Q_n(x)$ its Lüroth denominator. For $k \ge 0$ let
$S_k$ be the set of numbers $d_k \prod_{j < k} d_j (d_j - 1)$, where $d_0, \ldots, d_k$ are
integers at least $2$ (the $k$-th Lüroth denominators, indexed from $0$). For $q \ge 2$ put
$r(q) = -\log \psi(q) / \log q$, and let
$\lambda_\psi = \liminf_{k \to \infty} \liminf_{q \in S_k, q \to \infty} r(q)$,
$\bar\lambda_\psi = \liminf_{k \to \infty} \limsup_{q \in S_k, q \to \infty} r(q)$,
$\tau_\psi = \liminf_{q \to \infty} r(q)$ and $\bar\tau_\psi = \limsup_{q \to \infty} r(q)$,
all taken in $[0, \infty]$. Then $\tau_\psi \le \lambda_\psi$, $\bar\lambda_\psi \le \bar\tau_\psi$
and $1/(1 + \bar\lambda_\psi) \le \dim_H L(\psi) \le 1/(1 + \lambda_\psi)$, where $1/\infty = 0$.

Since $S_k$ is indexed from $0$, it is the paper's $S_{k+1}$; this does not change the outer
limit inferior.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 8.

Stated but not proved: `MetaMathlibExt.dimH_lurothWellApproximableSet_bounds_denominators` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#dim-h-luroth-well-approximable-set-bound-2).

## Without monotonicity the Lüroth dimension can vanish

For every real number $\tau \ge 0$
there is a function $\psi$ from the natural numbers to $(0, 1]$ such that: $\psi$ is not
non-increasing on $\{q : q \ge N\}$ for any $N$; the lower order at infinity
$\liminf_{q \to \infty} (-\log \psi(q) / \log q)$ of $1/\psi$ equals $\tau$; and the set
$L(\psi)$ of $x \in (0, 1]$ such that $|x - P_n(x)/Q_n(x)| < \psi(Q_n(x))/Q_n(x)$ for infinitely
many $n$, where $P_n(x)/Q_n(x)$ is the $n$-th Lüroth convergent of $x$ and $Q_n(x)$ its Lüroth
denominator, has Hausdorff dimension $0$.

Since $0 < 1/(1 + \tau)$, the Tan–Zhou conjecture fails without monotonicity.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 9.

Stated but not proved: `MetaMathlibExt.exists_not_antitone_dimH_lurothWellApproximableSet_eq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#exists-not-antitone-dim-h-luroth-well-ap).

## Dimension of Lüroth well approximable sets under a divergence condition

Let $\psi$ be a
function from the natural numbers to $(0, 1]$. Let $L(\psi)$ be the set of $x \in (0, 1]$ such
that $|x - P_n(x)/Q_n(x)| < \psi(Q_n(x))/Q_n(x)$ for infinitely many $n$, where $P_n(x)/Q_n(x)$
is the $n$-th Lüroth convergent of $x$ and $Q_n(x)$ its Lüroth denominator. Let
$\tau_\psi = \liminf_{q \to \infty} (-\log \psi(q) / \log q)$, taken in $[0, \infty]$, be the
lower order at infinity of $1/\psi$, and suppose $\tau_\psi > 1$. Put $t = 1/(1 + \tau_\psi)$,
with $t = 0$ if $\tau_\psi = \infty$, and $\theta_t(q) = \min\{1, 2^{-t} q^{1-t} \psi(q)^t\}$.
Suppose that $\theta_t$ is non-increasing on $\{q : q \ge 1\}$ and that the partial sums
$\sum_{q=1}^{N} -(\psi(q)/q)^t ((1 - t) \log q + t \log(\psi(q)/2))$ tend to $+\infty$ as
$N \to \infty$. Then the Hausdorff dimension of $L(\psi)$ is $1/(1 + \tau_\psi)$, read as $0$
when $\tau_\psi = \infty$.

The paper's monotonicity of $\theta_t$ on $\mathbb{N}$ is taken on $q \ge 1$ (at $q = 0$ the
formula gives $0$). The terms of the series need not be nonnegative, so its divergence to
$\infty$ is read as the partial sums tending to $+\infty$.

## Sources

- Ying Wai Lee, *Lüroth Expansions in Diophantine Approximation: Metric Properties and Conjectures*, INTEGERS 26 (2026), Article A45, Theorem 10.

Stated but not proved: `MetaMathlibExt.dimH_lurothWellApproximableSet_of_tendsto_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LurothDiophantineApproximationWanted.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html#dim-h-luroth-well-approximable-set-of-te).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lüroth series](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/l-roth-series)
