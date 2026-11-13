---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.HypergraphColoringShared.HypergraphColorable, MathlibExt.Combinatorics.HypergraphChromaticEdgeCountErdosProblem832Wanted.chromaticEdgeLowerBound, MathlibExt.Combinatorics.HypergraphChromaticEdgeCountErdosProblem832Wanted.chromaticEdgeLowerBound_refuted
statement: formalized
---

# Hypergraph chromatic number

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hypergraph-chromatic-number/index.html).

## Colorable hypergraph

A hypergraph $H$ on the vertex set $\{0, \dots, n-1\}$, given as a
finite set of edges (sets of vertices), is $k$-colorable when some coloring of the vertices with
$k$ colors leaves no edge monochromatic: every edge of $H$ contains two vertices of different
colors.

Formalized by `MathlibExt.Combinatorics.HypergraphColoringShared.HypergraphColorable`, a definition declared in [WantedExt/Combinatorics/HypergraphColoringShared.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/HypergraphColoringShared.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hypergraph-chromatic-number/index.html#hypergraph-colorable).

## Erdős Problem 832

The statement that for every integer $r \ge 3$ there is a $K$ such that
for every $k \ge K$, every $n$ and every $r$-uniform hypergraph $H$ on the vertex set
$\{0, \dots, n-1\}$ with chromatic number $k$ (it is $k$-colorable but not $(k-1)$-colorable),
$H$ has at least $\binom{(r-1)(k-1)+1}{r}$ edges, and if it has exactly that many edges then it is
the complete $r$-uniform hypergraph on some set of $(r-1)(k-1)+1$ of its vertices.

Formalized by `MathlibExt.Combinatorics.HypergraphChromaticEdgeCountErdosProblem832Wanted.chromaticEdgeLowerBound`, a definition declared in [WantedExt/Combinatorics/HypergraphChromaticEdgeCountErdosProblem832Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/HypergraphChromaticEdgeCountErdosProblem832Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hypergraph-chromatic-number/index.html#chromatic-edge-lower-bound).

## Alon's refutation of Erdős Problem 832

There is an integer $r \ge 3$ such that for
infinitely many $k$ there are an $n$ and an $r$-uniform hypergraph $H$ on the vertex set
$\{0, \dots, n-1\}$ with chromatic number $k$ (it is $k$-colorable but not $(k-1)$-colorable)
that either has fewer than $\binom{(r-1)(k-1)+1}{r}$ edges, or has exactly that many edges but is
not the complete $r$-uniform hypergraph on any set of $(r-1)(k-1)+1$ of its vertices.

Alon deduced this from an upper bound through Turán numbers: for an absolute constant $C$, every
$r \ge C$ and every $k \ge Cr$, some $r$-uniform hypergraph with chromatic number at least $k$ has
at most $(7/8)^r \binom{(r-1)(k-1)+1}{r}$ edges, and an edge-minimal one among these has
chromatic number exactly $k$. Known Turán bounds disprove the conjecture for every $r \ge 4$; the
case $r = 3$ is open.

## Sources

- T. F. Bloom, Erdős Problems, Problem #832, https://www.erdosproblems.com/832 (status DISPROVED); resolution: N. Alon, Hypergraphs with high chromatic number, Graphs Combin. 1 (1985), 387-389, with f(k, s) the least number of edges of a k-uniform hypergraph of chromatic number at least s: 'Erdős and Hajnal conjectured that for every fixed k, if s > s_0(k) then equality holds in (2)' (f(k, s) = C((s - 1)(k - 1) + 1, k)), and 'This conjecture is false, as easily follows from' Proposition 1 (an upper bound for f(k, s) through Turán numbers); erdosproblems.com/832: for an absolute C, r ≥ C and k ≥ C r there is an r-uniform hypergraph with chromatic number at least k and at most (7/8)^r C((r - 1)(k - 1) + 1, r) edges, known Turán bounds disprove the conjecture for every r ≥ 4, and r = 3 remains open, https://web.math.princeton.edu/~nalon/PDFS/Publications/Hypergraphs%20with%20high%20chromatic%20number.pdf.

Stated but not proved: `MathlibExt.Combinatorics.HypergraphChromaticEdgeCountErdosProblem832Wanted.chromaticEdgeLowerBound_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/HypergraphChromaticEdgeCountErdosProblem832Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/HypergraphChromaticEdgeCountErdosProblem832Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hypergraph-chromatic-number/index.html#chromatic-edge-lower-bound-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypergraph chromatic number](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hypergraph-chromatic-number/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hypergraph-chromatic-number)
