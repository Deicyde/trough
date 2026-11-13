---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.MatchingInP.matchingDec, MetaMathlibExt.Complexity.KeyTheorems.MatchingInP.matching_in_p
statement: formalized
---

# Matching in general graphs

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/matching-in-general-graphs/index.html).

## General matching decision problem

The decision problem that accepts a bitstring $x$
exactly when $x$ decodes, under the canonical bitstring encoding, to a triple $(n, E, K)$ of a
natural number $n$, a list $E$ of pairs of natural numbers and a natural number $K$ such that
every pair $(u, v)$ in $E$ has $u < n$, $v < n$ and $u \neq v$, and some sublist $M$ of $E$
(a subsequence, keeping the order of $E$) with no repeated entries and length at least $K$ has
the property that any two different pairs $(u_1, v_1)$ and $(u_2, v_2)$ in $M$ share no
element: $u_1, v_1 \notin \{u_2, v_2\}$. Bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MatchingInP.matchingDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/MatchingInPWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MatchingInPWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/matching-in-general-graphs/index.html#matching-dec).

## General matching is in P (Edmonds' blossom algorithm)

The general matching decision
problem belongs to the complexity class P. This is the problem of deciding, for a vertex count
$n$, a list $E$ of edges joining distinct vertices below $n$ and a target $K$, encoded as a
bitstring, whether $E$ contains at least $K$ distinct pairwise vertex-disjoint edges.

## Sources

- J. Edmonds, "Paths, trees, and flowers", Canadian Journal of Mathematics 17 (1965), 449-467.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.MatchingInP.matching_in_p` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MatchingInPWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MatchingInPWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/matching-in-general-graphs/index.html#matching-in-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matching in general graphs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/matching-in-general-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/matching-in-general-graphs)
