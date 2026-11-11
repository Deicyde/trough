---
declaration: section
origin: cited
lean: MetaMathlibExt.slowANimAfter, MetaMathlibExt.slowANimMoves, MetaMathlibExt.sum_lt_of_mem_slowANimMoves, MetaMathlibExt.slowANimGame, MetaMathlibExt.slowANimMoves_zero, MetaMathlibExt.slowANim_isP_zero, MetaMathlibExt.SlowANimReduced, MetaMathlibExt.slowANimReduction
statement: formalized
---

# Slow Nim

61 results, 33 proved and 28 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html).

## Playing on a set of stacks

Let $p$ be a position of Slow$A$-Nim on $n$ stacks, with
$p_i$ tokens on stack $i$, and let $S$ be a set of stacks. The position after playing on $S$ is
obtained by removing one token from each stack of $S$: its stack $i$ holds $p_i - 1$ if
$i \in S$ and $p_i$ otherwise, where an empty stack of $S$ stays empty.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition in Section 1.

Formalized by `MetaMathlibExt.slowANimAfter`, a definition declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-after).

## Options in Slow A-Nim

Let $A$ be a finite set of natural numbers and $p$ a position on
$n$ stacks. The options of $p$ in Slow$A$-Nim are the positions obtained from $p$ by choosing a
nonempty set $S$ of stacks with $|S| \in A$, each holding at least one token, and removing one
token from each stack of $S$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition in Section 1.

Formalized by `MetaMathlibExt.slowANimMoves`, a definition declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-moves).

## Moves in Slow$A$-Nim decrease the token count

For every finite set $A$ of natural numbers
and all positions $p$, $q$ of Slow$A$-Nim on $n$ stacks, if $q$ is reached from $p$ by one move,
then the total number of tokens strictly decreases: $\sum_i q_i < \sum_i p_i$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition in Section 1.

Formalized by `MetaMathlibExt.sum_lt_of_mem_slowANimMoves`, a theorem declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#sum-lt-of-mem-slow-anim-moves).

## Slow$A$-Nim

For $n \in \mathbb{N}$ and a finite set $A$ of natural numbers, Slow$A$-Nim
$\mathrm{SN}(n, A)$ is the impartial game whose positions assign a number $p_i$ of tokens to
each of $n$ labelled stacks $i$, and whose options from $p$ are obtained by choosing a nonempty
set $S$ of stacks with $|S| \in A$, each holding at least one token, and removing one token from
each stack of $S$. Its rank is the total number of tokens $\sum_i p_i$, which every move lowers,
and its start position is the empty position.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition in Section 1.

Formalized by `MetaMathlibExt.slowANimGame`, a definition declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-game).

## The empty position has no options

For every finite set $A$ of natural numbers, the
position of Slow$A$-Nim on $n$ stacks in which every stack is empty has no options.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Section 2.

Formalized by `MetaMathlibExt.slowANimMoves_zero`, a theorem declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-moves-zero).

## The empty position is a P-position

For every $n$ and every finite set $A$ of natural
numbers, the position of Slow$A$-Nim $\mathrm{SN}(n, A)$ with all $n$ stacks empty is a
P-position, since it has no options.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Section 2.

Formalized by `MetaMathlibExt.slowANim_isP_zero`, a theorem declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-is-p-zero).

## Reduced positions of Slow $A$-Nim

A position $p$ of Slow $A$-Nim on $n$ stacks is
reduced when for every stack $i$ there is a terminal position $t$ (one with no options) that is
reachable from $p$ by a sequence of zero or more moves and has $t_i = 0$.

In the source's notation, $u_i(p) = \min_j t^{(j)}_i(p)$, the minimum over the terminal
positions $t^{(j)}(p)$ reachable from $p$, counts the unplayable tokens of stack $i$, and $p$ is
reduced exactly when $u_i(p) = 0$ for every $i$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition in Section 3.1.

Formalized by `MetaMathlibExt.SlowANimReduced`, a definition declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduced).

## Reduction of a Slow$A$-Nim position

Let $A$ be a finite set of natural numbers and let $p$
be a position of Slow$A$-Nim on $n$ stacks. For each stack $i$, let $u_i(p)$ be the least height
of stack $i$ over all terminal positions (positions with no moves) reachable from $p$ by a sequence
of zero or more moves. The reduction of $p$ is the position $r(p)$ with $r(p)_i = p_i - u_i(p)$
for every stack $i$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition in Section 3.1.

Formalized by `MetaMathlibExt.slowANimReduction`, a definition declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduction).

## The empty position is reduced

For every finite set $A$ of natural numbers and every
$n$, the position of Slow $A$-Nim on $n$ stacks in which every stack is empty is reduced.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition in Section 3.1.

Formalized by `MetaMathlibExt.slowANimReduced_zero`, a theorem declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduced-zero).

## The reduction never adds tokens

For every finite set $A$ of natural numbers, every
position $p$ of Slow$A$-Nim on $n$ stacks and every stack $i$, the reduction $r(p)$ of $p$
satisfies $r(p)_i \le p_i$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition in Section 3.1.

