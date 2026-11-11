---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.SamplePartition, MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.IsMerge, MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.jumpMatrix, MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.jumpLaw, MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.kingmanProb, MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.partitionRate, MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.timeLaw, MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.restrictMatrix
statement: formalized
---

# Partition-valued Kingman coalescent

36 results, 35 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html).

## Set partitions of a labeled sample

The set partitions of a sample of `n` labeled genes `{0, …, n - 1}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.SamplePartition`, an abbreviation declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#sample-partition).

## Partition obtained by merging two blocks

`π'` arises from `π` by merging two blocks: `π` refines `π'` and has exactly one more
block (so exactly two blocks of `π` lie in one block of `π'`, and the others are blocks of
`π'`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.IsMerge`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#is-merge).

## Jump chain of Kingman's coalescent

The transition matrix of the jump chain of Kingman's coalescent: from a partition with
`k ≥ 2` blocks, move to each of the `k.choose 2` partitions obtained by merging two blocks with
probability `1 / k.choose 2`; a partition with at most one block is absorbing.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.jumpMatrix`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#jump-matrix).

## Law of Kingman's jump chain after m jumps

The law of the jump chain after `m` jumps, started from the partition into singletons:
`jumpLaw n m π` is the probability that the partition after `m` coalescences is `π`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.jumpLaw`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#jump-law).

## Kingman's formula

The probability `(n - k)! k! (k - 1)! ∏_{B ∈ π} |B|! / (n! (n - 1)!)`
of a partition `π` with `k` blocks of a sample of size `n` (meaningful for `1 ≤ k ≤ n`; for
the empty sample it gives `1` to the empty partition).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.kingmanProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#kingman-prob).

## Rate matrix of Kingman's partition-valued coalescent

The rate matrix of Kingman's partition-valued coalescent: each pair of blocks merges at
rate `1`, so a partition with `k` blocks is left at total rate `k.choose 2` (time in units of
`2N` generations).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.partitionRate`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#partition-rate).

## Time-t marginal of Kingman's coalescent

The time-`t` marginal of Kingman's `n`-coalescent started from singletons:
`timeLaw n t π = exp (t • partitionRate n) ⊥ π` is the probability that the ancestral partition
of the sample at time `t ≥ 0` (in units of `2N` generations) is `π`. The matrix exponential is
defined for every real `t`; the identities below hold for every real `t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.timeLaw`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#time-law).

## Restriction matrix on sample partitions

The restriction map as a `0/1` matrix: entry `(π, ρ)` is `1` iff `π.comap Fin.castSucc = ρ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.restrictMatrix`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#restrict-matrix).

## Mergers

A partition with `k` blocks has exactly `k.choose 2` partitions that arise
from it by merging two blocks.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.card_isMerge`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#card-is-merge).

## Splitting identity

Summing `∏_{B ∈ π} |B|!` over the partitions `π` that merge to
`π'` gives `(n - #π'.parts) / 2 · ∏_{B ∈ π'} |B|!`: a block of size `b` has
`(2^b - 2) / 2` splits into two blocks, and `∑_{∅ ≠ A ⊊ B} |A|! |B \ A|! = (b - 1) b!`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.two_mul_sum_prod_factorial_isMerge`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 847](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L847). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#two-mul-sum-prod-factorial-is-merge).

## Kingman's formula at the partition into singletons

Kingman's formula gives probability `1` to the partition into singletons.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.kingmanProb_bot`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 994](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L994). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#kingman-prob-bot).

## Kingman's formula for a partition with k blocks

Kingman's formula for a partition with `k` blocks.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.kingmanProb_of_card`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1000](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1000). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#kingman-prob-of-card).

## Backward equation of Kingman's formula

For a partition `π'` with `k` blocks,
`1 ≤ k < n`, the Kingman probabilities of the partitions merging to `π'` sum to
`(k + 1).choose 2` times the Kingman probability of `π'`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.sum_kingmanProb_isMerge`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1012](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1012). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#sum-kingman-prob-is-merge).

## Kingman's jump-chain matrix is row-stochastic

The jump-chain transition matrix is row-stochastic.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.jumpMatrix_mem_rowStochastic`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1051](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1051). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#jump-matrix-mem-row-stochastic).

## Kingman's formula

**Kingman's formula** (Kingman 1982; Durrett 2008, ch. 1). For `m < n`, after `m`
coalescences the jump chain started from singletons is at a partition `π` with probability
`kingmanProb n π = (n - k)! k! (k - 1)! ∏_{B ∈ π} |B|! / (n! (n - 1)!)` if `π` has `k = n - m`
blocks, and `0` otherwise. (For `m ≥ n - 1` the chain has been absorbed at the one-block
partition.)

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.jumpLaw_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1069](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1069). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#jump-law-eq).

## Jump-chain law sums to one

The jump chain's law after `m` jumps sums to one (its entries are nonnegative by
`jumpMatrix_mem_rowStochastic`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.sum_jumpLaw`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#sum-jump-law).

## Kingman's formula is a probability distribution

**Kingman's formula is a probability distribution** on the partitions with `k` blocks, for
`1 ≤ k ≤ n`. Equivalently, `∑_{π, k blocks} ∏_{B ∈ π} |B|! = n! (n - 1)! / ((n - k)! k! (k - 1)!)`,
the Lah number `L(n, k)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.sum_kingmanProb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#sum-kingman-prob).

## Kingman's formula is invariant under relabeling

