---
declaration: section
origin: cited
lean: MetaMathlibExt.iterate_logb_tetration_strictMono_and_converges, MetaMathlibExt.div_exp_one_rpow_lt_Gamma_add_one, MetaMathlibExt.Gamma_add_one_mul_log_le_Gamma_rpow_self, MetaMathlibExt.exists_tetration_eq_iterate_rpow_eventually, MetaMathlibExt.exists_tetration_eq_iterate_rpow, MetaMathlibExt.iterate_factorial_lt_iterate_factorial, MetaMathlibExt.exists_iterate_factorial_eq_iterate_rpow_ten, MetaMathlibExt.exists_iterate_factorial_eq_tetration
statement: formalized
---

# Iterated factorials and power towers

11 results, 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html).

## Iterated logarithms of power towers increase to a limit

Let $a, b$ be real numbers
with $e^{1/e} < a < b$. For $n \ge 0$ let $b \uparrow\uparrow n$ be the $n$-fold iterate of
$x \mapsto b^x$ starting at $1$ (so $b \uparrow\uparrow 0 = 1$ and $b \uparrow\uparrow 1 = b$),
and let $a_n = \log_a^{(n)}(b \uparrow\uparrow n)$ be its $n$-fold iterated base-$a$
logarithm, so that $a_0 = 1$. Then the sequence $(a_n)_{n \ge 0}$ is strictly increasing and
converges to a real number.

The paper's "increasing" is read as strictly increasing, and its finite limit as convergence
to a real number.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Lemma 2 (`jis-2025-25.2.8-lem-2`).

Stated but not proved: `MetaMathlibExt.iterate_logb_tetration_strictMono_and_converges` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#iterate-logb-tetration-strict-mono-and-c).

## Lower bound $\Gamma(x + 1) > (x/e)^x$ for the Gamma function

For every real number
$x \ge 1$, $\Gamma(x + 1) > (x/e)^x$.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Lemma 9 (`jis-2025-25.2.8-lem-9`).

Stated but not proved: `MetaMathlibExt.div_exp_one_rpow_lt_Gamma_add_one` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#div-exp-one-rpow-lt-gamma-add-one).

## Upper bound $\Gamma(x + 1) \ln \Gamma(x + 1) \le \Gamma(x)^{\Gamma(x)}$

For every real
number $x > 4$, $\Gamma(x + 1) \ln \Gamma(x + 1) \le \Gamma(x)^{\Gamma(x)}$.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Lemma 9 (`jis-2025-25.2.8-lem-9`).

Stated but not proved: `MetaMathlibExt.Gamma_add_one_mul_log_le_Gamma_rpow_self` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#gamma-add-one-mul-log-le-gamma-rpow-self).

## Normalization of power towers

Let $a, b > e^{1/e}$ be real numbers with $a \ne b$. For
a real number $c$ and $m \ge 0$ let $E_m(b, c)$ be the $m$-fold iterate of $x \mapsto b^x$
starting at $c$ (the tower $b^{b^{\cdots^{c}}}$ with $m$ copies of $b$), and let
$a \uparrow\uparrow n$ be the $n$-fold iterate of $x \mapsto a^x$ starting at $1$. Then there
are a natural number $N$, an integer $k$ and a convergent sequence $(c_n)$ of real numbers such
that for every $n \ge N$ we have $n + k \ge 0$, $1 < c_n < b$ and
$a \uparrow\uparrow n = E_{n+k}(b, c_n)$.

The paper leaves the condition $n + k \ge 0$ implicit.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Theorem 1 (`jis-2025-25.2.8-thm-1`), quoted from the author's earlier paper.

Stated but not proved: `MetaMathlibExt.exists_tetration_eq_iterate_rpow_eventually` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#exists-tetration-eq-iterate-rpow-eventua).

## Power towers rewritten in another base

Let $a, b > e^{1/e}$ be real numbers and $n > 0$
a natural number. Let $a \uparrow\uparrow n$ be the $n$-fold iterate of $x \mapsto a^x$ starting
at $1$, and $E_p(b, c)$ the $p$-fold iterate of $x \mapsto b^x$ starting at $c$. Then there are
a natural number $p$ and a real number $c$ with $1 < c \le b$ such that
$a \uparrow\uparrow n = E_p(b, c)$.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Lemma 3 (`jis-2025-25.2.8-lem-3`), quoted from the author's earlier paper.

Stated but not proved: `MetaMathlibExt.exists_tetration_eq_iterate_rpow` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#exists-tetration-eq-iterate-rpow).

## Comparison of iterated factorials

For natural numbers $j$ and $m$ let $F_j(m)$ be the
$j$-fold iterated factorial $m!\cdots!$ (with $j$ factorials). Let $n, n' \ge 3$ and $k > k'$ be
natural numbers. If $n' < F_{k-k'}(n)$, then $F_{k'}(n') < F_k(n)$.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Theorem 4 (`jis-2025-25.2.8-thm-4`).

Stated but not proved: `MetaMathlibExt.iterate_factorial_lt_iterate_factorial` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#iterate-factorial-lt-iterate-factorial).

## Iterated factorials as base-$10$ power towers

