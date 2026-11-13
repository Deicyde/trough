---
declaration: section
origin: cited
lean: SimpleGraph.classicalRamsey, SimpleGraph.graphRamsey, SimpleGraph.graphRamsey_eq_sInf, SimpleGraph.graphPairRamsey, SimpleGraph.graphPairRamsey_eq_sInf, SimpleGraph.diagonalGraphRamsey, SimpleGraph.IsRamseySizeLinear, MathlibExt.Combinatorics.ErdosProblem570Wanted.conjecture
statement: formalized
---

# Graph Ramsey numbers

13 results, 10 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html).

## The Ramsey property for cliques

For natural numbers $s$, $t$ and $N$, the classical
Ramsey property for $(s, t)$ holds at $N$ when every simple graph $G$ on $N$ vertices contains the
complete graph $K_s$ as a subgraph, or its complement $\overline{G}$ contains $K_t$ as a subgraph.

Thus the graph and its complement encode the two colors of a complete graph.

Formalized by `SimpleGraph.classicalRamsey`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#classical-ramsey).

## Classical Ramsey numbers

For natural numbers $s$ and $t$, the Ramsey number $R(s, t)$ is
the least $N$ such that every simple graph on $N$ vertices contains the complete graph $K_s$ as a
subgraph or has a complement containing $K_t$ as a subgraph, and $0$ if there is no such $N$.

Such an $N$ always exists by the finite Ramsey theorem.

Formalized by `SimpleGraph.graphRamsey`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#graph-ramsey).

## Classical Ramsey numbers as an infimum

For all natural numbers $s$ and $t$, the Ramsey
number $R(s, t)$ equals the infimum in $\mathbb{N}$ (where the empty set has infimum $0$) of the
set of $N$ such that every simple graph on $N$ vertices contains the complete graph $K_s$ as a
subgraph or has a complement containing $K_t$ as a subgraph.

Formalized by `SimpleGraph.graphRamsey_eq_sInf`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#graph-ramsey-eq-s-inf).

## Ramsey number of a pair of graphs

For finite simple graphs $G$ and $H$, the Ramsey number
$R(G, H)$ is the least $n$ such that every simple graph $C$ on $n$ vertices contains a copy of $G$
as a subgraph or has a complement containing a copy of $H$ as a subgraph, and $0$ if there is no
such $n$.

Formalized by `SimpleGraph.graphPairRamsey`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#graph-pair-ramsey).

## The pair Ramsey number as an infimum

For finite simple graphs $G$ and $H$, the Ramsey
number $R(G, H)$ equals the infimum in $\mathbb{N}$ (where the empty set has infimum $0$) of the
set of $n$ such that every simple graph $C$ on $n$ vertices contains a copy of $G$ as a subgraph
or has a complement containing a copy of $H$ as a subgraph.

Formalized by `SimpleGraph.graphPairRamsey_eq_sInf`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#graph-pair-ramsey-eq-s-inf).

## Diagonal Ramsey number of a graph

For a finite simple graph $G$, the diagonal Ramsey
number of $G$ is $R(G, G)$: the least $n$ such that for every simple graph $C$ on $n$ vertices,
$C$ or its complement contains a copy of $G$ as a subgraph, and $0$ if there is no such $n$.

Formalized by `SimpleGraph.diagonalGraphRamsey`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#diagonal-graph-ramsey).

## Ramsey size linear graphs

Let $G$ be a finite simple graph. For a finite simple graph
$H$, write $R(G, H)$ for the least $m$ such that every simple graph on $m$ vertices contains a
copy of $G$ or has a complement containing a copy of $H$ ($0$ if there is no such $m$), and write
$e(H)$ for the number of edges of $H$. Then $G$ is Ramsey size linear if there is a real constant
$c > 0$ such that for every $n$ and every simple graph $H$ on $n$ vertices with no isolated
vertices, $R(G, H) \le c \cdot e(H)$.

Formalized by `SimpleGraph.IsRamseySizeLinear`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Ramsey.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#is-ramsey-size-linear).

## Erdős Problem 570 (cycle versus graph Ramsey bound)

The statement that for every natural
number $k \ge 3$ there is an $M$ such that for every $m \ge M$ and every finite simple graph $H$
with exactly $m$ edges and no isolated vertices, the Ramsey number $R(C_k, H)$ of the cycle $C_k$
on $k$ vertices and $H$ is at most $2m + \lfloor (k-1)/2 \rfloor$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem570Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem570Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem570Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#conjecture).

## Resolution of Erdős Problem 570

For every natural number $k \ge 3$ there is an $M$ such that
for every $m \ge M$ and every finite simple graph $H$ with exactly $m$ edges and no isolated
vertices, the Ramsey number $R(C_k, H)$ of the cycle $C_k$ on $k$ vertices and $H$ is at most
$2m + \lfloor (k-1)/2 \rfloor$.