Formalized by `MetaMathlibExt.slowANimReduction_le`, a theorem declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduction-le).

## Legal move sequences in Slow A-Nim

Let $A$ be a finite set of natural numbers and $p$ a
position of Slow$A$-Nim on $n$ stacks. A finite sequence $S_1, \dots, S_m$ of sets of stacks is
legal from $p$ when it is empty, or when $S_1$ is nonempty, $|S_1| \in A$, every stack in $S_1$
holds at least one token in $p$, and $S_2, \dots, S_m$ is legal from the position obtained from
$p$ by removing one token from each stack of $S_1$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Lemma 1 and its proof.

Formalized by `MetaMathlibExt.SlowANimLegalSeq`, a definition declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-legal-seq).

## The empty move sequence is legal

For every finite set $A$ of natural numbers and every
position $p$ of Slow$A$-Nim on $n$ stacks, the empty sequence of moves is legal from $p$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Lemma 1 and its proof.

Formalized by `MetaMathlibExt.slowANimLegalSeq_nil`, a theorem declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-legal-seq-nil).

## Set of P-positions

Let $R$ be a move relation on a type of positions, where $R\,x\,y$
means that $y$ is an option of $x$. A set $P$ of positions is a set of P-positions for $R$ when
no position of $P$ has an option in $P$, and every position outside $P$ has an option in $P$.

When there is no infinite sequence of moves, there is at most one such set.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Section 1 (characterization of P-positions).

Formalized by `MetaMathlibExt.IsPPositionSet`, a definition declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#is-pposition-set).

## Uniqueness of the set of P-positions

Let $R$ be a move relation on a type of positions,
where $R\,x\,y$ means that $y$ is an option of $x$, and suppose that there is no infinite
sequence of moves (the relation "$y$ is an option of $x$" is well-founded). If $P$ and $Q$ are
both sets of P-positions for $R$, then $P = Q$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Section 1 (characterization of P-positions).

Formalized by `MetaMathlibExt.IsPPositionSet.eq`, a theorem declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#eq).

## Partial structure of the P-positions of Slow $A$-Nim

Let $A \subseteq \{1, \dots, n\}$
and let $p$ be a position of Slow $A$-Nim on $n$ stacks. If every stack height of $p$ is even,
then $p$ is a P-position. If the number of stacks of $p$ with odd height lies in $A$, then $p$
is not a P-position.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Proposition 1.

Stated but not proved: `MetaMathlibExt.slowANim_partialStructure` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-partial-structure).

## P-positions of Slow A-Nim with A = \{1, k}, k odd

Let $k$ be odd with $1 \le k \le n$
and let $A = \{1, k\}$. A position $p = (p_1, \dots, p_n)$ of Slow$A$-Nim on $n$ stacks is a
P-position if and only if its total number of tokens $p_1 + \dots + p_n$ is even.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Theorem 2.

Stated but not proved: `MetaMathlibExt.slowANim_one_odd_isP_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-one-odd-is-p-iff).

## P-positions of Slow A-Nim with A = \{1, n}, n even

Let $n \ge 1$ be even and let
$A = \{1, n\}$. A position $p = (p_1, \dots, p_n)$ of Slow$A$-Nim on $n$ stacks is a P-position
if and only if its total number of tokens $p_1 + \dots + p_n$ and its smallest stack
$\min_i p_i$ are both even.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Theorem 2.

Stated but not proved: `MetaMathlibExt.slowANim_one_n_even_isP_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-one-n-even-is-p-iff).

## P-positions of Slow $\{1,2\}$-Nim on three stacks

In Slow $A$-Nim with $A = \{1, 2\}$
on three stacks, let $p = (p_0, p_1, p_2)$ be a position with $p_0 \le p_1 \le p_2$. Then $p$
is a P-position if and only if its three stack heights are all even or all odd.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Theorem 3.

Stated but not proved: `MetaMathlibExt.slowANim_one_two_three_isP_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-one-two-three-is-p-iff).

## P-positions of Slow $\{1,2\}$-Nim on four stacks

In Slow $A$-Nim with $A = \{1, 2\}$
on four stacks, let $p = (p_0, p_1, p_2, p_3)$ be a position with
$p_0 \le p_1 \le p_2 \le p_3$. Then $p$ is a P-position if and only if either all four stack
heights are even, or $p_0$ is even and $p_1$, $p_2$, $p_3$ are odd.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Theorem 3.

Stated but not proved: `MetaMathlibExt.slowANim_one_two_four_isP_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-one-two-four-is-p-iff).

## P-positions of Slow A-Nim with A = \{1, 2} on five stacks

Let $A = \{1, 2\}$ and let
$p = (p_1, \dots, p_5)$ be a position of Slow$A$-Nim on five stacks in canonical form, that is,
$p_1 \le p_2 \le \dots \le p_5$. Then $p$ is a P-position if and only if all five stacks are
even, or $p_1, p_2$ are even and $p_3, p_4, p_5$ are odd, or $p_1, p_2, p_5$ are odd and
$p_3, p_4$ are even, or $p_1, p_2, p_3, p_4$ are odd and $p_5$ is even.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Theorem 3.

