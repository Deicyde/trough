---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.LocallySparseTripleSystemErdosProblem1076Wanted.exSingle, MathlibExt.Combinatorics.LocallySparseTripleSystemErdosProblem1076Wanted.singleFamilyAsymptotic, MathlibExt.Combinatorics.LocallySparseTripleSystemErdosProblem1076Wanted.singleFamilyAsymptotic_refuted
statement: formalized
---

# Locally sparse triple systems

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/locally-sparse-triple-systems/index.html).

## Extremal number for $k$ vertices spanning $k - 2$ triples

For $k, n \in \mathbb{N}$ let
$\mathcal{F}_k$ be the family of all $3$-uniform hypergraphs with $k$ vertices and $k - 2$ edges.
Then $\mathrm{ex}_3(n, \mathcal{F}_k)$ is the largest number of triples in a $3$-uniform
hypergraph $E$ on the vertex set $\{0, \dots, n-1\}$ that contains no member of $\mathcal{F}_k$,
meaning that no set of exactly $k$ vertices contains $k - 2$ or more triples of $E$ (a member may
have isolated vertices, and extra triples can be dropped). Here $k - 2$ is read as $0$ when
$k < 2$, and $\mathrm{ex}_3(n, \mathcal{F}_k) = 0$ when no such hypergraph exists, which happens
exactly when $k \le 2$ and $k \le n$.

Formalized by `MathlibExt.Combinatorics.LocallySparseTripleSystemErdosProblem1076Wanted.exSingle`, a definition declared in [WantedExt/Combinatorics/LocallySparseTripleSystemErdosProblem1076Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LocallySparseTripleSystemErdosProblem1076Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/locally-sparse-triple-systems/index.html#ex-single).

## Erdős Problem 1076 as worded

For $k, n \in \mathbb{N}$ let
$\mathrm{ex}_3(n, \mathcal{F}_k)$ be the largest number of triples in a $3$-uniform hypergraph on
$n$ vertices in which no $k$ vertices span $k - 2$ or more triples, that is, which contains no
member of the family $\mathcal{F}_k$ of $3$-graphs with $k$ vertices and $k - 2$ edges. This is
the statement that for every $k \ge 5$, $\mathrm{ex}_3(n, \mathcal{F}_k) / n^2 \to 1/6$ as
$n \to \infty$, that is, $\mathrm{ex}_3(n, \mathcal{F}_k) \sim n^2 / 6$.

Formalized by `MathlibExt.Combinatorics.LocallySparseTripleSystemErdosProblem1076Wanted.singleFamilyAsymptotic`, a definition declared in [WantedExt/Combinatorics/LocallySparseTripleSystemErdosProblem1076Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LocallySparseTripleSystemErdosProblem1076Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/locally-sparse-triple-systems/index.html#single-family-asymptotic).

## Erdős Problem 1076 fails as worded

For $k, n \in \mathbb{N}$ let $\mathcal{F}_k$ be the family
of $3$-graphs with $k$ vertices and $k - 2$ edges, and let $\mathrm{ex}_3(n, \mathcal{F}_k)$ be the
largest number of triples in a $3$-uniform hypergraph on $n$ vertices that contains no member of
$\mathcal{F}_k$, that is, in which no $k$ vertices span $k - 2$ or more triples. It is not true
that for every $k \ge 5$, $\mathrm{ex}_3(n, \mathcal{F}_k) / n^2 \to 1/6$ as $n \to \infty$.

Already $k = 5$ fails: Glock proved that the largest triple system on $n$ vertices with no five
vertices spanning three triples has $(1 + o(1)) n^2 / 5$ triples, so
$\mathrm{ex}_3(n, \mathcal{F}_5) / n^2 \to 1/5$; his §1 states this as the answer to whether $1/6$
is sharp for every $k$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1076, https://www.erdosproblems.com/1076 (status PROVED); resolution: S. Glock, Triple systems with no three triples spanning at most five points, Bull. Lond. Math. Soc. 51 (2019), 230-236, abstract and Theorem 2: lim n⁻² f⁽³⁾(n; 5, 3) = 1/5, where f⁽³⁾(n; k, s) is the largest number of triples on n points containing no k points spanning s triples; §1 poses the question whether the lower bound lim inf n⁻² f⁽³⁾(n; k, k - 2) ≥ 1/6 is sharp in general, and Theorem 2 shows it is not for k = 5 (arXiv:1809.02100), https://arxiv.org/abs/1809.02100.

Stated but not proved: `MathlibExt.Combinatorics.LocallySparseTripleSystemErdosProblem1076Wanted.singleFamilyAsymptotic_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/LocallySparseTripleSystemErdosProblem1076Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LocallySparseTripleSystemErdosProblem1076Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/locally-sparse-triple-systems/index.html#single-family-asymptotic-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Locally sparse triple systems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/locally-sparse-triple-systems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/locally-sparse-triple-systems)
