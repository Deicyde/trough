---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ThreeChromaticHypergraphDegreeErdosProblem833Wanted.threeChromaticHighDegreeVertex, MathlibExt.Combinatorics.ThreeChromaticHypergraphDegreeErdosProblem833Wanted.threeChromaticHighDegreeVertex_holds
statement: formalized
---

# Degrees in 3-chromatic hypergraphs

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/degrees-in-3-chromatic-hypergraphs/index.html).

## Erdős Problem 833

The statement that there is a real $c > 0$ such that for every natural
number $r \ge 2$, every $n$ and every hypergraph $H$ on the vertex set $\{0, \dots, n-1\}$ (a
finite set of edges, each a set of exactly $r$ vertices) that is $3$-colorable but not
$2$-colorable, some vertex lies in at least $(1 + c)^r$ edges of $H$.

Formalized by `MathlibExt.Combinatorics.ThreeChromaticHypergraphDegreeErdosProblem833Wanted.threeChromaticHighDegreeVertex`, a definition declared in [WantedExt/Combinatorics/ThreeChromaticHypergraphDegreeErdosProblem833Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ThreeChromaticHypergraphDegreeErdosProblem833Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/degrees-in-3-chromatic-hypergraphs/index.html#three-chromatic-high-degree-vertex).

## Erdős Problem 833 holds

There is a real $c > 0$ such that for every natural number $r \ge 2$,
every $n$ and every hypergraph $H$ on the vertex set $\{0, \dots, n-1\}$ (a finite set of edges,
each a set of exactly $r$ vertices) that is $3$-colorable but not $2$-colorable, some vertex lies
in at least $(1 + c)^r$ edges of $H$.

Erdős and Lovász proved that every $r$-uniform hypergraph with chromatic number $3$ has a vertex
in at least $2^{r-1} / (4r)$ edges (Theorem 2 with $k = 2$), which exceeds $(1 + c)^r$ for a small
absolute $c$ once $r$ is large, while for every $r$ some vertex lies in two edges (pairwise
disjoint edges can be $2$-colored).

## Sources

- T. F. Bloom, Erdős Problems, Problem #833, https://www.erdosproblems.com/833 (status PROVED); resolution: P. Erdős and L. Lovász, Problems and results on 3-chromatic hypergraphs and some related questions, Infinite and finite sets (Colloq. Keszthely, 1973), Colloq. Math. Soc. János Bolyai 10 (1975), 609-627, Theorem 2: a (k + 1)-chromatic r-uniform hypergraph has an edge meeting at least k^{r-1}/4 other edges, so some vertex has degree at least k^{r-1}/(4r); for k = 2 this is 2^{r-1}/(4r), https://users.renyi.hu/~p_erdos/1975-34.pdf.

Stated but not proved: `MathlibExt.Combinatorics.ThreeChromaticHypergraphDegreeErdosProblem833Wanted.threeChromaticHighDegreeVertex_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThreeChromaticHypergraphDegreeErdosProblem833Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ThreeChromaticHypergraphDegreeErdosProblem833Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/degrees-in-3-chromatic-hypergraphs/index.html#three-chromatic-high-degree-vertex-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Degrees in 3-chromatic hypergraphs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/degrees-in-3-chromatic-hypergraphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/degrees-in-3-chromatic-hypergraphs)
