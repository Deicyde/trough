---
declaration: section
origin: cited
lean: MetaMathlibExt.sumDistinctPartsModEq, MetaMathlibExt.sumDistinctPartsMultAtLeast, MetaMathlibExt.sumDistinctParts_small_values, MetaMathlibExt.dysonRank, MetaMathlibExt.dysonRank_small_values, MetaMathlibExt.partitionCrank, MetaMathlibExt.partitionCrank_small_values, MetaMathlibExt.sumDistinctPartsModEq_eq_sum_partition
statement: formalized
---

# Merca's identities for sums of different parts

21 results, 7 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html).

## Sum of different parts congruent to $r$ modulo $m$

For natural numbers $m$, $r$, $n$,
$a_{r,m}(n)$ is the sum, over all partitions $\mu$ of $n$, of the different parts $x$ of $\mu$
with $x \bmod m = r$; a part contributes $x$ once regardless of its multiplicity. It is used
with $0 \le r < m$, where $x \bmod m = r$ means $x \equiv r \pmod m$.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Section 1 (definition of `a_{r,m}(n)`).

Formalized by `MetaMathlibExt.sumDistinctPartsModEq`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mod-eq).

## Sum of different parts appearing at least $m$ times

For natural numbers $m$ and $n$,
$s_m(n)$ is the sum, over all partitions $\mu$ of $n$, of the different parts of $\mu$ that
appear at least $m$ times in $\mu$; such a part $j$ contributes $j$ once regardless of its
multiplicity.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Section 1 (definition of `s_m(n)`).

Formalized by `MetaMathlibExt.sumDistinctPartsMultAtLeast`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mult-at-least).

## Small values of Merca's distinct-part sums

For natural numbers $m$, $r$ and $n$, let
$a_{r,m}(n)$ be the sum, over all partitions of $n$, of the different parts $x$ of the partition
with $x \bmod m = r$, and let $s_m(n)$ be the sum, over all partitions of $n$, of the different
parts that occur at least $m$ times in the partition; each such part counts once per partition.
Then $a_{r,m}(0) = 0$ and $s_m(0) = 0$ for all $m$ and $r$, and moreover $a_{0,1}(1) = 1$,
$s_1(1) = 1$ and $s_2(1) = 0$.

The empty partition of $0$ has no parts, and $1$ has the single partition $1$.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Section 1 (definitions of `a_{r,m}(n)` and `s_m(n)`).

Formalized by `MetaMathlibExt.sumDistinctParts_small_values`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-small-values).

## Dyson's rank of a partition

The rank of a partition $\mu$ of $n$ is the integer
$r(\mu) = \mu_1 - \ell(\mu)$, the largest part $\mu_1$ of $\mu$ minus its number of parts
$\ell(\mu)$, where the largest part of the empty partition is taken to be $0$. In particular the
empty partition has rank $0$.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Section 2 (definition of the rank before Theorem 8).

Formalized by `MetaMathlibExt.dysonRank`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#dyson-rank).

## Rank of the partitions of $0$ and $1$

The empty partition of $0$ and the partition $(1)$
of $1$ both have Dyson rank $0$.

Consequently the number of partitions of $k$ with nonnegative rank is $1$ for $k = 0$ and
$k = 1$, no partition of $1$ has positive rank, and no partition of $0$ has rank at most $-2$.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Section 2 (definition of the rank before Theorem 8).

Formalized by `MetaMathlibExt.dysonRank_small_values`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#dyson-rank-small-values).

## Crank of a partition

Let $\mu$ be a partition of $n$ and let $\omega(\mu)$ be the number
of parts of $\mu$ equal to $1$. The crank of $\mu$ (Andrews and Garvan) is the integer defined as
follows: if $\omega(\mu) = 0$, it is the largest part of $\mu$, where the largest part of the
empty partition is taken to be $0$; if $\omega(\mu) > 0$, it is the number of parts of $\mu$
larger than $\omega(\mu)$, counted with multiplicity, minus $\omega(\mu)$.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Section 2 (definition of the crank before Theorem 11).

Formalized by `MetaMathlibExt.partitionCrank`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#partition-crank).

## Crank of the partitions of $0$ and $1$

The empty partition of $0$ has crank $0$, and the
partition $(1)$ of $1$ has crank $0 - 1 = -1$.

