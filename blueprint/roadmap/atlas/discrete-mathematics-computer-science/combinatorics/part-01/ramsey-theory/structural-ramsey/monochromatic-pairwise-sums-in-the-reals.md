---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MonochromaticPairSumsRealsErdosProblem965Wanted.alephOneMonochromaticPairSums, MathlibExt.Combinatorics.MonochromaticPairSumsRealsErdosProblem965Wanted.alephOneMonochromaticPairSums_refuted
statement: formalized
---

# Monochromatic pairwise sums in the reals

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-pairwise-sums-in-the-reals/index.html).

## Erdős Problem 965

The statement that for every colouring of the real numbers with two
colours there is a set $A \subseteq \mathbb{R}$ of cardinality $\aleph_1$ such that all sums
$a + b$ with $a, b \in A$ and $a \ne b$ have the same colour.

Formalized by `MathlibExt.Combinatorics.MonochromaticPairSumsRealsErdosProblem965Wanted.alephOneMonochromaticPairSums`, a definition declared in [WantedExt/Combinatorics/MonochromaticPairSumsRealsErdosProblem965Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MonochromaticPairSumsRealsErdosProblem965Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-pairwise-sums-in-the-reals/index.html#aleph-one-monochromatic-pair-sums).

## Erdős Problem 965 is false

It is not the case that for every colouring of the real
numbers with two colours there is a set $A \subseteq \mathbb{R}$ of cardinality $\aleph_1$ such
that all sums $a + b$ with $a, b \in A$ and $a \ne b$ have the same colour.

Komjáth, and independently Soukup and Weiss, constructed in ZFC a $2$-colouring of $\mathbb{R}$
such that for every uncountable $A \subseteq \mathbb{R}$, in particular every $A$ of cardinality
$\aleph_1$, the sums $a + b$ of distinct $a, b \in A$ take both colours.

## Sources

- T. F. Bloom, Erdős Problems, Problem #965, https://www.erdosproblems.com/965 (status DISPROVED (LEAN)); resolution: P. Komjáth, A certain 2-coloring of the reals, Real Anal. Exchange (2016), 227-231, erdosproblems.com/965: Komjáth, and independently Soukup and Weiss, proved without the continuum hypothesis that some 2-colouring of ℝ makes the sums of k distinct elements of any uncountable A ⊆ ℝ non-monochromatic, for every k ≥ 1 (the case k = 2 disproves the question), https://www.erdosproblems.com/965.

Stated but not proved: `MathlibExt.Combinatorics.MonochromaticPairSumsRealsErdosProblem965Wanted.alephOneMonochromaticPairSums_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticPairSumsRealsErdosProblem965Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MonochromaticPairSumsRealsErdosProblem965Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-pairwise-sums-in-the-reals/index.html#aleph-one-monochromatic-pair-sums-refute).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic pairwise sums in the reals](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-pairwise-sums-in-the-reals/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-pairwise-sums-in-the-reals)
