---
declaration: section
origin: cited
lean: MetaMathlibExt.linearRecurrence_of_finite_window, MetaMathlibExt.rootsOfUnity_product_mul_eq_comp_pow, MetaMathlibExt.riordan_stepSum_coeff, MetaMathlibExt.binomialStepSum_recurrence_of_window, MetaMathlibExt.shiftedBinomialStepSum_recurrence_of_window, MetaMathlibExt.rationalRiordan_stepSum_linearRecurrence, MetaMathlibExt.catalanTriangle_stepFive_sub_eq_fib
statement: formalized
---

# Recurrences for step sums of binomial coefficients

7 results, 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien/index.html).

## Finite window criterion for linear recurrences

Let $R$ be a commutative ring, let
$x, A, a : \mathbb{N} \to R$ and let $r, s, N \in \mathbb{N}$. Suppose that
$x_n = \sum_{i=1}^{r} A_i x_{n-i}$ for all $n \ge r$, that $N \ge r + s - 1$, and that
$x_n = \sum_{i=1}^{s} a_i x_{n-i}$ for all $n$ with $s \le n \le N$. Then
$x_n = \sum_{i=1}^{s} a_i x_{n-i}$ for all $n \ge s$.

## Sources

- Eduardo H. M. Brietzke, *Recurrence Relations for Sums of Binomial Coefficients and Some Generalizations*, Journal of Integer Sequences 27 (2024), Article 24.3.4, Proposition 1.

Stated but not proved: `MetaMathlibExt.linearRecurrence_of_finite_window` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien/index.html#linear-recurrence-of-finite-window).

## Roots-of-unity products of integer polynomials

Let $f \in \mathbb{Z}[x]$ have degree
$r$, let $k > 0$ be a natural number and let $\omega = e^{2\pi i/k}$. Then there are
$G, T \in \mathbb{Z}[x]$ such that $G(x) = f(\omega x) f(\omega^2 x) \cdots f(\omega^{k-1} x)$
as polynomials over $\mathbb{C}$, $T$ has degree $r$, and $f(x) G(x) = T(x^k)$.

## Sources

- Eduardo H. M. Brietzke, *Recurrence Relations for Sums of Binomial Coefficients and Some Generalizations*, Journal of Integer Sequences 27 (2024), Article 24.3.4, Proposition 2.

Stated but not proved: `MetaMathlibExt.rootsOfUnity_product_mul_eq_comp_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien/index.html#roots-of-unity-product-mul-eq-comp-pow).

## Step sums along a Riordan array

Let $K$ be a field, let $g, h \in K[[x]]$ with
$h(0) = 0$, and write $d(n, m) = [x^n]\, g(x) h(x)^m$. Then for all natural numbers $k > 1$,
$p < k$ and $n$,
$\sum_{j=0}^{n} d(n, kj + p) = [x^n]\, g(x) h(x)^p (1 - h(x)^k)^{-1}$.

Since $h(0) = 0$, $d(n, m) = 0$ for $m > n$, so the left side is the full sum over all
$j \ge 0$.

## Sources

- Eduardo H. M. Brietzke, *Recurrence Relations for Sums of Binomial Coefficients and Some Generalizations*, Journal of Integer Sequences 27 (2024), Article 24.3.4, Proposition 5.

Stated but not proved: `MetaMathlibExt.riordan_stepSum_coeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien/index.html#riordan-step-sum-coeff).

## Window criterion for step sums of binomial coefficients

Let $\alpha, k, \gamma, p, s$
be natural numbers with $\alpha > 1$, $k > 1$, $\gamma \ge 1$ and $p < k$, and let
$\delta_1, \delta_2, \ldots$ be integers. For $n \in \mathbb{N}$ let $c(n)$ be the sum of
$\binom{\alpha n}{m}$ over all $m$ with $0 \le m \le \alpha n$ and
$m \equiv \gamma n + p \pmod{k}$, that is, $c(n) = \sum_{j \in \mathbb{Z}}
\binom{\alpha n}{\gamma n + p + kj}$. If $c(n) = \sum_{i=1}^{s} \delta_i c(n - i)$ for all $n$
with $s \le n \le k^2 + s - 1$, then $c(n) = \sum_{i=1}^{s} \delta_i c(n - i)$ for all $n \ge s$.

The coefficients $\delta_i$ need only work for this one residue $p$; the source's hypothesis,
with one family $\delta_i$ for every $p$, is a special case.

## Sources

- Eduardo H. M. Brietzke, *Recurrence Relations for Sums of Binomial Coefficients and Some Generalizations*, Journal of Integer Sequences 27 (2024), Article 24.3.4, Proposition 8.

