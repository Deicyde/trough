---
declaration: section
origin: cited
lean: MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount, MathlibExt.Probability.DiversityStatisticsWanted.shannonCount, MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount_le, MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount_ge_triangular, MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount_ge, MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount_asymp, MathlibExt.Probability.DiversityStatisticsWanted.shannonCount_le, MathlibExt.Probability.DiversityStatisticsWanted.shannonCount_superpolynomial
statement: formalized
---

# Number of values of diversity indices

8 results, 2 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html).

## Number of values of the Gini–Simpson index

For a natural number $N$, $\gamma(N)$ is the
number of distinct values of $a_1^2 + \dots + a_k^2$ over all finite sequences $(a_1, \dots, a_k)$
of natural numbers with $a_1 + \dots + a_k = N$.

For $N \ge 1$, the Gini–Simpson index of a sample of size $N$ with type counts $a_1, \dots, a_k$ is
$1 - \sum_i (a_i / N)^2$, so $\gamma(N)$ is the number of possible values of the Gini–Simpson index
across all samples of size $N$.

Formalized by `MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount`, a definition declared in [WantedExt/Probability/DiversityStatisticsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/DiversityStatisticsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html#gini-simpson-count).

## Number of values of the Shannon index

For a natural number $N$, $\sigma(N)$ is the number
of distinct real numbers $-\sum_{i=1}^{k} (a_i / N) \log (a_i / N)$ over all finite sequences $(a_1,
\dots, a_k)$ of natural numbers with $a_1 + \dots + a_k = N$, where a term with $a_i = 0$ counts as
$0$ (the convention $0 \log 0 = 0$).

For $N \ge 1$, this is the number of possible values of the Shannon index across all samples of size
$N$.

Formalized by `MathlibExt.Probability.DiversityStatisticsWanted.shannonCount`, a definition declared in [WantedExt/Probability/DiversityStatisticsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/DiversityStatisticsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html#shannon-count).

## Upper bound on the number of Gini–Simpson values

Let $\gamma(N)$ be the number of distinct
values of $a_1^2 + \dots + a_k^2$ over all finite sequences $(a_1, \dots, a_k)$ of natural numbers
with $a_1 + \dots + a_k = N$ (for $N \ge 1$, the number of possible values of the Gini–Simpson index
across samples of size $N$). Then for every natural number $N$,

$$\gamma(N) \le \tfrac{1}{2} N^2 - \tfrac{1}{2} N + 1.$$

## Sources

- Bradley K. Moon and Noah A. Rosenberg, "Integer Sequences for Diversity Statistics", Proposition 4.

Stated but not proved: `MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount_le` is written with `theorem_wanted` in [WantedExt/Probability/DiversityStatisticsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/DiversityStatisticsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html#gini-simpson-count-le).

## Triangular-number lower bound on the number of Gini–Simpson values

Let $\gamma(N)$ be the
number of distinct values of $a_1^2 + \dots + a_k^2$ over all finite sequences $(a_1, \dots, a_k)$
of natural numbers with $a_1 + \dots + a_k = N$ (for $N \ge 1$, the number of possible values of the
Gini–Simpson index across samples of size $N$). Let $m$ and $r$ be natural numbers with $r \le m$,
and let $N = \binom{m+1}{2} + r$. Then

$$\tfrac{1}{3} m (m^2 + 3r - 1) + 1 \le \gamma(N).$$

## Sources

- Bradley K. Moon and Noah A. Rosenberg, "Integer Sequences for Diversity Statistics", Proposition 5.

Stated but not proved: `MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount_ge_triangular` is written with `theorem_wanted` in [WantedExt/Probability/DiversityStatisticsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/DiversityStatisticsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html#gini-simpson-count-ge-triangular).

## Quadratic lower bound on the number of Gini–Simpson values

Let $\gamma(N)$ be the number of
distinct values of $a_1^2 + \dots + a_k^2$ over all finite sequences $(a_1, \dots, a_k)$ of natural
numbers with $a_1 + \dots + a_k = N$ (for $N \ge 1$, the number of possible values of the
Gini–Simpson index across samples of size $N$). Then for every natural number $N$,

$$\tfrac{1}{2} \left( \lfloor N^2 / 5 \rfloor - N \right) \le \gamma(N).$$

## Sources

- Bradley K. Moon and Noah A. Rosenberg, "Integer Sequences for Diversity Statistics", Proposition 6.

Stated but not proved: `MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount_ge` is written with `theorem_wanted` in [WantedExt/Probability/DiversityStatisticsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/DiversityStatisticsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html#gini-simpson-count-ge).

## Asymptotics of the number of Gini–Simpson values

Let $\gamma(N)$ be the number of distinct
values of $a_1^2 + \dots + a_k^2$ over all finite sequences $(a_1, \dots, a_k)$ of natural numbers
with $a_1 + \dots + a_k = N$ (for $N \ge 1$, the number of possible values of the Gini–Simpson index
across samples of size $N$). Then $\gamma(N) / N^2 \to 1/2$ as $N \to \infty$, that is, $\gamma(N)
\sim \tfrac{1}{2} N^2$.

## Sources

- Bradley K. Moon and Noah A. Rosenberg, "Integer Sequences for Diversity Statistics", Proposition 7.

Stated but not proved: `MathlibExt.Probability.DiversityStatisticsWanted.giniSimpsonCount_asymp` is written with `theorem_wanted` in [WantedExt/Probability/DiversityStatisticsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/DiversityStatisticsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html#gini-simpson-count-asymp).

## Upper bound on the number of Shannon values

Let $\sigma(N)$ be the number of distinct real
numbers $-\sum_{i=1}^{k} (a_i / N) \log (a_i / N)$ over all finite sequences $(a_1, \dots, a_k)$ of
natural numbers with $a_1 + \dots + a_k = N$, where a term with $a_i = 0$ counts as $0$ (for $N \ge
1$, the number of possible values of the Shannon index across samples of size $N$). Then for every
natural number $N \ge 1$,

$$\sigma(N) \le \exp\left(\pi \sqrt{2/3} \sqrt{N}\right).$$

## Sources

- Bradley K. Moon and Noah A. Rosenberg, "Integer Sequences for Diversity Statistics", Proposition 8.

Stated but not proved: `MathlibExt.Probability.DiversityStatisticsWanted.shannonCount_le` is written with `theorem_wanted` in [WantedExt/Probability/DiversityStatisticsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/DiversityStatisticsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html#shannon-count-le).

## The number of Shannon values grows faster than every polynomial

Let $\sigma(N)$ be the
number of distinct real numbers $-\sum_{i=1}^{k} (a_i / N) \log (a_i / N)$ over all finite sequences
$(a_1, \dots, a_k)$ of natural numbers with $a_1 + \dots + a_k = N$, where a term with $a_i = 0$
counts as $0$ (for $N \ge 1$, the number of possible values of the Shannon index across samples of
size $N$). Then for every nonzero polynomial $q$ with real coefficients, $\sigma(N) / |q(N)| \to
\infty$ as $N \to \infty$.

## Sources

- Bradley K. Moon and Noah A. Rosenberg, "Integer Sequences for Diversity Statistics", Theorem 9.

Stated but not proved: `MathlibExt.Probability.DiversityStatisticsWanted.shannonCount_superpolynomial` is written with `theorem_wanted` in [WantedExt/Probability/DiversityStatisticsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/DiversityStatisticsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html#shannon-count-superpolynomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Number of values of diversity indices](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/number-of-values-of-diversity-indices)
