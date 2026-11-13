---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.LongestCommonSubsequence.LongestCommonSubsequenceInstance, MetaMathlibExt.Complexity.NPComplete.LongestCommonSubsequence.LongestCommonSubsequenceFeasible, MetaMathlibExt.Complexity.NPComplete.LongestCommonSubsequence.longestCommonSubsequenceDec, MetaMathlibExt.Complexity.NPComplete.LongestCommonSubsequence.longestCommonSubsequence_npComplete
statement: formalized
---

# Longest common subsequence of many strings

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/longest-common-subsequence-of-many-strings/index.html).

## Longest-common-subsequence instances

A longest-common-subsequence instance is a pair
$(R, K)$ of a finite list $R$ of binary strings (finite lists of booleans) and a natural number
$K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestCommonSubsequence.LongestCommonSubsequenceInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/LongestCommonSubsequenceWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestCommonSubsequenceWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/longest-common-subsequence-of-many-strings/index.html#longest-common-subsequence-instance).

## Feasible longest-common-subsequence instances

A longest-common-subsequence instance
$(R, K)$ is feasible when there is a binary string $w$ of length at least $K$ that is a
subsequence of every string in $R$, that is, $w$ is obtained from each string in $R$ by deleting
some of its entries.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestCommonSubsequence.LongestCommonSubsequenceFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/LongestCommonSubsequenceWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestCommonSubsequenceWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/longest-common-subsequence-of-many-strings/index.html#longest-common-subsequence-feasible).

## The LONGEST COMMON SUBSEQUENCE decision problem

LONGEST COMMON SUBSEQUENCE is the
decision problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding, to a feasible longest-common-subsequence instance. Bitstrings that do not
decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestCommonSubsequence.longestCommonSubsequenceDec`, a definition declared in [WantedExt/Complexity/NPComplete/LongestCommonSubsequenceWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestCommonSubsequenceWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/longest-common-subsequence-of-many-strings/index.html#longest-common-subsequence-dec).

## LONGEST COMMON SUBSEQUENCE is NP-complete

The LONGEST COMMON SUBSEQUENCE decision
problem, over binary strings, belongs to NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), LONGEST COMMON SUBSEQUENCE; D. Maier, "The complexity of some problems on subsequences and supersequences" (1978).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.LongestCommonSubsequence.longestCommonSubsequence_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/LongestCommonSubsequenceWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestCommonSubsequenceWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/longest-common-subsequence-of-many-strings/index.html#longest-common-subsequence-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Longest common subsequence of many strings](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/longest-common-subsequence-of-many-strings/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/longest-common-subsequence-of-many-strings)
