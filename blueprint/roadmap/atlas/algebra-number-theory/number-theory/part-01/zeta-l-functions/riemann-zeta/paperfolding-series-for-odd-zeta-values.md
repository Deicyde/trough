---
declaration: section
origin: cited
lean: MetaMathlibExt.hurwitzZeta_three_quarters_two_mul_add_one, MetaMathlibExt.riemannZeta_two_mul_add_one_sub_eq_tsum_paperfolding_thueMorse, MetaMathlibExt.tsum_paperfolding_two_mul_add_one, MetaMathlibExt.tsum_neg_one_pow_paperfolding
statement: formalized
---

# Paperfolding series for odd zeta values

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/paperfolding-series-for-odd-zeta-values/index.html).

## Hurwitz zeta at $3/4$ and odd arguments

For every integer $k \ge 1$,

$$
\zeta(2k+1, \tfrac34) = -\frac{2^{2k-1} \pi^{2k+1} |E_{2k}|}{(2k)!} +
2^{2k} (2^{2k+1} - 1) \zeta(2k+1),
$$

where $\zeta(s, a)$ is the Hurwitz zeta function (for $\operatorname{Re} s > 1$,
$\zeta(s, a) = \sum_{n \ge 0} (n + a)^{-s}$), $\zeta(s)$ is the Riemann zeta function and $E_{2k}$
is the even-index Euler number.

The even-index Euler numbers are defined by a binomial recurrence equivalent to the generating
function $1 / \cosh t = \sum_n E_n t^n / n!$. The source writes $k \in \mathbb{N}$; $k = 0$ is
excluded since $s = 1$ is the pole of both zeta functions.

## Sources

- László Tóth, *Evaluating ζ(s) at Odd Positive Integers Using Automatic Dirichlet Series*, Journal of Integer Sequences 28 (2025), Article 25.4.4, Lemma 3 (`jis-2025-25.4.4-lem-3`).

Stated but not proved: `MetaMathlibExt.hurwitzZeta_three_quarters_two_mul_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/TothOddZetaWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TothOddZetaWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/paperfolding-series-for-odd-zeta-values/index.html#hurwitz-zeta-three-quarters-two-mul-add).

## Tóth's paperfolding and Thue–Morse series for $\zeta(2k+1)$

Let $(f_n)_{n \ge 0}$ be the
regular paperfolding sequence and $(t_n)_{n \ge 0}$ the Thue–Morse sequence, both indexed from
$0$, and let $E_{2k}$ be the even-index Euler number. For every integer $k \ge 1$,

$$
\zeta(2k+1) - \frac{2^{2k-1} |E_{2k}| \pi^{2k+1}}{(2k)!} =
\sum_{n \ge 0} \frac{N_k(n)}{(n+1)^{2k+1}},
$$

where

$$
N_k(n) = (2^{4k+1} - 2^{2k})(2 f_n - 1) +
2^{-(2k+1)} \bigl((2^{2k+1} + 1) t_n + (2^{2k+1} - 1) t_{n+1}\bigr).
$$

In the source's indexing $b_n = f_{n-1}$ for $n \ge 1$ (so $b_{2n} = b_n$, $b_{4n+1} = 0$ and
$b_{4n+3} = 1$), the right side is $\sum_{n \ge 1} N(n;k)/n^{2k+1}$ with
$N(n;k) = (2^{4k+1} - 2^{2k})(2b_n - 1) +
2^{-(2k+1)}((2^{2k+1} + 1) t_{n-1} + (2^{2k+1} - 1) t_n)$.

## Sources

- László Tóth, *Evaluating ζ(s) at Odd Positive Integers Using Automatic Dirichlet Series*, Journal of Integer Sequences 28 (2025), Article 25.4.4, Theorem 2 (`jis-2025-25.4.4-thm-2`); `bₙ`, `tₙ` read from arXiv:2508.04151v1.

Stated but not proved: `MetaMathlibExt.riemannZeta_two_mul_add_one_sub_eq_tsum_paperfolding_thueMorse` is written with `theorem_wanted` in [WantedExt/NumberTheory/TothOddZetaWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TothOddZetaWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/paperfolding-series-for-odd-zeta-values/index.html#riemann-zeta-two-mul-add-one-sub-eq-tsum).

## A paperfolding Dirichlet series at odd integers

Let $(f_n)_{n \ge 0}$ be the regular
paperfolding sequence, indexed from $0$, and let $E_{2k}$ be the even-index Euler number. For
every integer $k \ge 1$,

$$
(2^{4k+1} - 2^{2k}) \sum_{n \ge 0} \frac{2 f_n - 1}{(n+1)^{2k+1}}
= -\frac{2^{2k-1} \pi^{2k+1} |E_{2k}|}{(2k)!}.
$$

In the source's indexing $b_n = f_{n-1}$ for $n \ge 1$, the sum is
$\sum_{n \ge 1} (2 b_n - 1)/n^{2k+1}$.

## Sources

- László Tóth, *Evaluating ζ(s) at Odd Positive Integers Using Automatic Dirichlet Series*, Journal of Integer Sequences 28 (2025), Article 25.4.4, Lemma 5 (`jis-2025-25.4.4-lem-5`); `bₙ` read from arXiv:2508.04151v1.

Stated but not proved: `MetaMathlibExt.tsum_paperfolding_two_mul_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/TothOddZetaWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TothOddZetaWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/paperfolding-series-for-odd-zeta-values/index.html#tsum-paperfolding-two-mul-add-one).

## The $\pm 1$ paperfolding Dirichlet series at odd integers

Let $(f_n)_{n \ge 0}$ be the
regular paperfolding sequence, indexed from $0$, and let $E_{2k}$ be the even-index Euler number.
For every integer $k \ge 1$,

$$
\sum_{n \ge 0} \frac{(-1)^{f_n}}{(n+1)^{2k+1}} =
\frac{\pi^{2k+1} |E_{2k}|}{(2^{2k+2} - 2)(2k)!}.
$$

In the source's indexing $b_n = f_{n-1}$ for $n \ge 1$, this is the sum over $n \ge 1$ of
$(-1)^{b_n}/n^{2k+1}$. The source prints the sum as $\sum_{n \ge 0} (-1)^{b_n}/(n+1)^{2k+1}$,
which uses $b_0$, left undetermined by the recurrence $b_{2n} = b_n$; its proof (from Lemma 5)
gives the sum over $n \ge 1$ stated here.

## Sources

- László Tóth, *Evaluating ζ(s) at Odd Positive Integers Using Automatic Dirichlet Series*, Journal of Integer Sequences 28 (2025), Article 25.4.4, Corollary 7 (`jis-2025-25.4.4-cor-7`); `bₙ` read from arXiv:2508.04151v1.

Stated but not proved: `MetaMathlibExt.tsum_neg_one_pow_paperfolding` is written with `theorem_wanted` in [WantedExt/NumberTheory/TothOddZetaWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TothOddZetaWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/paperfolding-series-for-odd-zeta-values/index.html#tsum-neg-one-pow-paperfolding).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Paperfolding series for odd zeta values](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/paperfolding-series-for-odd-zeta-values/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/paperfolding-series-for-odd-zeta-values)
