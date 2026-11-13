---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6ShiftedDerivedSeriesTerm, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6DerivedSeriesConstant, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6ConvergentSumExtension, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6Entry6Term, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6PartialSum, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.hasSum_chapter6DerivedSeriesConstant, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6ConvergentSumExtension_sub_sub_one, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.summable_chapter6ShiftedDerivedSeriesTerm_natCast
statement: formalized
proof: formalized
---

# Ramanujan's extension of partial sums

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html).

## Terms of the shifted derivative series

For $f : \mathbb{R} \to \mathbb{R}$, natural numbers
$q$ and $k$, and $x \in \mathbb{R}$, the $k$-th term of the shifted series of $q$-th derivatives of
$f$ is $f^{(q)}(k + 1 + x)$, where $f^{(q)}$ is the $q$-th iterated derivative of $f$ and a
derivative that does not exist is taken to be $0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6ShiftedDerivedSeriesTerm`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#chapter6-shifted-derived-series-term).

## Ramanujan's derivative-series constants

For $f : \mathbb{R} \to \mathbb{R}$ and a natural
number $q$, the constant $c_q$ is $\sum_{k \ge 1} f^{(q)}(k)$, the sum of the values of the
$q$-th iterated derivative of $f$ at the positive integers, where a derivative that does not
exist is taken to be $0$ and a series that is not summable is given the value $0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6DerivedSeriesConstant`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#chapter6-derived-series-constant).

## Ramanujan's extension of partial sums

For $f : \mathbb{R} \to \mathbb{R}$, the extension of
the partial sums of $f$ to real arguments is the function
$F(x) = \sum_{k \ge 1} f(k) - \sum_{k \ge 1} f(k + x)$ on $\mathbb{R}$, where each series is an
unconditional sum and a series that is not summable is given the value $0$.

When $\sum_{k \ge 1} f(k)$ is summable, $F(m) = f(1) + \cdots + f(m)$ for every natural number
$m$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6ConvergentSumExtension`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#chapter6-convergent-sum-extension).

## Terms of the Taylor series in Entry 6

For $f : \mathbb{R} \to \mathbb{R}$,
$x \in \mathbb{R}$ and a natural number $j$, the $j$-th term is $-c_{j+1} x^{j+1} / (j+1)!$, where
$c_q = \sum_{k \ge 1} f^{(q)}(k)$ with $f^{(q)}$ the $q$-th iterated derivative of $f$; a
derivative that does not exist is taken to be $0$ and a series that is not summable is given the
value $0$.

Under the smoothness, summability and domination hypotheses of Entry 6, these are the
nonconstant terms of the Taylor series at $0$ of Ramanujan's extension
$F(x) = \sum_{k \ge 1} f(k) - \sum_{k \ge 1} f(k + x)$, whose constant term is $F(0) = 0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6Entry6Term`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#chapter6-entry6-term).

## Partial sums of a real function over the positive integers

For
$f : \mathbb{R} \to \mathbb{R}$ and a natural number $n$, the partial sum is
$f(1) + f(2) + \cdots + f(n)$, which is $0$ when $n = 0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6PartialSum`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#chapter6-partial-sum).

## The derivative-series constant is the sum of its series

Let
$f : \mathbb{R} \to \mathbb{R}$, let $q$ be a natural number, and let $f^{(q)}$ be the $q$-th
iterated derivative of $f$, where a derivative that does not exist is taken to be $0$. If the
family $\bigl(f^{(q)}(k + 1)\bigr)_{k \in \mathbb{N}}$ is summable, then its sum is the constant
$c_q = \sum_{k \ge 1} f^{(q)}(k)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.hasSum_chapter6DerivedSeriesConstant`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#has-sum-chapter6-derived-series-constant).

## Difference equation for Ramanujan's extension

Let $f : \mathbb{R} \to \mathbb{R}$ and let
$F(y) = \sum_{k \ge 1} f(k) - \sum_{k \ge 1} f(k + y)$, where a series that is not summable is
given the value $0$. If $x \in \mathbb{R}$ and the series $\sum_{k \ge 0} f(k + x)$ is summable,
then $F(x) - F(x - 1) = f(x)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6ConvergentSumExtension_sub_sub_one`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#chapter6-convergent-sum-extension-sub-su).

## Tails of the shifted series of derivatives converge

Let $f : \mathbb{R} \to \mathbb{R}$
and $q \in \mathbb{N}$, and write $f^{(q)}$ for the $q$-th iterated derivative of $f$, where a
derivative that does not exist is taken to be $0$. If the series
$\sum_{k \ge 0} f^{(q)}(k + 1)$ converges absolutely, then for every $m \in \mathbb{N}$ the series
$\sum_{k \ge 0} f^{(q)}(k + 1 + m)$ converges absolutely.

The second series is the $m$-th tail of the first.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.summable_chapter6ShiftedDerivedSeriesTerm_natCast`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#summable-chapter6-shifted-derived-series).

