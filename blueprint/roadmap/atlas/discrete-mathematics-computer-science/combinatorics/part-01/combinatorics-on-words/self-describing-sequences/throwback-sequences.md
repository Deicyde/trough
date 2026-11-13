---
declaration: section
origin: cited
lean: MetaMathlibExt.kozar_throwback_recurrence, MetaMathlibExt.throwback, MetaMathlibExt.throwbackSequence, MetaMathlibExt.throwback_examples, MetaMathlibExt.partialPlacement, MetaMathlibExt.partialPlacement_zero_examples, MetaMathlibExt.throwback_final_position_or_frequently_leader, MetaMathlibExt.throwbackSequence_infinite_eq
statement: formalized
---

# Throwback sequences

15 results, 6 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html).

## Kozar's conjecture on the throwback sequence

For a sequence
$Y = (Y_0, Y_1, Y_2, \dots)$ of natural numbers, the throwback step produces the sequence $Y'$
with $Y'_i = Y_{i+1}$ for $i < Y_0$, $Y'_{Y_0} = Y_0$, and $Y'_i = Y_i$ for $i > Y_0$: the
leading term $Y_0$ moves to index $Y_0$, the terms $Y_1, \dots, Y_{Y_0}$ shift one place to the
left, and all later terms stay in place. Let $X$ be the sequence with $X_i = i + 3$ (that is,
$3, 4, 5, \dots$), and let $T_k$ be the leading term of the sequence obtained from $X$ by $k$
throwback steps. Then for every natural number $n \ge 3$ and every natural number $N$ there is
$k \ge N$ with $T_k = n$; that is, every $n \ge 3$ equals $T_k$ for infinitely many $k$.

This is Kozar's conjecture for OEIS A357081. Darnell and Dribus prove a more general recurrence
theorem for every sequence of distinct positive integers.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, “Throwback Sequences of Positive Integers”, <https://cs.uwaterloo.ca/journals/JIS/VOL28/Dribus/dribus4.tex>; conjecture/introduction lines 71–80; exact throwback definition lines 98–103; general recurrence theorem and proof lines 124–137.

Formalized by `MetaMathlibExt.kozar_throwback_recurrence`, a theorem declared in [MathlibExt/Combinatorics/Sequences/KozarThrowbackRecurrence.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Sequences/KozarThrowbackRecurrence.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#kozar-throwback-recurrence).

## Throwback operation

Let $s = (s_0, s_1, s_2, \dots)$ be a sequence of elements of a set
$A$, each element $a$ carrying a weight $w(a) \in \mathbb{N}$. The throwback $\tau_w(s)$ moves the
leader $s_0$ to index $w(s_0)$, moves the entries at indices $1, \dots, w(s_0)$ one place left and
leaves later entries in place: $\tau_w(s)_i = s_{i+1}$ for $i < w(s_0)$,
$\tau_w(s)_{w(s_0)} = s_0$, and $\tau_w(s)_i = s_i$ for $i > w(s_0)$.

With $A = \mathbb{N}$ and $w$ the identity, this is the throwback $\tau$ of Darnell and Dribus on
sequences of positive integers. With $A = \mathbb{N}$, the initial arrangement $s_i = i$ and
weights $w(i) = x_i$ for a sequence $X = (x_0, x_1, \dots)$, it tracks the original index of each
term, so repeated values stay distinguishable.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Section 2.

Formalized by `MetaMathlibExt.throwback`, a definition declared in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback).

## Throwback sequence

For a sequence $X = (x_0, x_1, \dots)$ of natural numbers, the throwback
sequence $T(X) = (t_0, t_1, \dots)$ records the successive leaders under the throwback operation:
$t_n$ is the leader (the entry at index $0$) of $\tau^n(X)$, where $\tau$ is the throwback
operation in which each entry's weight is its own value.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Section 2.

Formalized by `MetaMathlibExt.throwbackSequence`, a definition declared in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback-sequence).

## Throwback of the integers from 3 on

Let $X = (3, 4, 5, \dots)$, that is, $x_i = i + 3$.
The first five terms of its throwback $\tau(X)$ are $4, 5, 6, 3, 7$, and the first six terms of
its throwback sequence $T(X)$ are $3, 4, 5, 6, 3, 7$ (OEIS A357081).

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Table 1.

Formalized by `MetaMathlibExt.throwback_examples`, a theorem declared in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback-examples).

## Partial placement sequences

