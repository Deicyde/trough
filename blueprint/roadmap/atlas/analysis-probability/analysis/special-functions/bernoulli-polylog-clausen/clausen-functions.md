---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9ClausenTerm_norm_bound, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9ClausenTerm_summable_of_two_le, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9Clausen_zero, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9Clausen_one, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9Clausen_of_two_le, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.ramanujan_part1_ch9_entry13_bernoulligen, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9OddClausenTerm_norm_bound, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9OddClausenTerm_summable_of_two_le
statement: formalized
proof: formalized
---

# Clausen functions

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html).

## Termwise bound for the Clausen series (Chapter 9, Entry 13)

For natural numbers $m$ and
$k$ and a real number $x$, let $t_k = \sin((k+1)x)/(k+1)^m$ if $m$ is even and
$t_k = \cos((k+1)x)/(k+1)^m$ if $m$ is odd. Then $\lvert t_k\rvert \le 1/(k+1)^m$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9ClausenTerm_norm_bound`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-clausen-term-norm-bound).

## Summability of the Clausen series (Chapter 9, Entry 13)

For every natural number
$m \ge 2$ and every real $x$, the series $\sum_{k \ge 1} \sin(kx)/k^m$ (if $m$ is even) or
$\sum_{k \ge 1} \cos(kx)/k^m$ (if $m$ is odd) is summable.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9ClausenTerm_summable_of_two_le`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-clausen-term-summable-of-two-le).

## Clausen function of order zero (Chapter 9, Entry 13)

The Clausen-type functions $C_m$
of Entry 13 are defined by $C_1(x) = -\log\lvert 2\sin(x/2)\rvert$ and, for $m \ge 2$,
$C_m(x) = \sum_{k \ge 1} \sin(kx)/k^m$ for even $m$ and $C_m(x) = \sum_{k \ge 1} \cos(kx)/k^m$
for odd $m$, together with the convention $C_0 = 0$: for every real $x$, $C_0(x) = 0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9Clausen_zero`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-clausen-zero).

## Clausen function of order one (Chapter 9, Entry 13)

The order-one Clausen-type function
$C_1$ of Entry 13 is the log-sine function: for every real $x$,
$C_1(x) = -\log\lvert 2\sin(x/2)\rvert$, with the convention $\log 0 = 0$, so that $C_1$ vanishes
at the integer multiples of $2\pi$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9Clausen_one`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-clausen-one).

## Clausen functions of order at least two as series (Chapter 9, Entry 13)

Let $C_m$ be the
Clausen-type function of Entry 13, with $C_0 = 0$ and $C_1(x) = -\log\lvert 2\sin(x/2)\rvert$.
For every natural number $m \ge 2$ and every real $x$, $C_m(x) = \sum_{k \ge 1} \sin(kx)/k^m$ if
$m$ is even and $C_m(x) = \sum_{k \ge 1} \cos(kx)/k^m$ if $m$ is odd.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.chapter9Clausen_of_two_le`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-clausen-of-two-le).

## Integrals of $u^n \cot(u/2)$ via Clausen functions (Chapter 9, Entry 13)

For real $x$
let $C_1(x) = -\log\lvert 2\sin(x/2)\rvert$ and, for $m \ge 2$, let
$C_m(x) = \sum_{k \ge 1} \sin(kx)/k^m$ if $m$ is even and $C_m(x) = \sum_{k \ge 1} \cos(kx)/k^m$
if $m$ is odd. Let $n \ge 1$ be a natural number and $x$ a nonzero real number with
$\lvert x\rvert < 2\pi$. Then the function $u \mapsto \frac{u^n}{2}\cot\frac{u}{2}$ is integrable
on the interval between $0$ and $x$; the partial sums $\sum_{k=1}^{N} \cos(kx)/k$ converge to
$C_1(x)$ as $N \to \infty$; for every natural number $m$ with $2 \le m \le n + 1$ the series
defining $C_m(x)$ is summable; and, with $\zeta$ the Riemann zeta function,

$$
\int_0^x \frac{u^n}{2}\cot\frac{u}{2}\,du = \cos\frac{n\pi}{2}\,n!\,\zeta(n+1) -
\sum_{j=0}^{n} (-1)^{j(j+1)/2}\,\frac{n!}{(n-j)!}\,x^{n-j}\,C_{j+1}(x).
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry13Bernoulligen.ramanujan_part1_ch9_entry13_bernoulligen`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean, line 1698](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry13Bernoulligen.lean#L1698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#ramanujan-part1-ch9-entry13-bernoulligen).

## Bound on the terms of the odd Clausen series

For integers $m, k \ge 0$ let $s_m = \sin$ if
$m$ is even and $s_m = \cos$ if $m$ is odd. Then for all integers $m, k \ge 0$ and every real $x$,

$$\left| \frac{s_m((2k+1)x)}{(2k+1)^m} \right| \le \frac{1}{(2k+1)^m}.$$

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9OddClausenTerm_norm_bound`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-odd-clausen-term-norm-bound).

## Summability of the odd Clausen series for $m \ge 2$

Let $m \ge 2$ be an integer, and let
$s_m = \sin$ if $m$ is even and $s_m = \cos$ if $m$ is odd. Then for every real $x$ the series
$\sum_{k \ge 0} s_m((2k+1)x)/(2k+1)^m$ is summable.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9OddClausenTerm_summable_of_two_le`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-odd-clausen-term-summable-of-tw).

