---
declaration: section
origin: cited
lean: MetaMathlibExt.IsWordSquare, MetaMathlibExt.IsSquareFreeWord, MetaMathlibExt.IsInfiniteSquareFreeWord, MetaMathlibExt.TernaryAlphabet, MetaMathlibExt.IsTernarySquareFreeLength, MetaMathlibExt.IsInfiniteTernarySquareFreeWord, MetaMathlibExt.IsSquareFreeWord.of_isInfix, MetaMathlibExt.isSquareFreeWord_iff_inits_tails
statement: formalized
proof: formalized
---

# Square-free words

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html).

## Square word

A word $w$ over an alphabet $\alpha$ is a square if $w = xx$ for some nonempty
word $x$, where $xx$ denotes the concatenation of $x$ with itself.

Formalized by `MetaMathlibExt.IsWordSquare`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html#is-word-square).

## Square-free finite word

A finite word $w$ over an alphabet $\alpha$ is square-free if no
factor of $w$ is a square, where a factor of $w$ is a word $s$ with $w = psq$ for some words $p$
and $q$, and a square is a word $xx$ with $x$ nonempty.

Formalized by `MetaMathlibExt.IsSquareFreeWord`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html#is-square-free-word).

## Square-free infinite word

An infinite word $u = u_0 u_1 u_2 \cdots$ over an alphabet
$\alpha$ is square-free if it contains no two adjacent equal nonempty blocks: for all $i \ge 0$ and
all $k \ge 1$ there is some $j < k$ with $u_{i+j} \ne u_{i+k+j}$.

Formalized by `MetaMathlibExt.IsInfiniteSquareFreeWord`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html#is-infinite-square-free-word).

## The ternary alphabet for square-free words

The ternary alphabet is the set $\{0, 1, 2\}$
of natural numbers less than $3$; its three letters play the role of $a$, $b$ and $c$.

Formalized by `MetaMathlibExt.TernaryAlphabet`, an abbreviation declared in [MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html#ternary-alphabet).

## Square-free ternary words of length $n$

For a natural number $n$, a finite word $w$ over
the ternary alphabet is a square-free ternary word of length $n$ if $w$ is square-free and $w$ has
length exactly $n$.

Formalized by `MetaMathlibExt.IsTernarySquareFreeLength`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html#is-ternary-square-free-length).

## Square-free infinite ternary word

An infinite word $u = u_0 u_1 u_2 \cdots$ over the
ternary alphabet is a square-free infinite ternary word if it is square-free as an infinite word.

Formalized by `MetaMathlibExt.IsInfiniteTernarySquareFreeWord`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html#is-infinite-ternary-square-free-word).

## Factors of square-free words are square-free

If a finite word $v$ is square-free and $u$
is a factor of $v$, that is, $v = puq$ for some words $p$ and $q$, then $u$ is square-free.

Formalized by `MetaMathlibExt.IsSquareFreeWord.of_isInfix`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html#of-is-infix).

## Square-freeness via prefixes of suffixes

A finite word $w$ is square-free if and only if,
for every prefix $s$ of a suffix of $w$ and every nonempty prefix $x$ of $s$, we have $s \ne xx$,
where $xx$ denotes the concatenation of $x$ with itself.

This form is directly decidable when letter equality is decidable.

Formalized by `MetaMathlibExt.isSquareFreeWord_iff_inits_tails`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/SquareFreeWord.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html#is-square-free-word-iff-inits-tails).

## Crochemore's square-freeness test

Let $f$ map each letter of the three-letter alphabet
$\{a, b, c\}$ to a finite word over a set $T$, and extend $f$ to words by concatenation,
$f(x_1 \cdots x_n) = f(x_1) \cdots f(x_n)$. Then $f$ maps every square-free word over
$\{a, b, c\}$ to a square-free word if and only if it maps every square-free word over
$\{a, b, c\}$ of length at most $5$ to a square-free word.

A word is square-free when no factor has the form $uu$ with $u$ nonempty. No non-erasing
hypothesis is assumed: the image of a letter may be empty.

Proof: reduce erasing morphisms first, then apply Currie's synchronization
method to a shortest square occurrence and its shortest source-word cover.

## Sources

- Currie, lines 99-100 of <https://cs.uwaterloo.ca/journals/JIS/VOL22/Currie/currie20.tex>; primary reference Crochemore, Theoret. Comput. Sci. 18(2) (1982), DOI 10.1016/0304-3975(82)90023-8.

Formalized by `MetaMathlibExt.crochemore_squarefree_test_set`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/CrochemoreSquarefreeCriterion.lean, line 1245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/CrochemoreSquarefreeCriterion.lean#L1245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html#crochemore-squarefree-test-set).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Square-free words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/square-free-words)
