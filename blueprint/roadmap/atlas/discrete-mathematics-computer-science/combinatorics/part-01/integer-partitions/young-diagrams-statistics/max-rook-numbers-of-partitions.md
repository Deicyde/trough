---
declaration: section
origin: cited
lean: MetaMathlibExt.boardMaxRookNumber, MetaMathlibExt.partitionFerrersBoard, MetaMathlibExt.partitionMaxRookNumber, MetaMathlibExt.maxRookPartitionCount, MetaMathlibExt.partitionMaxRookNumberMax, MetaMathlibExt.partitionFerrersBoard_two_one, MetaMathlibExt.partitionMaxRookNumber_five_three_two_one, MetaMathlibExt.partitionMaxRookNumberMax_zero
statement: formalized
---

# Max-rook numbers of partitions

22 results, 8 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html).

## Max-rook number of a board

For a finite board $B \subseteq \mathbb{N} \times \mathbb{N}$,
whose cell $(i, j)$ lies in row $i$ and column $j$, the max-rook number of $B$ is the largest
size of a subset of $B$ that contains at most one cell of each row and at most one cell of each
column, that is, the largest number of non-attacking rooks that can be placed on $B$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Section 2 (max-rook number).

Formalized by `MetaMathlibExt.boardMaxRookNumber`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#board-max-rook-number).

## Ferrers board of a partition

Let $p$ be a partition of $n$, and number rows and columns
from $0$. The Ferrers board of $p$ is the finite set of cells
$(i, j) \in \mathbb{N} \times \mathbb{N}$ such that the $(i+1)$-st largest part of $p$ exceeds $j$,
that is, such that more than $i$ parts of $p$, counted with multiplicity, exceed $j$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Section 1 (Ferrers diagram and Ferrers board).

Formalized by `MetaMathlibExt.partitionFerrersBoard`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#partition-ferrers-board).

## Max-rook number of a partition

The max-rook number $R(\pi)$ of a partition $\pi$ of $n$
is the largest number of non-attacking rooks on the Ferrers board of $\pi$: the largest number
of cells of the board, no two in the same row and no two in the same column.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Section 2.

Formalized by `MetaMathlibExt.partitionMaxRookNumber`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#partition-max-rook-number).

## Partitions with a given max-rook number

For natural numbers $k$ and $n$, $R_k(n)$ is
the number of partitions of $n$ whose max-rook number, the largest number of non-attacking rooks
on the Ferrers board, equals $k$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Equation (2.2).

Formalized by `MetaMathlibExt.maxRookPartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count).

## Largest max-rook number among partitions of $n$

For a natural number $n \ge 1$, $F(n)$
is the largest max-rook number $R(\pi)$ over all partitions $\pi$ of $n$, where $R(\pi)$ is the
largest number of non-attacking rooks on the Ferrers board of $\pi$. By convention $F(0) = 1$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Equation (2.1).

Formalized by `MetaMathlibExt.partitionMaxRookNumberMax`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#partition-max-rook-number-max).

## Ferrers board of the partition $(2, 1)$

With rows and columns numbered from $0$, the
Ferrers board of the partition $(2, 1)$ of $3$ consists of exactly the three cells $(0, 0)$,
$(0, 1)$ and $(1, 0)$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Section 1 (Ferrers board); characteristic check of `partitionFerrersBoard`.

Formalized by `MetaMathlibExt.partitionFerrersBoard_two_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#partition-ferrers-board-two-one).

## Max-rook number of the partition $(5, 3, 2, 1)$

The partition $(5, 3, 2, 1)$ of $11$
has max-rook number $4$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Figure 1.

Formalized by `MetaMathlibExt.partitionMaxRookNumber_five_three_two_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#partition-max-rook-number-five-three-two).

## The convention $F(0) = 1$

The function $F$, whose value $F(n)$ for $n \ge 1$ is the
largest max-rook number of a partition of $n$, takes the value $F(0) = 1$ at $n = 0$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, after Equation (2.1).

Formalized by `MetaMathlibExt.partitionMaxRookNumberMax_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#partition-max-rook-number-max-zero).

