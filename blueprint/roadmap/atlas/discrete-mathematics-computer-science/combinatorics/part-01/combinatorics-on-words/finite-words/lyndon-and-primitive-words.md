---
declaration: section
origin: cited
lean: MetaMathlibExt.IsPrimitiveWord, MetaMathlibExt.wittWordContent, MetaMathlibExt.IsLyndonWord, MetaMathlibExt.wittWordContent_append, MetaMathlibExt.wittWordContent_singleton, MetaMathlibExt.wittWordContent_cons, MetaMathlibExt.sum_wittWordContent, MetaMathlibExt.WordsOfContent
statement: formalized
proof: formalized
---

# Lyndon and primitive words

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html).

## Primitive word

A nonempty finite word is primitive if it is not a proper power of another word.

Formalized by `MetaMathlibExt.IsPrimitiveWord`, a definition declared in [MathlibExt/Combinatorics/Words/PrimitiveWord.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/PrimitiveWord.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#is-primitive-word).

## Content of a word

Let $r$ be a natural number. The content of a word $w$ over the alphabet
$\{0, \dots, r-1\}$ is the function that assigns to each letter $i$ the number of occurrences of $i$
in $w$.

Formalized by `MetaMathlibExt.wittWordContent`, a definition declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#witt-word-content).

## Lyndon word

Let $\alpha$ be a linearly ordered alphabet, and order the words over
$\alpha$ lexicographically. A word $w$ over $\alpha$ of length $n$ is a Lyndon word if it is
nonempty and, for every $k$ with $0 < k < n$, $w$ is strictly smaller than its rotation by $k$,
the word obtained by moving the first $k$ letters of $w$ to the end.

Formalized by `MetaMathlibExt.IsLyndonWord`, a definition declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#is-lyndon-word).

## Content is additive under concatenation

For a natural number $r$, words $u$ and $v$ over
the alphabet $\{0, \dots, r-1\}$, and every letter $i$, the number of occurrences of $i$ in the
concatenation $uv$ is the number of occurrences of $i$ in $u$ plus the number of occurrences
of $i$ in $v$.

Formalized by `MetaMathlibExt.wittWordContent_append`, a theorem declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#witt-word-content-append).

## Content of a one-letter word

Let $r$ be a natural number. For every letter $i$ of the
alphabet $\{0, \dots, r-1\}$, the content of the one-letter word $i$ takes the value $1$ at $i$ and
the value $0$ at every other letter.

Formalized by `MetaMathlibExt.wittWordContent_singleton`, a theorem declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#witt-word-content-singleton).

## Content of a word after prepending a letter

Let $r$ be a natural number, let $w$ be a word
over the alphabet $\{0, \dots, r-1\}$, let $i$ be a letter, and write $c(u)$ for the content of a
word $u$ (the number of occurrences of each letter in $u$). If $iw$ denotes $w$ with $i$ prepended,
then $c(iw)(i) = c(w)(i) + 1$ and $c(iw)(j) = c(w)(j)$ for every letter $j \ne i$.

Formalized by `MetaMathlibExt.wittWordContent_cons`, a theorem declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#witt-word-content-cons).

## The content of a word sums to its length

For a natural number $r$ and a word $w$ over
the alphabet $\{0, \dots, r-1\}$, summing over all letters $i$ the number of occurrences of $i$
in $w$ gives the length of $w$.

Formalized by `MetaMathlibExt.sum_wittWordContent`, a theorem declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#sum-witt-word-content).

## Words with prescribed content

Let $r$ be a natural number. Given a function $d$ from the
alphabet $\{0, \dots, r-1\}$ to the natural numbers, the words of content $d$ are the words $w$ over
this alphabet whose content equals $d$, that is, in which each letter $i$ occurs exactly $d(i)$
times.

Formalized by `MetaMathlibExt.WordsOfContent`, a definition declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#words-of-content).

## Lyndon words of given content

For a natural number $r$ and natural numbers
$n_0, \dots, n_{r-1}$, the set of Lyndon words over the alphabet $\{0, \dots, r-1\}$, ordered as
the natural numbers, in which each letter $i$ occurs exactly $n_i$ times.

Formalized by `MetaMathlibExt.LyndonWordsOfContent`, a definition declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#lyndon-words-of-content).

## Words of given content are counted by the multinomial coefficient

Let $r$ be a natural
number, let $n_0, \dots, n_{r-1}$ be natural numbers, and let $n = n_0 + \dots + n_{r-1}$. The
number of words over the alphabet $\{0, \dots, r-1\}$ in which each letter $i$ occurs exactly
$n_i$ times is the multinomial coefficient
$\binom{n}{n_0, \ldots, n_{r-1}} = \frac{n!}{n_0! \cdots n_{r-1}!}$.

Formalized by `MetaMathlibExt.card_wordsOfContent_eq_multinomial`, a theorem declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#card-words-of-content-eq-multinomial).

## Primitivity via distinct rotations

Let $w$ be a word of length $n$, and for
$0 \le k < n$ let $w_k$ be the rotation of $w$ by $k$, obtained by moving the first $k$ letters
of $w$ to the end. Then $w$ is primitive if and only if $w$ is nonempty and the $n$ words
$w_0, w_1, \dots, w_{n-1}$ are pairwise distinct.

Formalized by `MetaMathlibExt.isPrimitiveWord_iff_nodup_cyclicPermutations`, a theorem declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#is-primitive-word-iff-nodup-cyclic-permu).

## Nontrivial rotations move a primitive word

If $w$ is a primitive word of length $n$
and $0 < k < n$, then the rotation of $w$ by $k$, obtained by moving the first $k$ letters of $w$
to the end, is different from $w$.

Formalized by `MetaMathlibExt.rotate_ne_of_isPrimitiveWord`, a theorem declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#rotate-ne-of-is-primitive-word).

## Primitive words of given content

For a natural number $r$ and natural numbers
$n_0, \dots, n_{r-1}$, the set of primitive words over the alphabet $\{0, \dots, r-1\}$ in which
each letter $i$ occurs exactly $n_i$ times.

Formalized by `MetaMathlibExt.PrimitiveWordsOfContent`, a definition declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 734](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L734). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#primitive-words-of-content).

## Lyndon words are primitive

Every Lyndon word over a linearly ordered alphabet is
primitive.

Formalized by `MetaMathlibExt.isPrimitiveWord_of_isLyndonWord`, a theorem declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 772](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L772). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#is-primitive-word-of-is-lyndon-word).

## Witt's formula for the number of Lyndon words of given content

Let $r$ be a natural
number and let $n_0, \dots, n_{r-1}$ be natural numbers with $n = n_0 + \dots + n_{r-1} > 0$.
Order the alphabet $\{0, \dots, r-1\}$ as the natural numbers and order words over it
lexicographically. Then the number of Lyndon words over this alphabet in which each letter $i$
occurs exactly $n_i$ times equals, as a rational number, Witt's multigraded value
$M(n_0, \dots, n_{r-1}) = \frac{1}{n} \sum_{d \mid g} \mu(d) \binom{n/d}{n_0/d, \ldots, n_{r-1}/d}$,
where $g = \gcd(n_0, \dots, n_{r-1})$, the sum runs over the positive divisors $d$ of $g$, and
$\mu$ is the Möbius function.

Formalized by `MetaMathlibExt.card_lyndonWordsOfContent_eq_wittMultigradedValue`, a theorem declared in [MathlibExt/Combinatorics/Words/LyndonWord.lean, line 1176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/LyndonWord.lean#L1176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html#card-lyndon-words-of-content-eq-witt-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lyndon and primitive words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/lyndon-and-primitive-words)
