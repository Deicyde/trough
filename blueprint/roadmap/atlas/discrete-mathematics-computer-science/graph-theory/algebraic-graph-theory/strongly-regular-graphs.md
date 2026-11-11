---
declaration: section
origin: cited
lean: SimpleGraph.IsSRGWith.adj_of_adj_of_adj_of_mu_zero, SimpleGraph.IsSRGWith.nonprincipal_eigenvalue_quadratic, MathlibExt.Combinatorics.SimpleGraph.StronglyRegularWanted.srg_connected_mu_zero_complete, MathlibExt.Combinatorics.SimpleGraph.StronglyRegularWanted.srg_reachable_eq_or_adj_mu_zero, MathlibExt.Combinatorics.SimpleGraph.StronglyRegularWanted.srg_nonprincipal_eigenvalue_quadratic
statement: formalized
proof: formalized
---

# Strongly regular graphs

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/strongly-regular-graphs/index.html).

## Two-edge paths close into triangles when μ = 0

Let $G$ be a finite strongly regular
graph with parameters $(n, k, \ell, \mu)$ where $\mu = 0$: $G$ has $n$ vertices, every vertex
has degree $k$, any two adjacent vertices have exactly $\ell$ common neighbors, and any two
distinct nonadjacent vertices have no common neighbor. If $u$, $v$, $w$ are vertices of $G$
such that $u$ is adjacent to $v$, $v$ is adjacent to $w$, and $u \neq w$, then $u$ is adjacent
to $w$.

Formalized by `SimpleGraph.IsSRGWith.adj_of_adj_of_adj_of_mu_zero`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/strongly-regular-graphs/index.html#adj-of-adj-of-adj-of-mu-zero).

## Non-principal eigenvalues of a strongly regular graph

Let $G$ be a finite strongly
regular graph with parameters $(n, k, \ell, \mu)$: $G$ has $n$ vertices, every vertex has degree
$k$, any two adjacent vertices have exactly $\ell$ common neighbors, and any two distinct
nonadjacent vertices have exactly $\mu$ common neighbors. Let $A$ be the adjacency matrix of $G$
over $\mathbb{C}$. Then every eigenvalue $x \in \mathbb{C}$ of $A$ with $x \neq k$ satisfies
$x^2 = (\ell - \mu) x + (k - \mu)$.

Formalized by `SimpleGraph.IsSRGWith.nonprincipal_eigenvalue_quadratic`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/strongly-regular-graphs/index.html#nonprincipal-eigenvalue-quadratic).

## Connected strongly regular graphs with μ = 0 are complete

Let $G$ be a finite strongly
regular graph with parameters $(n, k, \ell, \mu)$ where $\mu = 0$: $G$ has $n$ vertices, every
vertex has degree $k$, any two adjacent vertices have exactly $\ell$ common neighbors, and any
two distinct nonadjacent vertices have no common neighbor. If $G$ is connected, then $G$ is
complete, that is, any two distinct vertices of $G$ are adjacent.

Proof: The $\mu = 0$ common-neighbor count makes every nontrivial two-edge walk a
triangle, so walk induction makes each component a clique. Connectedness then
gives completeness. Brouwer and Haemers, Section 9.1.4, state the component
fact: $\mu = 0$ makes the graph a disjoint union of complete graphs.

## Sources

- A. E. Brouwer and W. H. Haemers, Spectra of Graphs, Springer 2012, Ch. 9 (disconnected and complete strongly regular graphs); C. Godsil and G. Royle, Algebraic Graph Theory, GTM 207, Ch. 10.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.StronglyRegularWanted.srg_connected_mu_zero_complete`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/strongly-regular-graphs/index.html#srg-connected-mu-zero-complete).

## Components of a strongly regular graph with μ = 0 are cliques

Let $G$ be a finite strongly
regular graph with parameters $(n, k, \ell, \mu)$ where $\mu = 0$: $G$ has $n$ vertices, every
vertex has degree $k$, any two adjacent vertices have exactly $\ell$ common neighbors, and any
two distinct nonadjacent vertices have no common neighbor. If $v$ and $w$ are vertices of $G$
joined by a walk, then $v = w$ or $v$ and $w$ are adjacent. Thus each connected component of
$G$ is a clique.

Without $\mu = 0$ this is false: two nonadjacent vertices of the 5-cycle, a strongly regular
graph with parameters $(5, 2, 0, 1)$, are joined by a walk but are neither equal nor adjacent.

Proof: Induct on a witnessing walk and close each two-edge segment using the
zero common-neighbor count. Brouwer and Haemers, Section 9.1.4, state the
result: $\mu = 0$ makes the graph a disjoint union of complete graphs.

## Sources

- A. E. Brouwer and W. H. Haemers, Spectra of Graphs, Springer 2012, Ch. 9 (a disconnected strongly regular graph is a disjoint union of complete graphs); C. Godsil and G. Royle, Algebraic Graph Theory, GTM 207, Ch. 10.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.StronglyRegularWanted.srg_reachable_eq_or_adj_mu_zero`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/strongly-regular-graphs/index.html#srg-reachable-eq-or-adj-mu-zero).

## Non-principal eigenvalues of a connected non-complete strongly regular graph

Let $G$ be a
finite strongly regular graph with parameters $(n, k, \ell, \mu)$: $G$ has $n$ vertices, every
vertex has degree $k$, any two adjacent vertices have exactly $\ell$ common neighbors, and any
two distinct nonadjacent vertices have exactly $\mu$ common neighbors. Suppose that $G$ is
connected and not complete, and let $A$ be its adjacency matrix over $\mathbb{C}$. Then every
eigenvalue $x \in \mathbb{C}$ of $A$ with $x \neq k$ satisfies $x^2 = (\ell - \mu) x + (k - \mu)$.

Proof: Apply the identity $A^2 = kI + \ell A + \mu \bar{A}$, where $I$ is the identity matrix
and $\bar{A}$ is the adjacency matrix of the complement of $G$, to an eigenvector $v$ for $x$;
regularity makes the coordinate sum of $v$ zero, so $\bar{A} v = -(1 + x) v$, and this gives
the quadratic. This is the proof of Theorem 9.1.2, (ii) ⇒ (iii), in Brouwer and Haemers,
Section 9.1.3.

## Sources

- A. E. Brouwer and W. H. Haemers, Spectra of Graphs, Springer 2012, Ch. 9, eigenvalues of strongly regular graphs; C. Godsil and G. Royle, Algebraic Graph Theory, GTM 207, Ch. 10 (eigenvalues of strongly regular graphs).

Formalized by `MathlibExt.Combinatorics.SimpleGraph.StronglyRegularWanted.srg_nonprincipal_eigenvalue_quadratic`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/StronglyRegular.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/strongly-regular-graphs/index.html#srg-nonprincipal-eigenvalue-quadratic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strongly regular graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/strongly-regular-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/strongly-regular-graphs)