## Generating function of the largest max-rook number

Let $F(n)$ be the largest max-rook
number of a partition of $n$ for $n \ge 1$, and $F(0) = 1$. For every complex number $q$ with
$|q| < 1$, the series $\sum_{n \ge 0} F(n) q^n$ is summable with sum

$$\frac{(q^2;q^2)_\infty \, (-q;q)_\infty - q}{1 - q},$$

where $(a;q)_\infty = \prod_{k \ge 0} (1 - a q^k)$ is the infinite q-Pochhammer symbol.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 1 (`jis-2026-26.2.6-thm-1`).

Stated but not proved: `MetaMathlibExt.hasSum_partitionMaxRookNumberMax` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#has-sum-partition-max-rook-number-max).

## Generating function of $R_3(n)$

Let $R_3(n)$ be the number of partitions of $n$ with
max-rook number $3$. In the ring $\mathbb{Z}[[q]]$ of formal power series with integer
coefficients,

$$(1-q)^3(1+q+q^2) \sum_{n \ge 0} R_3(n)\, q^n = q^6(1+2q+q^2+2q^3-q^4-q^6-q^7+q^8).$$

This is the rational generating function of $R_3(n)$ with its denominator cleared.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 2 (`jis-2026-26.2.6-thm-2`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_three_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-three-gen-fun).

## Linear recurrence for $R_3(n)$

Let $R_3(n)$ be the number of partitions of $n$ with
max-rook number $3$. For every natural number $n > 14$,
$R_3(n) = 2R_3(n-1) - R_3(n-2) + R_3(n-3) - 2R_3(n-4) + R_3(n-5)$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Corollary 3 (`jis-2026-26.2.6-cor-3`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_three_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-three-recurrenc).

## Generating function of partitions with max-rook number 4

Let $R_4(n)$ be the number of
partitions of $n$ with max-rook number $4$. In the ring of formal power series in $q$ with integer
coefficients,

$$(1-q)(1-q^2)(1-q^3)(1-q^4) \sum_{n \ge 0} R_4(n) q^n = q^{10} P(q),$$

where

$$P(q) = 1 + 4q + 6q^2 + 7q^3 + 6q^4 + 2q^5 - 5q^7 - 5q^8 - 5q^9 + q^{11} + 3q^{12} + 2q^{13} -
q^{16}.$$

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 4 (`jis-2026-26.2.6-thm-4`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_four_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-four-gen-fun).

## Generating function of partitions with max-rook number 5

Let $R_5(n)$ be the number of
partitions of $n$ with max-rook number $5$. In the ring of formal power series in $q$ with integer
coefficients,

$$(1-q)^2(1-q^3)(1-q^4)(1-q^5) \sum_{n \ge 0} R_5(n) q^n = q^{15} P(q),$$

where

$$P(q) = 1 + 4q + 6q^2 + 8q^3 + 8q^4 + 4q^5 + 4q^6 - 5q^7 - 5q^8 - 10q^9 - 7q^{10} -
5q^{11} + 4q^{13} + 6q^{14} + 7q^{15} + 2q^{17} - 4q^{18} - q^{19} - q^{20} - q^{21} +
q^{22} - q^{23} + q^{24}.$$

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 5 (`jis-2026-26.2.6-thm-5`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_five_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-five-gen-fun).

## Quasi-polynomial formula for partitions with max-rook number 3