Relabeling the sample by a permutation (`Finpartition.comap`) preserves Kingman's
formula.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.kingmanProb_comap_perm`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#kingman-prob-comap-perm).

## Exchangeability

**Exchangeability** of the jump chain: for `m < n`, relabeling the sample does not change
the probability of a partition after `m` coalescences.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.jumpLaw_comap_perm`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#jump-law-comap-perm).

## Number of blocks of a sample partition

The number of blocks of a partition of a sample of `n`, as an element of `Fin (n + 1)` (a
state of the block-counting process).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.numBlocks`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#num-blocks).

## Kingman's formula arranged by number of blocks

Kingman's formula arranged by number of blocks: entry `(k, π)` is `kingmanProb n π` if `π`
has `k` blocks and `0` otherwise. For `1 ≤ k ≤ n`, row `k` is the law of the jump chain after
`n - k` jumps (`jumpLaw_eq`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.kingmanMatrix`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#kingman-matrix).

## Last row of Kingman's matrix is the singleton point mass

Row `n` of `kingmanMatrix n` is the point mass at the partition into singletons.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.kingmanMatrix_last`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#kingman-matrix-last).

## Kingman's formula intertwines the block-counting generator with the partition rate matrix

**Kingman's formula intertwines the block-counting generator with the partition rate
matrix**: `G * Λ = Λ * Q`. This is the backward equation `sum_kingmanProb_isMerge` in matrix
form.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.blockCountingGenerator_mul_kingmanMatrix`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#block-counting-generator-mul-kingman-mat).

## The time-`t` marginal of the partition-valued coalescent

**The time-`t` marginal of the partition-valued coalescent** (Kingman 1982): for
every real `t`, the probability of a partition `π` with `k` blocks is the probability that the
block-counting process goes from `n` to `k` lineages in time `t`, times Kingman's formula.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.timeLaw_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#time-law-eq).

## Time-t marginal via Tavaré's formula

The time-`t` marginal with Tavaré's closed form for the block-counting factor: for a
partition `π` of a sample of `n` (so `π` has at least one block when `n ≥ 1`),
`P(Π_t = π) = tavareProb n k t · kingmanProb n π` with `k = #π.parts`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.timeLaw_eq_tavareProb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#time-law-eq-tavare-prob).

## Exchangeability

**Exchangeability** of the time-`t` marginal.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.timeLaw_comap_perm`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#time-law-comap-perm).

## Rows of the partition rate matrix sum to zero

Each row of the partition rate matrix sums to `0`: a partition with `k` blocks has
`k.choose 2` mergers (`card_isMerge`), each at rate `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.sum_partitionRate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#sum-partition-rate).

## Partition rate matrix is a rate matrix

The partition rate matrix is a rate matrix: off-diagonal entries are `0` or `1`, and each
row sums to `0` (`sum_partitionRate`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.isRateMatrix_partitionRate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#is-rate-matrix-partition-rate).

## Time-t marginal as a continuous-time chain transition

`timeLaw` is a row of the transition function `P t = exp (t • partitionRate n)` of the
continuous-time chain with rate matrix `partitionRate n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.timeLaw_eq_ctmcTransition`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#time-law-eq-ctmc-transition).

## Partition coalescent transition matrix is row-stochastic

For `t ≥ 0` the transition matrix `exp (t • partitionRate n)` is row-stochastic.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.ctmcTransition_partitionRate_mem_rowStochastic`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#ctmc-transition-partition-rate-mem-row-s).

## Nonnegativity of the time-t marginal

For `t ≥ 0` the time-`t` marginal is nonnegative; with `sum_timeLaw` it is a probability
distribution on the partitions of the sample.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.timeLaw_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#time-law-nonneg).

## Time-t marginal sums to one

The time-`t` marginal sums to one over all partitions: `∑_π timeLaw n t π = 1` (for every
real `t`, since the rows of the rate matrix sum to `0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.sum_timeLaw`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#sum-time-law).

## Lumpability of restriction

**Lumpability of restriction** (Kingman 1982): restricting to the first `n` genes
intertwines the rate matrices of the `(n + 1)`- and `n`-coalescents.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.partitionRate_mul_restrictMatrix`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#partition-rate-mul-restrict-matrix).

## Consistency

**Consistency** (Kingman 1982): the time-`t` law of the restriction of the
`(n + 1)`-coalescent to the first `n` genes is the time-`t` law of the `n`-coalescent.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescent.sum_timeLaw_restrict`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean, line 1396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescent.lean#L1396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#sum-time-law-restrict).

## Path probability of the Kingman coalescent jump chain

The probability that the jump chain of Kingman's `n`-coalescent, started from the partition
into singletons, follows the list of partitions `l`: `0` unless `l` starts at the partition
into singletons, and otherwise the product of the one-step transition probabilities
`jumpMatrix n` along `l`. The empty list has probability `0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescentWanted.pathProb`, a definition declared in [WantedExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescentWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescentWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#path-prob).

## Consistency of the jump chains

**Consistency of the jump chains** (Kingman 1982): for `n ≥ 1`, restricting each
partition of a path of the `(n + 1)`-jump chain (a list of `n + 1` partitions) to the first `n`
genes and deleting consecutive repetitions gives a list of `n` partitions of `Fin n` distributed
as the path of the `n`-jump chain.

## Sources

- Kingman (1982); Durrett (2008), ch. 1.

Stated but not proved: `MathlibExt.Biology.PopulationGenetics.Coalescent.PartitionCoalescentWanted.sum_pathProb_restrict` is written with `theorem_wanted` in [WantedExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescentWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Biology/PopulationGenetics/Coalescent/PartitionCoalescentWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html#sum-path-prob-restrict).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition-valued Kingman coalescent](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/partition-valued-kingman-coalescent)
