---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.NonAveragingSetSizeErdosProblem186Wanted.IsNonAveraging, MathlibExt.Combinatorics.NonAveragingSetSizeErdosProblem186Wanted.nonAveragingMaxSizeQuarterExponent, MathlibExt.Combinatorics.NonAveragingSetSizeErdosProblem186Wanted.nonAveragingMaxSizeQuarterExponent_holds
statement: formalized
---

# Non-averaging sets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/non-averaging-sets/index.html).

## Non-averaging sets

A finite set $A$ of natural numbers is non-averaging if no $a \in A$ is
the arithmetic mean of a nonempty set $S \subseteq A \setminus \{a\}$, that is,
$\sum_{s \in S} s \ne |S| \cdot a$ for every $a \in A$ and every nonempty
$S \subseteq A \setminus \{a\}$.

Equivalently, no element of $A$ is the arithmetic mean of at least two distinct elements of $A$.

Formalized by `MathlibExt.Combinatorics.NonAveragingSetSizeErdosProblem186Wanted.IsNonAveraging`, a definition declared in [WantedExt/Combinatorics/NonAveragingSetSizeErdosProblem186Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NonAveragingSetSizeErdosProblem186Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/non-averaging-sets/index.html#is-non-averaging).

## Erdős Problem 186 on non-averaging sets

For every $\varepsilon > 0$ and every sufficiently
large $N$, the largest non-averaging subset of $\{1, \dots, N\}$ has size between
$N^{1/4 - \varepsilon}$ and $N^{1/4 + \varepsilon}$: some non-averaging subset of
$\{1, \dots, N\}$ has at least $N^{1/4 - \varepsilon}$ elements, and every non-averaging subset
of $\{1, \dots, N\}$ has at most $N^{1/4 + \varepsilon}$ elements. In short, the largest
non-averaging subset of $\{1, \dots, N\}$ has size $N^{1/4 + o(1)}$.

Formalized by `MathlibExt.Combinatorics.NonAveragingSetSizeErdosProblem186Wanted.nonAveragingMaxSizeQuarterExponent`, a definition declared in [WantedExt/Combinatorics/NonAveragingSetSizeErdosProblem186Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NonAveragingSetSizeErdosProblem186Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/non-averaging-sets/index.html#non-averaging-max-size-quarter-exponent).

## Pham–Zakharov theorem on non-averaging sets

For every $\varepsilon > 0$ and every
sufficiently large $N$, some non-averaging subset of $\{1, \dots, N\}$ has at least
$N^{1/4 - \varepsilon}$ elements, and every non-averaging subset of $\{1, \dots, N\}$ has at most
$N^{1/4 + \varepsilon}$ elements. Thus the largest non-averaging subset of $\{1, \dots, N\}$ has
size $N^{1/4 + o(1)}$.

Bosznay constructed non-averaging subsets of $\{1, \dots, N\}$ of size $\gg N^{1/4}$, and Pham and
Zakharov proved the matching upper bound $N^{1/4 + o(1)}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #186, https://www.erdosproblems.com/186 (status SOLVED); resolution: H. T. Pham and D. Zakharov, Sharp bound for the Erdős-Straus non-averaging set problem, Geom. Funct. Anal. 35 (2025), 1712-1738, arXiv:2410.14624 (upper bound); Á. P. Bosznay, On the lower estimation of non-averaging sets, Acta Math. Hungar. 53 (1989), 155-157 (lower bound), Pham-Zakharov main theorem: the largest non-averaging subset of {1, …, n} has size n^{1/4 + o(1)}; erdosproblems.com/186: N^{1/4} ≪ F(N) ≪ N^{1/4 + o(1)}, https://arxiv.org/abs/2410.14624.

Stated but not proved: `MathlibExt.Combinatorics.NonAveragingSetSizeErdosProblem186Wanted.nonAveragingMaxSizeQuarterExponent_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/NonAveragingSetSizeErdosProblem186Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NonAveragingSetSizeErdosProblem186Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/non-averaging-sets/index.html#non-averaging-max-size-quarter-exponent-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Non-averaging sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/non-averaging-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/non-averaging-sets)
