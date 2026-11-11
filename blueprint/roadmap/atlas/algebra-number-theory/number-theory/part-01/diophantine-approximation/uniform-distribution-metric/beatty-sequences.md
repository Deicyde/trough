---
declaration: section
origin: cited
lean: MetaMathlibExt.beattyTerm, MetaMathlibExt.beattyTerm_eq_floor, MetaMathlibExt.IsAlmostBeattySequence, MetaMathlibExt.IsPositiveNatThreeWayPartition, MetaMathlibExt.IsAlmostBeattyPartition, MetaMathlibExt.beattyTerm_isAlmostBeattySequence, MetaMathlibExt.uspensky_no_partition_into_three_or_more_beatty_sequences, MetaMathlibExt.beatty_complementary_iff_irrational_inv_add_inv
statement: formalized
---

# Beatty sequences

20 results, 7 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html).

## Beatty term

For a positive integer $n$ and a real number $\alpha$, the Beatty term
$b_n(\alpha)$ is the natural number $\max(\lfloor n/\alpha \rfloor, 0)$: the $n$-th term
$\lfloor n \cdot (1/\alpha) \rfloor$ of the Beatty sequence of slope $1/\alpha$, truncated at
$0$. Division by zero is read as $0$, so $b_n(0) = 0$.

Formalized by `MetaMathlibExt.beattyTerm`, a definition declared in [MathlibExt/NumberTheory/AlmostBeattyPartition.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/AlmostBeattyPartition.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-term).

## Beatty term as a natural-number floor

For every positive integer $n$ and every real
number $\alpha$, the Beatty term $b_n(\alpha)$ equals the natural-number floor of $n/\alpha$:
the largest natural number $m$ with $m \le n/\alpha$ when $n/\alpha \ge 0$, and $0$ when
$n/\alpha < 0$. Division by zero is read as $0$, so $n/0 = 0$.

Formalized by `MetaMathlibExt.beattyTerm_eq_floor`, a theorem declared in [MathlibExt/NumberTheory/AlmostBeattyPartition.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/AlmostBeattyPartition.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-term-eq-floor).

## Almost Beatty sequence

Let $\alpha$ be a real number. A sequence $(s_n)_{n \ge 1}$ of
natural numbers indexed by the positive integers is an almost Beatty sequence for $\alpha$ when
$0 < \alpha < 1$, the sequence is strictly increasing, $s_n > 0$ for every $n \ge 1$, and
there is a natural number $B$ with $|s_n - b_n(\alpha)| \le B$ for every $n \ge 1$, where
$b_n(\alpha)$ is the Beatty term, equal to $\lfloor n/\alpha \rfloor$ once $\alpha > 0$.

