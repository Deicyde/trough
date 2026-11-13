---
declaration: section
origin: cited
lean: MetaMathlibExt.card_coloredPartitions_differentColors, MetaMathlibExt.card_coloredPartitions_fullyDifferent, MetaMathlibExt.card_coloredPartitions_fullyDifferent_le, MetaMathlibExt.ncard_constantBlockPartitions_eq_doubleCompositions, MetaMathlibExt.ncard_distinctConstantBlockPartitions_eq_coloredCompositions, MetaMathlibExt.generalized_euler_partition_theorem, MetaMathlibExt.euler_partition_theorem_restrictedCompositions, MetaMathlibExt.coloredPartitions_differentParts_eq_restrictedColors
statement: formalized
---

# Colored partitions and Euler-type identities

8 results, 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html).

## Colored partitions with distinct colors

A colored part is a pair $(m, j)$ of integers
with $1 \le j \le m$, read as the part $m$ in color $j$. For every $n \ge 0$, the number of
nonempty finite sets of colored parts $(m, j)$ with $m \le n$ in which no two colored parts have
the same color $j$ is $(n + 1)! - 1$.

A colored partition whose parts have pairwise different colors has no repeated colored part, so
it is the same as a finite set of colored parts; the empty partition is not counted.

## Sources

- Beimar J. Naranjo and José L. Ramírez, *On Colored Partitions and Euler-Type Identities*, INTEGERS 26 (2026), Article A20, Theorem 1.

Stated but not proved: `MetaMathlibExt.card_coloredPartitions_differentColors` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html#card-colored-partitions-different-colors).

## Formula for colored partitions into fully different parts

A colored part is a pair
$(m, j)$ of integers with $1 \le j \le m$, read as the part $m$ in color $j$. For $n \ge 0$, let
$\mathrm{pf}_c(n)$ be the number of finite sets of colored parts whose sizes $m$ sum to $n$ and
in which no two colored parts have the same size and no two have the same color. Then
$\mathrm{pf}_c(n)$ is the sum, over all partitions of $n$ into distinct parts
$p_1 > p_2 > \cdots > p_k$, of the product $p_k (p_{k-1} - 1) \cdots (p_1 - (k - 1))$.

The identity is stated for all $n \ge 0$; at $n = 0$ both sides equal $1$, while the paper states
it for $n \ge 1$.

## Sources

- Beimar J. Naranjo and José L. Ramírez, *On Colored Partitions and Euler-Type Identities*, INTEGERS 26 (2026), Article A20, Theorem 2.

Stated but not proved: `MetaMathlibExt.card_coloredPartitions_fullyDifferent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html#card-colored-partitions-fully-different).

## Colored partitions into fully different parts with bounded size

A colored part is a pair
$(m, j)$ of integers with $1 \le j \le m$, read as the part $m$ in color $j$. For every $n \ge 0$,
the number of nonempty finite sets of colored parts $(m, j)$ with $m \le n$ in which no two
colored parts have the same size $m$ and no two have the same color $j$ is $B_{n+1} - 1$, where
$B_k$ denotes the $k$-th Bell number.

## Sources

- Beimar J. Naranjo and José L. Ramírez, *On Colored Partitions and Euler-Type Identities*, INTEGERS 26 (2026), Article A20, Theorem 3.

Stated but not proved: `MetaMathlibExt.card_coloredPartitions_fullyDifferent_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html#card-colored-partitions-fully-different-2).

## Constant-block partitions and double compositions

For $n \ge 0$, count the pairs
$(A, P)$ where $A$ is a multiset of $n$ positive integers whose distinct elements are exactly
$1, \dots, k$ for some $k \ge 0$, and $P$ is a partition of $A$ into constant blocks, that is,
a multiset of nonempty multisets, each with all its elements equal, whose sum is $A$. The number
of such pairs equals the number $d_c(n)$ of double compositions of $n$, that is, compositions of
$n$ in which each summand $m$ is colored by a partition of $m$:

$$d_c(n) = \sum_{(c_1, \dots, c_r)} p(c_1) \cdots p(c_r),$$

where the sum runs over all compositions $(c_1, \dots, c_r)$ of $n$ and $p(m)$ is the number of
partitions of $m$.

## Sources

