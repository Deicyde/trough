---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.BicliqueEdgeCoverInstance, MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.WellFormed, MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.BicliqueEdgeCoverFeasible, MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.bicliqueEdgeCoverDec, MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.bicliqueEdgeCover_npComplete
statement: formalized
---

# Biclique edge cover

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/biclique-edge-cover/index.html).

## Biclique edge cover instances

An instance of BICLIQUE EDGE COVER is a tuple
$(L, R, E, K)$ of natural numbers $L$, $R$ and $K$ and a finite list $E$ of pairs of natural
numbers. Here $L$ counts the left vertices, $R$ counts the right vertices, each pair $(a, b)$ in
$E$ is an edge from left vertex $a$ to right vertex $b$, and $K$ is the bound on the number of
bicliques.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.BicliqueEdgeCoverInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/biclique-edge-cover/index.html#biclique-edge-cover-instance).

## Well-formed biclique edge cover instances

An instance $(L, R, E, K)$ of BICLIQUE EDGE
COVER is well formed when the list $E$ has no repeated entries and every pair $(a, b)$ in $E$
satisfies $a < L$ and $b < R$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/biclique-edge-cover/index.html#well-formed).

## Feasible biclique edge cover instances

An instance $(L, R, E, K)$ of BICLIQUE EDGE
COVER is feasible when there is a list of at most $K$ pairs $(A, B)$ of finite lists of natural
numbers, with every element of $A$ less than $L$ and every element of $B$ less than $R$, such
that for every pair $(u, v)$ in $E$ some listed pair $(A, B)$ has $u \in A$, $v \in B$ and
$(a, b)$ in $E$ for all $a \in A$ and $b \in B$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.BicliqueEdgeCoverFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/biclique-edge-cover/index.html#biclique-edge-cover-feasible).

## The biclique edge cover decision problem

BICLIQUE EDGE COVER is the decision problem
that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding
of biclique edge cover instances, to an instance that is well formed and feasible; it rejects
every bitstring that fails to decode.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.bicliqueEdgeCoverDec`, a definition declared in [WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/biclique-edge-cover/index.html#biclique-edge-cover-dec).

## BICLIQUE EDGE COVER is NP-complete

The biclique edge cover decision problem belongs to
NP, and every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), BICLIQUE COVER.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.BicliqueEdgeCover.bicliqueEdgeCover_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BicliqueEdgeCoverWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/biclique-edge-cover/index.html#biclique-edge-cover-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Biclique edge cover](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/biclique-edge-cover/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/biclique-edge-cover)
