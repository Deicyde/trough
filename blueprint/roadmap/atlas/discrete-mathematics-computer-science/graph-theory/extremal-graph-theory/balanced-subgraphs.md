---
declaration: section
origin: cited
lean: SimpleGraph.IsBalanced, MathlibExt.GraphTheory.ErdosProblem1077Wanted.mainPositive, MathlibExt.GraphTheory.ErdosProblem1077Wanted.disprovedMain, MathlibExt.GraphTheory.ErdosProblem1077Wanted.mainPositive_refuted
statement: formalized
---

# Balanced subgraphs

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/balanced-subgraphs/index.html).

## Balanced graph

Let $G$ be a finite simple graph and $D$ a real number. The graph $G$ is
$D$-balanced if its maximum degree $\Delta(G)$ is at most $D$ times its minimum degree
$\delta(G)$, that is, $\Delta(G) \le D \cdot \delta(G)$.

Formalized by `SimpleGraph.IsBalanced`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Balanced.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Balanced.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/balanced-subgraphs/index.html#is-balanced).

## Erdős–Simonovits balanced subgraph claim

For all reals $\varepsilon$ and $\alpha$ with
$0 < \varepsilon < 1$ and $0 < \alpha < 1$, for all sufficiently large real $D$ and then all
sufficiently large $n$, every simple graph $G$ on the vertex set $\{0, \dots, n-1\}$ with more
than $n^{1+\alpha}$ edges has a (not necessarily induced) subgraph $H$ with some number $m$ of
vertices such that $H$ is $D$-balanced (its maximum degree is at most $D$ times its minimum
degree), $m > n^{1-\alpha}$, and $H$ has more than $\varepsilon m^{1+\alpha}$ edges.

This claim (Erdős Problem 1077) is false.

Formalized by `MathlibExt.GraphTheory.ErdosProblem1077Wanted.mainPositive`, a definition declared in [WantedExt/GraphTheory/ErdosProblem1077Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem1077Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/balanced-subgraphs/index.html#main-positive).

## Negation of the Erdős–Simonovits balanced subgraph claim

The proposition that the
Erdős–Simonovits balanced subgraph claim fails, that is, that it is not the case that for all
reals $\varepsilon$ and $\alpha$ with $0 < \varepsilon < 1$ and $0 < \alpha < 1$, for all
sufficiently large real $D$ and then all sufficiently large $n$, every simple graph $G$ on the
vertex set $\{0, \dots, n-1\}$ with more than $n^{1+\alpha}$ edges has a (not necessarily
induced) subgraph $H$ with some number $m$ of vertices such that $H$ is $D$-balanced (its maximum
degree is at most $D$ times its minimum degree), $m > n^{1-\alpha}$, and $H$ has more than
$\varepsilon m^{1+\alpha}$ edges.

Formalized by `MathlibExt.GraphTheory.ErdosProblem1077Wanted.disprovedMain`, a definition declared in [WantedExt/GraphTheory/ErdosProblem1077Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem1077Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/balanced-subgraphs/index.html#disproved-main).

## The Erdős–Simonovits balanced subgraph claim is false

It is not the case that for all reals
$\varepsilon$ and $\alpha$ with $0 < \varepsilon < 1$ and $0 < \alpha < 1$, for all sufficiently
large real $D$ and then all sufficiently large $n$, every simple graph $G$ on the vertex set
$\{0, \dots, n-1\}$ with more than $n^{1+\alpha}$ edges has a (not necessarily induced) subgraph
$H$ with some number $m$ of vertices such that $H$ is $D$-balanced (its maximum degree is at most
$D$ times its minimum degree), $m > n^{1-\alpha}$, and $H$ has more than $\varepsilon m^{1+\alpha}$
edges.

The disproof uses a bipartite witness: the requirement $m > n^{1-\alpha}$ is too strong, and the
correct order is $n^{\alpha}$ per Jun Gao and Jiang–Longbrake [JiLo25], per erdosproblems.com/1077.

## Sources

- External Lean disproof of Erdos Problem 1077, plby/lean-proofs, https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos1077.lean#L265.

Stated but not proved: `MathlibExt.GraphTheory.ErdosProblem1077Wanted.mainPositive_refuted` is written with `theorem_wanted` in [WantedExt/GraphTheory/ErdosProblem1077Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem1077Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/balanced-subgraphs/index.html#main-positive-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Balanced subgraphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/balanced-subgraphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/extremal-graph-theory/balanced-subgraphs)