Let $X = (x_0, x_1, \dots)$ be a sequence of natural
numbers; the source takes $X$ strictly increasing with positive terms. The partial placement
sequences $P_n(X)$, for $n \ge 0$, are indexed by positions $z \in \mathbb{Z}$, and each
position is either empty or holds a term of $X$. $P_0(X)$ holds $x_0$ at the multiples of
$x_0 + 1$ and is empty elsewhere. $P_{n+1}(X)$ agrees with $P_n(X)$ at the filled positions of
$P_n(X)$ and fills some of its empty (open) positions with $x_{n+1}$, as follows. Let $s$ be
the least natural number that is an open position of $P_n(X)$ ($s = 0$ if there is none), and
let $d = x_{n+1} - (n + 1) + 1 = x_{n+1} - n$, an integer. An open position $z$ of $P_n(X)$
receives $x_{n+1}$ exactly when $d$ divides the signed number of open positions of $P_n(X)$
between $s$ and $z$, where open positions in $[s, z)$ count $+1$ and those in $[z, s)$ count
$-1$; all other open positions stay empty. When $d > 0$ and $P_n(X)$ has an open position
$\ge 0$, this places $x_{n+1}$ at $s$ and then, in both directions, at every $d$-th open
position.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Section 4.

Formalized by `MetaMathlibExt.partialPlacement`, a definition declared in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#partial-placement).

## First partial placement sequence of the integers from 3 on

Let $X = (3, 4, 5, \dots)$,
that is, $x_i = i + 3$. The partial placement sequence $P_0(X)$ holds the term $3$ at
positions $0$, $4$ and $-4$, and its positions $1$, $2$ and $3$ are empty.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Table 4.

Formalized by `MetaMathlibExt.partialPlacement_zero_examples`, a theorem declared in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#partial-placement-zero-examples).

## Each term eventually settles or leads infinitely often

Let $X = (x_0, x_1, \dots)$ be a
sequence of positive integers, with positions numbered from $0$, the leader being at position
$0$. Track the terms of $X$ by their original indices: start from the arrangement
$(0, 1, 2, \dots)$ and apply the throwback repeatedly, where the leader, with original index
$i$, moves to position $x_i$. Then for every index $j$, either there are a position $p > 0$ and
a number $N$ such that the term with original index $j$ is at position $p$ after $k$ throwbacks
for every $k \ge N$, or there are infinitely many $k$ such that this term is the leader after
$k$ throwbacks.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Lemma 1 (`jis-2025-25.5.1-lem-1`).

Stated but not proved: `MetaMathlibExt.throwback_final_position_or_frequently_leader` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback-final-position-or-frequently-l).

## Every term recurs in the throwback sequence

Let $X = (x_0, x_1, \dots)$ be a sequence of
pairwise distinct positive integers, and let $T(X) = (t_0, t_1, \dots)$ be its throwback
sequence. Then every term $x_j$ of $X$ appears infinitely often in $T(X)$: there are infinitely
many $k$ with $t_k = x_j$.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Theorem 2 (`jis-2025-25.5.1-thm-2`).

Stated but not proved: `MetaMathlibExt.throwbackSequence_infinite_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback-sequence-infinite-eq).

## Recursive bound on the time to become leader

Let $X = (x_0, x_1, \dots)$ be a sequence
of pairwise distinct positive integers, with positions numbered from $0$, the leader being at
position $0$. Let $\tau$ be the throwback and $T(X) = (t_0, t_1, \dots)$ the throwback
sequence, so $t_k$ is the leader of $\tau^k(X)$. Let $n \ge 1$, and let $N$ be the number of
indices $i$ with $x_i < n$. Suppose $a$ and $b$ are natural numbers such that for every
$m \ge 0$, the term at position $n - 1$ of $\tau^m(X)$ equals $t_{m+k}$ for some $k \le a$, and
the term at position $N$ of $\tau^m(X)$ equals $t_{m+k}$ for some $k \le b$. Then for every
$m \ge 0$, the term at position $n$ of $\tau^m(X)$ equals $t_{m+k}$ for some $k \le a + b + 1$.

This is the bound $M(n) \le M(n - 1) + M(N) + 1$ of the source, stated for upper bounds, where
$M(n)$ is the largest number of throwbacks the term at position $n$ of any $\tau^m(X)$ needs to
become leader.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Lemma 3 (`jis-2025-25.5.1-lem-3`).

Stated but not proved: `MetaMathlibExt.throwback_leader_time_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback-leader-time-le).

## Limiting frequencies in throwback sequences

Let $X = (x_0, x_1, \dots)$ be a sequence of
pairwise distinct positive integers with throwback sequence $T(X) = (t_0, t_1, \dots)$, and for a
natural number $w$ let $\sigma(w)$ be the number of indices $i$ with $x_i < w$. Then for every
index $j$, writing $x = x_j$, the number of $k < N$ with $t_k = x$, divided by $N$, converges as
$N \to \infty$ to

$$f(x) = \frac{1}{x - \sigma(x) + 1} \prod_{w} \frac{w - \sigma(w)}{w - \sigma(w) + 1},$$

where the product runs over the values $w < x$ taken by $X$.

