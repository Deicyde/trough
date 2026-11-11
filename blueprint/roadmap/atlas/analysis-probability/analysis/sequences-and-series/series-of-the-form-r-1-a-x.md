---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry13Ramanujanfactorial.ramanujan_part1_ch6_entry13_ramanujanfactorial, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry16FiniteSum.ramanujan_part1_ch6_entry16_finite_sum_general, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry16FiniteSum.ramanujan_part1_ch6_entry16_finite_sum, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry16InfiniteSum.ramanujan_part1_ch6_entry16_infinite_sum, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry17Stirlingcoeffs.ramanujan_part1_ch6_entry17_stirlingcoeffs
statement: formalized
proof: formalized
---

# Series of the form Σ rᵏ/(1 − a xᵏ)

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-of-the-form-r-1-a-x/index.html).

## Ramanujan's transformation of the alternating series of 1/(x^k - 1)

For every real number
$x$ with $|x| > 1$, we have $x^k - 1 \ne 0$ and $x^{k^2}(x^{2k} - 1) \ne 0$ for every integer
$k \ge 1$, the series $\sum_{k \ge 1} (-1)^{k+1}/(x^k - 1)$ and
$\sum_{k \ge 1} (-1)^{k+1}(x^{2k} + 1)/(x^{k^2}(x^{2k} - 1))$ are summable, and
$\sum_{k=1}^{\infty} (-1)^{k+1}/(x^k - 1) =
\sum_{k=1}^{\infty} (-1)^{k+1}(x^{2k} + 1)/(x^{k^2}(x^{2k} - 1))$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 6.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry13Ramanujanfactorial.ramanujan_part1_ch6_entry13_ramanujanfactorial`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry13Ramanujanfactorial.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry13Ramanujanfactorial.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-of-the-form-r-1-a-x/index.html#ramanujan-part1-ch6-entry13-ramanujanfac).

## A finite identity for $\sum_k r^k/(1-ax^k)$ over a field

Let $K$ be a field, let
$a, r, x \in K$ and let $n \ge 0$ be an integer. Suppose that $1 - a x^k \ne 0$ and
$1 - r x^{k-1} \ne 0$ for every integer $k$ with $1 \le k \le n$. Then
$\sum_{k=1}^{n} \frac{r^k}{1 - a x^k} = \sum_{k=1}^{n} \frac{(a r x^k)^k}{1 - a x^k} +
\sum_{k=1}^{n} \frac{a^{k-1} \left( (r x^{k-1})^k - (r x^{k-1})^{n+1} \right)}{1 - r x^{k-1}}$.
For $n = 0$ all three sums are empty.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry16FiniteSum.ramanujan_part1_ch6_entry16_finite_sum_general`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry16FiniteSum.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry16FiniteSum.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-of-the-form-r-1-a-x/index.html#ramanujan-part1-ch6-entry16-finite-sum-g).

## Ramanujan's finite identity for $\sum_k r^k/(1-ax^k)$

Let $a, r, x$ be real numbers
and let $n$ be a positive integer. Suppose that $1 - a x^k \ne 0$ and $1 - r x^{k-1} \ne 0$ for
every integer $k$ with $1 \le k \le n$. Then
$\sum_{k=1}^{n} \frac{r^k}{1 - a x^k} = \sum_{k=1}^{n} \frac{(a r x^k)^k}{1 - a x^k} +
\sum_{k=1}^{n} \frac{a^{k-1} \left( (r x^{k-1})^k - (r x^{k-1})^{n+1} \right)}{1 - r x^{k-1}}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 6. It follows from `ramanujan_part1_ch6_entry16_finite_sum_general` with `K := ℝ`; the hypothesis `hn` is unused and keeps the source's shape.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry16FiniteSum.ramanujan_part1_ch6_entry16_finite_sum`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry16FiniteSum.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry16FiniteSum.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-of-the-form-r-1-a-x/index.html#ramanujan-part1-ch6-entry16-finite-sum).

## Ramanujan's infinite identity for $\sum_k r^k/(1-ax^k)$

Let $a, r, x$ be complex
numbers with $|r| < 1$ and $|x| \le 1$ such that $1 - a x^k \ne 0$ for every integer $k \ge 1$,
and such that, if $|x| = 1$, then $|a r| < 1$ and there is a real $\delta > 0$ with
$|1 - a x^k| \ge \delta$ for every $k \ge 1$. Then $1 - r x^{k-1} \ne 0$ for every $k \ge 1$, the
three series $\sum_{k=1}^{\infty} \frac{r^k}{1 - a x^k}$,
$\sum_{k=1}^{\infty} \frac{(a r x^k)^k}{1 - a x^k}$ and
$\sum_{k=1}^{\infty} \frac{a^{k-1} r^k x^{(k-1)k}}{1 - r x^{k-1}}$ are summable, and the first
equals the sum of the other two.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 6. The infinite form of `Entry16FiniteSum.ramanujan_part1_ch6_entry16_finite_sum`.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry16InfiniteSum.ramanujan_part1_ch6_entry16_infinite_sum`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry16InfiniteSum.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry16InfiniteSum.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-of-the-form-r-1-a-x/index.html#ramanujan-part1-ch6-entry16-infinite-sum).

## Ramanujan's identity for $\sum_k (a + kb) \nu^k / (1 - m x^k)$

Let $a, b, m, \nu, x$ be
real numbers with $|x| \le 1$, $|\nu| < 1$ and $m \ne 0$, such that $|m \nu| < 1$ if $|x| = 1$,
and such that $1 - m x^k \ne 0$ for every integer $k \ge 0$ (here $x^0 = 1$). Then
$1 - \nu x^k \ne 0$ for every $k \ge 0$, the series
$L = \sum_{k=0}^{\infty} \frac{(a + kb) \, \nu^k}{1 - m x^k}$,
$F = \sum_{k=0}^{\infty} \frac{(a + kb) (1 - m \nu x^{2k}) (m \nu x^k)^k}{(1 - m x^k)(1 - \nu x^k)}$
and $G = \sum_{k=0}^{\infty} \frac{(m \nu x^k)^{k+1}}{(1 - \nu x^k)^2}$ are summable, and
$L = F + \frac{b}{m} G$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 6.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry17Stirlingcoeffs.ramanujan_part1_ch6_entry17_stirlingcoeffs`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry17Stirlingcoeffs.lean, line 842](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry17Stirlingcoeffs.lean#L842). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-of-the-form-r-1-a-x/index.html#ramanujan-part1-ch6-entry17-stirlingcoef).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Series of the form Σ rᵏ/(1 − a xᵏ)](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-of-the-form-r-1-a-x/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/series-of-the-form-r-1-a-x)
