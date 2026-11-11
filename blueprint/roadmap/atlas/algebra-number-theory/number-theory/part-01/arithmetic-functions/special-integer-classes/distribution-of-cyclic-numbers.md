---
declaration: section
origin: cited
lean: MetaMathlibExt.IsCyclicNumber, MetaMathlibExt.oppermannCyclicCountLeft, MetaMathlibExt.oppermannCyclicCountRight, MetaMathlibExt.oppermannCyclicLeftApproximation, MetaMathlibExt.oppermannCyclicApproximation, MetaMathlibExt.oppermannCyclicRightApproximation, MetaMathlibExt.cyclicCount_isEquivalent_compositeCyclicCount, MetaMathlibExt.cyclicCountingFunctions_regularlyVarying_index_one
statement: formalized
---

# Distribution of cyclic numbers

15 results, 6 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html).

## Cyclic numbers

A positive integer $n$ is cyclic when $\gcd(n, \varphi(n)) = 1$, where
$\varphi$ is Euler's totient function.

Formalized by `MetaMathlibExt.IsCyclicNumber`, a definition declared in [MathlibExt/NumberTheory/OppermannCyclicNumbers.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/OppermannCyclicNumbers.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#is-cyclic-number).

## Cyclic numbers in the left Oppermann interval

For a natural number $n$, this is the
number of cyclic numbers $k$ with $n^2 - n \le k \le n^2$.

Formalized by `MetaMathlibExt.oppermannCyclicCountLeft`, a definition declared in [MathlibExt/NumberTheory/OppermannCyclicNumbers.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/OppermannCyclicNumbers.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#oppermann-cyclic-count-left).

## Cyclic numbers in the right Oppermann interval

For a natural number $n$, this is the
number of cyclic numbers $k$ with $n^2 \le k \le n^2 + n$.

Formalized by `MetaMathlibExt.oppermannCyclicCountRight`, a definition declared in [MathlibExt/NumberTheory/OppermannCyclicNumbers.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/OppermannCyclicNumbers.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#oppermann-cyclic-count-right).

## Left-hand approximation for cyclic numbers near squares

Let $\gamma$ be the
Euler–Mascheroni constant and, for real $x$, let $L(x) = \log \log \log (x^2)$. The left-hand
approximation is the function of the real variable $x$ given by

$$
\frac{x}{e^{\gamma} L(x)} \left(1 - \frac{\gamma}{L(x)}\right).
$$

Here $\log y$ means $\log |y|$, with $\log 0 = 0$, and a quotient by $0$ is $0$, so the expression
is defined for every real $x$. J. E. Cohen conjectures that, at $x = n$, it is asymptotic to
the number of cyclic numbers in $[n^2 - n, n^2]$.

Formalized by `MetaMathlibExt.oppermannCyclicLeftApproximation`, a definition declared in [MathlibExt/NumberTheory/OppermannCyclicNumbers.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/OppermannCyclicNumbers.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#oppermann-cyclic-left-approximation).

## Simplified approximation for cyclic numbers near squares

Let $\gamma$ be the
Euler–Mascheroni constant and, for real $x$, let $L(x) = \log \log \log x$. The simplified
approximation is the function of the real variable $x$ given by

$$
\frac{x}{e^{\gamma} L(x)} \left(1 - \frac{\gamma}{L(x)}\right).
$$

Here $\log y$ means $\log |y|$, with $\log 0 = 0$, and a quotient by $0$ is $0$, so the expression
is defined for every real $x$. J. E. Cohen conjectures that, at $x = n$, it is asymptotic to
the number of cyclic numbers in $[n^2 - n, n^2]$ and to the number in $[n^2, n^2 + n]$.

Formalized by `MetaMathlibExt.oppermannCyclicApproximation`, a definition declared in [MathlibExt/NumberTheory/OppermannCyclicNumbers.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/OppermannCyclicNumbers.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#oppermann-cyclic-approximation).

## Right-hand approximation for cyclic numbers near squares

Let $\gamma$ be the
Euler–Mascheroni constant and, for real $x$, let $L(x) = \log \log \log (x(x+1))$. The right-hand
approximation is the function of the real variable $x$ given by

$$
\frac{x}{e^{\gamma} L(x)} \left(1 - \frac{\gamma}{L(x)}\right).
$$

Here $\log y$ means $\log |y|$, with $\log 0 = 0$, and a quotient by $0$ is $0$, so the expression
is defined for every real $x$. J. E. Cohen conjectures that, at $x = n$, it is asymptotic to
the number of cyclic numbers in $[n^2, n^2 + n]$.

Formalized by `MetaMathlibExt.oppermannCyclicRightApproximation`, a definition declared in [MathlibExt/NumberTheory/OppermannCyclicNumbers.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/OppermannCyclicNumbers.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#oppermann-cyclic-right-approximation).

## Asymptotic count of cyclic and composite cyclic numbers

For real $x$, let $A(x)$ be the
number of cyclic numbers $m$ with $1 \le m \le x$, and let $cc(x)$ be the number of composite
cyclic numbers $m \le x$, that is, cyclic numbers $m > 1$ that are not prime. Then, as
$x \to \infty$, $A(x) \sim cc(x)$ and $cc(x) \sim x e^{-\gamma} / \log \log \log x$, where
$\gamma$ is the Euler–Mascheroni constant.

## Sources

- John M. Campbell and Joel E. Cohen, *Cyclic Numbers and Gaps*, INTEGERS 25 (2025), Article A23, Lemma 1.

Stated but not proved: `MetaMathlibExt.cyclicCount_isEquivalent_compositeCyclicCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclicNumberGapsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclicNumberGapsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#cyclic-count-is-equivalent-composite-cyc).

## The cyclic counting functions vary regularly with index one

For real $x$, let $A(x)$ be
the number of cyclic numbers $m$ with $1 \le m \le x$, let $\pi(x)$ be the number of primes
$p \le x$, and let $cc(x)$ be the number of composite cyclic numbers $m \le x$, that is, cyclic
numbers $m > 1$ that are not prime. Then for every real $\lambda > 0$, each of
$A(\lambda x) / A(x)$, $\pi(\lambda x) / \pi(x)$ and $cc(\lambda x) / cc(x)$ tends to $\lambda$
as $x \to \infty$.

Every prime is cyclic, so $\pi(x)$ is also the number of prime cyclic numbers $\le x$.

## Sources

- John M. Campbell and Joel E. Cohen, *Cyclic Numbers and Gaps*, INTEGERS 25 (2025), Article A23, Theorem 1.

Stated but not proved: `MetaMathlibExt.cyclicCountingFunctions_regularlyVarying_index_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclicNumberGapsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclicNumberGapsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#cyclic-counting-functions-regularly-vary).

## Taylor's law for cyclic numbers

Let $c_1 < c_2 < \cdots$ be the cyclic numbers in
increasing order, so $c_1 = 1$. For $n \ge 1$ let $m(c,n) = \frac{1}{n} \sum_{i=1}^{n} c_i$ be
the mean of $c_1, \dots, c_n$, and for $n \ge 2$ let
$v(c,n) = \frac{1}{n-1} \sum_{i=1}^{n} (c_i - m(c,n))^2$ be their variance. Then for every real
$b$, as $n \to \infty$, $v(c,n) / m(c,n)^b$ tends to $\infty$ if $b < 2$, to $1/3$ if $b = 2$,
and to $0$ if $b > 2$.

## Sources

- John M. Campbell and Joel E. Cohen, *Cyclic Numbers and Gaps*, INTEGERS 25 (2025), Article A23, Theorem 1.

Stated but not proved: `MetaMathlibExt.cyclicNumbers_variance_div_mean_rpow_tendsto` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclicNumberGapsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclicNumberGapsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#cyclic-numbers-variance-div-mean-rpow-te).

## Mean and variance of the cyclic numbers

Let $c_1 < c_2 < \cdots$ be the cyclic numbers
in increasing order, so $c_1 = 1$. For $n \ge 1$ let $m(c,n) = \frac{1}{n} \sum_{i=1}^{n} c_i$ be
the mean of $c_1, \dots, c_n$, and for $n \ge 2$ let
$v(c,n) = \frac{1}{n-1} \sum_{i=1}^{n} (c_i - m(c,n))^2$ be their variance. Then, as
$n \to \infty$, $m(c,n) \sim c_n / 2$ and $v(c,n) \sim c_n^2 / 12$.

## Sources

- John M. Campbell and Joel E. Cohen, *Cyclic Numbers and Gaps*, INTEGERS 25 (2025), Article A23, Theorem 1.

Stated but not proved: `MetaMathlibExt.cyclicNumbers_mean_variance_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclicNumberGapsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclicNumberGapsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#cyclic-numbers-mean-variance-is-equivale).

## Relation between the moments of the cyclic numbers

Let $c_1 < c_2 < \cdots$ be the
cyclic numbers in increasing order, so $c_1 = 1$, and for $n \ge 1$ and a natural number $k$ let
$\mu'(c,n,k) = \frac{1}{n} \sum_{i=1}^{n} c_i^k$ be the $k$-th moment of $c_1, \dots, c_n$. Then
for all natural numbers $j \ge 1$ and $k$, as $n \to \infty$,

$$
\mu'(c,n,k) \sim \frac{(j+1)^{k/j}}{k+1} \, \mu'(c,n,j)^{k/j}.
$$

## Sources

- John M. Campbell and Joel E. Cohen, *Cyclic Numbers and Gaps*, INTEGERS 25 (2025), Article A23, Theorem 1.

Stated but not proved: `MetaMathlibExt.cyclicNumbers_moment_isEquivalent_moment_rpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclicNumberGapsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclicNumberGapsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#cyclic-numbers-moment-is-equivalent-mome).

## Generalized Taylor's law for cyclic numbers

Let $c_1 < c_2 < \cdots$ be the cyclic
numbers in increasing order, so $c_1 = 1$. For $n \ge 1$ and a natural number $k$ let
$\mu'(c,n,k) = \frac{1}{n} \sum_{i=1}^{n} c_i^k$ be the $k$-th moment of $c_1, \dots, c_n$, and
let $m(c,n) = \mu'(c,n,1)$ be their mean. Then for every natural number $k$, as $n \to \infty$,

$$
\mu'(c,n,k) \sim \frac{2^k}{1+k} \, m(c,n)^k.
$$

## Sources

- John M. Campbell and Joel E. Cohen, *Cyclic Numbers and Gaps*, INTEGERS 25 (2025), Article A23, Theorem 1.

Stated but not proved: `MetaMathlibExt.cyclicNumbers_moment_isEquivalent_mean_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclicNumberGapsWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclicNumberGapsWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#cyclic-numbers-moment-is-equivalent-mean).

## Gaps between cyclic numbers under the Riemann hypothesis

Assume the Riemann hypothesis.
Let $c_1 < c_2 < \cdots$ be the cyclic numbers in increasing order and $p_1 < p_2 < \cdots$ the
primes in increasing order. Then the gaps $d_n = c_{n+1} - c_n$ between consecutive cyclic
numbers satisfy $d_n = o(\sqrt{p_n} \log p_n)$ as $n \to \infty$.

## Sources

- John M. Campbell and Joel E. Cohen, *Cyclic Numbers and Gaps*, INTEGERS 25 (2025), Article A23, Theorem 2.

Stated but not proved: `MetaMathlibExt.cyclicNumber_gap_isLittleO_of_riemannHypothesis` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclicNumberGapsWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclicNumberGapsWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#cyclic-number-gap-is-little-o-of-riemann).

## Cohen's Oppermann conjecture for cyclic numbers

For every natural number $n > 1$ there are
cyclic numbers $c$ and $c'$ with $n^2 - n < c < n^2 < c' < n^2 + n$. Moreover, let $C_L(n)$ and
$C_R(n)$ be the numbers of cyclic numbers in $[n^2 - n, n^2]$ and in $[n^2, n^2 + n]$, and let
$A_L$, $A_R$ and $A$ be the left-hand, right-hand and simplified approximations for cyclic numbers
near squares. Then, as $n \to \infty$ through the natural numbers, $C_L(n) \sim A_L(n)$,
$A_L(n) \sim A(n)$, $C_R(n) \sim A_R(n)$ and $A_R(n) \sim A(n)$.

## Sources

- J. E. Cohen, *Conjectures about Primes and Cyclic Numbers*, J. Integer Seq. 28 (2025), Article 25.4.1.

Stated but not proved: `MetaMathlibExt.oppermannAnalogForCyclicNumbers` is written with `theorem_wanted` in [WantedExt/NumberTheory/OppermannAnalogForCyclicsWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OppermannAnalogForCyclicsWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#oppermann-analog-for-cyclic-numbers).

## Power sums of cyclic numbers

Let $k \ge 1$ be an integer. Let $c_n$ be the $n$-th cyclic
number ($c_1 = 1$), let $C(x)$ be the number of cyclic numbers $m \le x$, and let $\gamma$ be the
Euler–Mascheroni constant. Then, as $n \to \infty$ through the natural numbers,

$$
\sum_{i=1}^{n} c_i^k \sim \frac{n c_n^k}{k+1}
\sim \frac{n^{k+1} e^{k\gamma} (\log \log \log n)^k}{k+1},
$$

and, as $x \to \infty$ through the real numbers,

$$
\sum_{m \le x,\ m \text{ cyclic}} m^k \sim \frac{C(x)\, c_{C(x)}^k}{k+1}
\sim \frac{C(x)\, x^k}{k+1}
\sim \frac{x^{k+1}}{(k+1) e^{\gamma} \log \log \log x}
\left(1 - \frac{\gamma}{\log \log \log x}\right).
$$

## Sources

- Joel E. Cohen, *Conjectures about Primes and Cyclic Numbers*, Journal of Integer Sequences 28 (2025), Article 25.4.7, Theorem 1 (`jis-2025-25.4.7-thm-1`).

Stated but not proved: `MetaMathlibExt.sum_pow_cyclicNumbers_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/SumsOfCyclicNumbersWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SumsOfCyclicNumbersWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html#sum-pow-cyclic-numbers-is-equivalent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distribution of cyclic numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/distribution-of-cyclic-numbers)
