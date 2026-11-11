---
declaration: section
origin: cited
lean: MetaMathlibExt.DominationState, MetaMathlibExt.dominationPolynomial, MetaMathlibExt.vertexDominationState, MetaMathlibExt.IsDominationSignature, MetaMathlibExt.DominationSignature, MetaMathlibExt.allCoveredSignature, MetaMathlibExt.DominationCompatible, MetaMathlibExt.occupiedCount
statement: formalized
---

# Domination polynomials of grids

20 results, 15 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html).

## Domination states

A domination state is one of three labels: uncovered, covered or
occupied.

Relative to a set $S$ of vertices of a graph, a vertex is occupied if it lies in $S$, covered if
it lies outside $S$ but is adjacent to a vertex of $S$, and uncovered otherwise.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 1.

Formalized by `MetaMathlibExt.DominationState`, an inductive type declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-state).

## Domination polynomial

For a finite graph $G$, the domination polynomial of $G$ is the
polynomial $\sum_S z^{|S|}$ with integer coefficients, the sum running over the dominating sets
$S$ of $G$.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Section 1.

Formalized by `MetaMathlibExt.dominationPolynomial`, a definition declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-polynomial).

## Domination state of a vertex

Let $G$ be a simple graph, $S$ a finite set of vertices of
$G$ and $v$ a vertex of $G$. The domination state of $v$ relative to $S$ in $G$ is occupied if
$v \in S$, covered if $v \notin S$ and $v$ is adjacent in $G$ to some vertex of $S$, and
uncovered otherwise.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 1.

Formalized by `MetaMathlibExt.vertexDominationState`, a definition declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#vertex-domination-state).

## Domination signature

Let $R$ be a simple graph on a vertex set $V$ (the row). A map
$\sigma$ assigning to each vertex of $V$ a domination state (uncovered, covered or occupied) is a
signature for $R$ if no uncovered vertex is adjacent in $R$ to an occupied vertex: for all
vertices $i, j$ adjacent in $R$, it is not the case that $\sigma(i)$ is uncovered and $\sigma(j)$
is occupied.

When $R$ is the path on $m$ vertices, signatures are the strings of length $m$ in which no
uncovered entry is next to an occupied one; when $R$ is the cycle on $m$ vertices the condition
also applies to the first and last entries (the paper's cyclic signatures).

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 3.

Formalized by `MetaMathlibExt.IsDominationSignature`, a definition declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#is-domination-signature).

## Signatures of a row graph

For a simple graph $R$ on a vertex set $V$ (the row), a
signature of $R$ is a map $\sigma$ assigning to each vertex of $V$ a domination state (uncovered,
covered or occupied) such that $\sigma$ is a domination signature for $R$, that is, no uncovered
vertex is adjacent in $R$ to an occupied vertex. This is the type of all signatures of $R$; when
$R$ is a cycle they are the paper's cyclic signatures.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 3.

Formalized by `MetaMathlibExt.DominationSignature`, a definition declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-signature).

## All-covered signature

For a graph $R$ (the row), the all-covered signature
$\sigma_\bullet$ of $R$ is the signature that gives every vertex of $R$ the state covered; it
is a signature because it has no uncovered vertex.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Theorem 7.

Formalized by `MetaMathlibExt.allCoveredSignature`, a definition declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#all-covered-signature).

## Compatible row signatures

Let $R$ be a graph (the row) and let $\sigma$ and $\tau$
assign a domination state (uncovered, covered or occupied) to each vertex of $R$. The new row
$\tau$ is compatible with the previous row $\sigma$ when, for every vertex $i$ of $R$: if
$\sigma(i)$ is uncovered then $\tau(i)$ is occupied; if $\sigma(i)$ is occupied then $\tau(i)$
is not uncovered; and if $\tau(i)$ is covered then $\sigma(i)$ is occupied or some neighbour $j$
of $i$ in $R$ has $\tau(j)$ occupied.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 5.

Formalized by `MetaMathlibExt.DominationCompatible`, a definition declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-compatible).

## Number of occupied vertices

Let $V$ be a finite set and let $\sigma$ assign a domination
state (uncovered, covered or occupied) to each element of $V$. The occupied count
$\operatorname{occ}(\sigma)$ is the number of elements $i \in V$ such that $\sigma(i)$ is occupied.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 6.

Formalized by `MetaMathlibExt.occupiedCount`, a definition declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#occupied-count).

## Domination transfer matrix

