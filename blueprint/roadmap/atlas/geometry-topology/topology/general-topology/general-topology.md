---
declaration: section
origin: cited
lean: IsPreconnected.inter_frontier_nonempty_of_inter_compl, MathlibExt.Analysis.FunctionalAnalysis.BoundedMetricTopologicallyEquivalentWanted.dist_div_one_add_dist_balls_equivalent, HomogeneousSpace, IsIrreducible.topologicalKrullDim_add_one_le_of_isClosed_of_ne, MathlibExt.Topology.KuratowskiClosureComplement.kuratowski_closure_complement, Metric.IsSeparated'
statement: formalized
---

# General topology: its own results

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/index.html).

Point-set topology of topological and metric spaces: connectedness, separation and cardinal invariants, homogeneous spaces, direct and inverse limits of spaces, restricted products, and dimension theory.

## A preconnected set meets the frontier of every set it crosses

Let $s$ be a
preconnected subset of a topological space $X$ and let $A \subseteq X$. If both $s \cap A$ and
$s \cap (X \setminus A)$ are nonempty, then $s$ meets the frontier
$\partial A = \overline{A} \setminus \operatorname{int} A$ of $A$, that is,
$s \cap \partial A$ is nonempty.

Formalized by `IsPreconnected.inter_frontier_nonempty_of_inter_compl`, a theorem declared in [MathlibExt/Topology/Connected/Frontier.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Connected/Frontier.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/index.html#inter-frontier-nonempty-of-inter-compl).

## Bounded metric $d/(1+d)$ is equivalent to $d$

Let $(X,d)$ be a metric space and define

\[
\delta(x,y):=\frac{d(x,y)}{1+d(x,y)}, \qquad x,y\in X.
\]
Prove that $d$ and $\delta$ are equivalent metrics on $X$.

Lean variant: the source statement asserts only that `d`-balls and `δ`-balls are mutually nested,
which omits the claim that `δ` is a metric; the metric axioms of `δ` are added as a first conjunct.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Inequalities in real analysis), problem `ma_proofbench_l1_65`, with the change above.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.BoundedMetricTopologicallyEquivalentWanted.dist_div_one_add_dist_balls_equivalent` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/BoundedMetricTopologicallyEquivalentWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/BoundedMetricTopologicallyEquivalentWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/index.html#dist-div-one-add-dist-balls-equivalent).

## Homogeneous topological space

A topological space is homogeneous if its homeomorphism group acts transitively.

Formalized by `HomogeneousSpace`, a class declared in [MathlibExt/Topology/HomogeneousSpace.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/HomogeneousSpace.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/index.html#homogeneous-space).

## Krull dimension drops on proper closed subsets of irreducible sets

A proper closed subset of an irreducible set has Krull dimension at
least one less than the ambient set.

Formalized by `IsIrreducible.topologicalKrullDim_add_one_le_of_isClosed_of_ne`, a theorem declared in [MathlibExt/Topology/KrullDimension.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/KrullDimension.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/index.html#topological-krull-dim-add-one-le-of-is-c).

## Kuratowski's closure-complement theorem

Let $X$ be a topological space and $s \subseteq X$.
The sets that can be obtained from $s$ by applying closure and complement finitely many times
(including $s$ itself) form a finite family of at most $14$ distinct sets.

## Sources

- Casimir Kuratowski, "Sur l'opération Ā de l'Analysis Situs," *Fundamenta Mathematicae* 3 (1922), 182–199, DOI 10.4064/FM-3-1-182-199.

Formalized by `MathlibExt.Topology.KuratowskiClosureComplement.kuratowski_closure_complement`, a theorem declared in [MathlibExt/Topology/KuratowskiClosureComplement.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/KuratowskiClosureComplement.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/index.html#kuratowski-closure-complement).

## Non-strictly separated sets

Let $X$ be a pseudo-extended metric space (distances lie in
$[0, \infty]$ and distinct points may be at distance $0$), write $d$ for its extended distance,
and let $\varepsilon \in [0, \infty]$. A set $s \subseteq X$ is $\varepsilon$-separated if
$\varepsilon \le d(x, y)$ for all distinct points $x, y \in s$.

Formalized by `Metric.IsSeparated'`, a definition declared in [MathlibExt/Topology/MetricSpace/MetricSeparated.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/MetricSeparated.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/index.html#is-separated).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: General topology](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/general-topology)