Stated but not proved: `MetaMathlibExt.binomialStepSum_recurrence_of_window` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien/index.html#binomial-step-sum-recurrence-of-window).

## Window criterion for shifted step sums of binomial coefficients

Let
$\alpha, \beta, k, \gamma, p, s$ be natural numbers with $\alpha > 1$, $k > 1$, $\gamma > 1$ and
$p < k$, and let $\delta_1, \delta_2, \ldots$ be integers. For $n \in \mathbb{N}$ let $c(n)$ be
the sum of $\binom{\alpha n + \beta}{m}$ over all $m$ with $0 \le m \le \alpha n + \beta$ and
$m \equiv \gamma n + p \pmod{k}$, that is,
$c(n) = \sum_{j \in \mathbb{Z}} \binom{\alpha n + \beta}{\gamma n + p + kj}$. If
$c(n) = \sum_{i=1}^{s} \delta_i c(n - i)$ for all $n$ with $s \le n \le k^2 + s - 1$, then
$c(n) = \sum_{i=1}^{s} \delta_i c(n - i)$ for all $n \ge s$.

The coefficients $\delta_i$ need only work for this one residue $p$; the source's hypothesis,
with one family $\delta_i$ for every $p$, is a special case.

## Sources

- Eduardo H. M. Brietzke, *Recurrence Relations for Sums of Binomial Coefficients and Some Generalizations*, Journal of Integer Sequences 27 (2024), Article 24.3.4, Theorem 9.

Stated but not proved: `MetaMathlibExt.shiftedBinomialStepSum_recurrence_of_window` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien/index.html#shifted-binomial-step-sum-recurrence-of).

## Step sums of a rational Riordan array satisfy a common recurrence

Let
$g_1, g_2, h_1, h_2 \in \mathbb{Z}[x]$ with $g_2(0) = h_1(0) = h_2(0) = 1$, let $\nu \ge 1$ and
$k \ge 1$ be natural numbers, and in $\mathbb{Q}[[x]]$ let $g = g_1/g_2$ and
$h = x^\nu h_1/h_2$. For $p, n \in \mathbb{N}$ let
$a_p(n) = \sum_{j=0}^{n} [x^n]\, g h^{kj+p}$. Then there are $r \in \mathbb{N}$ and integers
$\alpha_1, \ldots, \alpha_r$ such that $a_p(n) = \sum_{i=1}^{r} \alpha_i a_p(n - i)$ for every
$p < k$ and every $n \ge r$.

Since $h$ has no constant term, $[x^n]\, g h^m = 0$ for $m > n$, so $a_p(n)$ is the full sum
over all $j \ge 0$.

## Sources

- Eduardo H. M. Brietzke, *Recurrence Relations for Sums of Binomial Coefficients and Some Generalizations*, Journal of Integer Sequences 27 (2024), Article 24.3.4, Proposition 11.

Stated but not proved: `MetaMathlibExt.rationalRiordan_stepSum_linearRecurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien/index.html#rational-riordan-step-sum-linear-recurre).

## Alternating step-five sums of Catalan's triangle are Fibonacci numbers

For natural
numbers $n$ and $k$ let $d(n, k) = \frac{k + 1}{n + 1} \binom{2(n + 1)}{n - k}$ if $k \le n$,
and $d(n, k) = 0$ if $k > n$. Let $F_m$ be the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$). Then
for every $n \in \mathbb{N}$,
$\sum_{j=0}^{n} \bigl(d(n, 5j + 1) - d(n, 5j + 2)\bigr) = F_{2n}$ and
$\sum_{j=0}^{n} \bigl(d(n, 5j) - d(n, 5j + 3)\bigr) = F_{2n+1}$.

The numbers $d(n, k)$ form Catalan's triangle (OEIS A039598), the Riordan array $(g, xg)$ with
$g(x) = (1 - 2x - \sqrt{1 - 4x})/(2x^2)$; since $d(n, m) = 0$ for $m > n$, the sums are the full
sums over all $j \ge 0$.

## Sources

- Eduardo H. M. Brietzke, *Recurrence Relations for Sums of Binomial Coefficients and Some Generalizations*, Journal of Integer Sequences 27 (2024), Article 24.3.4, Proposition 13.

Stated but not proved: `MetaMathlibExt.catalanTriangle_stepFive_sub_eq_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BinomialSumRecurrencesWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien/index.html#catalan-triangle-step-five-sub-eq-fib).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Recurrences for step sums of binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/recurrences-for-step-sums-of-binomial-coefficien)