Formalized by `MetaMathlibExt.IsAlmostBeattySequence`, a definition declared in [MathlibExt/NumberTheory/AlmostBeattyPartition.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/AlmostBeattyPartition.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#is-almost-beatty-sequence).

## Three-way partition of the positive integers

Three sequences $s_1, s_2, s_3$ of natural
numbers indexed by the positive integers partition the positive integers when their ranges are
pairwise disjoint, that is, $s_i(m) \ne s_j(n)$ for all $i \ne j$ and all positive integers $m$
and $n$, and the union of their ranges is exactly the set of positive integers: a natural
number $k$ is a value of some $s_i$ if and only if $k > 0$.

Formalized by `MetaMathlibExt.IsPositiveNatThreeWayPartition`, a definition declared in [MathlibExt/NumberTheory/AlmostBeattyPartition.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/AlmostBeattyPartition.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#is-positive-nat-three-way-partition).

## Almost Beatty partition

Given real numbers $\alpha_1, \alpha_2, \alpha_3$, three
sequences $s_1, s_2, s_3$ of natural numbers indexed by the positive integers form an almost
Beatty partition when, for each $i$, the sequence $s_i$ is an almost Beatty sequence for
$\alpha_i$, and the three sequences form a three-way partition of the positive integers: their
ranges are pairwise disjoint and their union is the set of positive integers.

Formalized by `MetaMathlibExt.IsAlmostBeattyPartition`, a definition declared in [MathlibExt/NumberTheory/AlmostBeattyPartition.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/AlmostBeattyPartition.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#is-almost-beatty-partition).

## Beatty sequences are almost Beatty

For every real number $\alpha$ with
$0 < \alpha < 1$, the sequence of Beatty terms $n \mapsto b_n(\alpha) = \lfloor n/\alpha \rfloor$,
indexed by the positive integers $n$, is an almost Beatty sequence for $\alpha$.

The proof takes the bound $B = 0$ and derives strict monotonicity and positivity from
$0 < \alpha < 1$.

Formalized by `MetaMathlibExt.beattyTerm_isAlmostBeattySequence`, a theorem declared in [MathlibExt/NumberTheory/AlmostBeattyPartition.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/AlmostBeattyPartition.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-term-is-almost-beatty-sequence).

## Uspensky's theorem on Beatty partitions

For a real number $\alpha$ with
$0 < \alpha < 1$, let $B_\alpha = \{\lfloor n/\alpha \rfloor : n \text{ an integer}, n \ge 1\}$
be its Beatty sequence. Let $k \ge 3$ and let $\alpha_1, \dots, \alpha_k$ be real numbers with
$0 < \alpha_i < 1$ for every $i$. Then $B_{\alpha_1}, \dots, B_{\alpha_k}$ do not partition the
positive integers: it is not the case both that $B_{\alpha_i} \cap B_{\alpha_j} = \emptyset$
for all $i \ne j$ and that $B_{\alpha_1} \cup \dots \cup B_{\alpha_k} = \{1, 2, 3, \dots\}$.

No irrationality hypothesis is imposed on the $\alpha_i$.

## Sources

- A. J. Hildebrand, Xiaomin Li, Junxian Li, and Yun Xie, *Almost Beatty Partitions*, Journal of Integer Sequences 22 (2019), Article 19.4.6, Theorem B (Uspensky's theorem), lines 234–236, <https://cs.uwaterloo.ca/journals/JIS/VOL22/Hildebrand/hilde2.tex>; first proved by Uspensky in 1927 (lines 238–244).

Formalized by `MetaMathlibExt.uspensky_no_partition_into_three_or_more_beatty_sequences`, a theorem declared in [MathlibExt/NumberTheory/Beatty/UspenskyBeattyPartition.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Beatty/UspenskyBeattyPartition.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#uspensky-no-partition-into-three-or-more).

## Beatty's theorem and its converse

Let $\alpha$ and $\beta$ be positive real numbers. The
set of the numbers $\lfloor k\alpha\rfloor$ for positive integers $k$ and the set of the numbers
$\lfloor k\beta\rfloor$ for positive integers $k$ are disjoint and their union is the set of
positive integers if and only if $\alpha$ is irrational and $\alpha^{-1} + \beta^{-1} = 1$.

The hypothesis $\beta > 0$ cannot be dropped: for irrational $0 < \alpha < 1$ the number $\beta$
with $\alpha^{-1} + \beta^{-1} = 1$ is negative, and the two sets do not partition the positive
integers.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Theorem 1 (Beatty–Rayleigh).

Stated but not proved: `MetaMathlibExt.beatty_complementary_iff_irrational_inv_add_inv` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-complementary-iff-irrational-inv).

## Counting $\beta$-Beatty terms between $\lfloor n\alpha\rfloor$ and $\lfloor n\beta\rfloor$

Let $\alpha$ be an irrational number with $1 < \alpha < 2$, let $\beta$ be a real number with
$\alpha^{-1} + \beta^{-1} = 1$, and let $B$ be the set of the numbers $\lfloor k\beta\rfloor$ for
positive integers $k$. Then for every positive integer $n$, the number of elements of $B$ in the
open interval $(\lfloor n\alpha\rfloor, \lfloor n\beta\rfloor)$ equals
$\lfloor n(2 - \alpha)\rfloor$.

By Beatty's theorem, the Beatty sequences of $\alpha$ and $\beta$ are then complementary.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Theorem 3.

Stated but not proved: `MetaMathlibExt.beatty_card_compl_between_eq_floor` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-card-compl-between-eq-floor).

## Counting $\alpha$-Beatty terms between $\lfloor n\alpha\rfloor$ and $\lfloor n\beta\rfloor$

Let $\alpha$ be an irrational number with $1 < \alpha < 2$, let $\beta$ be a real number with
$\alpha^{-1} + \beta^{-1} = 1$, and let $A$ be the set of the numbers $\lfloor k\alpha\rfloor$ for
positive integers $k$. Then for every positive integer $n$, the number of elements of $A$ in the
open interval $(\lfloor n\alpha\rfloor, \lfloor n\beta\rfloor)$ equals
$\lfloor n(\beta - 2)\rfloor$.

By Beatty's theorem, the Beatty sequences of $\alpha$ and $\beta$ are then complementary.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Theorem 4.

Stated but not proved: `MetaMathlibExt.beatty_card_self_between_eq_floor` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-card-self-between-eq-floor).

## Polanco's floor identity for $\lfloor (2 - \alpha) n \rfloor$

Let $\alpha$ be an
irrational real number with $1 < \alpha < 2$, let $\beta$ be a real number with
$\alpha^{-1} + \beta^{-1} = 1$, and write $a_m = \lfloor m\alpha \rfloor$ and
$b_m = \lfloor m\beta \rfloor$ for integers $m$ (so $b_0 = 0$). Then for every positive
integer $n$,

$$
\lfloor \beta^{-1} (b_{n-1} + 1) \rfloor - \lfloor \beta^{-1} a_n \rfloor
= \lfloor (2 - \alpha) n \rfloor.
$$

Since $\alpha > 1$, Beatty's theorem says that the conditions "$\alpha$ is irrational and
$\alpha^{-1} + \beta^{-1} = 1$" mean exactly that $(a_n)_{n \ge 1}$ and $(b_n)_{n \ge 1}$ are
complementary Beatty sequences.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Theorem 5, identity (7).

Stated but not proved: `MetaMathlibExt.beatty_floor_inv_sub_eq_floor_two_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-floor-inv-sub-eq-floor-two-sub).

## Polanco's floor identity for $\lfloor (\beta - 2) n \rfloor$

Let $\alpha$ be an
irrational real number with $1 < \alpha < 2$, let $\beta$ be a real number with
$\alpha^{-1} + \beta^{-1} = 1$, and write $a_n = \lfloor n\alpha \rfloor$ and
$b_n = \lfloor n\beta \rfloor$. Then for every positive integer $n$,

$$
\lfloor \alpha^{-1} b_n \rfloor - \lfloor \alpha^{-1} (a_n + 1) \rfloor
= \lfloor (\beta - 2) n \rfloor.
$$

Since $\alpha > 1$, Beatty's theorem says that the conditions "$\alpha$ is irrational and
$\alpha^{-1} + \beta^{-1} = 1$" mean exactly that $(a_n)_{n \ge 1}$ and $(b_n)_{n \ge 1}$ are
complementary Beatty sequences.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Theorem 5, identity (8).

Stated but not proved: `MetaMathlibExt.beatty_floor_inv_sub_eq_floor_sub_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-floor-inv-sub-eq-floor-sub-two).

## The $\beta$-Beatty counts between $\lfloor n\alpha\rfloor$ and $\lfloor n\beta\rfloor$ form a Beatty sequence

**The $\beta$-Beatty counts between $\lfloor n\alpha\rfloor$ and $\lfloor n\beta\rfloor$ form a
Beatty sequence.** Let $\alpha$ be an irrational number with $1 < \alpha < 2$, let $\beta$ be a
real number with $\alpha^{-1} + \beta^{-1} = 1$, and let $B$ be the set of the numbers
$\lfloor k\beta\rfloor$ for positive integers $k$. Then there is a real number $r$ with
$0 < r < 1$ such that for every positive integer $n$, the number of elements of $B$ in the open
interval $(\lfloor n\alpha\rfloor, \lfloor n\beta\rfloor)$ equals $\lfloor nr\rfloor$.

By Beatty's theorem, the Beatty sequences of $\alpha$ and $\beta$ are then complementary.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Corollary 3.

Stated but not proved: `MetaMathlibExt.beatty_card_compl_between_isBeatty` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-card-compl-between-is-beatty).

