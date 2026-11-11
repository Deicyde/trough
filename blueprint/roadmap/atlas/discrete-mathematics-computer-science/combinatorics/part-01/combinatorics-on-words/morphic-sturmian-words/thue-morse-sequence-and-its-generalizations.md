---
declaration: section
origin: cited
lean: MetaMathlibExt.GeneralizedThueMorse.shiftLetter, MetaMathlibExt.GeneralizedThueMorse.shiftWord, MetaMathlibExt.GeneralizedThueMorse.shiftWord_mem, MetaMathlibExt.GeneralizedThueMorse.shiftWord_length, MetaMathlibExt.GeneralizedThueMorse.shiftLetter_val, MetaMathlibExt.GeneralizedThueMorse.block, MetaMathlibExt.GeneralizedThueMorse.length_flatten_eq, MetaMathlibExt.GeneralizedThueMorse.block_length
statement: formalized
proof: formalized
---

# Thue–Morse sequence and its generalizations

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html).

## Cyclic letter shift

For $L \in \mathbb{N}$ and letters $a, t$ of the alphabet
$\{0, \dots, L-1\}$, the cyclic shift of $a$ by $t$ is the letter $(a + t) \bmod L$. Writing the
letters as $a_0, \dots, a_{L-1}$, it sends $a_i$ to $a_{(i + t) \bmod L}$.

## Sources

- JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.shiftLetter`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#shift-letter).

## Cyclic shift of a word

Let $L$ be a natural number and let $t$ be a letter of the
alphabet $\{0, 1, \dots, L - 1\}$. The cyclic shift by $t$ of a word $w = a_1 a_2 \cdots a_n$
over this alphabet is the word $\sigma_t(a_1) \sigma_t(a_2) \cdots \sigma_t(a_n)$ of the same
length, where $\sigma_t(a) = (a + t) \bmod L$ is the cyclic shift of a letter.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.shiftWord`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#shift-word).

## Letters of a cyclically shifted word

Let $L$ be a natural number and let $t$ and $b$ be
letters of the alphabet $\{0, 1, \dots, L - 1\}$. For a letter $a$ write
$\sigma_t(a) = (a + t) \bmod L$ for its cyclic shift by $t$, and for a word $w$ over this
alphabet write $\sigma_t(w)$ for the word obtained by shifting each letter of $w$. Then $b$
occurs in $\sigma_t(w)$ if and only if $b = \sigma_t(a)$ for some letter $a$ occurring in $w$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.shiftWord_mem`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#shift-word-mem).

## Cyclic shifting preserves word length

For every $L \in \mathbb{N}$, every letter $t$ of
the alphabet $\{0, \dots, L-1\}$ and every finite word $w$ over that alphabet, the word obtained
from $w$ by shifting each letter cyclically by $t$ has the same length as $w$.

## Sources

- JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.shiftWord_length`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#shift-word-length).

## Value of the cyclic letter shift

For every $L \in \mathbb{N}$ and all letters $a, t$ of
the alphabet $\{0, \dots, L-1\}$, the cyclic shift of $a$ by $t$ is the letter
$(a + t) \bmod L$.

## Sources

- JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.shiftLetter_val`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#shift-letter-val).

## Blocks of the generalized Thue–Morse sequence

Let $L > 1$ and $k > 1$ be natural numbers,
take the letters $0, 1, \dots, L-1$ (the elements of $\mathbb{Z}/L\mathbb{Z}$), and let $\kappa$
assign a shift $\kappa(j, n) \in \mathbb{Z}/L\mathbb{Z}$ to each $j \in \{1, \dots, k-1\}$ and
each $n \ge 0$. For a word $w$ and $t \in \mathbb{Z}/L\mathbb{Z}$, let $f^t(w)$ be the word
obtained from $w$ by adding $t$ modulo $L$ to every letter. The blocks $A_n$ of the
$(L, k, \kappa)$-Thue–Morse sequence are the words given by $A_0 = 0$ (a word of one letter)
and $A_{n+1} = A_n \, f^{\kappa(1, n)}(A_n) \, f^{\kappa(2, n)}(A_n) \cdots
f^{\kappa(k-1, n)}(A_n)$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.block`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#block).

## Length of a concatenation of equal-length lists

Let $l$ be a list of lists over a type
and let $m \in \mathbb{N}$. If every list in $l$ has length $m$, then the concatenation of the
lists in $l$ has length $n \cdot m$, where $n$ is the number of lists in $l$.

