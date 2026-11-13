---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.HajnalSzemerediWanted.exists_equitable_coloring_of_maxDegree_lt, MathlibExt.Combinatorics.SimpleGraph.HajnalSzemerediWanted.hajnal_szemeredi_equitable_coloring, MathlibExt.Combinatorics.ErdosProblem914Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem914Wanted.conjecture_holds
statement: formalized
---

# Hajnal–Szemerédi theorem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/hajnal-szemer-di-theorem/index.html).

## Equitable coloring with more colors than the maximum degree

Let $G$ be a simple graph on a
finite vertex set with maximum degree $\Delta(G)$, and let $k$ be a natural number with
$\Delta(G) < k$. Then $G$ has a proper coloring with the $k$ colors $0, 1, \dots, k-1$ that is
equitable: for any two colors $i$ and $j$, the number of vertices of color $i$ is at most one more
than the number of vertices of color $j$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.HajnalSzemerediWanted.exists_equitable_coloring_of_maxDegree_lt`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HajnalSzemeredi.lean, line 3531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HajnalSzemeredi.lean#L3531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/hajnal-szemer-di-theorem/index.html#exists-equitable-coloring-of-max-degree).

## Hajnal–Szemerédi theorem

Let $G$ be a simple graph on a finite vertex set with maximum degree
$\Delta(G)$, and let $k$ be a natural number with $\Delta(G) < k$. Then $G$ has a proper coloring
with the $k$ colors $0, 1, \dots, k-1$ that is equitable: for any two colors $i$ and $j$, the
number of vertices of color $i$ is at most one more than the number of vertices of color $j$.

## Sources

- A. Hajnal and E. Szemerédi, "Proof of a conjecture of P. Erdős", Combinatorial Theory and Its Applications II, Colloq. Math. Soc. János Bolyai 4 (1970), 601-623.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.HajnalSzemerediWanted.hajnal_szemeredi_equitable_coloring`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HajnalSzemeredi.lean, line 3572](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HajnalSzemeredi.lean#L3572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/hajnal-szemer-di-theorem/index.html#hajnal-szemeredi-equitable-coloring).

## Erdős Problem 914 on clique factors and equitable colourings

The proposition asserts
that for all integers $r \ge 2$ and $m \ge 1$ and every finite simple graph $G$ with exactly $rm$
vertices, (a) if every vertex of $G$ has degree at least $m(r - 1)$, then $G$ contains $m$
pairwise disjoint cliques of $r$ vertices each, and (b) if every vertex of $G$ has degree at most
$m - 1$, then $G$ has a proper colouring with $m$ colours in which every colour class has exactly
$r$ vertices.

Formalized by `MathlibExt.Combinatorics.ErdosProblem914Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem914Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem914Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/hajnal-szemer-di-theorem/index.html#conjecture).

## Hajnal–Szemerédi theorem in clique-factor and equitable-colouring form

For all integers
$r \ge 2$ and $m \ge 1$ and every finite simple graph $G$ with exactly $rm$ vertices, (a) if every
vertex of $G$ has degree at least $m(r - 1)$, then $G$ contains $m$ pairwise disjoint cliques of
$r$ vertices each, and (b) if every vertex of $G$ has degree at most $m - 1$, then $G$ has a
proper colouring with $m$ colours in which every colour class has exactly $r$ vertices.

This resolves Erdős Problem 914 affirmatively: part (a) was proved by Corrádi and Hajnal for
$r = 3$ and by Hajnal and Szemerédi for all $r$, and part (b) is its equitable-colouring
reformulation, obtained by applying (a) to the complement of $G$.

## Sources

- A. Hajnal and E. Szemerédi, Proof of a conjecture of P. Erdős (1970), 601–623, https://mathscinet.ams.org/mathscinet-getitem?mr=297607; External Lean proof of Erdős Problem 914, plby/lean-proofs, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.29.1/ErdosProblems/Erdos914.lean.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem914Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem914Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem914Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/hajnal-szemer-di-theorem/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hajnal–Szemerédi theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/hajnal-szemer-di-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/hajnal-szemer-di-theorem)