Consequently the number of partitions of $0$ with nonnegative crank is $1$, and no partition of
$1$ has nonnegative crank.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Section 2 (definition of the crank before Theorem 11).

Formalized by `MetaMathlibExt.partitionCrank_small_values`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#partition-crank-small-values).

## Merca's identity for different parts in a residue class

Let $m$, $r$ and $n$ be natural
numbers with $r < m$, let $a_{r,m}(n)$ be the sum, over all partitions of $n$, of the different
parts congruent to $r$ modulo $m$, each counted once per partition whatever its multiplicity, and
let $p(k)$ be the number of partitions of $k$. Then

$$a_{r,m}(n) = \sum_{j \ge 0,\ mj + r \le n} (mj + r)\, p(n - mj - r).$$

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 1 (i).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsModEq_eq_sum_partition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mod-eq-eq-sum-partiti).

## Merca's identity for $s_m(n)$

Let $m \ge 1$ and $n$ be natural numbers, write $s_m(n)$
for the sum of the different parts that appear at least $m$ times in partitions of $n$, and
$p(k)$ for the number of partitions of $k$. Then $s_m(n) = \sum_{j \ge 0,\ mj \le n} j\, p(n - mj)$.

The paper's hypothesis $0 \le r < m$ forces $m \ge 1$; for $m = 0$ the right side diverges.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 1 (ii).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsMultAtLeast_eq_sum_partition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mult-at-least-eq-sum).

## Different parts in a residue class and even-minus-odd partition counts

Let $m$, $r$ and
$n$ be natural numbers with $r < m$, and for $k \ge 0$ let $a_{r,m}(k)$ be the sum, over all
partitions of $k$, of the different parts congruent to $r$ modulo $m$, each counted once per
partition whatever its multiplicity. Let $p_{e-o}(k) = \sum_{\mu} (-1)^{\ell(\mu)}$, the sum over
the partitions $\mu$ of $k$ with $\ell(\mu)$ the number of parts of $\mu$; it is the number of
partitions of $k$ with an even number of parts minus the number with an odd number of parts. Then

$$a_{r,m}(n) + 2 \sum_{k \ge 1,\ k^2 \le n} (-1)^k a_{r,m}(n - k^2)
= \sum_{j \ge 0,\ mj + r \le n} (mj + r)\, p_{e-o}(n - mj - r).$$

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 2.

Stated but not proved: `MetaMathlibExt.sumDistinctPartsModEq_square_eq_evenOdd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mod-eq-square-eq-even).

## Twice-square sum of $a_{r,m}$ and distinct odd parts

Let $m, r, n$ be natural numbers
with $r < m$. Write $a_{r,m}(k)$ for the sum of the different parts congruent to $r$ modulo $m$
in all partitions of $k$, and $q_{\mathrm{odd}}(k)$ for the number of partitions of $k$ into
distinct odd parts. Then

$$
a_{r,m}(n) + 2 \sum_{k \ge 1,\ 2k^2 \le n} (-1)^k a_{r,m}(n - 2k^2)
= \sum_{j \ge 0,\ mj + r \le n} (mj + r)\, q_{\mathrm{odd}}(n - mj - r).
$$

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 4.

Stated but not proved: `MetaMathlibExt.sumDistinctPartsModEq_twiceSquare_eq_oddDistinct` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mod-eq-twice-square-e).

## Signed triangular sum of $a_{r,m}$ and distinct partitions

Let $m, r, n$ be natural
numbers with $r < m$. Write $a_{r,m}(k)$ for the sum of the different parts congruent to $r$
modulo $m$ in all partitions of $k$, $q(k)$ for the number of partitions of $k$ into distinct
parts, and $\tilde q(\ell)$ for $q(\ell/2)$ when $\ell$ is even and for $0$ when $\ell$ is odd.
Then

$$
\sum_{k \ge 0,\ k(k+1)/2 \le n} (-1)^{k(k+1)/2} a_{r,m}\bigl(n - k(k+1)/2\bigr)
= \sum_{j \ge 0,\ mj + r \le n} (mj + r)\, \tilde q(n - mj - r).
$$

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 6.

Stated but not proved: `MetaMathlibExt.sumDistinctPartsModEq_triangular_eq_distinct_half` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mod-eq-triangular-eq).

## Signed triangular sum of $s_m$ and distinct partitions

Let $m \ge 1$ and $n$ be natural
numbers. Write $s_m(k)$ for the sum of the different parts that appear at least $m$ times in
partitions of $k$, $q(k)$ for the number of partitions of $k$ into distinct parts, and
$\tilde q(\ell)$ for $q(\ell/2)$ when $\ell$ is even and for $0$ when $\ell$ is odd. Then

$$
\sum_{k \ge 0,\ k(k+1)/2 \le n} (-1)^{k(k+1)/2} s_m\bigl(n - k(k+1)/2\bigr)
= \sum_{j \ge 0,\ mj \le n} j\, \tilde q(n - mj).
$$

The paper says $m \ge 0$; for $m = 0$ the right side diverges.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 7.

Stated but not proved: `MetaMathlibExt.sumDistinctPartsMultAtLeast_triangular_eq_distinct_half` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mult-at-least-triangu).

## Different parts in a residue class and partitions of nonnegative rank

Let $m$, $r$ and
$n$ be natural numbers with $r < m$, and for $k \ge 0$ let $a_{r,m}(k)$ be the sum, over all
partitions of $k$, of the different parts congruent to $r$ modulo $m$, each counted once per
partition whatever its multiplicity. Let $N(k)$ be the number of partitions of $k$ whose Dyson
rank (largest part minus number of parts) is nonnegative. Then

$$\sum_{j \ge 0,\ j(3j+1)/2 \le n} (-1)^j a_{r,m}(n - j(3j+1)/2)
= \sum_{j \ge 0,\ mj + r \le n} (mj + r)\, N(n - mj - r).$$

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 8 (i).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsModEq_pentagonal_eq_nonnegRank` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mod-eq-pentagonal-eq).