## Sources

- JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.length_flatten_eq`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#length-flatten-eq).

## Length of the generalized Thue–Morse blocks

Let $L > 1$ and $k > 1$ be natural numbers
and let $\kappa$ assign a shift $\kappa(j, n) \in \mathbb{Z}/L\mathbb{Z}$ to each
$j \in \{1, \dots, k-1\}$ and each $n \ge 0$. For every $n \ge 0$, the block $A_n$ of the
$(L, k, \kappa)$-Thue–Morse sequence has exactly $k^n$ letters.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.block_length`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#block-length).

## Each generalized Thue–Morse block is a prefix of the next

Let $L > 1$ and $k > 1$ be
natural numbers and let $\kappa$ assign a shift $\kappa(j, n) \in \mathbb{Z}/L\mathbb{Z}$ to each
$j \in \{1, \dots, k-1\}$ and each $n \ge 0$. For every $n \ge 0$, the block $A_n$ of the
$(L, k, \kappa)$-Thue–Morse sequence is a prefix of $A_{n+1}$: there is a word $w$ with
$A_{n+1} = A_n w$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.block_prefix_succ`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#block-prefix-succ).

## The generalized Thue–Morse blocks form a chain of prefixes

Let $L > 1$ and $k > 1$ be
natural numbers and let $\kappa$ assign a shift $\kappa(j, n) \in \mathbb{Z}/L\mathbb{Z}$ to each
$j \in \{1, \dots, k-1\}$ and each $n \ge 0$. For all natural numbers $m \le n$, the block $A_m$
of the $(L, k, \kappa)$-Thue–Morse sequence is a prefix of $A_n$: there is a word $w$ with
$A_n = A_m w$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.block_prefix`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#block-prefix).

## A crude exponential bound

For every natural number $k > 1$ and every $m \in \mathbb{N}$,
we have $m < k^{m+1}$.

## Sources

- JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.lt_pow_succ_self`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#lt-pow-succ-self).

## Indexing into a concatenation

Let $l_1$ and $l_2$ be lists over a type, and let $m$ be a
natural number less than the length of $l_1$. Then the entry at position $m$ of the concatenation
of $l_1$ followed by $l_2$ equals the entry at position $m$ of $l_1$ (positions start at $0$).

## Sources

- JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.get_append_left`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#get-append-left).

## The infinite generalized Thue–Morse word

Let $L, k \ge 2$, let
$\kappa : \{1, \dots, k-1\} \times \mathbb{N} \to \{0, \dots, L-1\}$ be a shift schedule, and let
$A_0, A_1, \dots$ be the blocks of the $(L, k, \kappa)$-Thue–Morse sequence. The infinite word
$A_\infty$ over the alphabet $\{0, \dots, L-1\}$ has, for every $m \in \mathbb{N}$, as its letter
at position $m$ (positions start at $0$) the letter at position $m$ of the block $A_{m+1}$,
which has $k^{m+1} > m$ letters.

The letter is read by checked indexing, with no default letter.

## Sources

- JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.infLetter`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#inf-letter).

## Later blocks agree with the infinite word

Let $L, k \ge 2$, let
$\kappa : \{1, \dots, k-1\} \times \mathbb{N} \to \{0, \dots, L-1\}$ be a shift schedule, and let
$A_0, A_1, \dots$ be the blocks and $A_\infty$ the infinite word of the
$(L, k, \kappa)$-Thue–Morse sequence. For all $m, N \in \mathbb{N}$ with $m + 1 \le N$ and $m$
less than the length of $A_N$, the letter at position $m$ of $A_N$ equals the letter at
position $m$ of $A_\infty$ (positions start at $0$).

## Sources

- JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.infLetter_coherence`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#inf-letter-coherence).

## Classical shift schedule

The classical shift schedule is the map $\kappa$ that assigns
to the index $j = 1$ and every $n \in \mathbb{N}$ the letter $\kappa(1, n) = 1$ of the alphabet
$\{0, 1\}$. It is the schedule of the classical Thue–Morse sequence, the
$(L, k, \kappa)$-Thue–Morse sequence with $L = k = 2$.

## Sources

