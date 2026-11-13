---
declaration: section
origin: cited
lean: MetaMathlibExt.clawFree, MetaMathlibExt.independence_poly_of_claw_free_splits, MetaMathlibExt.clawFree_iff_not_isIndContained, MetaMathlibExt.independencePoly_coeff, MetaMathlibExt.aeval_independencePoly, MetaMathlibExt.independencePoly_bot, MetaMathlibExt.independencePoly_top, SimpleGraph.IsClawFree
statement: formalized
proof: formalized
---

# Independence polynomial of claw-free graphs

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html).

## Claw-free graphs and independence polynomials

## Claw-free finite graph

A simple graph $G$ on a finite vertex set $V$ is claw-free if it
has no induced claw $K_{1,3}$: there are no vertices $c, \ell_1, \ell_2, \ell_3 \in V$ such that
$\ell_1, \ell_2, \ell_3$ are pairwise distinct, each is adjacent to $c$ and different from $c$,
and no two of them are adjacent.

## Sources

- Moussa Benoumhani, "On the Modes of the Independence Polynomial of the Centipede," Journal of Integer Sequences 15 (2012), Article 12.5.1, unnumbered Chudnovsky–Seymour theorem, lines 142–144, https://cs.uwaterloo.ca/journals/JIS/VOL15/Benoumhani/benoumhani8.tex quoting M. Chudnovsky and P. Seymour, "The roots of the independence polynomial of a clawfree graph," J. Combin. Theory Ser. B 97 (2007), 350–357 (biblio lines 499–501).

Formalized by `MetaMathlibExt.clawFree`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#claw-free).

## Chudnovsky–Seymour theorem

Let $G$ be a claw-free simple graph on a finite vertex set
$V$, and let $I(G) = \sum_{k=0}^{|V|} i_k X^k \in \mathbb{Z}[X]$ be its independence polynomial,
where $i_k$ is the number of independent sets of $G$ with $k$ vertices. Then $I(G)$, viewed as a
polynomial with real coefficients, splits over $\mathbb{R}$: it is a constant times a product of
linear factors $X - r$ with $r \in \mathbb{R}$, so all its roots are real.

## Sources

- Moussa Benoumhani, "On the Modes of the Independence Polynomial of the Centipede," Journal of Integer Sequences 15 (2012), Article 12.5.1, unnumbered Chudnovsky–Seymour theorem, lines 142–144, https://cs.uwaterloo.ca/journals/JIS/VOL15/Benoumhani/benoumhani8.tex quoting M. Chudnovsky and P. Seymour, "The roots of the independence polynomial of a clawfree graph," J. Combin. Theory Ser. B 97 (2007), 350–357 (biblio lines 499–501).

Formalized by `MetaMathlibExt.independence_poly_of_claw_free_splits`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 2066](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L2066). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#independence-poly-of-claw-free-splits).

## Claw-free finite graphs have no induced claw

Let $G$ be a simple graph on a finite
vertex set. Then $G$ is claw-free if and only if the claw $K_{1,3}$, the star graph on four
vertices whose center is adjacent to the other three, is not an induced subgraph of $G$, that is,
there is no injective map from its vertices to those of $G$ that preserves both adjacency and
nonadjacency.

Formalized by `MetaMathlibExt.clawFree_iff_not_isIndContained`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 2078](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L2078). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#claw-free-iff-not-is-ind-contained).

## Coefficients of the independence polynomial

Let $G$ be a simple graph on a finite vertex
set $V$, and let $I(G) = \sum_{k=0}^{|V|} i_k X^k \in \mathbb{Z}[X]$ be its independence
polynomial, where $i_k$ is the number of independent sets of $G$ with $k$ vertices. Then for every
natural number $k$, the coefficient of $X^k$ in $I(G)$ is the number of independent sets of $G$
with exactly $k$ vertices.

Formalized by `MetaMathlibExt.independencePoly_coeff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 2152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L2152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#independence-poly-coeff).

## Evaluating the independence polynomial

Let $G$ be a simple graph on a finite vertex set
$V$, and let $I(G) = \sum_{k=0}^{|V|} i_k X^k \in \mathbb{Z}[X]$ be its independence polynomial,
where $i_k$ is the number of independent sets of $G$ with $k$ vertices. Then for every element
$x$ of a commutative ring $R$, the value of $I(G)$ at $x$ is $\sum_S x^{|S|}$, the sum running
over all independent sets $S \subseteq V$ of $G$, the empty set included.

Formalized by `MetaMathlibExt.aeval_independencePoly`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 2204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L2204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#aeval-independence-poly).

## Independence polynomial of the edgeless graph

Let $V$ be a finite set. For a simple
graph $G$ on $V$, let $I(G) = \sum_{k=0}^{|V|} i_k X^k \in \mathbb{Z}[X]$ be its independence
polynomial, where $i_k$ is the number of independent sets of $G$ with $k$ vertices. If $G$ is the
graph on $V$ with no edges, then $I(G) = (1 + X)^{|V|}$.

Formalized by `MetaMathlibExt.independencePoly_bot`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 2272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L2272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#independence-poly-bot).

## Independence polynomial of the complete graph

Let $V$ be a finite set. For a simple
graph $G$ on $V$, let $I(G) = \sum_{k=0}^{|V|} i_k X^k \in \mathbb{Z}[X]$ be its independence
polynomial, where $i_k$ is the number of independent sets of $G$ with $k$ vertices. If $G$ is the
complete graph on $V$, then $I(G) = 1 + |V|\,X$.

Formalized by `MetaMathlibExt.independencePoly_top`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 2299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L2299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#independence-poly-top).

## Claw-free graph

A simple graph $G$ on a vertex set $V$, not necessarily finite, is
claw-free if it has no induced claw $K_{1,3}$: there are no vertices
$c, \ell_1, \ell_2, \ell_3 \in V$ such that $\ell_1, \ell_2, \ell_3$ are pairwise distinct, each
is adjacent to $c$ and different from $c$, and no two of them are adjacent.

Formalized by `SimpleGraph.IsClawFree`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 2393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L2393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#is-claw-free).

## Claw-free graphs have no induced claw

Let $G$ be a simple graph on an arbitrary vertex
set. Then $G$ is claw-free if and only if the claw $K_{1,3}$, the star graph on four vertices
whose center is adjacent to the other three, is not an induced subgraph of $G$, that is, there is
no injective map from its vertices to those of $G$ that preserves both adjacency and
nonadjacency.

Formalized by `SimpleGraph.isClawFree_iff_not_isIndContained`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 2399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L2399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#is-claw-free-iff-not-is-ind-contained).

## The two definitions of claw-free agree

A simple graph on a finite vertex set is a
claw-free finite graph if and only if it is a claw-free graph in the sense defined for graphs on
arbitrary vertex sets.

Formalized by `MetaMathlibExt.clawFree_iff_isClawFree`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean, line 2475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ClawFreeIndependencePoly.lean#L2475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html#claw-free-iff-is-claw-free).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Independence polynomial of claw-free graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/independence-and-domination/independence-polynomial-of-claw-free-graphs)
