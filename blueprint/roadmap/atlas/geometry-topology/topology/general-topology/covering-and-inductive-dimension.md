---
declaration: section
origin: cited
lean: MathlibExt.Topology.ScottishBook187bWanted.CoverLE, MathlibExt.Topology.ScottishBook187bWanted.scottishBook187b_refuted
statement: formalized
---

# Covering and inductive dimension

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/covering-and-inductive-dimension/index.html).

## Covering dimension at most n

A topological space $X$ has covering dimension at most
$n \in \mathbb{N}$ if every finite open cover $U_1, \dots, U_m$ of $X$ has a finite open
refinement $V_1, \dots, V_k$ (open sets covering $X$, each contained in some $U_i$) in which any
$n + 2$ members with distinct indices have empty intersection, that is, the refinement has order
at most $n + 1$.

Formalized by `MathlibExt.Topology.ScottishBook187bWanted.CoverLE`, a definition declared in [WantedExt/Topology/ScottishBook187bWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook187bWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/covering-and-inductive-dimension/index.html#cover-le).

## Small inductive and covering dimension can differ for compact Hausdorff spaces

Scottish
Book Problem 187, part (2), has a negative answer: it is not the case that for every compact
Hausdorff space $X$ and every $n \in \mathbb{N}$, $X$ has small inductive dimension at most $n$
if and only if $X$ has covering dimension at most $n$.

The small inductive dimension is used here; Alexandroff's typescript does not say whether small or
large inductive dimension is meant. The Lunts–Lokutsievskii example is a compact Hausdorff space
$X$ whose covering dimension $\dim X$ differs from its small inductive dimension
$\operatorname{ind} X$ (Encyclopedia of Mathematics, "Dimension theory"; R. Engelking, Dimension
Theory, North-Holland, 1978).

## Sources

- P. Alexandroff, Problem 187 part (2) of the Scottish Book, typescript pp. 82–83.

Stated but not proved: `MathlibExt.Topology.ScottishBook187bWanted.scottishBook187b_refuted` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook187bWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook187bWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/covering-and-inductive-dimension/index.html#scottish-book187b-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Covering and inductive dimension](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/covering-and-inductive-dimension/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/general-topology/covering-and-inductive-dimension)