For a term $w$ of $X$, $\sigma(w)$ is the index of $w$ in the increasing rearrangement of $X$.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Theorem 4 (`jis-2025-25.5.1-thm-4`).

Stated but not proved: `MetaMathlibExt.throwbackSequence_limiting_frequency` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback-sequence-limiting-frequency).

## Every term has a nonzero limiting frequency

Let $X = (x_0, x_1, \dots)$ be a sequence of
pairwise distinct positive integers, and let $T(X) = (t_0, t_1, \dots)$ be its throwback
sequence. Then for every $j$, the proportion $\#\{k < N : t_k = x_j\} / N$ of terms equal to
$x_j$ among the first $N$ terms of $T(X)$ converges, as $N \to \infty$, to a nonzero real number.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Corollary 5 (`jis-2025-25.5.1-cor-5`).

Stated but not proved: `MetaMathlibExt.throwbackSequence_limiting_frequency_ne_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback-sequence-limiting-frequency-ne).

## Partial placement sequences are periodic

Let $X = (x_0, x_1, \dots)$ be a strictly
increasing sequence of positive integers and let $n \ge 0$. Then the partial placement sequence
$P_n(X)$ is periodic: there is an integer $p > 0$ such that for every position
$z \in \mathbb{Z}$, the positions $z + p$ and $z$ of $P_n(X)$ are either both empty or hold the
same term.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Lemma 6 (`jis-2025-25.5.1-lem-6`).

Stated but not proved: `MetaMathlibExt.partialPlacement_periodic` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#partial-placement-periodic).

## Throwback sequences of increasing sequences are uniformly recurrent

Let
$X = (x_0, x_1, \dots)$ be a strictly increasing sequence of positive integers with throwback
sequence $T(X) = (t_0, t_1, \dots)$. Then every block of consecutive terms of $T(X)$ recurs with
bounded gaps: for all natural numbers $i$ and $L$ there is a natural number $G$ such that for
every natural number $m$ there is an index $j$ with $m \le j \le m + G$ and $t_{j+s} = t_{i+s}$
for all $s < L$.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Theorem 7 (`jis-2025-25.5.1-thm-7`).

Stated but not proved: `MetaMathlibExt.throwbackSequence_uniformly_recurrent` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback-sequence-uniformly-recurrent).

## Minimal complete blocks of partial placements match configurations

Let
$X = (x_0, x_1, \dots)$ be a strictly increasing sequence of positive integers, let $\tau$ be
the throwback, let $n \ge 0$, and write $P_n(X)_z$ for the entry, possibly empty, of the
partial placement sequence $P_n(X)$ at position $z \in \mathbb{Z}$. The minimal complete block
at $z$ is the word $P_n(X)_z, P_n(X)_{z+1}, \dots, P_n(X)_{z+L-1}$, empty positions included,
where $L$ is the least length for which these positions contain every $x_i$ with $i \le n$
($L = 0$ if there is no such length). Then for all natural numbers $k$ and $l$, the minimal
complete blocks at $k$ and at $l$ are equal if and only if each of $x_0, \dots, x_n$ occupies
the same positions in $\tau^k(X)$ as in $\tau^l(X)$. Moreover, for every $z \in \mathbb{Z}$ the
minimal complete block at $z$ equals the minimal complete block at some natural number $k$.
So minimal complete blocks of $P_n(X)$ correspond bijectively to the configurations of
$x_0, \dots, x_n$ in the sequences $\tau^k(X)$ with $k \ge 0$.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Lemma 8 (`jis-2025-25.5.1-lem-8`).

Stated but not proved: `MetaMathlibExt.partialPlacement_minimal_complete_blocks_iff_configurations` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#partial-placement-minimal-complete-block).

## Perfect mixing for consecutive integers

Let $m \ge 1$ and $n \ge 0$, let
$X = (m, m + 1, m + 2, \dots)$, and let $\tau$ be the throwback. Then the positions of the terms
$m, m + 1, \dots, m + n$ in $\tau^k(X)$ are different for different $k$ with
$0 \le k < (m + 1)^{n + 1}$: for $0 \le k < l < (m + 1)^{n + 1}$, some $m + i$ with $i \le n$
occupies different positions in $\tau^k(X)$ and $\tau^l(X)$. Moreover, each of
$m, m + 1, \dots, m + n$ occupies the same positions in $\tau^{(m+1)^{n+1}}(X)$ as in $X$.

## Sources

- Jesiah Darnell and Benjamin F. Dribus, *Throwback Sequences of Positive Integers*, Journal of Integer Sequences 28 (2025), Article 25.5.1, Theorem 9 (`jis-2025-25.5.1-thm-9`).

Stated but not proved: `MetaMathlibExt.throwback_consecutive_perfect_mixing` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThrowbackSequencesWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ThrowbackSequencesWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html#throwback-consecutive-perfect-mixing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Throwback sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/throwback-sequences)
