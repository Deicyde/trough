---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.subdivision, MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.ContainsCopy, MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.ex, MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.conjecture, MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.conjecture_holds, MathlibExt.Combinatorics.ErdosProblem146Wanted.EP146.DegenerateExtremalClaim, MathlibExt.Combinatorics.ErdosProblem146Wanted.DegenerateExtremalClaim_refuted
statement: formalized
---

# Turán numbers of bipartite graphs

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs/index.html).

## The $(k-1)$-subdivision of a graph

For a simple graph $H$ on the vertex set
$\{0, \dots, m - 1\}$ and a natural number $k \ge 2$, the $(k-1)$-subdivision $H^{k-1}$ is the
graph obtained from $H$ by replacing each edge $ij$ with $i < j$ by a path
$i, (ij, 0), (ij, 1), \dots, (ij, k - 2), j$ of length $k$ through $k - 1$ new vertices, the paths
of different edges sharing no new vertices. For $k \le 1$ there are no new vertices and the
resulting graph has no edges.

Formalized by `MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.subdivision`, a definition declared in [WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs/index.html#subdivision).

## Containing a copy of a graph

A simple graph $G$ contains a copy of a simple graph $F$ if
there is an injective map $f$ from the vertices of $F$ to the vertices of $G$ such that $f(u)$ and
$f(v)$ are adjacent in $G$ whenever $u$ and $v$ are adjacent in $F$; the copy need not be induced.

Formalized by `MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.ContainsCopy`, a definition declared in [WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs/index.html#contains-copy).

## The extremal number of a graph

For a natural number $n$ and a simple graph $F$, the
extremal number $\mathrm{ex}(n, F)$ is the maximum number of edges of a simple graph on the vertex
set $\{0, \dots, n - 1\}$ that contains no copy of $F$. It is $0$ when every simple graph on these
$n$ vertices contains a copy of $F$.

Formalized by `MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.ex`, a definition declared in [WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs/index.html#ex).

## The Conlon–Lee subdivision conjecture

For a simple graph $H$ and a natural number $k$,
write $H^{k-1}$ for the $(k-1)$-subdivision of $H$, and for a simple graph $F$ and a natural
number $n$ write $\mathrm{ex}(n, F)$ for the extremal number of $F$ on $n$ vertices. The
conjecture is the statement that for every even natural number $k \ge 2$, every natural number
$m$ and every simple graph $H$ on the vertex set $\{0, \dots, m - 1\}$, there are real numbers
$\delta > 0$ and $C$ such that $\mathrm{ex}(n, H^{k-1}) \le C \cdot n^{1 + 1/k - \delta}$ for
every natural number $n$. In other words, $\mathrm{ex}(n, H^{k-1}) = O(n^{1 + 1/k - \delta})$
for some $\delta > 0$.

Formalized by `MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs/index.html#conjecture).

## The Conlon–Lee subdivision conjecture holds

For a simple graph $F$ and a natural number
$n$, let $\mathrm{ex}(n, F)$ be the maximum number of edges of a simple graph on $n$ vertices
that contains no copy of $F$ (not necessarily induced), or $0$ if there is no such graph. For a
simple graph $H$ and a natural number $k \ge 2$, let $H^{k-1}$ be the graph obtained from $H$ by
replacing each edge with a path of length $k$ through $k - 1$ new vertices (internally disjoint
for different edges). Then for every even natural number $k \ge 2$, every natural number $m$ and
every simple graph $H$ on the vertex set $\{0, \dots, m - 1\}$, there are real numbers
$\delta > 0$ and $C$ such that $\mathrm{ex}(n, H^{k-1}) \le C \cdot n^{1 + 1/k - \delta}$ for
every natural number $n$.

This was proved by Janzer (Bull. London Math. Soc. 53 (2021) 108–118, Theorem 1.7).

## Sources

- O. Janzer, The extremal number of longer subdivisions, Bull. London Math. Soc. 53 (2021) 108-118, arXiv:1905.08001, https://doi.org/10.1112/blms.12404.

Stated but not proved: `MathlibExt.Combinatorics.ConlonLeeSubdivisionConjectureWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ConlonLeeSubdivisionConjectureWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs/index.html#conjecture-holds).

## Erdős–Simonovits degeneracy conjecture (Erdős Problem 146)

The statement that for
every finite simple graph $H$ and every natural number $r \ge 1$, if $H$ is bipartite and
$r$-degenerate (every nonempty set of vertices contains a vertex with at most $r$ neighbours in
that set), then $\mathrm{ex}(n; H) = O(n^{2 - 1/r})$ as $n \to \infty$, where
$\mathrm{ex}(n; H)$ is the largest number of edges of a simple graph on $n$ vertices containing
no copy of $H$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem146Wanted.EP146.DegenerateExtremalClaim`, a definition declared in [WantedExt/Combinatorics/ErdosProblem146Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem146Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs/index.html#degenerate-extremal-claim).

## Counterexample to the Erdős–Simonovits degeneracy conjecture

It is not true that for
every finite simple graph $H$ and every natural number $r \ge 1$ such that $H$ is bipartite and
$r$-degenerate (every nonempty set of vertices contains a vertex with at most $r$ neighbours in
that set), the extremal number $\mathrm{ex}(n; H)$ (the largest number of edges of a simple
graph on $n$ vertices containing no copy of $H$) is $O(n^{2 - 1/r})$ as $n \to \infty$.

An internal OpenAI model constructed a connected bipartite $2$-degenerate graph $H$ with
$\mathrm{ex}(n; H) \ge c n^{3/2 + \varepsilon}$ for all large $n$, for some constants $c > 0$ and
$\varepsilon > 0$; erdosproblems.com/146 records the conjecture as disproved.

## Sources

- T. F. Bloom, Erdős Problem #146, erdosproblems.com (live page, LaTeX source and forum threads read 2026-10-22), https://www.erdosproblems.com/146; OpenAI, Ten proofs (section disproving the Erdős degeneracy conjecture), 2026, https://cdn.openai.com/pdf/ten-proofs-oai.pdf.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem146Wanted.DegenerateExtremalClaim_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem146Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem146Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs/index.html#degenerate-extremal-claim-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turán numbers of bipartite graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/extremal-graph-theory/tur-n-numbers-of-bipartite-graphs)
