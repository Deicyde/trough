---
declaration: section
origin: cited
lean: SimpleGraph.rookGraph, SimpleGraph.rookGraph_isDominating_iff
statement: formalized
---

# Domination in rook graphs

10 results, 2 proved and 8 whose declaration the Lean read here does not declare, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html).

## Rook graph

For natural numbers $n$ and $m$, the rook graph on the $n \times m$ board is the
simple graph whose vertices are the cells $(i, j)$ with $0 \le i < n$ and $0 \le j < m$, in which
two cells are adjacent if and only if they are distinct and lie in the same row (same $i$) or the
same column (same $j$).

Formalized by `SimpleGraph.rookGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/RookGraph.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/RookGraph.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-graph).

## Dominating sets of the rook graph

For natural numbers $n$ and $m$, a finite set $S$ of
cells of the $n \times m$ board dominates the rook graph on that board if and only if for every
cell $(i, j)$, some cell of $S$ lies in row $i$ or some cell of $S$ lies in column $j$.

Formalized by `SimpleGraph.rookGraph_isDominating_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/RookGraph.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/RookGraph.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-graph-is-dominating-iff).

## Rook placements covering all rows and columns

For natural numbers $n$, $m$ and $k$,
$E_{n,m}(k)$ is the number of $k$-element sets of cells of the $n \times m$ board that contain a
cell in every row and a cell in every column (Mertens' $E_{n,m}(k)$).

Formalized by `MathlibExt.GraphTheory.RookDominationPolynomialWanted.rookCoverCount`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-cover-count).

## Dominating rook placements

For natural numbers $n$, $m$ and $k$, $d_{n,m}(k)$ is the
number of $k$-element sets of cells of the $n \times m$ board that are dominating sets of the rook
graph on that board (Mertens' $d_{R_{n,m}}(k)$).

Formalized by `MathlibExt.GraphTheory.RookDominationPolynomialWanted.rookDominatingCount`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-dominating-count).

## Domination polynomial of the rook graph

For natural numbers $n$ and $m$, the rook
domination polynomial of the $n \times m$ board is the integer polynomial
$D_{n,m}(x) = \sum_{k=0}^{nm} d_{n,m}(k)\, x^k$, where $d_{n,m}(k)$ is the number of $k$-element
sets of cells of the $n \times m$ board that are dominating sets of the rook graph on that
board.

Formalized by `MathlibExt.GraphTheory.RookDominationPolynomialWanted.rookDominationPolynomial`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-domination-polynomial).

## Dominating rook placements via covering placements

For natural numbers $n, m \ge 1$ and
$k$, let $d_{n,m}(k)$ be the number of $k$-element sets of cells of the $n \times m$ board that
are dominating sets of the rook graph on that board, and let $E_{a,b}(k)$ be the number of
$k$-element sets of cells of the $a \times b$ board that contain a cell in every row and a cell
in every column. Then

$$d_{n,m}(k) = \binom{nm}{k} -
\sum_{r=1}^{n} \sum_{c=1}^{m} \binom{n}{r} \binom{m}{c} E_{n-r,m-c}(k).$$

## Sources

- Stephan Mertens, "Domination Polynomial of the Rook Graph", Theorem 1 (`thm:R-E`).

Formalized by `MathlibExt.GraphTheory.RookDominationPolynomialWanted.rookDominatingCount_eq_choose_sub_sum_rookCoverCount`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-dominating-count-eq-choose-sub-sum).

## Recursion for rook placements covering all rows and columns

For natural numbers
$n, m \ge 1$ and $k$, let $E_{a,b}(k)$ denote the number of $k$-element sets of cells of the
$a \times b$ board that contain a cell in every row and a cell in every column. Then

$$E_{n,m}(k) = \binom{nm}{k} -
\sum_{(r,c) \ne (0,0)} \binom{n}{r} \binom{m}{c} E_{n-r,m-c}(k),$$

where the sum runs over all pairs $(r, c) \ne (0, 0)$ with $0 \le r \le n$ and $0 \le c \le m$.

## Sources

- Stephan Mertens, "Domination Polynomial of the Rook Graph", Theorem 2 (`thm:E-recursion`).

Formalized by `MathlibExt.GraphTheory.RookDominationPolynomialWanted.rookCoverCount_eq_choose_sub_sum_rookCoverCount`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-cover-count-eq-choose-sub-sum-rook).

## Dominating rook placements at high density

For natural numbers $n, m \ge 1$ and $k$ with
$k > nm - n - m - \min(n, m) + 2$, let $d_{n,m}(k)$ be the number of $k$-element sets of cells
of the $n \times m$ board that are dominating sets of the rook graph on that board. Then

$$d_{n,m}(k) = \binom{nm}{k} - nm \binom{(n-1)(m-1)}{k}.$$

## Sources

- Stephan Mertens, "Domination Polynomial of the Rook Graph", Corollary 3 (`cor:high-density`).

Formalized by `MathlibExt.GraphTheory.RookDominationPolynomialWanted.rookDominatingCount_eq_choose_sub_mul_choose`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-dominating-count-eq-choose-sub-mul).

## Single-sum formula for the rook domination polynomial

For natural numbers $n, m \ge 1$,
the rook domination polynomial $D_{n,m}(x)$ of the $n \times m$ board, an integer polynomial,
satisfies

$$D_{n,m}(x) = ((1+x)^n - 1)^m -
(-1)^m \sum_{k=0}^{m-1} (-1)^k \binom{m}{k} ((1+x)^k - 1)^n.$$

## Sources

- Stephan Mertens, "Domination Polynomial of the Rook Graph", Theorem 4 (`thm:domination-polynomial`).

Formalized by `MathlibExt.GraphTheory.RookDominationPolynomialWanted.rookDominationPolynomial_eq`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-domination-polynomial-eq).

## Symmetric formula for the rook domination polynomial

For natural numbers $n, m \ge 1$,
the rook domination polynomial $D_{n,m}(x)$ of the $n \times m$ board, an integer polynomial,
satisfies

$$D_{n,m}(x) = ((1+x)^n - 1)^m + ((1+x)^m - 1)^n -
(-1)^{n+m} \sum_{\ell=0}^{n} \sum_{k=0}^{m} (-1)^{k+\ell}
\binom{n}{\ell} \binom{m}{k} (1+x)^{k\ell}.$$

## Sources

- Stephan Mertens, "Domination Polynomial of the Rook Graph", Corollary 5 (`cor:domination-polynomial`).

Formalized by `MathlibExt.GraphTheory.RookDominationPolynomialWanted.rookDominationPolynomial_eq_symmetric`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html#rook-domination-polynomial-eq-symmetric).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Domination in rook graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/independence-and-domination/domination-in-rook-graphs)