Let $R$ be a simple graph on a finite vertex set (the row).
The transfer matrix $A$ of $R$ is the matrix with entries in $\mathbb{Z}[z]$, rows indexed by the
new signature $\tau$ and columns by the old signature $\sigma$, both ranging over the signatures
of $R$, whose entry $A_{\tau\sigma}$ is $z^{\operatorname{occ}(\tau)}$ if $\tau$ is compatible
with $\sigma$ and $0$ otherwise; here $\operatorname{occ}(\tau)$ is the number of occupied
vertices of $\tau$. When $R$ is the cycle on $m$ vertices this is Mertens' matrix $\bar A$.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 6.

Formalized by `MetaMathlibExt.dominationTransferMatrix`, a definition declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-transfer-matrix).

## Almost dominating polynomial

Let $R$ be a finite graph (the row), $n$ a natural number
and $\sigma$ an assignment of a domination state to each vertex of $R$. Let $H$ be the box
product of $R$ with the path on the vertices $0, \dots, n$, so that the last row of $H$ consists
of the vertices $(i, n)$. Relative to a vertex set $S$ of $H$, a vertex is occupied if it lies in
$S$, covered if it lies outside $S$ but is adjacent to a vertex of $S$, and uncovered otherwise.
The almost dominating polynomial $G^\sigma(z)$ is the polynomial $\sum_S z^{|S|}$ with integer
coefficients, the sum running over the vertex sets $S$ of $H$ such that no vertex of $H$ outside
the last row is uncovered and every vertex $(i, n)$ of the last row has state $\sigma(i)$.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 2.

Formalized by `MetaMathlibExt.almostDominatingPolynomial`, a definition declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#almost-dominating-polynomial).

## A vertex is occupied exactly when it lies in the set

Let $G$ be a simple graph, $S$ a
finite set of vertices of $G$ and $v$ a vertex of $G$. Then the domination state of $v$ relative
to $S$ in $G$ is occupied if and only if $v \in S$.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 1.

Formalized by `MetaMathlibExt.vertexDominationState_eq_occupied_iff`, a theorem declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#vertex-domination-state-eq-occupied-iff).

## Dominating sets have no uncovered vertex

Let $G$ be a simple graph and $S$ a finite set
of vertices of $G$. Then $S$ dominates $G$ if and only if no vertex of $G$ has domination state
uncovered relative to $S$ in $G$.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Definition 1.

Formalized by `MetaMathlibExt.isDominating_iff_forall_vertexDominationState_ne_uncovered`, a theorem declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#is-dominating-iff-forall-vertex-dominati).

## The domination polynomial at one counts dominating sets

For every finite graph $G$, the
value at $1$ of the domination polynomial of $G$ equals the number of dominating sets of $G$.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Section 1.

Formalized by `MetaMathlibExt.dominationPolynomial_eval_one`, a theorem declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-polynomial-eval-one).

## The all-covered signature has no occupied vertex

For every simple graph $R$ on a finite
vertex set, the number of occupied vertices of the all-covered signature of $R$ is $0$.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Theorem 7.

Formalized by `MetaMathlibExt.occupiedCount_allCoveredSignature`, a theorem declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#occupied-count-all-covered-signature).

## Transfer matrix column of the all-covered signature

Let $R$ be a simple graph on a
finite vertex set (the row), let $A$ be its domination transfer matrix, with entries in
$\mathbb{Z}[z]$, and let $\sigma_\bullet$ be its all-covered signature. For every signature $\tau$
of $R$, the entry $A_{\tau\sigma_\bullet}$ equals $z^{\operatorname{occ}(\tau)}$, where
$\operatorname{occ}(\tau)$ is the number of occupied vertices of $\tau$, if every covered vertex of
$\tau$ is adjacent in $R$ to an occupied vertex of $\tau$, and equals $0$ otherwise.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Theorem 7.

Formalized by `MetaMathlibExt.dominationTransferMatrix_apply_allCoveredSignature`, a theorem declared in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-transfer-matrix-apply-all-cov).

## Grid domination polynomial as a sum of almost dominating polynomials

For all natural
numbers $m$ and $n$, let $P_k$ denote the path on the vertices $0, \dots, k - 1$. Then the
domination polynomial of the grid $P_m \mathbin{\square} P_{n+1}$ equals $\sum_\sigma G^\sigma(z)$,
the sum running over the signatures $\sigma$ of the row graph $P_m$ with no uncovered vertex,
where $G^\sigma(z)$ is the almost dominating polynomial of $P_m$ with $n + 1$ rows and last-row
state $\sigma$.

The grid is taken with at least one row, so that the last row carrying $\sigma$ exists.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Lemma 4 (`jis-2024-24.7.6-lem-4`).