Let $k \ge 3$ be a natural number, let
$F_n(k)$ be the $n$-fold iterated factorial of $k$, viewed as a real number, and for a real
number $c$ and $m \ge 0$ let $E_m(10, c)$ be the $m$-fold iterate of $x \mapsto 10^x$ starting
at $c$. Then there are an integer $\ell$, a natural number $N > 0$, a sequence $(c_n)$ of real
numbers and a real number $L$ with the following properties: for every $n \ge N$ we have
$n + \ell \ge 0$, $1 < c_n \le 10$ and $F_n(k) = E_{n+\ell}(10, c_n)$; the sequence
$(c_n)_{n \ge N}$ is strictly increasing and converges to $L$; and
$E_{n+\ell}(10, L) / (F_n(k) \ln F_n(k)) \to 1 / \ln 10$ as $n \to \infty$.

The paper leaves the condition $n + \ell \ge 0$ implicit.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Theorem 5 (`jis-2025-25.2.8-thm-5`).

Stated but not proved: `MetaMathlibExt.exists_iterate_factorial_eq_iterate_rpow_ten` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#exists-iterate-factorial-eq-iterate-rpow).

## Iterated factorials as tetrations

Let $k \ge 3$ be a natural number and $F_n(k)$ the
$n$-fold iterated factorial of $k$; for a real number $\beta$ let $\beta \uparrow\uparrow n$ be
the $n$-fold iterate of $x \mapsto \beta^x$ starting at $1$. Then there is a sequence $(b_n)$ of
real numbers such that $b_n > e^{1/e}$ and $F_n(k) = b_n \uparrow\uparrow n$ for every
$n \ge 1$, and $(b_n)$ converges to a limit $b \le k!$.

The case $n = 0$ is excluded, as the paper defines power towers only for $n \ge 1$.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Theorem 8 (`jis-2025-25.2.8-thm-8`).

Stated but not proved: `MetaMathlibExt.exists_iterate_factorial_eq_tetration` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#exists-iterate-factorial-eq-tetration).

## Iterated Gamma values as power towers

Let $z > 1$ be a real number with
$\Gamma(z) = z$, let $b > e^{1/e}$ and $x > z$ be real numbers, let $\Gamma^n$ be the $n$-fold
iterate of $\Gamma$, and for a real number $c$ and $m \ge 0$ let $E_m(b, c)$ be the $m$-fold
iterate of $y \mapsto b^y$ starting at $c$. Then there are an integer $\ell$, a natural number
$N > 0$, a sequence $(c_n)$ of real numbers and a real number $L$ with the following
properties: for every $n \ge N$ we have $n + \ell \ge 0$, $1 < c_n \le b$ and
$\Gamma^n(x) = E_{n+\ell}(b, c_n)$; the sequence $(c_n)_{n \ge N}$ is strictly increasing and
converges to $L$; and
$E_{n+\ell}(b, L) / ((\Gamma^n(x) - 1) \ln(\Gamma^n(x) - 1)) \to 1 / \ln b$ as $n \to \infty$.

This is a corrected reading of the printed statement: $x > z$ for the printed $x \ge z$ (at
$x = z$ the orbit is constant while $E_{n+\ell}(b, c_n)$ tends to infinity); $\Gamma^n(x)$ for
the printed $\Gamma^n(k)$ ($k$ is unbound); and $c_n \le b$, the bound of the proof and of its
restatement in the proof of Theorem 12, for the printed $c_n \le 10$ (copied from Theorem 5).

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Theorem 10 (`jis-2025-25.2.8-thm-10`).

Stated but not proved: `MetaMathlibExt.exists_iterate_Gamma_eq_iterate_rpow` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#exists-iterate-gamma-eq-iterate-rpow).

## Gamma of an iterated exponential exceeds the next iterate

Let $b \ge e$ and, for
$m \ge 0$, let $E_m(b, b)$ be the $m$-fold iterate of $x \mapsto b^x$ started at $b$, so that
$E_0(b, b) = b$ and $E_{m+1}(b, b) = b^{E_m(b, b)}$. Then for every integer $n > 0$,
$E_{n+1}(b, b) < \Gamma(E_n(b, b))$.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Lemma 11 (`jis-2025-25.2.8-lem-11`).

Stated but not proved: `MetaMathlibExt.iterate_rpow_succ_lt_Gamma_iterate_rpow` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#iterate-rpow-succ-lt-gamma-iterate-rpow).

## Tetrations as iterated Gamma values

Let $z > 1$ be a real number with $\Gamma(z) = z$,
and let $b > z$. Let $b \uparrow\uparrow n$ be the $n$-fold iterate of $y \mapsto b^y$ starting
at $1$, and $\Gamma^n$ the $n$-fold iterate of $\Gamma$. Then there is a convergent sequence
$(x_n)$ of real numbers, strictly decreasing from some index on, such that
$b \uparrow\uparrow n = \Gamma^n(x_n)$ for every $n \ge 1$.

The case $n = 0$ is excluded, as the paper defines power towers only for $n \ge 1$.

## Sources

- Karol Gryszka, *Exponential versus Factorial Revisited*, Journal of Integer Sequences 28 (2025), Article 25.2.8, Theorem 12 (`jis-2025-25.2.8-thm-12`).

Stated but not proved: `MetaMathlibExt.exists_tetration_eq_iterate_Gamma` is written with `theorem_wanted` in [WantedExt/Analysis/ExponentialVersusFactorialWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ExponentialVersusFactorialWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html#exists-tetration-eq-iterate-gamma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Iterated factorials and power towers](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/gamma-function/iterated-factorials-and-power-towers)