- Beimar J. Naranjo and José L. Ramírez, *On Colored Partitions and Euler-Type Identities*, INTEGERS 26 (2026), Article A20, Theorem 4.

Stated but not proved: `MetaMathlibExt.ncard_constantBlockPartitions_eq_doubleCompositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html#ncard-constant-block-partitions-eq-doubl).

## Distinct constant-block partitions and colored compositions

For $n \ge 0$, count the
pairs $(A, P)$ where $A$ is a multiset of $n$ positive integers whose distinct elements are
exactly $1, \dots, k$ for some $k \ge 0$, and $P$ is a partition of $A$ into pairwise distinct
constant blocks, that is, a multiset of pairwise distinct nonempty multisets, each with all its
elements equal, whose sum is $A$. The number of such pairs equals the number of compositions of
$n$ in which each summand $m$ is colored by a partition of $m$ into distinct parts:

$$\sum_{(c_1, \dots, c_r)} q(c_1) \cdots q(c_r),$$

where the sum runs over all compositions $(c_1, \dots, c_r)$ of $n$ and $q(m)$ is the number of
partitions of $m$ into distinct parts.

## Sources

- Beimar J. Naranjo and José L. Ramírez, *On Colored Partitions and Euler-Type Identities*, INTEGERS 26 (2026), Article A20, Corollary 1.

Stated but not proved: `MetaMathlibExt.ncard_distinctConstantBlockPartitions_eq_coloredCompositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html#ncard-distinct-constant-block-partitions).

## Generalized Euler partition theorem

Let $S$ be a set of compositions (finite sequences
of positive integers) such that doubling every summand of a member of $S$ gives a member of $S$,
and halving every summand of a member of $S$ whose summands are all even gives a member of $S$.
Let $n \ge 0$. The number of partitions of $n$ into colored parts in which each part $k$ is
colored by a composition in $S$ with sum $k$, and no colored part (a pair of part and color)
appears twice, equals the number of such partitions of $n$, with repetition allowed, in which no
even part is colored by a composition whose summands are all even. The same holds when each part
$k$ is colored by a composition in $S$ with sum at most $k$.

## Sources

- Beimar J. Naranjo and José L. Ramírez, *On Colored Partitions and Euler-Type Identities*, INTEGERS 26 (2026), Article A20, Theorem 5.

Stated but not proved: `MetaMathlibExt.generalized_euler_partition_theorem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html#generalized-euler-partition-theorem).

## Euler partition theorem for restricted compositions

A composition (a finite sequence of
positive integers) is $\ell$-restricted if it has at most $\ell$ summands. Let $\ell \ge 0$ and
$n \ge 0$. The number of partitions of $n$ into colored parts in which each part $k$ is colored
by an $\ell$-restricted composition of $k$, and no colored part (a pair of part and color)
appears twice, equals the number of such partitions of $n$, with repetition allowed, in which no
even part is colored by a composition whose summands are all even.

## Sources

- Beimar J. Naranjo and José L. Ramírez, *On Colored Partitions and Euler-Type Identities*, INTEGERS 26 (2026), Article A20, Corollary 3.

Stated but not proved: `MetaMathlibExt.euler_partition_theorem_restrictedCompositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html#euler-partition-theorem-restricted-compo).

## Colored partitions with different parts

A colored part is a pair $(m, j)$ of integers
with $1 \le j \le m$, read as the part $m$ in color $j$, and a colored partition of $n$ is a
finite multiset of colored parts whose sizes $m$ sum to $n$. For every $n \ge 0$, the number of
colored partitions of $n$ in which no colored part is repeated equals the number of colored
partitions of $n$ in which no even part has an even color, and it also equals the number of
colored partitions of $n$ in which no even part has an odd color.

## Sources

- Beimar J. Naranjo and José L. Ramírez, *On Colored Partitions and Euler-Type Identities*, INTEGERS 26 (2026), Article A20, Corollary 4.

Stated but not proved: `MetaMathlibExt.coloredPartitions_differentParts_eq_restrictedColors` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/ColoredPartitionsEulerTypeWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html#colored-partitions-different-parts-eq-re).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Colored partitions and Euler-type identities](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-partitions/partition-identities/colored-partitions-and-euler-type-identities)
