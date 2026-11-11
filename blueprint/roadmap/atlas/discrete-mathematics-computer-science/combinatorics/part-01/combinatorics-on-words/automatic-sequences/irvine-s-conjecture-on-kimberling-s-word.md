---
declaration: section
origin: cited
lean: MetaMathlibExt.kimberlingMorphism, MetaMathlibExt.kimberlingBlock, MetaMathlibExt.kimberlingBlock_one, MetaMathlibExt.kimberlingBlock_two, MetaMathlibExt.kimberlingBlock_prefix_succ, MetaMathlibExt.kimberlingBlock_prefix, MetaMathlibExt.two_pow_le_length_kimberlingBlock, MetaMathlibExt.kimberlingWord
statement: formalized
---

# Irvine's conjecture on Kimberling's word

32 results, 23 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html).

## Kimberling's morphism

Kimberling's morphism $h$ sends each letter of the alphabet
$\{0, 1\}$ to a finite word over $\{0, 1\}$, by $h(1) = 110$ and $h(0) = 11$.

The letters $0$ and $1$ are represented by the Boolean values false and true.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 1 and Section 2 (the morphism `h`).

Formalized by `MetaMathlibExt.kimberlingMorphism`, a definition declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-morphism).

## Kimberling's blocks

Let $h$ be Kimberling's morphism on the alphabet $\{0, 1\}$, given by
$h(1) = 110$ and $h(0) = 11$ and extended to finite words by concatenation. For each natural
number $n$, the $n$-th Kimberling block is the finite word $K_n = h^n(1)$, the $n$-th iterate of
$h$ applied to the one-letter word $1$. Thus $K_0 = 1$, $K_1 = 110$ and $K_2 = 11011011$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 2 (`K_n = h^n(1)`).

Formalized by `MetaMathlibExt.kimberlingBlock`, a definition declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-block).

## The first Kimberling block

For Kimberling's morphism $h$ on $\{0, 1\}$, given by
$h(1) = 110$ and $h(0) = 11$, the block $K_1 = h(1)$ is the word $110$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 2.

Formalized by `MetaMathlibExt.kimberlingBlock_one`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-block-one).

## The second Kimberling block

For Kimberling's morphism $h$ on $\{0, 1\}$, given by
$h(1) = 110$ and $h(0) = 11$, the block $K_2 = h^2(1)$ is the word $11011011$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 2.

Formalized by `MetaMathlibExt.kimberlingBlock_two`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-block-two).

## Each Kimberling block is a prefix of the next

Let $h$ be Kimberling's morphism on
$\{0, 1\}$, $h(1) = 110$ and $h(0) = 11$, and let $K_n = h^n(1)$. Then for every $n \ge 0$, the
word $K_n$ is a prefix of $K_{n+1}$.

Indeed $h(1) = 110$ begins with $1$, so $h^n(1)$ is a prefix of $h^n(110) = h^{n+1}(1)$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 2.

Formalized by `MetaMathlibExt.kimberlingBlock_prefix_succ`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-block-prefix-succ).

## Kimberling's blocks form a prefix chain

Let $h$ be Kimberling's morphism on $\{0, 1\}$,
$h(1) = 110$ and $h(0) = 11$, and let $K_n = h^n(1)$. Then $K_m$ is a prefix of $K_n$ for all
natural numbers $m \le n$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 2.

Formalized by `MetaMathlibExt.kimberlingBlock_prefix`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-block-prefix).

## Lower bound on the length of the Kimberling blocks

Let $h$ be Kimberling's morphism on
the alphabet $\{0, 1\}$, given by $h(1) = 110$ and $h(0) = 11$, and let $K_n = h^n(1)$. For every
natural number $n$, the word $K_n$ has length at least $2^n$.

This holds because the image of each letter under $h$ has length at least $2$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 2.

Formalized by `MetaMathlibExt.two_pow_le_length_kimberlingBlock`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#two-pow-le-length-kimberling-block).

## Kimberling's word

Let $K_n$ be the $n$-th Kimberling block, a finite word over
$\{0, 1\}$. Kimberling's word $k = k_1 k_2 k_3 \cdots = 1101101111\cdots$ (OEIS A285431) is the
infinite word over $\{0, 1\}$ whose letter $k_{i+1}$, for $i \ge 0$, is the $(i+1)$-th letter of
$K_m$, where $m = \lfloor \log_2 i \rfloor + 1$ for $i \ge 1$ and $m = 1$ for $i = 0$. The block
$K_m$ has length at least $2^m > i$, so this letter exists.

