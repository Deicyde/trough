---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.KSumMultisetDeterminesSetErdosProblem494Wanted.kSumMultiset, MathlibExt.Combinatorics.KSumMultisetDeterminesSetErdosProblem494Wanted.kSumMultisetDeterminesLargeSet, MathlibExt.Combinatorics.KSumMultisetDeterminesSetErdosProblem494Wanted.kSumMultisetDeterminesLargeSet_holds
statement: formalized
---

# Sets determined by their k-sums

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sets-determined-by-their-k-sums/index.html).

## Multiset of $k$-sums

For a finite set $A \subseteq \mathbb{C}$ and a natural number $k$,
$A_k$ is the multiset of the sums $\sum_{z \in S} z$ over the $k$-element subsets $S$ of $A$, that
is, of the sums of $k$ distinct elements of $A$, each subset counted once.

Formalized by `MathlibExt.Combinatorics.KSumMultisetDeterminesSetErdosProblem494Wanted.kSumMultiset`, a definition declared in [WantedExt/Combinatorics/KSumMultisetDeterminesSetErdosProblem494Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KSumMultisetDeterminesSetErdosProblem494Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sets-determined-by-their-k-sums/index.html#k-sum-multiset).

## Erdős Problem 494 for large sets

For a finite set $A \subseteq \mathbb{C}$ and a natural
number $k$, let $A_k$ be the multiset of the sums of the $k$-element subsets of $A$. This is the
statement that for every natural number $k \ge 3$ there is a natural number $n_0$ such that any
two finite sets $A, B \subseteq \mathbb{C}$ with $|A| = |B| \ge n_0$ and $A_k = B_k$ are equal.

This is the question of Selfridge and Straus with $|A|$ large in terms of $k$.

Formalized by `MathlibExt.Combinatorics.KSumMultisetDeterminesSetErdosProblem494Wanted.kSumMultisetDeterminesLargeSet`, a definition declared in [WantedExt/Combinatorics/KSumMultisetDeterminesSetErdosProblem494Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KSumMultisetDeterminesSetErdosProblem494Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sets-determined-by-their-k-sums/index.html#k-sum-multiset-determines-large-set).

## Large sets of complex numbers are determined by their $k$-sums

For a finite set
$A \subseteq \mathbb{C}$ and a natural number $k$, let $A_k$ be the multiset of the sums
$\sum_{z \in S} z$ over the $k$-element subsets $S$ of $A$. For every natural number $k \ge 3$
there is a natural number $n_0$ such that any two finite sets $A, B \subseteq \mathbb{C}$ with
$|A| = |B| \ge n_0$ and $A_k = B_k$ are equal.

Gordon, Fraenkel and Straus proved (Section 4) that for $s > 2$ two $n$-element multisets in a
torsion-free abelian group with the same multiset of $s$-sums are equal for all but finitely many
$n$; $\mathbb{C}$ is torsion-free and sets are multisets.

## Sources

- T. F. Bloom, Erdős Problems, Problem #494, https://www.erdosproblems.com/494 (status PROVED); resolution: B. Gordon, A. S. Fraenkel and E. G. Straus, On the determination of sets by the sets of sums of a certain order, Pacific J. Math. 12 (1962), 187-196, Section 4: for s > 2, F_s(n) = 1 for all but finitely many n, for finite multisets in any torsion-free abelian group, https://doi.org/10.2140/pjm.1962.12.187.

Stated but not proved: `MathlibExt.Combinatorics.KSumMultisetDeterminesSetErdosProblem494Wanted.kSumMultisetDeterminesLargeSet_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KSumMultisetDeterminesSetErdosProblem494Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KSumMultisetDeterminesSetErdosProblem494Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sets-determined-by-their-k-sums/index.html#k-sum-multiset-determines-large-set-hold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sets determined by their k-sums](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sets-determined-by-their-k-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sets-determined-by-their-k-sums)