## Multiplicities of the values of $\lfloor n\alpha\rfloor$ for $1/(k + 1) < \alpha < 1/k$

Let $k$ be a positive integer and let $\alpha$ be a real number with
$1/(k + 1) < \alpha < 1/k$. Then every non-negative integer $t$ equals $\lfloor n\alpha\rfloor$
for exactly $k$ or exactly $k + 1$ positive integers $n$, there are infinitely many $t$ for which
it is exactly $k$, and there are infinitely many $t$ for which it is exactly $k + 1$.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Lemma 1.

Stated but not proved: `MetaMathlibExt.beatty_floor_fiber_card_eq_or_eq_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-floor-fiber-card-eq-or-eq-succ).

## Multiplicity $k + 1$ for $\alpha$ is multiplicity $k$ for $\alpha/(1 - \alpha)$

Let $k$ be
a positive integer, let $\alpha$ be a real number with $1/(k + 1) < \alpha < 1/k$, and let
$\beta = \alpha/(1 - \alpha)$. Then a non-negative integer $t$ equals $\lfloor n\alpha\rfloor$ for
exactly $k + 1$ positive integers $n$ if and only if it equals $\lfloor n\beta\rfloor$ for exactly
$k$ positive integers $n$.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Lemma 2.

Stated but not proved: `MetaMathlibExt.beatty_floor_fiber_card_succ_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-floor-fiber-card-succ-iff).