- the classical $(2, 2, 1)$ example after JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.classicalKappa`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#classical-kappa).

## Classical Thue–Morse blocks

The classical Thue–Morse blocks are the blocks $A_n$ of the
$(2, 2, \kappa)$-Thue–Morse sequence with $\kappa(1, n) = 1$ for every $n \ge 0$. Thus $A_0$ is
the one-letter word $0$, and $A_{n+1}$ is $A_n$ followed by the word obtained from $A_n$ by
exchanging the letters $0$ and $1$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.classicalBlock`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#classical-block).

## Length of the classical Thue–Morse blocks

For every $n \in \mathbb{N}$, the classical
Thue–Morse block $A_n$ (the block $A_n$ of the $(L, k, \kappa)$-Thue–Morse sequence with
$L = k = 2$ and $\kappa(1, i) = 1$ for all $i \in \mathbb{N}$) has exactly $2^n$ letters.

## Sources

- the classical $(2, 2, 1)$ example after JIS Definition 2.2.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.classical_length`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#classical-length).

## Classical Thue–Morse block of order 0

The classical Thue–Morse block $A_0$ is the
one-letter word $0$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.classical_A0`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#classical-a0).

## Classical Thue–Morse block of order 1

The classical Thue–Morse block $A_1$ is the word
$01$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.classical_A1`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#classical-a1).

## Classical Thue–Morse block of order 2

The classical Thue–Morse block $A_2$ is the word
$0110$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.classical_A2`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#classical-a2).

## Classical Thue–Morse block of order 3

The classical Thue–Morse block $A_3$ is the word
$01101001$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.classical_A3`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#classical-a3).

## The classical Thue–Morse word begins with 01101001

Let $A_\infty$ be the infinite word
of the $(2, 2, \kappa)$-Thue–Morse sequence with $\kappa(1, n) = 1$ for every $n \ge 0$. The
letters of $A_\infty$ at positions $0, 1, \dots, 7$ are $0, 1, 1, 0, 1, 0, 0, 1$, so $A_\infty$
begins with $01101001$.

Formalized by `MetaMathlibExt.GeneralizedThueMorse.classical_inf_init`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/GeneralizedThueMorseSequence.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#classical-inf-init).

## Thue–Morse substitution

The Thue–Morse substitution $\sigma$ on the alphabet $\{0, 1\}$
sends each letter to a word of length two: $\sigma(0) = 01$ and $\sigma(1) = 10$.

## Sources

- Example 2 in Scott Balchin and Dan Rust, *Computations for Symbolic Substitutions*, Journal of Integer Sequences 20 (2017): https://cs.uwaterloo.ca/journals/JIS/VOL20/Rust/rust3.tex.

Formalized by `MetaMathlibExt.thueMorseSubstitution`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/ThueMorse.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/ThueMorse.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#thue-morse-substitution).

## Thue–Morse blocks

Let $\sigma$ be the Thue–Morse substitution, $\sigma(0) = 01$ and
$\sigma(1) = 10$, applied to finite words over $\{0, 1\}$ letter by letter. For a natural number
$n$, the $n$th Thue–Morse block is the finite word $\sigma^n(0)$: the $0$th block is the
one-letter word $0$, and the $(n+1)$st block is obtained from the $n$th by replacing each letter
$a$ with $\sigma(a)$.

Formalized by `MetaMathlibExt.thueMorseBlock`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/ThueMorse.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/ThueMorse.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#thue-morse-block).

## Thue–Morse sequence

The Thue–Morse sequence $t_0 t_1 t_2 \cdots$ over $\{0, 1\}$ is
indexed from $0$, and $t_n = 1$ exactly when the binary expansion of $n$ has an odd number of
digits equal to $1$; otherwise $t_n = 0$.

## Sources

- Eiji Miyanohara, *Transcendence of Digital Expansions Generated by a Generalized Thue-Morse Sequence*, Journal of Integer Sequences 18 (2015), which lists the initial blocks `0`, `01`, `0110` and `01101001` and the limit beginning `0110100110010110`: https://cs.uwaterloo.ca/journals/JIS/VOL18/Miyanohara/miy5.tex. Evaluation here uses the binary digits of the index, in time and space logarithmic in it, rather than an exponentially long block.

Formalized by `MetaMathlibExt.thueMorse`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/ThueMorse.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/ThueMorse.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html#thue-morse).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Thue–Morse sequence and its generalizations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/thue-morse-sequence-and-its-generalizations)
