---
declaration: section
origin: cited
lean: InfiniteWord.TribonacciLetter, InfiniteWord.tribonacciWordApprox, InfiniteWord.tribonacciWordApprox_add_three, InfiniteWord.tribonacciWordApprox_length_add_three, InfiniteWord.tribonacciWordApprox_length_ge, InfiniteWord.tribonacciWordApprox_prefix_succ, InfiniteWord.tribonacciWordApprox_prefix, InfiniteWord.tribonacciWordApprox_length_mono
statement: formalized
proof: formalized
---

# Tribonacci word

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html).

## The Tribonacci alphabet

The Tribonacci word is written over the three-letter alphabet
whose letters are $a$, $b$ and $c$.

Formalized by `InfiniteWord.TribonacciLetter`, an inductive type declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-letter).

## Finite Tribonacci words

The finite Tribonacci words $W(n)$, for $n \ge 0$, are the
words over the alphabet $\{a, b, c\}$ defined by $W(0) = a$, $W(1) = ab$, $W(2) = abac$ and
$W(n + 3) = W(n + 2)\,W(n + 1)\,W(n)$ for every $n \ge 0$, where juxtaposition denotes
concatenation.

Formalized by `InfiniteWord.tribonacciWordApprox`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-word-approx).

## Recursion for the finite Tribonacci words

For every $n \ge 0$, the finite Tribonacci
word $W(n + 3)$ is the concatenation $W(n + 2)\,W(n + 1)\,W(n)$.

Formalized by `InfiniteWord.tribonacciWordApprox_add_three`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-word-approx-add-three).

## Length recurrence for finite Tribonacci words

Writing $|w|$ for the length of a word
$w$, for every $n \ge 0$ the finite Tribonacci words satisfy
$|W(n + 3)| = |W(n + 2)| + |W(n + 1)| + |W(n)|$.

Formalized by `InfiniteWord.tribonacciWordApprox_length_add_three`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-word-approx-length-add-three).

## Length lower bound for finite Tribonacci words

For every $n \ge 0$, the finite
Tribonacci word $W(n)$ has length at least $n + 1$.

Formalized by `InfiniteWord.tribonacciWordApprox_length_ge`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-word-approx-length-ge).

## Each finite Tribonacci word is a prefix of the next

For every $n \ge 0$, the finite
Tribonacci word $W(n)$ is a prefix of $W(n + 1)$.

Formalized by `InfiniteWord.tribonacciWordApprox_prefix_succ`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-word-approx-prefix-succ).

## Finite Tribonacci words form a prefix chain

For all natural numbers $m \le n$, the
finite Tribonacci word $W(m)$ is a prefix of $W(n)$.

Formalized by `InfiniteWord.tribonacciWordApprox_prefix`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-word-approx-prefix).

## Lengths of finite Tribonacci words are monotone

For all natural numbers $m \le n$,
the length of the finite Tribonacci word $W(m)$ is at most the length of $W(n)$.

Formalized by `InfiniteWord.tribonacciWordApprox_length_mono`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-word-approx-length-mono).

## The infinite Tribonacci word

The infinite Tribonacci word is the sequence over the
alphabet $\{a, b, c\}$ whose letter at each position $k \ge 0$ (positions counted from $0$) is
the letter at position $k$ of the finite Tribonacci word $W(k)$; this position exists because
$W(k)$ has length at least $k + 1$.

Formalized by `InfiniteWord.tribonacciWord`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-word).

## Finite Tribonacci words agree with the infinite word

For all natural numbers
$k \le n$ such that $k$ is less than the length of the finite Tribonacci word $W(n)$, the
letter of $W(n)$ at position $k$ equals the letter of the infinite Tribonacci word at
position $k$, positions being counted from $0$.

Formalized by `InfiniteWord.tribonacciWord_eq_getElem_of_le`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Tribonacci.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html#tribonacci-word-eq-get-elem-of-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tribonacci word](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/tribonacci-word)