Stated but not proved: `MetaMathlibExt.dominationPolynomial_grid_eq_sum_almostDominatingPolynomial` is written with `theorem_wanted` in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-polynomial-grid-eq-sum-almost).

## Cylinder domination polynomial as a sum of almost dominating polynomials

For all
natural numbers $m$ and $n$, let $C_m$ be the cycle graph on the vertices $0, \dots, m - 1$, in
which distinct $i$ and $j$ are adjacent when $i - j \equiv \pm 1 \pmod m$, and let $P_{n+1}$ be
the path on the vertices $0, \dots, n$. Then the domination polynomial of the cylinder
$C_m \mathbin{\square} P_{n+1}$ equals $\sum_\sigma G^\sigma(z)$, the sum running over the
signatures $\sigma$ of the row graph $C_m$ with no uncovered vertex, where $G^\sigma(z)$ is the
almost dominating polynomial of $C_m$ with $n + 1$ rows and last-row state $\sigma$.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Lemma 4 (`jis-2024-24.7.6-lem-4`).

Stated but not proved: `MetaMathlibExt.dominationPolynomial_cylinder_eq_sum_almostDominatingPolynomial` is written with `theorem_wanted` in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-polynomial-cylinder-eq-sum-al).

## Transfer-matrix formula for the domination polynomial of the grid

For all natural
numbers $m$ and $n$, let $P_k$ denote the path on the vertices $0, \dots, k - 1$, let $A$ be the
domination transfer matrix of the row graph $P_m$, indexed by the signatures of $P_m$, and let
$\sigma_\bullet$ be the all-covered signature. Then the domination polynomial of the grid
$P_m \mathbin{\square} P_n$ is

$$\sum_\sigma (A^n)_{\sigma, \sigma_\bullet},$$

the sum running over the signatures $\sigma$ of $P_m$ with no uncovered vertex.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Theorem 7 (`jis-2024-24.7.6-thm-7`).

Stated but not proved: `MetaMathlibExt.dominationPolynomial_grid_eq_sum_transferMatrix_pow` is written with `theorem_wanted` in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-polynomial-grid-eq-sum-transf).

## Transfer-matrix formula for the domination polynomial of the cylinder

For all natural
numbers $m$ and $n$, let $C_m$ be the cycle graph on the vertices $0, \dots, m - 1$, in which
distinct $i$ and $j$ are adjacent when $i - j \equiv \pm 1 \pmod m$, and let $P_n$ be the path on
the vertices $0, \dots, n - 1$. Let $\bar A$ be the domination transfer matrix of the row graph
$C_m$, indexed by the signatures of $C_m$, and let $\sigma_\bullet$ be the all-covered signature.
Then the domination polynomial of the cylinder $C_m \mathbin{\square} P_n$ is

$$\sum_\sigma (\bar A^n)_{\sigma, \sigma_\bullet},$$

the sum running over the signatures $\sigma$ of $C_m$ with no uncovered vertex.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Theorem 7 (`jis-2024-24.7.6-thm-7`).

Stated but not proved: `MetaMathlibExt.dominationPolynomial_cylinder_eq_sum_transferMatrix_pow` is written with `theorem_wanted` in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-polynomial-cylinder-eq-sum-tr).

## Transfer-matrix formula for the domination polynomial of the torus

For all natural
numbers $m$ and $n$ with $n \ge 1$, let $C_k$ denote the cycle graph on the vertices
$0, \dots, k - 1$, in which distinct $i$ and $j$ are adjacent when $i - j \equiv \pm 1 \pmod k$,
and let $\bar A$ be the domination transfer matrix of the row graph $C_m$. Then the domination
polynomial of the torus $C_m \mathbin{\square} C_n$ equals the trace of $\bar A^n$.

The hypothesis $n \ge 1$ is needed: for $n = 0$ the trace counts the signatures of $C_m$, while
the torus $C_m \mathbin{\square} C_0$ has no vertices, so its domination polynomial is $1$. For
$n = 1$ and $n = 2$ the cycle $C_n$ is a single vertex and a single edge respectively.

## Sources

- Stephan Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, Theorem 8 (`jis-2024-24.7.6-thm-8`).

Stated but not proved: `MetaMathlibExt.dominationPolynomial_torus_eq_trace_transferMatrix_pow` is written with `theorem_wanted` in [WantedExt/GraphTheory/GridDominationTransferWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/GridDominationTransferWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html#domination-polynomial-torus-eq-trace-tra).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Domination polynomials of grids](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/independence-and-domination/domination-polynomials-of-grids)