Stated but not proved: `MetaMathlibExt.slowANim_one_two_five_isP_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-one-two-five-is-p-iff).

## NIRB criterion for reduced positions

Let $A \subseteq \{1, \dots, n\}$ be nonempty with
least element $a$, and let $p$ be a position of Slow $A$-Nim on $n$ stacks. Then $p$ is reduced
if and only if $a \cdot M \le \sum_i p_i$, where $M$ is the largest stack height of $p$ (taken
to be $0$ when $n = 0$).

The source assumes $n \ge 3$; the statement here is made for every $n$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Theorem 4.

Stated but not proved: `MetaMathlibExt.slowANimReduced_iff_nirb` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduced-iff-nirb).

## Legal move sequences depend only on the reduction

Let $A \subseteq \{1, \dots, n\}$ and
let $p$ be a position of Slow$A$-Nim on $n$ stacks, with reduction $r(p)$. A finite sequence of
moves, each given by its set of stacks, is legal from $r(p)$ if and only if it is legal from $p$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Lemma 1.

Stated but not proved: `MetaMathlibExt.slowANimLegalSeq_reduction_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-legal-seq-reduction-iff).

## Positions with the same reduction have the same outcome

Let
$A \subseteq \{1, \dots, n\}$. If two positions $p$ and $q$ of Slow$A$-Nim $\mathrm{SN}(n, A)$
have the same reduction, $r(p) = r(q)$, then $p$ is a P-position if and only if $q$ is a
P-position.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Corollary 1.