## The odd Clausen function vanishes at $m = 0$

For an integer $m \ge 0$ let $s_m = \sin$ if
$m$ is even and $s_m = \cos$ if $m$ is odd. The odd Clausen functions $O_m$, for integers
$m \ge 0$, are given by $O_1(x) = -\tfrac{1}{2} \log|\tan(x/2)|$, by
$O_m(x) = \sum_{k \ge 0} s_m((2k+1)x)/(2k+1)^m$ for $m \ge 2$, and at $m = 0$ by zero: for every
real $x$, $O_0(x) = 0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9OddClausen_zero`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-odd-clausen-zero).

## The odd Clausen function at $m = 1$

For an integer $m \ge 0$ let $s_m = \sin$ if $m$ is
even and $s_m = \cos$ if $m$ is odd. The odd Clausen functions $O_m$, for integers $m \ge 0$, are
given by $O_0 = 0$, by $O_m(x) = \sum_{k \ge 0} s_m((2k+1)x)/(2k+1)^m$ for $m \ge 2$, and at
$m = 1$ by a closed form: for every real $x$, $O_1(x) = -\tfrac{1}{2} \log|\tan(x/2)|$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9OddClausen_one`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-odd-clausen-one).

## The odd Clausen function as a series for $m \ge 2$

For an integer $m \ge 0$ let
$s_m = \sin$ if $m$ is even and $s_m = \cos$ if $m$ is odd. For real $x$, the odd Clausen
function $O_m(x)$ is $0$ if $m = 0$, is $-\tfrac{1}{2} \log|\tan(x/2)|$ if $m = 1$, and is
otherwise given by a series: for every integer $m \ge 2$ and every real $x$,
$O_m(x) = \sum_{k \ge 0} s_m((2k+1)x)/(2k+1)^m$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9OddClausen_of_two_le`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-odd-clausen-of-two-le).

## Odd-frequency part of a Clausen series for $m \ge 2$

Let $m \ge 2$ be an integer, and let
$s_m = \sin$ if $m$ is even and $s_m = \cos$ if $m$ is odd. For real $x$ write
$C_m(x) = \sum_{k \ge 1} s_m(kx)/k^m$ and $O_m(x) = \sum_{k \ge 0} s_m((2k+1)x)/(2k+1)^m$. Then
for every real $x$, $O_m(x) = C_m(x) - 2^{-m} C_m(2x)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9OddClausen_eq_clausen_sub_of_two_le`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-odd-clausen-eq-clausen-sub-of-t).

## Odd-frequency part of a Clausen function for $0 < |x| < \pi$

