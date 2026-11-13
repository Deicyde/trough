---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.LinearOrderingTournamentInstance, MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.WellFormed, MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.LinearOrderingTournamentFeasible, MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.linearOrderingTournamentDec, MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.linearOrderingTournament_npComplete
statement: formalized
---

# Linear ordering of tournaments

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/linear-ordering-of-tournaments/index.html).

## Tournament linear ordering instances

An instance of LINEAR ORDERING (TOURNAMENTS) is a
triple $(n, E, K)$ of a natural number $n$, the number of vertices, a list $E$ of ordered pairs
of natural numbers, the arcs, and a natural number $K$, the bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.LinearOrderingTournamentInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/linear-ordering-of-tournaments/index.html#linear-ordering-tournament-instance).

## Well-formed tournament linear ordering instances

An instance $(n, E, K)$ of LINEAR
ORDERING (TOURNAMENTS) is well formed when $n > 0$, $E$ has no repeated entries, every pair
$(a, b)$ in $E$ satisfies $a < n$, $b < n$, $a \ne b$ and $(b, a) \notin E$, and for all distinct
$a, b < n$ at least one of $(a, b)$ and $(b, a)$ lies in $E$. That is, $E$ is a tournament on the
vertices $0, \dots, n - 1$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/linear-ordering-of-tournaments/index.html#well-formed).

## Orderings with many forward arcs

An instance $(n, E, K)$ of LINEAR ORDERING
(TOURNAMENTS) is feasible when there are an ordering of the vertices $0, \dots, n - 1$ and a
subsequence $F$ of the list $E$ with at least $K$ entries such that for every pair $(a, b)$ in
$F$, the position of $a$ in the ordering is less than the position of $b$, where positions are
counted from $0$ and a number that does not occur in the ordering is given position $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.LinearOrderingTournamentFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/linear-ordering-of-tournaments/index.html#linear-ordering-tournament-feasible).

## LINEAR ORDERING (TOURNAMENTS) as a decision problem

The decision problem LINEAR
ORDERING (TOURNAMENTS) accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of triples of a natural number, a list of pairs of natural numbers and a
natural number, to an instance $(n, E, K)$ that is well formed ($n > 0$ and $E$ is a tournament
on the vertices $0, \dots, n - 1$ without repeated arcs) and feasible (some ordering of the
vertices has at least $K$ arcs of $E$ going forward). Bitstrings that do not decode, or that
decode to a malformed instance, are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.linearOrderingTournamentDec`, a definition declared in [WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/linear-ordering-of-tournaments/index.html#linear-ordering-tournament-dec).

## LINEAR ORDERING (TOURNAMENTS) is NP-complete

The decision problem LINEAR ORDERING
(TOURNAMENTS) on bitstrings lies in NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), LINEAR ORDERING; N. Alon, "Ranking tournaments" (2006) and the feedback arc set literature.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.LinearOrderingTournament.linearOrderingTournament_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LinearOrderingTournamentWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/linear-ordering-of-tournaments/index.html#linear-ordering-tournament-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear ordering of tournaments](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/linear-ordering-of-tournaments/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/linear-ordering-of-tournaments)
