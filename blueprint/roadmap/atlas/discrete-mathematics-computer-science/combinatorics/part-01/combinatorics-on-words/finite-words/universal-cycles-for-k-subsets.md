---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.UniversalCycleSubsetsWanted.IsUniversalCycle, MathlibExt.Combinatorics.UniversalCycleSubsetsWanted.conjecture, MathlibExt.Combinatorics.UniversalCycleSubsetsWanted.conjecture_holds
statement: formalized
---

# Universal cycles for k-subsets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/universal-cycles-for-k-subsets/index.html).

## Universal cycle for $k$-subsets

For natural numbers $n$ and $k$, let $N = \binom{n}{k}$.
A sequence $c_0, \dots, c_{N-1}$ of elements of $\{0, \dots, n-1\}$, read cyclically, is a
universal cycle for the $k$-subsets of $\{0, \dots, n-1\}$ when, for every starting position
$i < N$, the $k$ consecutive entries $c_i, c_{i+1}, \dots, c_{i+k-1}$ (indices taken modulo $N$)
are pairwise distinct, and every $k$-element subset of $\{0, \dots, n-1\}$ is the set of these
entries for exactly one starting position $i$.

## Sources

- Chung/Diaconis/Graham as cited in Cooper, Combinatorial Problems I Like, Words and Codes bullet 78 [AMR-030-0078].

Formalized by `MathlibExt.Combinatorics.UniversalCycleSubsetsWanted.IsUniversalCycle`, a definition declared in [WantedExt/Combinatorics/UniversalCycleSubsetsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/UniversalCycleSubsetsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/universal-cycles-for-k-subsets/index.html#is-universal-cycle).

## Chung–Diaconis–Graham universal cycle conjecture

The statement that for every natural
number $k$ there is a natural number $N$ such that every $n \ge N$ for which $k$ divides
$\binom{n-1}{k-1}$ admits a universal cycle for the $k$-subsets of $\{0, \dots, n-1\}$. Here
$n - 1$ and $k - 1$ are truncated at $0$, so for $k = 0$ the divisibility condition reads
$0 \mid 1$ and never holds.

## Sources

- Chung/Diaconis/Graham as cited in Cooper, Combinatorial Problems I Like, Words and Codes bullet 78 [AMR-030-0078].

Formalized by `MathlibExt.Combinatorics.UniversalCycleSubsetsWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/UniversalCycleSubsetsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/UniversalCycleSubsetsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/universal-cycles-for-k-subsets/index.html#conjecture).

## Existence of universal cycles for $k$-subsets

For every natural number $k$ there is a
natural number $N$ such that for every $n \ge N$ for which $k$ divides $\binom{n-1}{k-1}$, there
is a universal cycle for the $k$-subsets of $\{0, \dots, n-1\}$. Here $n - 1$ and $k - 1$ are
truncated at $0$, so for $k = 0$ the divisibility condition reads $0 \mid 1$ and never holds.

This is the Chung–Diaconis–Graham conjecture. Glock, Joos, Kühn and Osthus (Theorem 1.1)
proved it for every $k \ge 2$ in the language of tight Euler tours of the complete
$k$-uniform hypergraph; the case $k = 1$ is elementary.

## Sources

- Stefan Glock, Felix Joos, Daniela Kühn, Deryk Osthus, Euler tours in hypergraphs, Combinatorica 40 (2020), 679-690; arXiv:1808.07720, https://arxiv.org/abs/1808.07720.

Stated but not proved: `MathlibExt.Combinatorics.UniversalCycleSubsetsWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/UniversalCycleSubsetsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/UniversalCycleSubsetsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/universal-cycles-for-k-subsets/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Universal cycles for k-subsets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/universal-cycles-for-k-subsets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/universal-cycles-for-k-subsets)
