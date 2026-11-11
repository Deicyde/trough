---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.IsTiling, MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.transpositionsWithOne, MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.PartitionShape, MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.PartitionShape.contentSumAux, MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.PartitionShape.contentSum, MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.OrderedSetPartition, MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.SendsPartition, MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.IsPartitionTransitive
statement: formalized
---

# Tilings of the symmetric group by transpositions

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html).

## Fang Xia Tiling Problem

## Tiling of a group by two subsets

For subsets $X$ and $Y$ of a group $G$, the pair
$(X, Y)$ is a tiling (or factorisation) of $G$ if every $g \in G$ can be written as $g = xy$
with $x \in X$ and $y \in Y$ for exactly one pair $(x, y)$.

Formalized by `MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.IsTiling`, a definition declared in [WantedExt/Combinatorics/FangXiaTilingWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FangXiaTilingWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html#is-tiling).

## The identity and the transpositions

$T_n$ is the set of permutations of
$\{0, \dots, n-1\}$ consisting of the identity and all transpositions $(i\ j)$ with $i \ne j$.

Formalized by `MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.transpositionsWithOne`, a definition declared in [WantedExt/Combinatorics/FangXiaTilingWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FangXiaTilingWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html#transpositions-with-one).

## Integer partition as a list of row lengths

A partition of $n$ is encoded as a list
$(\lambda_0, \lambda_1, \dots, \lambda_{k-1})$ of positive integers with
$\lambda_0 \ge \lambda_1 \ge \dots \ge \lambda_{k-1}$ and $\lambda_0 + \dots + \lambda_{k-1} = n$;
the $\lambda_i$ are its row lengths.

Formalized by `MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.PartitionShape`, a structure declared in [WantedExt/Combinatorics/FangXiaTilingWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FangXiaTilingWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html#partition-shape).

## Shifted row-length sum

For a natural number $i$ and a list of natural numbers
$a_0, \dots, a_{k-1}$, this is the integer $\sum_{j=0}^{k-1} a_j\,(a_j - 2(i + j) - 1)$; the
empty list gives $0$.

With $i = 0$ and the row lengths of a partition, this is twice the content sum of the partition.

Formalized by `MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.PartitionShape.contentSumAux`, a definition declared in [WantedExt/Combinatorics/FangXiaTilingWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FangXiaTilingWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html#content-sum-aux).

## Twice the content sum of a partition

For a partition $\lambda$ of $n$ with row lengths
$\lambda_0 \ge \lambda_1 \ge \dots \ge \lambda_{k-1}$, this is the integer
$\sum_{i=0}^{k-1} \lambda_i\,(\lambda_i - 2i - 1)$.

This is twice the content sum $\sum_{(i,j) \in \lambda} (j - i)$ of the Young diagram of
$\lambda$ (rows $i$ and columns $j$ counted from $0$), so it is nonnegative exactly when the
content sum is. It is the row-length formula from the remark after Theorem 1.4 of Fang–Xia,
whose one-indexed terms are $\lambda_i\,(\lambda_i - 2i + 1)$.

Formalized by `MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.PartitionShape.contentSum`, a definition declared in [WantedExt/Combinatorics/FangXiaTilingWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FangXiaTilingWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html#content-sum).

## Ordered set partition of shape λ

Let $\lambda$ be a partition of $n$ with row lengths
$\lambda_0 \ge \dots \ge \lambda_{k-1}$. An ordered set partition of $\{0, \dots, n-1\}$ of shape
$\lambda$ is a sequence $(B_0, \dots, B_{k-1})$ of pairwise disjoint subsets of
$\{0, \dots, n-1\}$ whose union is $\{0, \dots, n-1\}$ and with $|B_i| = \lambda_i$ for every
$i$.

Formalized by `MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.OrderedSetPartition`, a structure declared in [WantedExt/Combinatorics/FangXiaTilingWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FangXiaTilingWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html#ordered-set-partition).

## Permutation sending one ordered set partition to another

Let $\lambda$ be a partition
of $n$ and let $P = (P_0, \dots, P_{k-1})$ and $Q = (Q_0, \dots, Q_{k-1})$ be ordered set
partitions of $\{0, \dots, n-1\}$ of shape $\lambda$. A permutation $\sigma$ of
$\{0, \dots, n-1\}$ sends $P$ to $Q$ if $\sigma(P_i) = Q_i$ for every $i$.

Formalized by `MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.SendsPartition`, a definition declared in [WantedExt/Combinatorics/FangXiaTilingWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FangXiaTilingWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html#sends-partition).

## λ-transitive sets of permutations

Let $\lambda$ be a partition of $n$ with row lengths
$\lambda_0 \ge \dots \ge \lambda_{k-1}$. A set $Y$ of permutations of $\{0, \dots, n-1\}$ is
$\lambda$-transitive, in the sense of Martin and Sagan, if there is a positive integer $r$ such
that for any two ordered set partitions $P = (P_0, \dots, P_{k-1})$ and
$Q = (Q_0, \dots, Q_{k-1})$ of $\{0, \dots, n-1\}$ of shape $\lambda$, exactly $r$ permutations
$\sigma \in Y$ satisfy $\sigma(P_i) = Q_i$ for every $i$.

Formalized by `MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.IsPartitionTransitive`, a definition declared in [WantedExt/Combinatorics/FangXiaTilingWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FangXiaTilingWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html#is-partition-transitive).

## Fang–Xia: tilings by transpositions and λ-transitivity

Let $S_n$ be the symmetric group
on $\{0, \dots, n-1\}$, let $T_n \subseteq S_n$ consist of the identity and all transpositions,
and let $Y \subseteq S_n$ be such that $(T_n, Y)$ is a tiling of $S_n$: every $g \in S_n$ can be
written as $g = xy$ with $x \in T_n$ and $y \in Y$ for exactly one pair $(x, y)$. Let $\lambda$
be a partition of $n$ with row lengths $\lambda_0 \ge \dots \ge \lambda_{k-1}$ such that
$\sum_{i=0}^{k-1} \lambda_i\,(\lambda_i - 2i - 1) \ge 0$ (equivalently, the content sum of the
Young diagram of $\lambda$ is nonnegative). Then $Y$ is $\lambda$-transitive: there is a
positive integer $r$ such that for any two ordered set partitions $P = (P_0, \dots, P_{k-1})$
and $Q = (Q_0, \dots, Q_{k-1})$ of $\{0, \dots, n-1\}$ with $|P_i| = |Q_i| = \lambda_i$ for
every $i$, exactly $r$ permutations $\sigma \in Y$ satisfy $\sigma(P_i) = Q_i$ for every $i$.

## Sources

- T. Fang and B. Xia, 'Tiling the symmetric group by transpositions', Bull. London Math. Soc. 58(5) (2026); DOI 10.1112/blms.70366; arXiv:2506.00360. The λ-transitivity notion in the statement is due to Martin–Sagan. Problem `fang_xia_tiling_partition_transitive` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.FangXiaTilingWanted.Combinatorics.FangXiaTilingProblem.fang_xia_partition_transitive_of_tiling` is written with `theorem_wanted` in [WantedExt/Combinatorics/FangXiaTilingWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FangXiaTilingWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html#fang-xia-partition-transitive-of-tiling).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tilings of the symmetric group by transpositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/tilings-board-placements/tilings-of-the-symmetric-group-by-transpositions)
