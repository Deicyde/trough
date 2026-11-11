---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ShortestCommonSupersequence.ShortestCommonSupersequenceInstance, MetaMathlibExt.Complexity.NPComplete.ShortestCommonSupersequence.ShortestCommonSupersequenceFeasible, MetaMathlibExt.Complexity.NPComplete.ShortestCommonSupersequence.shortestCommonSupersequenceDec, MetaMathlibExt.Complexity.NPComplete.ShortestCommonSupersequence.shortestCommonSupersequence_npComplete
statement: formalized
---

# Shortest common supersequence

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/shortest-common-supersequence/index.html).

## Shortest common supersequence instances

An instance of SHORTEST COMMON SUPERSEQUENCE is a
pair $(R, K)$ of a list $R$ of binary strings (lists of booleans) and a natural number $K$, the
length bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ShortestCommonSupersequence.ShortestCommonSupersequenceInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ShortestCommonSupersequenceWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ShortestCommonSupersequenceWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/shortest-common-supersequence/index.html#shortest-common-supersequence-instance).

## Feasible shortest common supersequence instances

An instance $(R, K)$ of SHORTEST COMMON
SUPERSEQUENCE, a list $R$ of lists of booleans together with a natural number $K$, is feasible
when there is a list $w$ of booleans of length at most $K$ such that every list in $R$ is a
subsequence of $w$ (its entries occur in $w$ in the same order, not necessarily consecutively).

Formalized by `MetaMathlibExt.Complexity.NPComplete.ShortestCommonSupersequence.ShortestCommonSupersequenceFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ShortestCommonSupersequenceWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ShortestCommonSupersequenceWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/shortest-common-supersequence/index.html#shortest-common-supersequence-feasible).

## The SHORTEST COMMON SUPERSEQUENCE decision problem

SHORTEST COMMON SUPERSEQUENCE is the
decision problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding, to a pair $(R, K)$ of a list $R$ of lists of booleans and a natural number
$K$ for which some list of booleans of length at most $K$ has every list in $R$ as a subsequence.
Bitstrings that do not decode to such a pair are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ShortestCommonSupersequence.shortestCommonSupersequenceDec`, a definition declared in [WantedExt/Complexity/NPComplete/ShortestCommonSupersequenceWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ShortestCommonSupersequenceWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/shortest-common-supersequence/index.html#shortest-common-supersequence-dec).

## SHORTEST COMMON SUPERSEQUENCE is NP-complete

The SHORTEST COMMON SUPERSEQUENCE decision
problem over binary strings belongs to NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

## Sources

- K.-J. Räihä and E. Ukkonen, "The shortest common supersequence problem over binary alphabet is NP-complete", Theoretical Computer Science 16 (1981), 187-198. (D. Maier, "The complexity of some problems on subsequences and supersequences", JACM 25 (1978), 322-336, proves SCS only for a five- symbol alphabet; the binary case is Räihä-Ukkonen.)

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ShortestCommonSupersequence.shortestCommonSupersequence_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ShortestCommonSupersequenceWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ShortestCommonSupersequenceWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/shortest-common-supersequence/index.html#shortest-common-supersequence-np-complet).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shortest common supersequence](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/shortest-common-supersequence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/shortest-common-supersequence)
