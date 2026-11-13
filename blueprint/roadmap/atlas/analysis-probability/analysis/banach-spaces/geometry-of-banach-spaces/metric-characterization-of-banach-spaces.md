---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook69Wanted.metricCenterSets, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook69Wanted.IsMetricCenter, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook69Wanted.ScottishBookProblem69Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook69Wanted.mazurUlam69_refuted
statement: formalized
---

# Metric characterization of Banach spaces

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/metric-characterization-of-banach-spaces/index.html).

## Iterated metric center sets

Let $p, q$ be points of a pseudometric space $E$ with
distance $d$. The iterated metric center sets $R_n \subseteq E$ of $(p, q)$, for
$n \in \mathbb{N}$, are defined by $R_0 = \{x \in E : d(p, x) + d(x, q) = d(p, q)\}$ and
$R_{n+1} = \{r \in R_n : d(r, x) \le \operatorname{diam}(R_n) / 2 \text{ for all } x \in R_n\}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook69Wanted.metricCenterSets`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook69Wanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook69Wanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/metric-characterization-of-banach-spaces/index.html#metric-center-sets).

## Metric center of a pair of points

Let $p, q, c$ be points of a pseudometric space $E$
and let $R_n$, for $n \in \mathbb{N}$, be the iterated metric center sets of $(p, q)$. We say
that $c$ is the metric center of $(p, q)$ when $c \in R_n$ for every $n$, and every point
$y \in E$ with $y \in R_n$ for every $n$ equals $c$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook69Wanted.IsMetricCenter`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook69Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook69Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/metric-characterization-of-banach-spaces/index.html#is-metric-center).

## Scottish Book Problem 69 claim

The statement that every complete pseudometric space
$E$ with the following two properties is isometric to a real Banach space: (1) for all
$p, q \in E$ there is exactly one point $c \in E$ that is the metric center of $(p, q)$, and
(2) for all $p, q \in E$ there is exactly one point $x \in E$ such that $q$ is the metric
center of $(p, x)$. Here "isometric to a real Banach space" means that there are a complete
real normed space $F$ and an isometric bijection $E \to F$. This is the affirmative answer to
Problem 69 of S. Mazur and S. Ulam in the Scottish Book.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook69Wanted.ScottishBookProblem69Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook69Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook69Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/metric-characterization-of-banach-spaces/index.html#scottish-book-problem69-claim).

## Mazur–Ulam Problem 69 refuted

The Scottish Book Problem 69 claim is false: there is a
complete pseudometric space $E$ such that (1) for all $p, q \in E$ there is exactly one point
$c \in E$ that is the metric center of $(p, q)$, and (2) for all $p, q \in E$ there is exactly
one point $x \in E$ such that $q$ is the metric center of $(p, x)$, but there is no complete
real normed space $F$ with an isometric bijection $E \to F$.

## Sources

- S. Mazur and S. Ulam, Problem 69 of the Scottish Book; typescript Ad 69 records the negative answer (S. Mazur, December 21, 1936).

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook69Wanted.mazurUlam69_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook69Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook69Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/metric-characterization-of-banach-spaces/index.html#mazur-ulam69-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Metric characterization of Banach spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/metric-characterization-of-banach-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/metric-characterization-of-banach-spaces)