Every block $K_n$ is a prefix of $k$, so $k$ is the common extension of the blocks.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 2 (the limit word `k`) and Section 5 (`k'_n = k_{n+1}`).

Formalized by `MetaMathlibExt.kimberlingWord`, a definition declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-word).

## Every Kimberling block is a prefix of Kimberling's word

Let $k = k_1 k_2 k_3 \cdots$ be
Kimberling's word and $K_n$ the $n$-th Kimberling block. For all natural numbers $i$ and $n$ with
$i < |K_n|$, the letter $k_{i+1}$ equals the $(i+1)$-th letter of $K_n$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 2.

Formalized by `MetaMathlibExt.kimberlingWord_eq_getD`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-word-eq-get-d).

## The first letters of Kimberling's word

The first four letters of Kimberling's word
$k = k_1 k_2 k_3 \cdots$ are $k_1 k_2 k_3 k_4 = 1101$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Table 1.

Formalized by `MetaMathlibExt.kimberlingWord_initial`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-word-initial).

## The 101st letter of Kimberling's word

The letter $k_{101}$ of Kimberling's word
$k = k_1 k_2 k_3 \cdots$ is $0$ (OEIS A285431).

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 2.

Formalized by `MetaMathlibExt.kimberlingWord_hundred`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-word-hundred).

## Table of Gutkovskiy's sequence

The Gutkovskiy tables $T_0, T_1, \dots$ are finite lists
of natural numbers, indexed from $0$, defined by $T_0 = [0]$ and, for $n \ge 0$, $T_{n+1}$ is
$T_n$ with the entry $(n + 1) - T_n[\lfloor T_n[n]/2 \rfloor]$ appended at the end. Here $T_n[j]$
is the entry of $T_n$ at index $j$, or $0$ if $T_n$ has fewer than $j + 1$ entries, and the
subtraction is truncated at $0$.

$T_n$ has $n + 1$ entries and lists the terms $g_0, \dots, g_n$ of Gutkovskiy's sequence, so each
step reads only values already computed.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 1, Equation (1).

Formalized by `MetaMathlibExt.gutkovskiyTable`, a definition declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#gutkovskiy-table).

## Gutkovskiy's sequence

Gutkovskiy's sequence (OEIS A286389) is the sequence of natural
numbers $g_0, g_1, \dots$ with $g_0 = 0$ and $g_n = n - g_{\lfloor g_{n-1}/2 \rfloor}$ for
$n \ge 1$ (subtraction of natural numbers, truncated at $0$).

Formally, $g_n$ is defined as $T_n[n]$, the entry at index $n$ of the Gutkovskiy table $T_n$, and
the recurrence is proved from the table.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 1, Equation (1).

Formalized by `MetaMathlibExt.gutkovskiy`, a definition declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#gutkovskiy).

## Number of entries of the Gutkovskiy table

For every natural number $n$, the Gutkovskiy
table up to index $n$, the array of the values $g_0, \dots, g_n$ of Gutkovskiy's sequence, has
exactly $n + 1$ entries.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 1, Equation (1).

Formalized by `MetaMathlibExt.size_gutkovskiyTable`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#size-gutkovskiy-table).

## Entries of the Gutkovskiy table

For natural numbers $k \le n$, the entry at index $k$
(counting from $0$) of the Gutkovskiy table $T_n$ is the term $g_k$ of Gutkovskiy's sequence.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 1, Equation (1).

Formalized by `MetaMathlibExt.getD_gutkovskiyTable`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#get-d-gutkovskiy-table).

## Gutkovskiy's sequence is bounded by the index

For every natural number $n$, the term
$g_n$ of Gutkovskiy's sequence satisfies $g_n \le n$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 1, Equation (1).

Formalized by `MetaMathlibExt.gutkovskiy_le`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#gutkovskiy-le).

## Recurrence for Gutkovskiy's sequence

For every natural number $n$, Gutkovskiy's sequence
satisfies $g_{n+1} = (n + 1) - g_{\lfloor g_n/2 \rfloor}$ (subtraction of natural numbers,
truncated at $0$).

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 1, Equation (1).

Formalized by `MetaMathlibExt.gutkovskiy_succ`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#gutkovskiy-succ).

## First terms of Gutkovskiy's sequence

