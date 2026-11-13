---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry1Corollary1BinomialSeries.ramanujan_part1_ch3_entry1_corollary1_binomial_series_general, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry1Corollary1BinomialSeries.ramanujan_part1_ch3_entry1_corollary1_binomial_series, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry1SeriesTransformation.ramanujan_part1_ch3_entry1_series_transformation_general, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry1SeriesTransformation.ramanujan_part1_ch3_entry1_series_transformation
statement: formalized
proof: formalized
---

# Series transformations via Taylor shifts

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/series-transformations-via-taylor-shifts/index.html).

## Ramanujan's binomial series transformation without the radius hypothesis

Let $n$ and $x$
be complex numbers with $|x| < 1$, write $(n)_k = n(n-1)\cdots(n-k+1)$ for the falling factorial
(with $(n)_0 = 1$), and let $Q_0, Q_1, Q_2, \ldots$ be complex numbers such that the double series

$$\sum_{j, m \ge 0} \frac{Q_j\, (n)_{j+m}\, x^{j+m}}{m!}$$

is absolutely summable. Then the series

$$\sum_{k=0}^{\infty} \Bigl(\sum_{j=0}^{k} \frac{Q_j}{(k-j)!}\Bigr) (n)_k\, x^k$$

and

$$\sum_{k=0}^{\infty} Q_k\, (n)_k\, x^k\, (1 + x)^{n-k}$$

converge unconditionally to the same sum, where $(1 + x)^{n-k} = e^{(n-k) \log(1+x)}$ with the
principal branch of the logarithm.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry1Corollary1BinomialSeries.ramanujan_part1_ch3_entry1_corollary1_binomial_series_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry1Corollary1BinomialSeries.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry1Corollary1BinomialSeries.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/series-transformations-via-taylor-shifts/index.html#ramanujan-part1-ch3-entry1-corollary1-bi).

## Ramanujan's binomial series transformation (Chapter 3, Entry 1, Corollary 1)

Let $n$ and
$x$ be complex numbers with $|x| < 1$, write $(n)_k = n(n-1)\cdots(n-k+1)$ for the falling
factorial (with $(n)_0 = 1$), and let $Q_0, Q_1, Q_2, \ldots$ be complex numbers such that, for
some $R > 0$, the power series $\sum_k Q_k z^k$ converges absolutely for every complex $z$ with
$|z| < R$. Suppose that the double series

$$\sum_{j, m \ge 0} \frac{Q_j\, (n)_{j+m}\, x^{j+m}}{m!}$$

is absolutely summable. Then the series

$$\sum_{k=0}^{\infty} \Bigl(\sum_{j=0}^{k} \frac{Q_j}{(k-j)!}\Bigr) (n)_k\, x^k$$

and

$$\sum_{k=0}^{\infty} Q_k\, (n)_k\, x^k\, (1 + x)^{n-k}$$

converge unconditionally to the same sum, where $(1 + x)^{n-k} = e^{(n-k) \log(1+x)}$ with the
principal branch of the logarithm.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 1, Corollary 1, printed p. 45 / PDF p. 55.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry1Corollary1BinomialSeries.ramanujan_part1_ch3_entry1_corollary1_binomial_series`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry1Corollary1BinomialSeries.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry1Corollary1BinomialSeries.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/series-transformations-via-taylor-shifts/index.html#ramanujan-part1-ch3-entry1-corollary1-bi-2).

## Ramanujan's series transformation without the radius hypothesis

Let $R_1 > 1$, let
$f : \mathbb{C} \to \mathbb{C}$ be analytic on the open disc $|z| < R_1$, and let
$Q_0, Q_1, Q_2, \ldots$ be complex numbers such that the double series

$$\sum_{j, m \ge 0} \frac{Q_j\, f^{(j+m)}(0)}{m!}$$

is absolutely summable. Then the series

$$\sum_{n=0}^{\infty} \Bigl(\sum_{j=0}^{n} \frac{Q_j}{(n-j)!}\Bigr) f^{(n)}(0)$$

and

$$\sum_{n=0}^{\infty} Q_n\, f^{(n)}(1)$$

converge unconditionally to the same sum.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry1SeriesTransformation.ramanujan_part1_ch3_entry1_series_transformation_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry1SeriesTransformation.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry1SeriesTransformation.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/series-transformations-via-taylor-shifts/index.html#ramanujan-part1-ch3-entry1-series-transf).

## Ramanujan's series transformation (Chapter 3, Entry 1)

Let $R_1 > 1$, let
$f : \mathbb{C} \to \mathbb{C}$ be analytic on the open disc $|z| < R_1$, and let
$Q_0, Q_1, Q_2, \ldots$ be complex numbers such that, for some $R_2 > 0$, the power series
$\sum_n Q_n z^n$ converges absolutely for every complex $z$ with $|z| < R_2$. Suppose that the
double series

$$\sum_{j, m \ge 0} \frac{Q_j\, f^{(j+m)}(0)}{m!}$$

is absolutely summable. Then the series

$$\sum_{n=0}^{\infty} \Bigl(\sum_{j=0}^{n} \frac{Q_j}{(n-j)!}\Bigr) f^{(n)}(0)$$

and

$$\sum_{n=0}^{\infty} Q_n\, f^{(n)}(1)$$

converge unconditionally to the same sum.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 1, printed p. 45 / PDF p. 55.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry1SeriesTransformation.ramanujan_part1_ch3_entry1_series_transformation`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry1SeriesTransformation.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry1SeriesTransformation.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/series-transformations-via-taylor-shifts/index.html#ramanujan-part1-ch3-entry1-series-transf-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Series transformations via Taylor shifts](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/series-transformations-via-taylor-shifts/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/power-series/series-transformations-via-taylor-shifts)