## Sources

- S. Cambie, A. Freschi, P. Morawski, K. Petrova, A. Pokrovskiy, Ramsey number of a cycle versus a graph of a given size, arXiv:2601.10238 (2026), https://arxiv.org/abs/2601.10238.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem570Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem570Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem570Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#conjecture-holds).

## Erdős Problem 800 on linear Ramsey numbers

The proposition asserts that there is a real
number $C > 0$ such that for every natural number $n$ and every simple graph $G$ on $n$ vertices
in which no two adjacent vertices both have degree at least $3$, the diagonal Ramsey number
$R(G, G)$ is at most $Cn$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem800Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem800Wanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem800Wanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#conjecture-2).

## Alon's theorem on linear Ramsey numbers

There is a real number $C > 0$ such that for every
natural number $n$ and every simple graph $G$ on $n$ vertices in which no two adjacent vertices
both have degree at least $3$, the diagonal Ramsey number $R(G, G)$ is at most $Cn$.

This answers Erdős Problem 800 affirmatively.

## Sources

- Noga Alon, Subdivided graphs have linear Ramsey numbers, Journal of Graph Theory 18 (1994), 343–347, https://doi.org/10.1002/jgt.3190180406.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem800Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem800Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem800Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#conjecture-holds-2).

## Superlinear threshold for triangle-good graphs (Erdős Problem 1182)

The statement that for
every real number $C$, for all sufficiently large natural numbers $n$, every connected graph $G$ on
the vertex set $\{0, \dots, n - 1\}$ with at most $Cn$ edges has $R(K_3, G) = 2n - 1$. Here
$R(K_3, G)$ is the Ramsey number of the pair: the least $N$ such that every graph on $N$ vertices
contains a triangle or has a complement containing a copy of $G$.

This is the last question of Erdős Problem 1182, whether $F(n) / n \to \infty$, where $F(n)$ is the
largest $m$ such that every connected graph $G$ on $n$ vertices with at most $m$ edges has
$R(K_3, G) = 2n - 1$; since this property is downward closed in $m$, the two forms agree.

Formalized by `MathlibExt.Combinatorics.TriangleGoodSparseConnectedGraphsErdosProblem1182Wanted.triangleGoodnessSuperlinearThreshold`, a definition declared in [WantedExt/Combinatorics/TriangleGoodSparseConnectedGraphsErdosProblem1182Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleGoodSparseConnectedGraphsErdosProblem1182Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#triangle-goodness-superlinear-threshold).

## No superlinear threshold for triangle-good graphs (Erdős Problem 1182)

It is not true
that for every real number $C$, for all sufficiently large natural numbers $n$, every connected
graph $G$ on the vertex set $\{0, \dots, n - 1\}$ with at most $Cn$ edges has
$R(K_3, G) = 2n - 1$. Equivalently, there is a real number $C$ such that for infinitely many $n$
some connected graph $G$ on $\{0, \dots, n - 1\}$ with at most $Cn$ edges has
$R(K_3, G) \ne 2n - 1$. Here $R(K_3, G)$ is the Ramsey number of the pair: the least $N$ such
that every graph on $N$ vertices contains a triangle or has a complement containing a copy of
$G$, and $0$ if there is no such $N$.

Brandt proved $F(n) \le 84n$, where $F(n)$ is the largest $m$ such that every connected graph on
$n$ vertices with at most $m$ edges has $R(K_3, G) = 2n - 1$. So for all large $n$ some connected
graph on $n$ vertices with at most $84n + 1$ edges has $R(K_3, G) \ne 2n - 1$, and the statement
fails for $C = 85$. Brandt's 1996 preprint is unrefereed; erdosproblems.com/1182 accepts it.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1182, https://www.erdosproblems.com/1182 (status OPEN); resolution: S. Brandt, Expanding graphs and Ramsey numbers, preprint, Serie A Mathematik, Freie Universität Berlin, 1996 (unrefereed; accepted on erdosproblems.com/1182), F(n) ≤ 84n, as recorded on erdosproblems.com/1182: 'The upper bound was improved to F(n) ≤ 84n by Brandt ... (This resolves the final question in the negative.)', https://ftp.math.fu-berlin.de/pub/math/publ/pre/1996/pr-a-96-24.ps.

Stated but not proved: `MathlibExt.Combinatorics.TriangleGoodSparseConnectedGraphsErdosProblem1182Wanted.triangleGoodnessSuperlinearThreshold_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/TriangleGoodSparseConnectedGraphsErdosProblem1182Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleGoodSparseConnectedGraphsErdosProblem1182Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html#triangle-goodness-superlinear-threshold-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph Ramsey numbers](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-ramsey-theory/graph-ramsey-numbers)