Let $R_3(n)$ be the number
of partitions of $n$ with max-rook number $3$. For every natural number $m$ and every
$a \in \{0, 1, 2\}$ with $3m + a > 9$, $R_3(3m + a)$ equals $6m^2 - 15m + 7$, $6m^2 - 11m + 2$
or $6m^2 - 7m - 1$ according as $a = 0$, $a = 1$ or $a = 2$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 6, first part (`jis-2026-26.2.6-thm-6`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_three_formula` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-three-formula).

## Periodicity of $R_3(n)$ modulo $p$

Let $R_3(n)$ be the number of partitions of $n$
with max-rook number $3$. For all natural numbers $p \ge 2$ and $n > 9$,
$R_3(n + 3p) \equiv R_3(n) \pmod{p}$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 6, second part (`jis-2026-26.2.6-thm-6`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_three_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-three-mod-eq).

## Asymptotic growth of $R_3(n)$

Let $R_3(n)$ be the number of partitions of $n$ with
max-rook number $3$. Then $R_3(n) \sim \frac{2}{3} n^2$ as $n \to \infty$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Corollary 7 (`jis-2026-26.2.6-cor-7`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_three_isEquivalent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-three-is-equiva).

## Quasi-polynomial formula for partitions with max-rook number 4

Let $R_4(n)$ be the number
of partitions of $n$ with max-rook number $4$. For all natural numbers $m$ and $a$ with
$0 \le a \le 11$ and $12m + a > 16$,

$$R_4(12m + a) = 192m^3 + b_a m^2 + c_a m + d_a,$$

where, listed for $a = 0, 1, \ldots, 11$,
$(b_a) = (-264, -216, -168, -120, -72, -24, 24, 72, 120, 168, 216, 264)$,
$(c_a) = (87, 44, 15, -12, -25, -36, -33, -28, -9, 12, 47, 84)$ and
$(d_a) = (-3, 5, 5, 7, 4, 3, -2, -3, -5, -5, -3, 3)$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 8, first part (`jis-2026-26.2.6-thm-8`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_four_formula` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-four-formula).

## A congruence for partitions with max-rook number 4

Let $R_4(n)$ be the number of
partitions of $n$ with max-rook number $4$. For all natural numbers $p \ge 2$ and $n > 16$,
$R_4(n + 12p) \equiv R_4(n) \pmod p$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 8, second part (`jis-2026-26.2.6-thm-8`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_four_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-four-mod-eq).

## Asymptotics of partitions with max-rook number 4

Let $R_4(n)$ be the number of partitions
of $n$ with max-rook number $4$. Then $R_4(n) \sim n^3/9$ as $n \to \infty$.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Corollary 9 (`jis-2026-26.2.6-cor-9`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_four_isEquivalent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-four-is-equival).

## Parity of $R_3(n)$

Let $R_3(n)$ be the number of partitions of $n$ with max-rook number
$3$. For every natural number $n > 9$, $R_3(n)$ is even if $n$ is odd and odd if $n$ is even.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 10 (`jis-2026-26.2.6-thm-10`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_three_mod_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-three-mod-two).

## Parity of the number of partitions with max-rook number 4

Let $R_4(n)$ be the number of
partitions of $n$ with max-rook number $4$. For every natural number $n > 16$, $R_4(n)$ is even if
$n \equiv 4 \pmod 8$ or $n \equiv 6 \pmod 8$, and odd otherwise.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 11 (`jis-2026-26.2.6-thm-11`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_four_mod_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-four-mod-two).

## Parity of the number of partitions with max-rook number 5

Let $R_5(n)$ be the number of
partitions of $n$ with max-rook number $5$. For every natural number $n > 25$, $R_5(n)$ is even if
$n \equiv 5 \pmod 8$ or $n \equiv 7 \pmod 8$, and odd otherwise.

## Sources

- N. Guru Sharan, *Rook Decomposition of the Partition Function*, Journal of Integer Sequences 29 (2026), Article 26.2.6, Theorem 13 (`jis-2026-26.2.6-thm-13`).

Stated but not proved: `MetaMathlibExt.maxRookPartitionCount_five_mod_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RookDecompositionWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html#max-rook-partition-count-five-mod-two).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Max-rook numbers of partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/max-rook-numbers-of-partitions)