Stated but not proved: `MetaMathlibExt.slowANim_isP_iff_of_reduction_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-is-p-iff-of-reduction-eq).

## Chopping a reduced position keeps it reduced

Let $A \subseteq \{1, \dots, n\}$ and let
$p$ be a reduced position of Slow $A$-Nim on $n$ stacks. Then for every $m \in \mathbb{N}$ the
position $\mathrm{ctt}(p, m)$ with stack heights $\mathrm{ctt}(p, m)_i = \min(p_i, m)$ is
reduced.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Lemma 2.

Stated but not proved: `MetaMathlibExt.slowANimReduced_min` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduced-min).

## The reduction chops at the largest reduced height

Let $A \subseteq \{1, \dots, n\}$ and
let $p$ be a position of Slow$A$-Nim on $n$ stacks, with largest stack height $M = \max_i p_i$
($M = 0$ when $n = 0$). For $m \in \mathbb{N}$ write $\mathrm{ctt}(p, m)$ for the position whose
stack $i$ has height $\min(p_i, m)$. If $m \le M$, the position $\mathrm{ctt}(p, m)$ is reduced,
and $\mathrm{ctt}(p, m')$ is not reduced for any $m'$ with $m < m' \le M$, then the reduction of
$p$ is $r(p) = \mathrm{ctt}(p, m)$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Lemma 3.

Stated but not proved: `MetaMathlibExt.slowANimReduction_eq_min` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduction-eq-min).

## General reduction lemma

Let $A \subseteq \{1, \dots, n\}$ be nonempty with least element
$a$, and let $p$ be a reduced position of Slow$A$-Nim $\mathrm{SN}(n, A)$ with largest stack
height $M$ and total $\Sigma(p) = \sum_i p_i$. Let $S$ be a set of $\ell \in A$ stacks, each
holding at least one token, and suppose that the position obtained from $p$ by removing one token
from each stack of $S$ is not reduced. Then $a M \le \Sigma(p)$ and, writing
$r = \Sigma(p) - a M$, either (R1) $\ell > a$, every stack of height $M$ lies in $S$, and
$r < \ell - a$; or (R2) some stack of height $M$ is not in $S$, and $r < \ell$.

The hypothesis that $p$ is reduced is implicit in the source, whose proof uses $r \ge 0$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Lemma 4.

Stated but not proved: `MetaMathlibExt.slowANim_generalReduction` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-general-reduction).

## P-positions after adding moves

Let $M$ and $E$ be move relations on a type of positions,
let $P$ be a set of P-positions for $M$, and let $Q \subseteq P$. Suppose that (1) no element of
$P \setminus Q$ has an $E$-move to an element of $P \setminus Q$, (2) every position outside $P$
that has an $M$-move into $Q$ has an $M$-move or an $E$-move into $P \setminus Q$, and (3) every
position of $Q$ has an $E$-move into $P \setminus Q$. Then $P \setminus Q$ is a set of
P-positions for the move relation "$M$ or $E$".

The relations $M$ and $E$ need not be disjoint.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Proposition 7.

Stated but not proved: `MetaMathlibExt.isPPositionSet_extend` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#is-pposition-set-extend).

## Moves of the playable game graph of Slow $A$-Nim

The playable (reduced) game graph of
Slow $A$-Nim on $n$ stacks has the reduced positions as its positions. For reduced positions
$x$ and $y$, there is a move from $x$ to $y$ when $y$ is the reduction $r(q)$ of some option
$q$ of $x$ in Slow $A$-Nim, that is, of some position reached from $x$ by one legal move.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition 3.

Formalized by `MetaMathlibExt.SlowANimReducedGraphMove`, a definition declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduced-graph-move).

## The empty position is terminal in the playable game graph

For every $n$ and every finite
set $A$ of natural numbers, the position of Slow$A$-Nim $\mathrm{SN}(n, A)$ with all $n$ stacks
empty has no move to any position in the playable game graph of $\mathrm{SN}(n, A)$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Definition 3.

Formalized by `MetaMathlibExt.not_slowANimReducedGraphMove_zero`, a theorem declared in [WantedExt/Combinatorics/SlowANimWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#not-slow-anim-reduced-graph-move-zero).

## P-positions of Slow $A$-Nim via the playable game graph

Let $n \in \mathbb{N}$ and
$A \subseteq \{1, \dots, n\}$. Let $\tilde P$ be a set of P-positions for the moves of the
playable game graph of Slow$A$-Nim $\mathrm{SN}(n, A)$, whose positions are the reduced
positions: no position in $\tilde P$ has a move to a position in $\tilde P$, and every reduced
position outside $\tilde P$ has a move to a position in $\tilde P$. Then a position $p$ of
$\mathrm{SN}(n, A)$ is a P-position if and only if its reduction $r(p)$ lies in $\tilde P$.

This combines the source's two statements, one for P-positions and one for N-positions.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Theorem 5.

Stated but not proved: `MetaMathlibExt.slowANim_isP_iff_reduction_mem` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-is-p-iff-reduction-mem).

## Options without reduction in Slow \{n - 1}-Nim

Let $n \ge 2$, $k = n - 1$ and $A = \{k\}$,
so that a move removes one token from each of exactly $k$ nonempty stacks. Let $p$ be a reduced
position of Slow$A$-Nim on $n$ stacks, with $s = (p_1 + \dots + p_n) \bmod 2k$ and $o$ odd stacks.
Let $p'$ be obtained from $p$ by playing on a set $S$ of $k$ stacks, each holding at least one
token in $p$, and let $j$ be the stack not in $S$. If $p'$ is reduced, then
$s' = (p'_1 + \dots + p'_n) \bmod 2k$ equals $s + k$ when $s < k$ and $s - k$ when $s \ge k$, and
the number $o'$ of odd stacks of $p'$ is $n - o + 1$ if $p_j$ is odd and $n - o - 1$ if $p_j$ is
even.

The closing remark of Lemma 5 that both values of $o'$ are legal when $0 < o < n$ is omitted: it
fails for $n = 3$ at $p = (0, 1, 1)$, whose only move omits the empty stack.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Lemma 5.

Stated but not proved: `MetaMathlibExt.slowANim_n_sub_one_option_of_reduced` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-n-sub-one-option-of-reduced).

## Options with reduction in Slow \{n - 1}-Nim

Let $n \ge 2$, $k = n - 1$ and $A = \{k\}$.
Let $p$ be a reduced position of Slow$A$-Nim on $n$ stacks, with $s = (p_1 + \dots + p_n) \bmod 2k$,
$o$ odd stacks, and maximum $M = \max_i p_i$ attained by $\alpha$ stacks. Let $p'$ be obtained
from $p$ by playing on a set $S$ of $k$ stacks, each holding at least one token in $p$, and
suppose that $p'$ is not reduced. Write $r = r(p')$ for its reduction,
$s' = (r_1 + \dots + r_n) \bmod 2k$ and $o'$ for the number of odd stacks of $r$. Then $M$ is
even if $s < k$ and odd if $s \ge k$. If $s \not\equiv 0 \pmod k$, then $r_i = \max(p_i - 1, 0)$
for every stack $i$, $o' = n - o$, and $s' = s + k - 1$ if $s < k$, $s' = s - (k + 1)$ if
$s > k$. If $s \equiv 0 \pmod k$, then $r_i = \max(p_i - 2, 0)$ for the stacks with $p_i = M$
and $r_i = \max(p_i - 1, 0)$ for the others; moreover, if $s = 0$ then
$\alpha \le \min(n - o, n - 2)$, $s' = k - 1 - \alpha$ and $o' = n - o - \alpha$, and if $s = k$
then $\alpha \le \min(o, n - 2)$, $s' = 2k - 1 - \alpha$ and $o' = n - o + \alpha$.

Stacks are labelled, so the paper's canonical-form display of $r(p')$ is written stackwise.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Lemma 6.

Stated but not proved: `MetaMathlibExt.slowANim_n_sub_one_option_of_not_reduced` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-n-sub-one-option-of-not-reduce).

## P-positions of the reduced game of Slow $\{n-1\}$-Nim

Let $n \ge 2$ and $A = \{n - 1\}$,
and let $\tilde P$ be a set of P-positions of the playable game graph of Slow $A$-Nim on $n$
stacks: no move of that graph joins two elements of $\tilde P$, and every reduced position
outside $\tilde P$ has a move into $\tilde P$. For a reduced position $q$, let $s$ be the
remainder of $\sum_i q_i$ modulo $2(n - 1)$ and let $o$ be the number of stacks of $q$ of odd
height. Then $s$ and $o$ have the same parity, and $q \in \tilde P$ if and only if $s < n - 2$
and $o \le s$, or $s = n - 2$ and $o \equiv n \pmod 2$, or $n - 2 < s < 2n - 3$ and
$o \le 2(n - 2) - s$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Theorem 6.

Stated but not proved: `MetaMathlibExt.slowANimReduced_mem_pPositions_n_sub_one_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduced-mem-p-positions-n-sub).