## The values of $\lfloor n\alpha\rfloor$ of each multiplicity form Beatty sets

Let $k$ be a
positive integer and let $\alpha$ be an irrational number with $1/(k + 1) < \alpha < 1/k$. Then
there are real numbers $\gamma > 0$ and $\delta > 0$ such that the positive integers $t$ that
equal $\lfloor n\alpha\rfloor$ for exactly $k + 1$ positive integers $n$ are exactly the numbers
$\lfloor m\gamma\rfloor$ for positive integers $m$, and the positive integers $t$ that equal
$\lfloor n\alpha\rfloor$ for exactly $k$ positive integers $n$ are exactly the numbers
$\lfloor m\delta\rfloor$ for positive integers $m$.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Corollary 1.

Stated but not proved: `MetaMathlibExt.beatty_floor_fiber_card_sets_isBeatty` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-floor-fiber-card-sets-is-beatty).

## Multiplicities of $\lfloor n\alpha\rfloor$ are $k$ plus the indicator of a Beatty set

Let
$k$ be a positive integer and let $\alpha$ be an irrational number with
$1/(k + 1) < \alpha < 1/k$. Then there is a real number $\delta > 0$ such that, writing $D$ for
the set of the numbers $\lfloor m\delta\rfloor$ for positive integers $m$, every non-negative
integer $t$ equals $\lfloor n\alpha\rfloor$ for exactly $k + 1$ positive integers $n$ if $t \in D$,
and for exactly $k$ positive integers $n$ if $t \notin D$.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Corollary 2.

Stated but not proved: `MetaMathlibExt.beatty_floor_fiber_card_eq_add_indicator` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-floor-fiber-card-eq-add-indicator).

## Increments of the $\beta$-Beatty counts between $\lfloor n\alpha\rfloor$ and $\lfloor n\beta\rfloor$

