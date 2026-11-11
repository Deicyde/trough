---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook4Wanted.fairCoinMeasure, MathlibExt.Analysis.ScottishBook4Wanted.schreierCesaroSubsequences
statement: formalized
---

# Cesàro means of random subsequences

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/ces-ro-means-of-random-subsequences/index.html).

## Fair coin measure

The fair coin measure is the measure on the Booleans
$\{\mathrm{true}, \mathrm{false}\}$ that gives mass $1/2$ to each of $\mathrm{true}$ and
$\mathrm{false}$, that is,
$\frac{1}{2}\delta_{\mathrm{true}} + \frac{1}{2}\delta_{\mathrm{false}}$.

Formalized by `MathlibExt.Analysis.ScottishBook4Wanted.fairCoinMeasure`, a definition declared in [WantedExt/Analysis/ScottishBook4Wanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook4Wanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/ces-ro-means-of-random-subsequences/index.html#fair-coin-measure).

## Schreier's theorem on Cesàro means of random subsequences

Let $(a_n)_{n \ge 0}$ be a
bounded sequence of real numbers whose Cesàro means $\frac{1}{n} \sum_{i < n} a_i$ converge
to a real number $S$ as $n \to \infty$. Give the space of Boolean sequences
$\omega = (\omega_n)_{n \ge 0}$ the infinite product of fair coin measures. For such $\omega$
let $n_0 < n_1 < \cdots$ list, in increasing order, the indices $n$ with
$\omega_n = \mathrm{true}$, with $n_k = 0$ whenever there are at most $k$ such indices. Then
for almost every $\omega$ the Cesàro means $\frac{1}{N} \sum_{k < N} a_{n_k}$ of the
subsequence $(a_{n_k})$ converge to $S$ as $N \to \infty$.

Identifying a subset of $\mathbb{N}$ with its indicator sequence $\omega$, this says that
almost every subsequence of $(a_n)$ has Cesàro means converging to $S$.

## Sources

- J. Schreier, Problem 4 of the Scottish Book, stated as a theorem in the Scottish Book typescript.

Stated but not proved: `MathlibExt.Analysis.ScottishBook4Wanted.schreierCesaroSubsequences` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook4Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook4Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/ces-ro-means-of-random-subsequences/index.html#schreier-cesaro-subsequences).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cesàro means of random subsequences](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/ces-ro-means-of-random-subsequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/summability/ces-ro-means-of-random-subsequences)