## P-positions of the reduced game of Slow $\{n-1, n\}$-Nim

Let $n \ge 2$ and
$A = \{n - 1, n\}$, and let $\tilde P$ be a set of P-positions of the playable game graph of
Slow $A$-Nim on $n$ stacks: no move of that graph joins two elements of $\tilde P$, and every
reduced position outside $\tilde P$ has a move into $\tilde P$. For a reduced position $q$, let
$s$ be the remainder of $\sum_i q_i$ modulo $2n - 2$ and let $o$ be the number of stacks of $q$
of odd height. Then $s$ and $o$ have the same parity, and $q \in \tilde P$ if and only if
$s < n - 2$ and $o \le s$, or $s = n - 2$, $o \equiv n \pmod 2$ and $o \ne n$, or
$n - 2 < s < 2n - 3$ and $o \le 2(n - 2) - s$.

## Sources

- Matthieu Dufour and Silvia Heubach, *On the 𝒫-Positions of Some Infinite Families of Slow`A`-Nim*, INTEGERS 26 (2026), Article G3, Theorem 8.

Stated but not proved: `MetaMathlibExt.slowANimReduced_mem_pPositions_n_sub_one_n_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/SlowANimWanted.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SlowANimWanted.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-reduced-mem-p-positions-n-sub-2).

## $m$-critical positions of exact slow $k$-NIM

Let $k$ and $m$ be natural numbers and let
$\mathrm{NIM}(k + 1, k)$ be Slow$A$-Nim on $k + 1$ piles with $A = \{k\}$: a move chooses a
nonempty set of exactly $k$ nonempty piles and removes one stone from each. Let $R$ be Smith's
remoteness function of this game. A position $x = (x_0, \dots, x_k)$ is $m$-critical when
$R(x) = m$ and $R(y) \ne m$ for every position $y < x$, where $y < x$ means $y_i \le x_i$ for
every $i$ and $y \ne x$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Theorem 1.

Formalized by `MetaMathlibExt.IsExactSlowNimCritical`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#is-exact-slow-nim-critical).

## The empty position is $0$-critical

Let $k$ be a natural number and let
$\mathrm{NIM}(k + 1, k)$ be Slow$A$-Nim on $k + 1$ piles with $A = \{k\}$, in which a move
chooses a nonempty set of exactly $k$ nonempty piles and removes one stone from each. The
position $x$ of $\mathrm{NIM}(k + 1, k)$ in which all $k + 1$ piles are empty is $0$-critical:
its Smith remoteness is $0$, and no position $y$ with $y_i \le x_i$ for every $i$ and $y \ne x$
has remoteness $0$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Theorem 1.

Formalized by `MetaMathlibExt.isExactSlowNimCritical_zero`, a theorem declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#is-exact-slow-nim-critical-zero).

## Pile kept by the M-rule

For a position $x \in \mathbb{N}^{n+1}$ with piles indexed by
$0, \dots, n$: if some entry of $x$ is even, the kept pile is the least index $i$ such that $x_i$
is even and $x_i \le x_j$ for every $j$ with $x_j$ even; otherwise it is the least index $i$
such that $x_j \le x_i$ for every $j$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 2 (the index `e(x)`). Such a pile always exists, so the default `0` of `getD` is never used.

Formalized by `MetaMathlibExt.exactSlowNimMRuleKept`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-mrule-kept).

## The M-move

For a position $x$ on $n + 1$ piles, the M-move keeps one pile, chosen by the
M-rule as the first pile holding the smallest even entry if some entry of $x$ is even, and
otherwise the first pile holding a largest entry. It removes one stone from every other pile,
where an empty pile stays empty.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Sections 1.2 and 2 (the M-rule).

Formalized by `MetaMathlibExt.exactSlowNimMRuleMove`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-mrule-move).

## Terminal positions of exact slow $k$-NIM

Let $n$ and $k$ be natural numbers and let
$x = (x_0, \dots, x_{n-1})$ be a position of Slow$A$-Nim on $n$ piles with $A = \{k\}$.
Then $x$ has no options if and only if $k = 0$ or fewer than $k$ of the piles are nonempty.

When $k = 0$ there is no move, since a move uses a nonempty set of exactly $k$ piles.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 1.1 (the moves of `NIM(n, k)`).

Formalized by `MetaMathlibExt.slowANimMoves_singleton_eq_empty_iff`, a theorem declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#slow-anim-moves-singleton-eq-empty-iff).

## Fuel-bounded length of M-rule play

Let $k$ and $f$ be natural numbers and let $x$ be a
position on $k + 1$ piles. Call $x$ terminal when $k = 0$ or fewer than $k$ of its piles are
nonempty. The value at $f$ and $x$ is $0$ when $f = 0$ or $x$ is terminal; otherwise it is $1$
plus the value at $f - 1$ and the position reached from $x$ by the M-move. Thus it counts the
M-moves played from $x$, stopping at a terminal position or after $f$ moves.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 1.2 (the function `M`).

Formalized by `MetaMathlibExt.exactSlowNimMRuleLengthAux`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-mrule-length-aux).

## Successor step of the truncated M-rule length

Let $k, f \in \mathbb{N}$ and
$x \in \mathbb{N}^{k+1}$, and write $M_f(x)$ for the number of M-rule steps from $x$ in
Slow$\{k\}$-Nim on $k + 1$ stacks, counted for at most $f$ steps. Then $M_{f+1}(x) = 0$ if $x$
has no options, and otherwise $M_{f+1}(x) = 1 + M_f(x')$, where $x'$ is the position obtained
from $x$ by the M-move.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 1.2 (the function `M`).

Formalized by `MetaMathlibExt.exactSlowNimMRuleLengthAux_succ`, a theorem declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-mrule-length-aux-succ).

## M-rule length

Let $k$ be a natural number and let $x = (x_0, \dots, x_k)$ be a position
on $k + 1$ piles. Then $M(x)$ is the number of M-moves played from $x$ until a terminal position
(one with $k = 0$ or fewer than $k$ nonempty piles) is reached, computed as the fuel-bounded
length of M-rule play with fuel $x_0 + \dots + x_k$.

For $0 < k$ every M-move from a nonterminal position removes $k$ stones, so this much fuel
suffices and $M(x)$ is the full length of the M-rule play from $x$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 1.2 (the function `M`).

Formalized by `MetaMathlibExt.exactSlowNimMRuleLength`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-mrule-length).

## M-rule length of the position (3, 3, 3)

In exact slow $2$-NIM on three piles,
$\mathrm{NIM}(3, 2)$, where a move removes one stone from each of exactly two nonempty piles, the
M-rule length of the position $(3, 3, 3)$ is $M(3, 3, 3) = 4$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 1.6 (example after Theorem 1).

Formalized by `MetaMathlibExt.exactSlowNimMRuleLength_three_three_three`, a theorem declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-mrule-length-three-three).

## M-rule length of the position (3, 5, 5)

In exact slow $2$-NIM on three piles,
$\mathrm{NIM}(3, 2)$, where a move removes one stone from each of exactly two nonempty piles, the
M-rule length of the position $(3, 5, 5)$ is $M(3, 5, 5) = 6$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 1.6 (example after Theorem 1).

Formalized by `MetaMathlibExt.exactSlowNimMRuleLength_three_five_five`, a theorem declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-mrule-length-three-five-f).

## Basic vectors of type (A0)

Let $k$ and $b$ be natural numbers. A vector
$z = (z_0, \dots, z_k)$ of $k + 1$ natural numbers is basic of type (A0) for $b$ when
$z_0 + \dots + z_k = kb$, $z_i \le b$ for every $i$, $b$ is even, and every $z_i$ is even.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 2 (basic vectors).

Formalized by `MetaMathlibExt.IsExactSlowNimBasicA0`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#is-exact-slow-nim-basic-a0).

## Basic vectors of type (A1)

Let $k$ and $b$ be natural numbers. A vector
$z = (z_0, \dots, z_k)$ of $k + 1$ natural numbers is basic of type (A1) for $b$ when
$z_0 + \dots + z_k = kb$, $z_i \le b$ for every $i$, $b$ is odd, and exactly one $z_i$ is even.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 2 (basic vectors).

Formalized by `MetaMathlibExt.IsExactSlowNimBasicA1`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#is-exact-slow-nim-basic-a1).

## Basic vectors of type (B)

Let $k$ and $b$ be natural numbers. A vector
$z = (z_0, \dots, z_k)$ of $k + 1$ natural numbers is basic of type (B) for $b$ when
$z_0 + \dots + z_k = kb + k - 1$, $z_i < b$ for every $i$, $b$ is even, and every $z_i$ is odd.
Here $kb + k - 1$ is computed in the natural numbers, so it is $0$ when $k = 0$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 2 (basic vectors).

Formalized by `MetaMathlibExt.IsExactSlowNimBasicB`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#is-exact-slow-nim-basic-b).

## Basic-vector value

For $k \in \mathbb{N}$ and $x \in \mathbb{N}^{k+1}$, the basic-vector
value $B(x)$ is the largest $b \le \sum_i x_i$ for which some $z \le x$ (componentwise) is a
basic vector of type (A0), (A1) or (B) with parameter $b$; such a $b$ exists, since $z = 0$ is
basic of type (A0) with parameter $0$. For $k \ge 1$ the bound is automatic, because every basic
$z \le x$ with parameter $b$ has $b \le k b \le \sum_i z_i \le \sum_i x_i$, so $B(x)$ is the
largest parameter of a basic vector $z \le x$.

For $k = 0$ that maximum does not exist ($z = 0$ is basic of type (A0) for every even $b$), and
the bound $b \le \sum_i x_i$ totalizes this degenerate case.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 2, equation (1).

Formalized by `MetaMathlibExt.exactSlowNimBasicValue`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-basic-value).

## The basic value is attained

Let $k$ be a natural number, let $x$ be a position on
$k + 1$ piles, and let $b = B(x)$ be its basic value. Then some $z \le x$ (componentwise) is a
basic vector of type (A0), (A1) or (B) with parameter $b$, that is, $z$ supports $x$. Here type
(A0) means $\sum_i z_i = kb$, $z_i \le b$ for all $i$, and $b$ and every $z_i$ are even; type
(A1) means $\sum_i z_i = kb$, $z_i \le b$ for all $i$, $b$ is odd and exactly one $z_i$ is even;
and type (B) means $\sum_i z_i = kb + k - 1$ (truncated subtraction), $z_i < b$ for all $i$, $b$
is even and every $z_i$ is odd.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 2, equation (1).

Formalized by `MetaMathlibExt.exists_supports_exactSlowNimBasicValue`, a theorem declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exists-supports-exact-slow-nim-basic-val).

## $m$-critical positions of exact slow $k$-NIM with $k + 1$ piles (Theorem 1)

Let $k \ge 1$
and $m$ be natural numbers, and let $x = (x_0, \dots, x_k)$ be a position of
$\mathrm{NIM}(k + 1, k)$, the game on $k + 1$ piles in which a move removes one stone from each
of exactly $k$ nonempty piles. Call $x$ $m$-critical when its Smith remoteness is $m$ and no
position $y < x$ (that is, $y_i \le x_i$ for every $i$ and $y \ne x$) has remoteness $m$. Then
$x$ is $m$-critical if and only if either
(A) $x_0 + \dots + x_k = km$, $x_i \le m$ for every $i$, every $x_i$ is even if $m$ is even,
and exactly one $x_i$ is even if $m$ is odd; or
(B) $x_0 + \dots + x_k = km + k - 1$, $x_i < m$ for every $i$, $m$ is even, and every $x_i$ is
odd.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Theorem 1.

Stated but not proved: `MetaMathlibExt.isExactSlowNimCritical_iff` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#is-exact-slow-nim-critical-iff).

## Moves from critical positions with even parameter (Corollary 1 (i))

Let $k \ge 1$, let
$m > 0$ be even, and let $x \in \mathbb{N}^{k+1}$ be an $m$-critical position of Slow$\{k\}$-Nim
on $k + 1$ stacks. Then the entries of $x$ are either all odd or all even. If they are all even,
then some entry satisfies $x_i < m$; every option $y$ of $x$ with $y_i < x_i$ for every $i$ such
that $x_i = m$ is $(m - 1)$-critical; and the position $x'$ obtained from $x$ by the M-move
satisfies $x'_i < x_i$ for every $i$ with $x_i = m$ and is $(m - 1)$-critical.

The hypothesis $m > 0$ and the restriction of the move claims to all-even $x$ are deviations from
the source.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Corollary 1 (i).

Stated but not proved: `MetaMathlibExt.exactSlowNim_critical_of_even` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-critical-of-even).

## Unique critical-lowering move for odd parameter (Corollary 1 (ii))

Let $k \ge 2$, let
$m$ be odd, and let $x \in \mathbb{N}^{k+1}$ be an $m$-critical position of Slow$\{k\}$-Nim on
$k + 1$ stacks. Then $x$ has exactly one even entry $x_i$. The position $x'$ obtained from $x$ by
removing one token from every pile other than $i$ is an option of $x$, it is the only option of
$x$ that is $(m - 1)$-critical, and it is the position reached from $x$ by the M-move.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Corollary 1 (ii).

Stated but not proved: `MetaMathlibExt.exactSlowNim_critical_of_odd` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-critical-of-odd).

## Proposition 1 (odd P-positions of exact slow k-NIM)

Let $0 < k$ and let
$\mathrm{NIM}(k + 1, k)$ be Slow$A$-Nim on $k + 1$ stacks with $A = \{k\}$. A position
$x = (x_0, \dots, x_k)$ of $\mathrm{NIM}(k + 1, k)$ all of whose entries are odd is a P-position if
and only if there is a natural number $m$ such that $x_0 + \dots + x_k = km + k - 1$, $x_i < m$
for every $i$, and $m$ is even.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Proposition 1.

Stated but not proved: `MetaMathlibExt.exactSlowNim_odd_isP_iff` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-odd-is-p-iff).

## Theorem 2 (the M-rule realizes Smith's remoteness)

Let $0 < k$ and let
$\mathrm{NIM}(k + 1, k)$ be exact slow $k$-NIM on $k + 1$ piles, that is, Slow$A$-Nim on $k + 1$
stacks with $A = \{k\}$, where a move removes one stone from each of exactly $k$ nonempty piles.
For every position $x$ of $\mathrm{NIM}(k + 1, k)$, the M-rule length $M(x)$ equals Smith's
remoteness $R(x)$ of $x$ in $\mathrm{NIM}(k + 1, k)$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Theorem 2.

Stated but not proved: `MetaMathlibExt.exactSlowNimMRuleLength_eq_smithRemoteness` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-mrule-length-eq-smith-rem).

## Positions supported by a (B) basic vector (Lemma 1)

Let $k \ge 1$, let $B$ be the
basic-vector value on $\mathbb{N}^{k+1}$, and let $x, z \in \mathbb{N}^{k+1}$ with $z \le x$
componentwise, where $z$ is a basic vector of type (B) with parameter $B(x)$. Then $x = z$, and
every option $x'$ of $x$ in Slow$\{k\}$-Nim on $k + 1$ stacks (a move removes one token from
each of exactly $k$ nonempty stacks) satisfies $B(x') = B(x) - 1$, where subtraction is
truncated at $0$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Lemma 1.

Stated but not proved: `MetaMathlibExt.exactSlowNimBasicValue_of_supports_basicB` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-basic-value-of-supports-b).

## Moves at a position supported by an (A0) basic vector (Lemma 2)

Let $k \ge 1$, let
$B$ be the basic-vector value on $\mathbb{N}^{k+1}$, and let $x, z \in \mathbb{N}^{k+1}$ with
$z \le x$ componentwise, where $z$ is a basic vector of type (A0) with parameter $B(x)$. Let $j$
be a pile with $x_i > 0$ for every $i \ne j$, and let $x'$ be obtained from $x$ by removing one
token from every pile other than $j$. Then $B(x') \le B(x) - 1$ and $B(x')$ is odd. Moreover, if
$z_j < B(x)$, or if $z_j = B(x)$ and $z_i < \min(B(x), x_i)$ for some $i$, then
$B(x') = B(x) - 1$. Here $B(x) - 1$ is truncated subtraction in $\mathbb{N}$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Lemma 2.

Stated but not proved: `MetaMathlibExt.exactSlowNimBasicValue_of_supports_basicA0` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-basic-value-of-supports-b-2).

## Moves at a position supported by an (A1) basic vector (Lemma 3)

Let $k \ge 1$, let
$B$ be the basic-vector value on $\mathbb{N}^{k+1}$, and let $x, z \in \mathbb{N}^{k+1}$ with
$z \le x$ componentwise, where $z$ is a basic vector of type (A1) with parameter $B(x)$. Then
every option $x'$ of $x$ in Slow$\{k\}$-Nim on $k + 1$ stacks (a move removes one token from
each of exactly $k$ nonempty stacks) satisfies $B(x') \ge B(x) - 2$, and the position $x''$
obtained from $x$ by the M-move satisfies $B(x'') = B(x) - 1$, where subtraction is truncated
at $0$.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Lemma 3.

Stated but not proved: `MetaMathlibExt.exactSlowNimBasicValue_of_supports_basicA1` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-basic-value-of-supports-b-3).

## Basic-vector value equals Smith's remoteness (Lemma 4)

Let $k \ge 1$ and consider
Slow$\{k\}$-Nim on $k + 1$ stacks, in which a move removes one token from each of exactly $k$
nonempty stacks. For every position $x \in \mathbb{N}^{k+1}$, the basic-vector value $B(x)$
equals Smith's remoteness of $x$ in this game.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Lemma 4.

Stated but not proved: `MetaMathlibExt.exactSlowNimBasicValue_eq_smithRemoteness` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-basic-value-eq-smith-remo).

## Binary encoding of natural numbers

The bitstring encoding of $\mathbb{N}$ that writes
$0$ as the empty string and a positive integer $n$ as its binary digits, least significant bit
first, together with Mathlib's decoding map, which recovers $n$ from its encoding. It is a
definition, not an instance; Theorem 3 installs it locally so that lists of piles are encoded as
self-delimiting binary blocks.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Theorem 3 ("integers are presented in binary").

Formalized by `MetaMathlibExt.exactSlowNimBinaryNatEncoding`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-binary-nat-encoding).

## Remoteness of exact slow k-NIM from a list of piles

For a list $(x_0, \dots, x_{n-1})$
of natural numbers of length $n$, the value is Smith's remoteness of the position
$(x_0, \dots, x_{n-1})$ of Slow$A$-Nim on $n$ stacks with $A = \{n - 1\}$, where $0 - 1 = 0$. For
$n = k + 1$ this game is exact slow $k$-NIM $\mathrm{NIM}(k + 1, k)$, so $k$ is part of the input;
the empty list gives the game on no stacks.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Theorem 3.

Formalized by `MetaMathlibExt.exactSlowNimRemotenessOfList`, a definition declared in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-remoteness-of-list).

## Theorem 3 (Smith's remoteness of exact slow k-NIM is polynomial-time computable)

The map
sending a list $(x_0, \dots, x_{n-1})$ of natural numbers of length $n$ to Smith's remoteness of
the position $(x_0, \dots, x_{n-1})$ of Slow$A$-Nim on $n$ stacks with $A = \{n - 1\}$ (where
$0 - 1 = 0$) is polynomial-time computable. Here natural numbers, in the input and the output,
are encoded in binary, and a list is encoded as the concatenation of the self-delimiting forms
of the encodings of its entries. For $n = k + 1$ this is the game $\mathrm{NIM}(k + 1, k)$, so $k$
is part of the input.

## Sources

- Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Theorem 3.

Stated but not proved: `MetaMathlibExt.exactSlowNimRemoteness_isPolyTime` is written with `theorem_wanted` in [WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ExactSlowNimRemotenessWanted.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html#exact-slow-nim-remoteness-is-poly-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Slow Nim](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/slow-nim/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/combinatorial-games/slow-nim)
