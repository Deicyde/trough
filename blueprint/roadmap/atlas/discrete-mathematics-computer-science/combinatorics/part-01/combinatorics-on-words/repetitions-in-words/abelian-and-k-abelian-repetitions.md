---
declaration: section
origin: cited
lean: MetaMathlibExt.wordFactorCount, MetaMathlibExt.IsKAbelianEquivalent, MetaMathlibExt.IsKAbelianSquare, MetaMathlibExt.IsKAbelianSquareFree, MetaMathlibExt.IsThreeAbelianEquivalent, MetaMathlibExt.IsThreeAbelianSquare, MetaMathlibExt.IsThreeAbelianSquareFree
statement: formalized
proof: formalized
---

# Abelian and k-abelian repetitions

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions/index.html).

## Number of occurrences of a factor

For words $w$ and $t$ over an alphabet with $t$
nonempty, the factor count of $t$ in $w$ is the number of positions of $w$ at which an occurrence
of $t$ starts, overlapping occurrences all being counted. The factor count of the empty word is
$0$.

Formalized by `MetaMathlibExt.wordFactorCount`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions/index.html#word-factor-count).

## $k$-abelian equivalence

For a natural number $k$, two words $u$ and $v$ over an alphabet
are $k$-abelian equivalent when $k \ge 1$, both $u$ and $v$ are nonempty, $u$ and $v$ have the
same prefix of length $k - 1$ and the same suffix of length $k - 1$ (a word shorter than
$k - 1$ counting as its own prefix and suffix), and every word $t$ of length $k$ occurs as a
factor of $u$, counting overlapping occurrences, exactly as often as it occurs in $v$.

Formalized by `MetaMathlibExt.IsKAbelianEquivalent`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions/index.html#is-kabelian-equivalent).

## $k$-abelian squares

For a natural number $k$, a word $w$ is a $k$-abelian square when
$w = uv$ for two nonempty words $u$ and $v$ that are $k$-abelian equivalent.

Formalized by `MetaMathlibExt.IsKAbelianSquare`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions/index.html#is-kabelian-square).

## $k$-abelian square-free words

For a natural number $k$, a finite word $w$ is
$k$-abelian square-free when $k \ge 1$ and no factor of $w$ (a word $x$ with $w = pxs$ for some
words $p$ and $s$) is a $k$-abelian square.

Formalized by `MetaMathlibExt.IsKAbelianSquareFree`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions/index.html#is-kabelian-square-free).

## $3$-abelian equivalence of ternary words

Two words $u$ and $v$ over the alphabet
$\{0, 1, 2\}$ are $3$-abelian equivalent when they are $k$-abelian equivalent for $k = 3$: both
are nonempty, they have the same prefix and the same suffix of length $2$ (a shorter word
counting as its own prefix and suffix), and every word of length $3$ occurs as a factor of $u$,
counting overlapping occurrences, exactly as often as it occurs in $v$.

Formalized by `MetaMathlibExt.IsThreeAbelianEquivalent`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions/index.html#is-three-abelian-equivalent).

## $3$-abelian squares over a ternary alphabet

A word $w$ over the alphabet $\{0, 1, 2\}$ is
a $3$-abelian square when $w = uv$ for two nonempty words $u$ and $v$ that are $3$-abelian
equivalent.

Formalized by `MetaMathlibExt.IsThreeAbelianSquare`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions/index.html#is-three-abelian-square).

## $3$-abelian square-free ternary words

A finite word $w$ over the alphabet $\{0, 1, 2\}$
is $3$-abelian square-free when no factor of $w$ (a word $x$ with $w = pxs$ for some words $p$
and $s$) is a $3$-abelian square.

Formalized by `MetaMathlibExt.IsThreeAbelianSquareFree`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/KAbelianSquareFreeWord.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions/index.html#is-three-abelian-square-free).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Abelian and k-abelian repetitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/abelian-and-k-abelian-repetitions)
