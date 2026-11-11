---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem574Wanted.IsFreeOf574Cycles, MathlibExt.Combinatorics.ErdosProblem574Wanted.extremalNumber, MathlibExt.Combinatorics.ErdosProblem574Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem574Wanted.conjecture_refuted
statement: formalized
---

# Turán numbers of cycles

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-cycles/index.html).

## Graphs without cycles of lengths $2k-1$ and $2k$

For a natural number $k$, a simple
graph $G$ is free of the cycle lengths $2k-1$ and $2k$ when it contains no copy of the cycle
graph $C_{2k-1}$ and no copy of the cycle graph $C_{2k}$, where a copy is an injective graph
homomorphism, that is, a subgraph that need not be induced.

Here $C_m$ is the cycle graph on $m$ vertices, which has no edges for $m \le 1$ and is a single
edge for $m = 2$, and $2k-1$ is computed in the natural numbers, so it is $0$ when $k = 0$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem574Wanted.IsFreeOf574Cycles`, a definition declared in [WantedExt/Combinatorics/ErdosProblem574Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem574Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-cycles/index.html#is-free-of574-cycles).

## Extremal number for cycles of lengths $2k-1$ and $2k$

For natural numbers $k$ and
$n$, $\mathrm{ex}(n; \{C_{2k-1}, C_{2k}\})$ is the supremum of the numbers of edges of the simple
graphs on the vertex set $\{0, \dots, n-1\}$ that contain no copy of the cycle graph $C_{2k-1}$
and no copy of the cycle graph $C_{2k}$, where the supremum of the empty set is $0$. Here $2k-1$
is computed in the natural numbers, so it is $0$ when $k = 0$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem574Wanted.extremalNumber`, a definition declared in [WantedExt/Combinatorics/ErdosProblem574Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem574Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-cycles/index.html#extremal-number).

## Erdős Problem 574

The statement that for every natural number $k \ge 2$ the ratio
$\mathrm{ex}(n; \{C_{2k-1}, C_{2k}\}) / (n/2)^{1 + 1/k}$ tends to $1$ as $n \to \infty$, that is,
$\mathrm{ex}(n; \{C_{2k-1}, C_{2k}\}) = (1 + o(1)) (n/2)^{1 + 1/k}$. Here
$\mathrm{ex}(n; \{C_{2k-1}, C_{2k}\})$ is the extremal number: the supremum of the numbers of
edges of simple graphs on $n$ vertices that contain no copy of the cycle graph $C_{2k-1}$ and no
copy of the cycle graph $C_{2k}$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem574Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem574Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem574Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-cycles/index.html#conjecture).

## Erdős Problem 574 is false

It is not the case that for every natural number $k \ge 2$ the
ratio $\mathrm{ex}(n; \{C_{2k-1}, C_{2k}\}) / (n/2)^{1 + 1/k}$ tends to $1$ as $n \to \infty$.
Here $\mathrm{ex}(n; \{C_{2k-1}, C_{2k}\})$ is the extremal number: the supremum of the numbers
of edges of simple graphs on $n$ vertices that contain no copy of the cycle graph $C_{2k-1}$ and
no copy of the cycle graph $C_{2k}$.

Lazebnik, Ustimenko and Woldar (Discrete Math. 1999), per Füredi–Simonovits
(arXiv:1306.5167, Construction 4.28), blow up one side of Benson's girth-12 bipartite graph to
get bipartite $C_{10}$-free graphs (hence also $C_9$-free) with
$4(n/5)^{6/5} > 0.5798\, n^{6/5}$ edges for infinitely many $n$, refuting the case $k = 5$.

## Sources

- Zoltán Füredi and Miklós Simonovits, The history of degenerate (bipartite) extremal graph problems, in Erdős Centennial, Bolyai Soc. Math. Stud. 25 (2013), arXiv:1306.5167, https://arxiv.org/abs/1306.5167.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem574Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem574Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem574Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-cycles/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turán numbers of cycles](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-cycles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-cycles)
