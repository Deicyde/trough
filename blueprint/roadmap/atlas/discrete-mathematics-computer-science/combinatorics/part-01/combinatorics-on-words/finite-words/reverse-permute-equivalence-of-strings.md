---
declaration: section
origin: cited
lean: MetaMathlibExt.ReversePermute.KString, MetaMathlibExt.ReversePermute.rpRelation
statement: formalized
proof: formalized
---

# Reverse-permute equivalence of strings

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/reverse-permute-equivalence-of-strings/index.html).

## $k$-strings

For a natural number $k$, a $k$-string is a finite sequence (possibly empty)
of elements of $\{0, 1, \ldots, k-1\}$.

Formalized by `MetaMathlibExt.ReversePermute.KString`, an abbreviation declared in [MathlibExt/Combinatorics/InfiniteWord/RPRelation.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/RPRelation.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/reverse-permute-equivalence-of-strings/index.html#kstring).

## The reverse-permute relation

For a natural number $k$, a $k$-string $s$ is related to a
$k$-string $t$ by the reverse-permute (RP) relation when there is a permutation $\sigma$ of
$\{0, 1, \ldots, k-1\}$ such that $t$ is obtained, either from $s$ or from the reversal of $s$,
by replacing each entry $x$ with $\sigma(x)$.

Formalized by `MetaMathlibExt.ReversePermute.rpRelation`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/RPRelation.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/RPRelation.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/reverse-permute-equivalence-of-strings/index.html#rp-relation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reverse-permute equivalence of strings](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/reverse-permute-equivalence-of-strings/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/reverse-permute-equivalence-of-strings)
