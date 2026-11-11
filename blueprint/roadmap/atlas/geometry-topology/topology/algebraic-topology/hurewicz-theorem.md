---
declaration: section
origin: cited
lean: MathlibExt.Topology.HurewiczWanted.Topology.Hurewicz.IntegralHomology, MathlibExt.Topology.HurewiczWanted.Topology.Hurewicz.hurewicz_h1_abelianization
statement: formalized
---

# Hurewicz theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/hurewicz-theorem/index.html).

## Integral singular homology

For a natural number $n$ and a topological space $X$,
$H_n(X; \mathbb{Z})$ denotes the $n$-th singular homology group of $X$ with coefficients in
$\mathbb{Z}$, regarded as an abelian group.

Formalized by `MathlibExt.Topology.HurewiczWanted.Topology.Hurewicz.IntegralHomology`, an abbreviation declared in [WantedExt/Topology/HurewiczWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/HurewiczWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/hurewicz-theorem/index.html#integral-homology).

## First homology is the abelianized fundamental group

Let $X$ be a path-connected
topological space and let $x \in X$. Then the abelianization of the fundamental group
$\pi_1(X, x)$ is isomorphic, as a group, to the first integral singular homology group
$H_1(X; \mathbb{Z})$ of $X$.

## Sources

- W. Hurewicz (1935); see Hatcher, *Algebraic Topology*, Theorem 2A.1. Knill, *Some fundamental theorems in mathematics*, §153. Problem `hurewicz_h1_abelianization` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.HurewiczWanted.Topology.Hurewicz.hurewicz_h1_abelianization` is written with `theorem_wanted` in [WantedExt/Topology/HurewiczWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/HurewiczWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/hurewicz-theorem/index.html#hurewicz-h1-abelianization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hurewicz theorem](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/hurewicz-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/algebraic-topology/hurewicz-theorem)
