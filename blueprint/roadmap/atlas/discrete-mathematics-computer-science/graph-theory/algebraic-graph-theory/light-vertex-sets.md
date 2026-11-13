---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.EpsilonLightSubsetWanted.IsEpsilonLight, MathlibExt.Combinatorics.EpsilonLightSubsetWanted.epsilonLightSubsetExists, MathlibExt.Combinatorics.EpsilonLightSubsetWanted.epsilonLightSubsetExists_holds
statement: formalized
---

# ε-light vertex sets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/light-vertex-sets/index.html).

## ε-light vertex sets

Let $G$ be a simple graph on a finite vertex set $V$, let
$\varepsilon$ be a real number and let $S \subseteq V$. Let $L$ be the real Laplacian matrix of
$G$ and $L_S$ the real Laplacian matrix of the graph on $V$ whose edges are the edges of $G$ with
both endpoints in $S$. The set $S$ is $\varepsilon$-light in $G$ if $\varepsilon L - L_S$ is
positive semidefinite.

Formalized by `MathlibExt.Combinatorics.EpsilonLightSubsetWanted.IsEpsilonLight`, a definition declared in [WantedExt/Combinatorics/EpsilonLightSubsetWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/EpsilonLightSubsetWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/light-vertex-sets/index.html#is-epsilon-light).

## The large ε-light subset property

The statement that there is a real constant $c > 0$
such that for every natural number $n$, every simple graph $G$ on the vertex set
$\{0, \dots, n-1\}$ and every real number $\varepsilon$ with $0 < \varepsilon < 1$, some set $S$
of vertices that is $\varepsilon$-light in $G$ has at least $c \varepsilon n$ elements.

Formalized by `MathlibExt.Combinatorics.EpsilonLightSubsetWanted.epsilonLightSubsetExists`, a definition declared in [WantedExt/Combinatorics/EpsilonLightSubsetWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/EpsilonLightSubsetWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/light-vertex-sets/index.html#epsilon-light-subset-exists).

## Every graph has a large ε-light vertex set

There is a real constant $c > 0$ such that for
every natural number $n$, every simple graph $G$ on the vertex set $\{0, \dots, n-1\}$ and every
real number $\varepsilon$ with $0 < \varepsilon < 1$, there is a set $S$ of vertices with at least
$c \varepsilon n$ elements that is $\varepsilon$-light in $G$: the matrix $\varepsilon L - L_S$ is
positive semidefinite, where $L$ is the real Laplacian matrix of $G$ and $L_S$ is the real
Laplacian matrix of the graph on all $n$ vertices whose edges are the edges of $G$ with both
endpoints in $S$.

Appendix B.6 of the source proves this, with $c = 1/42$, as Lemma B.1 (stated for weighted graphs).

## Sources

- First Proof authors, arXiv:2602.05192v2, Appendix B.6 (Lemma B.1), https://arxiv.org/html/2602.05192v2.

Stated but not proved: `MathlibExt.Combinatorics.EpsilonLightSubsetWanted.epsilonLightSubsetExists_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/EpsilonLightSubsetWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/EpsilonLightSubsetWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/light-vertex-sets/index.html#epsilon-light-subset-exists-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: ε-light vertex sets](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/light-vertex-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/light-vertex-sets)
