---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Distribution.CauchyPrincipalValueWanted.cauchyPrincipalValue_exists, MathlibExt.Analysis.Distribution.TestFunctionPartitionOfUnityWanted.testFunction_partitionOfUnity, MathlibExt.Analysis.Distribution.TemperedExamplesWanted.diracComb_toTemperedDistribution
statement: formalized
---

# Distributions: its own results

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/index.html).

Test functions, Schwartz functions, tempered distributions and distributional derivatives: principal values, Plemelj limits, Dirac comb, partitions of unity.

## Existence of the Cauchy principal value of $\varphi(x)/x$

For every real-valued Schwartz
function $\varphi$ on $\mathbb{R}$ there is a real number $L$ such that
$\int_{\{x \in \mathbb{R} \,:\, |x| \ge \varepsilon\}} \varphi(x)/x \, dx \to L$ as
$\varepsilon \to 0^+$, the integrals being taken with respect to Lebesgue measure.

## Sources

- F. Friedlander and M. Joshi, *Introduction to the Theory of Distributions*, Ch. 2.

Stated but not proved: `MathlibExt.Analysis.Distribution.CauchyPrincipalValueWanted.cauchyPrincipalValue_exists` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/CauchyPrincipalValueWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/CauchyPrincipalValueWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/index.html#cauchy-principal-value-exists).

## Smooth partitions of unity subordinate to a finite open cover

Let $E$ be a
finite-dimensional real normed space, $K \subseteq E$ a compact set, and $(U_i)_{i \in \iota}$ a
finite family of open subsets of $E$ with $K \subseteq \bigcup_i U_i$. Then there are smooth
compactly supported functions $\varphi_i : E \to \mathbb{R}$, one for each $i \in \iota$, such
that $\varphi_i(x) \ge 0$ for all $i$ and all $x \in E$, the closed support of each $\varphi_i$
is contained in $U_i$, and $\sum_{i \in \iota} \varphi_i(x) = 1$ for every $x \in K$.

## Sources

- <https://en.wikipedia.org/wiki/Partition_of_unity>.

Stated but not proved: `MathlibExt.Analysis.Distribution.TestFunctionPartitionOfUnityWanted.testFunction_partitionOfUnity` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/TestFunctionPartitionOfUnityWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/TestFunctionPartitionOfUnityWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/index.html#test-function-partition-of-unity).

## The Dirac comb is a tempered distribution

There is a tempered distribution $T$ on
$\mathbb{R}$, that is, a continuous $\mathbb{C}$-linear functional on the space of
complex-valued Schwartz functions on $\mathbb{R}$, such that $T(g)=\sum_{n\in\mathbb{Z}} g(n)$
for every complex-valued Schwartz function $g$ on $\mathbb{R}$.

## Sources

- <https://en.wikipedia.org/wiki/Dirac_comb>.

Stated but not proved: `MathlibExt.Analysis.Distribution.TemperedExamplesWanted.diracComb_toTemperedDistribution` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/TemperedExamplesWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/TemperedExamplesWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/index.html#dirac-comb-to-tempered-distribution).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distributions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/distributions)
