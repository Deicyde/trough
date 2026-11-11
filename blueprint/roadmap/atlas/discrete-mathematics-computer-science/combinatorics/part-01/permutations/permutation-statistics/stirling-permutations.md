---
declaration: section
origin: cited
lean: MetaMathlibExt.IsStirlingPermutation, MetaMathlibExt.StirlingPermSet
statement: formalized
proof: formalized
---

# Stirling permutations

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/stirling-permutations/index.html).

## Stirling permutations

Let $n$ be a natural number. A word $w = w_1 w_2 \cdots w_{2n}$ of
natural numbers is a Stirling permutation of order $n$ if every letter lies in $\{1, \dots, n\}$,
each $i \in \{1, \dots, n\}$ occurs exactly twice, and every letter strictly between the two
occurrences of $i$ is greater than $i$.

Formalized by `MetaMathlibExt.IsStirlingPermutation`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingPermutation.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingPermutation.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/stirling-permutations/index.html#is-stirling-permutation).

## The set of Stirling permutations

For a natural number $n$, $Q_n$ is the set of all
Stirling permutations of order $n$, viewed as words $w_1 w_2 \cdots w_{2n}$ of natural numbers.

Formalized by `MetaMathlibExt.StirlingPermSet`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingPermutation.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingPermutation.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/stirling-permutations/index.html#stirling-perm-set).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stirling permutations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/stirling-permutations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/permutations/permutation-statistics/stirling-permutations)