The first four terms of Gutkovskiy's sequence are
$g_0 = 0$, $g_1 = 1$, $g_2 = 2$ and $g_3 = 2$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Table 1.

Formalized by `MetaMathlibExt.gutkovskiy_initial`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#gutkovskiy-initial).

## Gutkovskiy's sequence at $100$

The term $g_{100}$ of Gutkovskiy's sequence is $74$, in
agreement with OEIS A286389.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 1, Equation (1).

Formalized by `MetaMathlibExt.gutkovskiy_hundred`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#gutkovskiy-hundred).

## Positions of the ones in Kimberling's word

Let $k = k_1 k_2 k_3 \cdots$ be Kimberling's
word over $\{0, 1\}$. For $n \ge 1$, $A_n$ is the position of the $n$-th $1$ in $k$, that is, the
$n$-th smallest index $j \ge 1$ with $k_j = 1$; by convention $A_0 = 0$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 8 (the sequence `A_n`).

Formalized by `MetaMathlibExt.kimberlingOnePosition`, a definition declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-one-position).

## Positions of the zeros in Kimberling's word

Let $k = k_1 k_2 k_3 \cdots$ be Kimberling's
word over $\{0, 1\}$. For $n \ge 1$, $B_n$ is the position of the $n$-th $0$ in $k$, that is, the
$n$-th smallest index $j \ge 1$ with $k_j = 0$; by convention $B_0 = 0$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Section 8 (the sequence `B_n`).

Formalized by `MetaMathlibExt.kimberlingZeroPosition`, a definition declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-zero-position).

## Position of the first one in Kimberling's word

The position $A_1$ of the first $1$ in
Kimberling's word $k = k_1 k_2 k_3 \cdots$, counted from $1$, is $A_1 = 1$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Table 3.

Formalized by `MetaMathlibExt.kimberlingOnePosition_one`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-one-position-one).

## The first zero of Kimberling's word

Let $B_n$ be the position of the $n$-th $0$ in
Kimberling's word $k = k_1 k_2 k_3 \cdots$. Then $B_1 = 3$: the first $0$ of $k$ is $k_3$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Table 3.

Formalized by `MetaMathlibExt.kimberlingZeroPosition_one`, a theorem declared in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-zero-position-one).

## Recursive structure of Kimberling's blocks

Let $h$ be Kimberling's morphism on $\{0, 1\}$,
$h(1) = 110$ and $h(0) = 11$, and let $K_n = h^n(1)$. Then for every $n \ge 2$,
$K_n = K_{n-1} K_{n-1} K_{n-2} K_{n-2}$ (concatenation of words).

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Proposition 1.

Stated but not proved: `MetaMathlibExt.kimberlingBlock_eq_append` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-block-eq-append).

## Irvine's conjecture for Gutkovskiy's sequence

Let $g_0, g_1, \dots$ be Gutkovskiy's
sequence and let $k_1 k_2 k_3 \cdots$ be Kimberling's word, with its letters read as the numbers
$0$ and $1$. Then $g_n = k_1 + \dots + k_n$ for every $n \ge 0$ (the empty sum when $n = 0$).

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Theorem 1.

Stated but not proved: `MetaMathlibExt.gutkovskiy_eq_sum_kimberlingWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#gutkovskiy-eq-sum-kimberling-word).

## Closed form for Gutkovskiy's sequence

Let $g_0, g_1, \dots$ be Gutkovskiy's sequence,
let $|K_i|$ be the length of the Kimberling block $K_i$, and let $\alpha = (\sqrt{3} - 1)/2$ and
$\beta = \sqrt{3}/3$. Let $n$ be a natural number and let $a_0, a_1, \dots, a_{m-1}$ be digits in
$\{0, 1, 2\}$ such that no two consecutive digits $a_i, a_{i+1}$ are both $2$ and
$n = \sum_{i < m} a_i |K_i|$. If $m \ge 1$ and $a_0 = 1$, then
$g_n = 2\lfloor \alpha n \rfloor + 1$; if $m \ge 1$ and $a_0 \in \{0, 2\}$, then
$g_n = 2\lfloor \alpha n + \beta \rfloor$.

Written most significant digit first, $a_{m-1} \cdots a_1 a_0$ is a $K$-representation of $n$
ending in the digit $a_0$; leading zeros are allowed.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Theorem 2.

Stated but not proved: `MetaMathlibExt.gutkovskiy_eq_two_mul_floor` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#gutkovskiy-eq-two-mul-floor).

## Positions of ones at the positions of zeros in Kimberling's word

Let
$k = k_1 k_2 k_3 \cdots$ be Kimberling's word, and for $n \ge 1$ let $A_n$ and $B_n$ be the
positions (counted from $1$) of the $n$-th $1$ and of the $n$-th $0$ in $k$. Then for every
$n \ge 1$, either $A_{B_n} = A_n + B_n - 1$ or $A_{B_n} = A_n + B_n$.

This answers a problem of Fokkink, Ortega and Rust.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Theorem 3.

Stated but not proved: `MetaMathlibExt.kimberlingOnePosition_kimberlingZeroPosition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#kimberling-one-position-kimberling-zero).