**Increments of the $\beta$-Beatty counts between $\lfloor n\alpha\rfloor$ and
$\lfloor n\beta\rfloor$.** Let $\alpha$ be an irrational number with $1 < \alpha < 2$, let $\beta$
be a real number with $\alpha^{-1} + \beta^{-1} = 1$, let $B$ be the set of the numbers
$\lfloor k\beta\rfloor$ for positive integers $k$, and for an integer $m$ let $r(m)$ be the number
of elements of $B$ in the open interval $(\lfloor m\alpha\rfloor, \lfloor m\beta\rfloor)$. Then for
every positive integer $n$, the difference $r(n + 1) - r(n)$ is $0$ or $1$, and it equals $1$ if
and only if $\lfloor (n + 1)\alpha\rfloor - \lfloor n\alpha\rfloor = 1$.

By Beatty's theorem, the Beatty sequences of $\alpha$ and $\beta$ are then complementary.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Lemma 4.

Stated but not proved: `MetaMathlibExt.beatty_card_compl_between_succ_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-card-compl-between-succ-sub).

## Increments of the $\alpha$-Beatty counts between $\lfloor n\alpha\rfloor$ and $\lfloor n\beta\rfloor$

**Increments of the $\alpha$-Beatty counts between $\lfloor n\alpha\rfloor$ and
$\lfloor n\beta\rfloor$.** Let $\beta$ be an irrational number with $\beta > 2$, let $\alpha$ be a
real number with $\alpha^{-1} + \beta^{-1} = 1$, let $A$ be the set of the numbers
$\lfloor k\alpha\rfloor$ for positive integers $k$, and for an integer $m$ let $c(m)$ be the number
of elements of $A$ in the open interval $(\lfloor m\alpha\rfloor, \lfloor m\beta\rfloor)$. Then for
every positive integer $n$, the difference $c(n + 1) - c(n)$ is $\lfloor\beta\rfloor - 2$ or
$\lfloor\beta\rfloor - 1$, and it equals $\lfloor\beta\rfloor - 2$ if and only if
$\lfloor (n + 1)\beta\rfloor - \lfloor n\beta\rfloor = \lfloor\beta\rfloor$.

By Beatty's theorem, the Beatty sequences of $\alpha$ and $\beta$ are then complementary.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Lemma 5.

Stated but not proved: `MetaMathlibExt.beatty_card_self_between_succ_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-card-self-between-succ-sub).

## Multiplicities of Polanco's skipping sequence

Let $k \ge 1$ be an integer, let
$\alpha$ be an irrational real number with $(2k - 1)/k < \alpha < (2k + 1)/(k + 1)$, and let
$\beta$ be a real number with $\alpha^{-1} + \beta^{-1} = 1$. Let
$A = \{\lfloor j\alpha \rfloor : j \ge 1\}$ and, for each positive integer $n$, let $c_n$ be
the number of elements of $A$ strictly between $\lfloor n\alpha \rfloor$ and
$\lfloor n\beta \rfloor$. Let $f(x) = 2 - 1/x$, let $f^{k-1}$ be its $(k-1)$-fold iterate, and
let $\delta = -1 + 1/f^{k-1}(\alpha - 1)$, that is,
$\delta = -1 + 1/(2 - 1/(2 - \cdots - 1/(\alpha - 1)))$ with $k - 1$ twos. Then for every
non-negative integer $m$, the number of positive integers $n$ with $c_n = m$ is $k$ if
$m = \lfloor j\delta \rfloor$ for some integer $j \ge 1$, and $k - 1$ otherwise, where an
infinite set is counted as having $0$ elements.

For $k = 1$ this gives $\delta = 1/(\alpha - 1) - 1 = \beta - 2$, and the multiplicity is one
or zero.

## Sources

- Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*, INTEGERS 25 (2025), Article A104, Lemma 6.

Stated but not proved: `MetaMathlibExt.beatty_skipping_card_eq_add_indicator` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeattyDecompositionWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BeattyDecompositionWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html#beatty-skipping-card-eq-add-indicator).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Beatty sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/beatty-sequences)