## Different parts in a residue class and partitions of positive rank

Let $m$, $r$ and $n$
be natural numbers with $r < m$, and for $k \ge 0$ let $a_{r,m}(k)$ be the sum, over all
partitions of $k$, of the different parts congruent to $r$ modulo $m$, each counted once per
partition whatever its multiplicity. Let $R(k)$ be the number of partitions of $k$ whose Dyson
rank (largest part minus number of parts) is positive. Then

$$\sum_{j \ge 1,\ j(3j+1)/2 \le n} (-1)^{j+1} a_{r,m}(n - j(3j+1)/2)
= \sum_{j \ge 0,\ mj + r \le n} (mj + r)\, R(n - mj - r).$$

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 8 (ii).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsModEq_pentagonal_eq_posRank` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mod-eq-pentagonal-eq-2).

## Pentagonal sum of $s_m$ and nonnegative rank

Let $m \ge 1$ and $n$ be natural numbers.
Write $s_m(k)$ for the sum of the different parts that appear at least $m$ times in partitions
of $k$, and $N(k)$ for the number of partitions of $k$ with nonnegative Dyson rank. Then

$$
\sum_{j \ge 0,\ j(3j+1)/2 \le n} (-1)^j s_m\bigl(n - j(3j+1)/2\bigr)
= \sum_{j \ge 0,\ mj \le n} j\, N(n - mj).
$$

The paper says $m \ge 0$; for $m = 0$ the right side diverges.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 9 (i).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsMultAtLeast_pentagonal_eq_nonnegRank` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mult-at-least-pentago).

## Pentagonal sum of $s_m$ and positive rank

Let $m \ge 1$ and $n$ be natural numbers.
Write $s_m(k)$ for the sum of the different parts that appear at least $m$ times in partitions
of $k$, and $R(k)$ for the number of partitions of $k$ with positive Dyson rank. Then

$$
\sum_{j \ge 1,\ j(3j+1)/2 \le n} (-1)^{j+1} s_m\bigl(n - j(3j+1)/2\bigr)
= \sum_{j \ge 0,\ mj \le n} j\, R(n - mj).
$$