## Gutkovskiy's sequence modulo 2 is generated by a morphism

Let $g_0, g_1, g_2, \ldots$ be
Gutkovskiy's sequence, and let $u$ be the map on the alphabet $\mathbb{N}$ with $u(0) = 01$ and
$u(b) = 0010$ for every letter $b \ne 0$. Then the infinite word $(g_n \bmod 2)_{n \ge 0}$ is the
limit of the iterates of $u$ at the letter $0$. On the letters $0$ and $1$ that occur, $u$ is the
morphism $0 \mapsto 01$, $1 \mapsto 0010$, and the word is OEIS A284772.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Theorem 4.

Stated but not proved: `MetaMathlibExt.isOmegaLimit_gutkovskiy_mod_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#is-omega-limit-gutkovskiy-mod-two).

## Gutkovskiy's sequence from its parities

Let $g_0, g_1, \dots$ be Gutkovskiy's sequence,
let $g'_n = g_n \bmod 2$ and let $h_n = \sum_{0 \le i < n} g'_i$. Then $g_n = 2h_n + g'_n$ for
every $n \ge 0$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Theorem 5.

Stated but not proved: `MetaMathlibExt.gutkovskiy_eq_two_mul_sum_mod_two_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#gutkovskiy-eq-two-mul-sum-mod-two-add).

## Lengths with two right-special factors in Kimberling's word

Let $k$ be Kimberling's word
and write $K_m$ for the length of the $m$-th Kimberling block. A word $u$ is a right-special factor
of $k$ if both $u0$ and $u1$ are factors of $k$. For every $n \ge 0$, $k$ has exactly two
right-special factors of length $n$ if and only if there is an $i \ge 0$ such that
$x_i \le n < x_i + K_{2i}$, where $x_i = K_1 + K_3 + \cdots + K_{2i+1}$, or
$y_i \le n < y_i + K_{2i+1}$, where $y_i = K_0 + K_2 + \cdots + K_{2i+2}$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Theorem 6.

Stated but not proved: `MetaMathlibExt.rightSpecialFactors_kimberlingWord_ncard_eq_two_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#right-special-factors-kimberling-word-nc).

## Factor complexity of Kimberling's word

Let $\rho(n)$ be the factor complexity of
Kimberling's word $k$, the number of distinct factors of $k$ of length $n$. Then, as $n \to \infty$
over the natural numbers, $\limsup \rho(n)/n = (30 + \sqrt{3})/23$ and
$\liminf \rho(n)/n = (3 + \sqrt{3})/4$.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Corollary 1.

Stated but not proved: `MetaMathlibExt.limsup_liminf_wordFactorComplexity_kimberlingWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#limsup-liminf-word-factor-complexity-kim).

## Critical exponent of Kimberling's word

Let $k = k_1 k_2 k_3 \cdots$ be Kimberling's
word. The supremum of the ratios $m/p$, over all integers $m \ge 1$ and $p \ge 1$ for which some
factor $k_{i+1} k_{i+2} \cdots k_{i+m}$ of $k$ ($i \ge 0$) has period $p$, that is,
$k_{i+1+j} = k_{i+1+j+p}$ for every $j \ge 0$ with $j + p < m$, is $(2\sqrt{3} + 12)/3$.

Allowing every period, not only the shortest one, does not change the supremum.

## Sources

- Jeffrey Shallit, *Proof of Irvine's Conjecture via Mechanized Guessing*, INTEGERS 24 (2024), Article A51, Theorem 7.

Stated but not proved: `MetaMathlibExt.sSup_exponent_kimberlingWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html#s-sup-exponent-kimberling-word).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Irvine's conjecture on Kimberling's word](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/irvine-s-conjecture-on-kimberling-s-word)
