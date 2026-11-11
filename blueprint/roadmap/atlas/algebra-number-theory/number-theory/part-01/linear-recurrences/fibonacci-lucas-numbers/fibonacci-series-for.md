---
declaration: section
origin: cited
lean: MetaMathlibExt.pi_sq_eq_fibonacci_factorial_series, MetaMathlibExt.pi_sq_eq_fibonacci_central_series, MetaMathlibExt.fibPiSquared_coeff_eq_fib, MetaMathlibExt.fibPiSquared_poly_eq_sum
statement: formalized
---

# Fibonacci series for π²

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-series-for/index.html).

## Fibonacci series for $\pi^2$ with polynomial weights

Let $p_1, p_2, \dots$ be polynomials
with integer coefficients such that $p_1 = 1$ and, for every $n \ge 1$,
$p_{n+1}(x) = (2x + 2n + 1)(2x + 2n + 2)\, p_n(x) - (x + 1)^2 p_n(x + 1)$. Let $(a_n)_{n \ge 0}$
be real numbers with $a_0 = -8\sqrt{5}/250$, $a_1 = (25 - 4\sqrt{5})/250$ and
$a_{n+1} = a_n + a_{n-1}$ for $n \ge 1$, and let $(b_n)_{n \ge 0}$ be real numbers with
$b_0 = b_1 = 0$ and $b_{n+1} = b_n + b_{n-1} + (-1)^{n+1} p_n(0)/(2n)!$ for $n \ge 1$. Write $F_m$
for the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$). Then for every $n \ge 1$,

$$\pi^2 = \frac{1}{a_{n-1}} \Bigl(b_{n-1} + (-1)^n \sum_{k=0}^{\infty}
\frac{(k!)^2 \, p_n(k) \, F_{2k+2}}{(2k+2n)!}\Bigr)$$

and

$$\pi^2 = \frac{1}{a_n} \Bigl(b_n + (-1)^{n+1} \sum_{k=0}^{\infty}
\frac{(k!)^2 \, p_n(k) \, F_{2k+1}}{(2k+2n)!}\Bigr).$$

## Sources

- Joseph Tonien, *Fibonacci and Pi Squared*, The Fibonacci Quarterly 62 (2024), no. 1, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.pi_sq_eq_fibonacci_factorial_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciPiSquaredWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FibonacciPiSquaredWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-series-for/index.html#pi-sq-eq-fibonacci-factorial-series).

## Two Fibonacci series for $\pi^2$

Writing $F_m$ for the Fibonacci numbers ($F_0 = 0$,
$F_1 = 1$),

$$\pi^2 = \frac{250}{8\sqrt{5}} \sum_{k=0}^{\infty} \frac{(k!)^2 \, F_{2k+2}}{(2k+2)!}
\quad \text{and} \quad
\pi^2 = \frac{250}{25 - 4\sqrt{5}} \sum_{k=0}^{\infty} \frac{(k!)^2 \, F_{2k+1}}{(2k+2)!}.$$

These are identities (2.3) and (2.4) of the paper, the case $n = 1$ of its Theorem 2.1.

## Sources

- Joseph Tonien, *Fibonacci and Pi Squared*, The Fibonacci Quarterly 62 (2024), no. 1, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.pi_sq_eq_fibonacci_central_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciPiSquaredWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FibonacciPiSquaredWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-series-for/index.html#pi-sq-eq-fibonacci-central-series).

## Fibonacci closed form of the sequence $a_n$

Let $(a_n)_{n \ge 0}$ be real numbers with
$a_0 = -8\sqrt{5}/250$, $a_1 = (25 - 4\sqrt{5})/250$ and $a_{n+1} = a_n + a_{n-1}$ for $n \ge 1$,
and write $F_m$ for the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$). Then for every $n \ge 0$,

$$a_{n+1} = \frac{25 - 4\sqrt{5}}{250} F_{n+1} - \frac{8\sqrt{5}}{250} F_n.$$

The paper states $a_n = \frac{25 - 4\sqrt{5}}{250} F_n - \frac{8\sqrt{5}}{250} F_{n-1}$ for all
$n \ge 0$ with the convention $F_{-1} = 1$; its case $n = 0$ is the initial value $a_0$.

## Sources

- Joseph Tonien, *Fibonacci and Pi Squared*, The Fibonacci Quarterly 62 (2024), no. 1, Lemma 2.3.

Stated but not proved: `MetaMathlibExt.fibPiSquared_coeff_eq_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciPiSquaredWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FibonacciPiSquaredWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-series-for/index.html#fib-pi-squared-coeff-eq-fib).

## Explicit formula for the polynomials $p_n$

Let $p_1, p_2, \dots$ be polynomials with
integer coefficients such that $p_1 = 1$ and, for every $n \ge 1$,
$p_{n+1}(x) = (2x + 2n + 1)(2x + 2n + 2)\, p_n(x) - (x + 1)^2 p_n(x + 1)$. Then for every
$n \ge 1$, as polynomials in $x$,

$$p_n(x) = \sum_{j=0}^{n-1} (-1)^j \binom{n-1}{j} \Bigl(\prod_{k=2j+3}^{2n} (2x + k)\Bigr)
\prod_{t=1}^{j} (x + t)^2.$$

## Sources

- Joseph Tonien, *Fibonacci and Pi Squared*, The Fibonacci Quarterly 62 (2024), no. 1, Lemma 2.4.

Stated but not proved: `MetaMathlibExt.fibPiSquared_poly_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciPiSquaredWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FibonacciPiSquaredWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-series-for/index.html#fib-pi-squared-poly-eq-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibonacci series for π²](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-series-for/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-series-for)