For real $x$ let
$C_1(x) = -\log|2 \sin(x/2)|$ and $O_1(x) = -\tfrac{1}{2} \log|\tan(x/2)|$. For an integer
$m \ge 2$, let $s_m = \sin$ if $m$ is even and $s_m = \cos$ if $m$ is odd, and let
$C_m(x) = \sum_{k \ge 1} s_m(kx)/k^m$ and $O_m(x) = \sum_{k \ge 0} s_m((2k+1)x)/(2k+1)^m$. Then
for every integer $m \ge 1$ and every real $x$ with $x \ne 0$ and $|x| < \pi$,
$O_m(x) = C_m(x) - 2^{-m} C_m(2x)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9OddClausen_eq_clausen_sub`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-odd-clausen-eq-clausen-sub).

## Odd reciprocal power sums in terms of $\zeta$

For every integer $m \ge 2$,

$$\sum_{k \ge 0} \frac{1}{(2k+1)^m} = \left(1 - \frac{1}{2^m}\right) \operatorname{Re} \zeta(m),$$

where $\zeta$ is the Riemann zeta function.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.chapter9ChiAtOne_eq_zeta`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#chapter9-chi-at-one-eq-zeta).

## Entry 14 of Chapter 9: the integral of $u^n / (2 \sin u)$

For an integer $m \ge 2$ write
$\lambda(m) = \sum_{k \ge 0} (2k+1)^{-m}$. For real $x$ let
$C_1(x) = -\tfrac{1}{2} \log|\tan(x/2)|$, and for an integer $m \ge 2$ let $s_m = \sin$ if $m$ is
even and $s_m = \cos$ if $m$ is odd, and let $C_m(x) = \sum_{k \ge 0} s_m((2k+1)x)/(2k+1)^m$. Let
$n \ge 1$ be an integer and $x$ a real number with $x \ne 0$ and $|x| < \pi$. Then
$u \mapsto u^n / (2 \sin u)$ is integrable on the interval between $0$ and $x$; the series
defining $\lambda(n+1)$ is summable; the partial sums $\sum_{k < N} \cos((2k+1)x)/(2k+1)$ tend
to $C_1(x)$ as $N \to \infty$; for every integer $m$ with $2 \le m \le n+1$ the series defining
$C_m(x)$ is summable; and

$$\int_0^x \frac{u^n}{2 \sin u}\,du = \cos\frac{n\pi}{2}\, n!\, \lambda(n+1) -
\sum_{j=0}^{n} (-1)^{j(j+1)/2} \frac{n!}{(n-j)!}\, x^{n-j}\, C_{j+1}(x).$$

The proof subtracts a scaled copy of Entry 13 at $2x$ from Entry 13 at $x$ and splits the zeta and
Clausen series into even and odd frequencies, following Berndt and Lewin, *Polylogarithms and
Associated Functions*, Chapter 4.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry14Xoversin.ramanujan_part1_ch9_entry14_xoversin`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean, line 703](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry14Xoversin.lean#L703). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#ramanujan-part1-ch9-entry14-xoversin).

## Entry 15 of Chapter 9: integrals of $u^n \cot u$ at $\pi/2 - x$

For an integer $k \ge 0$
and real $y$ write $F_k(y) = \int_{\pi/4}^{y} u^k \cot u \, du$. Let $n \ge 0$ be an integer. Then
for every integer $k$ with $0 \le k \le n$ and every real $y$ with $0 < y < \pi$, the function
$u \mapsto u^k \cot u$ is integrable on the interval between $\pi/4$ and $y$; and for every real
$x$ with $0 < x < \pi/2$,

$$2^n F_n(\pi/2 - x) = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \pi^{n-k}
\bigl(F_k(2x) - 2^k F_k(x)\bigr) - \sum_{k=0}^{n} (-1)^k \binom{n}{k} \pi^{n-k} F_k(\pi/2).$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry15Xcot.ramanujan_part1_ch9_entry15_xcot`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry15Xcot.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry15Xcot.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html#ramanujan-part1-ch9-entry15-xcot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Clausen functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/clausen-functions)
