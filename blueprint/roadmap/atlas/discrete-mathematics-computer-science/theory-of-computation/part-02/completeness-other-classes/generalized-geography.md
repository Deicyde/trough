---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.GeographyPSPACEComplete.GeoWins, MetaMathlibExt.Complexity.KeyTheorems.GeographyPSPACEComplete.geographyDec, MetaMathlibExt.Complexity.KeyTheorems.GeographyPSPACEComplete.geography_pspace_complete
statement: formalized
---

# Generalized geography

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/generalized-geography/index.html).

## Winning positions in Geography

Let $E$ be a list of pairs of natural numbers, read as
directed edges, let $v$ be a natural number (the current vertex) and let $V$ be a list of natural
numbers (the visited vertices). For a natural number $k$ (the fuel), the predicate
$\mathrm{GeoWins}(k, E, v, V)$ is defined by recursion on $k$: $\mathrm{GeoWins}(0, E, v, V)$ is
false, and $\mathrm{GeoWins}(k + 1, E, v, V)$ holds exactly when there is a natural number $w$
with $(v, w) \in E$ and $w \notin V$ such that $\mathrm{GeoWins}(k, E, w, V')$ is false, where
$V'$ is the list $V$ with $w$ added at the front.

Read as a game, the player to move wins when they can move the token along an edge of $E$ to a
vertex not in $V$ from which the opponent does not win; a player with no such move, or with no
fuel left, loses.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GeographyPSPACEComplete.GeoWins`, a definition declared in [WantedExt/Complexity/KeyTheorems/GeographyPSPACECompleteWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GeographyPSPACECompleteWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/generalized-geography/index.html#geo-wins).

## Geography as a decision problem

The Geography decision problem accepts a bitstring $x$
exactly when $x$ decodes, under the canonical bitstring encoding of triples $(n, E, s)$ of a
natural number, a list of pairs of natural numbers and a natural number, to a triple with
$s < n$, with both entries of every pair in $E$ less than $n$, and with
$\mathrm{GeoWins}(n + 1, E, s, [s])$, where $[s]$ is the list whose only entry is $s$.
Bitstrings that do not decode are rejected.

A play never revisits one of the $n$ vertices, so the fuel $n + 1$ never runs out: the condition
says that the player who moves first wins Geography on the directed graph with vertices
$0, \ldots, n - 1$ and edge list $E$, with the token starting on $s$ and $s$ marked visited.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GeographyPSPACEComplete.geographyDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/GeographyPSPACECompleteWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GeographyPSPACECompleteWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/generalized-geography/index.html#geography-dec).

## Geography is PSPACE-complete

The Geography decision problem belongs to PSPACE, and every
decision problem in PSPACE has a polynomial-time many-one reduction to it.

## Sources

- T. J. Schaefer, "On the complexity of some two- person perfect-information games", Journal of Computer and System Sciences 16 (1978), 185-225.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.GeographyPSPACEComplete.geography_pspace_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/GeographyPSPACECompleteWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GeographyPSPACECompleteWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/generalized-geography/index.html#geography-pspace-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized geography](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/generalized-geography/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/generalized-geography)