The paper says $m \ge 0$; for $m = 0$ the right side diverges.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 9 (ii).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsMultAtLeast_pentagonal_eq_posRank` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mult-at-least-pentago-2).

## Different parts in a residue class and Garden of Eden partitions

Let $m$, $r$ and $n$ be
natural numbers with $r < m$, and for $k \ge 0$ let $a_{r,m}(k)$ be the sum, over all partitions
of $k$, of the different parts congruent to $r$ modulo $m$, each counted once per partition
whatever its multiplicity. Let $G(k)$ be the number of Garden of Eden partitions of $k$, that is,
partitions of $k$ whose Dyson rank (largest part minus number of parts) is at most $-2$. Then

$$\sum_{j \ge 1,\ 3j(j+1)/2 \le n} (-1)^{j+1} a_{r,m}(n - 3j(j+1)/2)
= \sum_{j \ge 0,\ mj + r \le n} (mj + r)\, G(n - mj - r).$$

The sum on the left starts at $j = 1$. Starting it at $j = 0$ makes the identity false: for
$m = 1$, $r = 0$ and $n = 1$ the left side becomes $-a_{0,1}(1) = -1$ while the right side is $0$.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 10 (i).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsModEq_eq_gardenOfEden` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mod-eq-eq-garden-of-e).

## Garden of Eden identity for $s_m$

Let $m \ge 1$ and $n$ be natural numbers. Write
$s_m(k)$ for the sum of the different parts that appear at least $m$ times in partitions of
$k$, and $G(k)$ for the number of Garden of Eden partitions of $k$, those whose Dyson rank is
at most $-2$ (so $G(0) = 0$). Then

$$
\sum_{j \ge 1,\ 3j(j+1)/2 \le n} (-1)^{j+1} s_m\bigl(n - 3j(j+1)/2\bigr)
= \sum_{j \ge 0,\ mj \le n} j\, G(n - mj).
$$

The paper says $m \ge 0$; for $m = 0$ the right side diverges.

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 10 (ii).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsMultAtLeast_eq_gardenOfEden` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mult-at-least-eq-gard).

## Different parts in a residue class and partitions of nonnegative crank

Let $m$, $r$ and
$n$ be natural numbers with $r < m$, and for $k \ge 0$ let $a_{r,m}(k)$ be the sum, over all
partitions of $k$, of the different parts congruent to $r$ modulo $m$, each counted once per
partition whatever its multiplicity. Let $C(k)$ be the number of partitions of $k$ whose crank is
nonnegative. Then

$$\sum_{j \ge 0,\ j(j+1)/2 \le n} (-1)^j a_{r,m}(n - j(j+1)/2)
= \sum_{j \ge 0,\ mj + r \le n} (mj + r)\, C(n - mj - r).$$

The companion identity of the source with the number $D(k)$ of partitions of $k$ with positive
crank is not stated: it fails for this crank, since $D(1) = 0$ while $p(1) - C(1) = 1$, where
$p(k)$ is the number of partitions of $k$ (for $m = 2$, $r = 1$, $n = 2$ its left side is $1$ and
its right side is $0$).

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 11 (i).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsModEq_triangular_eq_nonnegCrank` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mod-eq-triangular-eq-2).

## Signed triangular sum of $s_m$ and nonnegative crank

Let $m \ge 1$ and $n$ be natural
numbers. Write $s_m(k)$ for the sum of the different parts that appear at least $m$ times in
partitions of $k$, and $C(k)$ for the number of partitions of $k$ with nonnegative crank. Then

$$
\sum_{j \ge 0,\ j(j+1)/2 \le n} (-1)^j s_m\bigl(n - j(j+1)/2\bigr)
= \sum_{j \ge 0,\ mj \le n} j\, C(n - mj).
$$

The paper says $m \ge 0$; for $m = 0$ the right side diverges. Part (ii) (with $D(k)$, positive
crank) is omitted: it is false for this crank ($m = 1$, $n = 2$: left side $s_1(1) = 1$, right
side $D(1) + 2 D(0) = 0$).

## Sources

- Cristina Ballantine, *Combinatorial Proofs of Merca's Identities Involving the Sum of Different Parts Congruent to r Modulo m in All Partitions of n*, INTEGERS 24 (2024), Article A15, Theorem 12 (i).

Stated but not proved: `MetaMathlibExt.sumDistinctPartsMultAtLeast_triangular_eq_nonnegCrank` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MercaDistinctPartsSumWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html#sum-distinct-parts-mult-at-least-triangu-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Merca's identities for sums of different parts](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/partition-identities/merca-s-identities-for-sums-of-different-parts)