## Ramanujan's extension agrees with the partial sums at natural numbers

Let
$f : \mathbb{R} \to \mathbb{R}$ and let $F(x) = \sum_{k \ge 1} f(k) - \sum_{k \ge 1} f(k + x)$,
where a series that is not summable is given the value $0$. If the series
$\sum_{k \ge 1} f(k)$ is summable, then $F(m) = f(1) + f(2) + \cdots + f(m)$ for every natural
number $m$ (for $m = 0$ the right side is the empty sum $0$).

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.chapter6ConvergentSumExtension_natCast`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#chapter6-convergent-sum-extension-nat-ca).

## Derivatives of Ramanujan's extension at the origin

Let $f : \mathbb{R} \to \mathbb{R}$ be
infinitely differentiable and let $\rho > 0$. Write $c_q = \sum_{k \ge 1} f^{(q)}(k)$ and
$F(x) = c_0 - \sum_{k \ge 1} f(k + x)$, where a series that is not summable is given the value
$0$. Suppose that the series $\sum_{k \ge 1} f^{(q)}(k)$ is summable for every $q \ge 0$, and
that for every $q \ge 1$ there is a summable sequence $(b_k)_{k \ge 0}$ with
$|f^{(q)}(k + 1 + x)| \le b_k$ for all $x \in [-\rho, \rho]$ and all $k \ge 0$. Then
$F^{(n)}(0) = -c_n$ for every natural number $n \ge 1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.iteratedDeriv_chapter6ConvergentSumExtension_apply_zero`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#iterated-deriv-chapter6-convergent-sum-e).

## Taylor expansion of Ramanujan's extension at the origin

Let $f : \mathbb{R} \to \mathbb{R}$
be infinitely differentiable and let $\rho > 0$. Write $c_q = \sum_{k \ge 1} f^{(q)}(k)$ and
$F(x) = c_0 - \sum_{k \ge 1} f(k + x)$, where a series that is not summable is given the value
$0$. Suppose that the series $\sum_{k \ge 1} f^{(q)}(k)$ is summable for every $q \ge 0$, that
for every $q \ge 1$ there is a summable sequence $(b_k)_{k \ge 0}$ with
$|f^{(q)}(k + 1 + x)| \le b_k$ for all $x \in [-\rho, \rho]$ and all $k \ge 0$, and that $F$ is
analytic at $0$. Then there is $r$ with $0 < r \le \rho$ such that for every real $x$ with
$|x| < r$ the series $\sum_{j \ge 0} -c_{j+1} x^{j+1} / (j+1)!$ is summable with sum $F(x)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.exists_hasSum_chapter6Entry6Term`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#exists-has-sum-chapter6-entry6-term).

## Ramanujan's extension of the partial sums of a smooth function

Let
$f : \mathbb{R} \to \mathbb{R}$ be infinitely differentiable and let $\rho > 0$. Suppose that for
every $q \in \mathbb{N}$ and every $x \in \mathbb{R}$ the series
$\sum_{k \ge 0} f^{(q)}(k + 1 + x)$ converges absolutely, and that for every $q \in \mathbb{N}$
there is a summable sequence $(b_k)_{k \ge 0}$ with $|f^{(q)}(k + 1 + x)| \le b_k$ for all
$k \in \mathbb{N}$ and all $x \in [-\rho, \rho]$. Put $c_q = \sum_{k \ge 0} f^{(q)}(k + 1)$ and
$F(x) = c_0 - \sum_{k \ge 0} f(k + 1 + x)$, and suppose that $F$ is analytic at $0$. Then
(i) for every $n \in \mathbb{N}$ the series $\sum_{k \ge 0} f^{(n)}(k + 1)$ converges absolutely
with sum $c_n$; (ii) $F(0) = 0$; (iii) $F(x) - F(x - 1) = f(x)$ for every $x \in \mathbb{R}$;
(iv) $F(m) = f(1) + f(2) + \dots + f(m)$ for every $m \in \mathbb{N}$, the empty sum being $0$;
(v) $F^{(n)}(0) = -c_n$ for every integer $n \ge 1$; and (vi) there is $r$ with $0 < r \le \rho$
such that for every real $x$ with $|x| < r$ the series
$\sum_{j \ge 0} -c_{j+1} x^{j+1} / (j + 1)!$ converges absolutely with sum $F(x)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 6.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry6Harmonic.ramanujan_part1_ch6_entry6_harmonic`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry6Harmonic.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html#ramanujan-part1-ch6-entry6-harmonic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan's extension of partial sums](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/ramanujan-s-extension-of-partial-sums)
