---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.LineagePair, MathlibExt.Biology.PopulationGenetics.Coalescent.RankedHistory, MathlibExt.Biology.PopulationGenetics.Coalescent.card_lineagePair, MathlibExt.Biology.PopulationGenetics.Coalescent.mergeBlocks, MathlibExt.Biology.PopulationGenetics.Coalescent.blocksAfter, MathlibExt.Biology.PopulationGenetics.Coalescent.blocksOf, MathlibExt.Biology.PopulationGenetics.Coalescent.partitionsOf, MathlibExt.Biology.PopulationGenetics.Coalescent.prod_choose_two_mul_two_pow
statement: formalized
proof: formalized
---

# Ranked labeled histories of coalescent trees

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html).

## Unordered pairs of lineages

The unordered pairs of lineages when there are `k` lineages labeled `0, …, k - 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LineagePair`, an abbreviation declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#lineage-pair).

## Ranked labeled history

A **ranked labeled history** of `n` labeled genes, encoded by its coalescence events: at
step `i < n - 1` there are `n - i` lineages and the step records the pair that merges (the
merged lineage takes the smaller label; the others keep their relative order).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.RankedHistory`, an abbreviation declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#ranked-history).

## Number of pairs of lineages

The number of pairs of `k` lineages is `k.choose 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.card_lineagePair`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#card-lineage-pair).

## Merging two lineage blocks

Merge the lineages (blocks of sampled genes) at positions `a < b` of a list of blocks: the
merged block replaces position `a`, and position `b` is removed.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.mergeBlocks`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#merge-blocks).

## Lineage blocks after the first coalescence events

The lineages (as blocks of sampled genes, indexed by lineage label) after the first `t`
coalescence events of a history, starting from the singletons `{0}, …, {n - 1}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.blocksAfter`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#blocks-after).

## Ancestral partitions along a history, indexed by lineage label

The ancestral partitions of the sample along a history, as lists of blocks indexed by
lineage label; entry `t` (for `t < n`) is the partition after `t` coalescence events.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.blocksOf`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#blocks-of).

## Ancestral partitions along a history as sets of blocks

The ancestral partitions of the sample along a history, as sets of blocks (forgetting the
lineage labels): the ranked labeled history in the sense of Edwards (1970).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.partitionsOf`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#partitions-of).

## Product of pair counts times a power of two is $n!(n-1)!$

`∏_{k=2}^n C(k, 2) * 2^{n-1} = n! (n - 1)!`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.prod_choose_two_mul_two_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#prod-choose-two-mul-two-pow).

## Reindexing the product of pair counts

Reindexing: `∏_{i < n - 1} C(n - i, 2) = ∏_{k=2}^n C(k, 2)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.prod_fin_choose_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#prod-fin-choose-two).

## Number of ranked labeled histories

`∏_{k=2}^n C(k, 2)` (Edwards 1970).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.card_rankedHistory`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#card-ranked-history).

## Number of ranked labeled histories

`#histories * 2^{n-1} = n! (n - 1)!`, i.e. there are
`n! (n - 1)! / 2^{n-1}` ranked labeled histories of `n` labeled genes (Edwards 1970).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.card_rankedHistory_mul_two_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#card-ranked-history-mul-two-pow).

## Random joining

**Random joining** (Edwards 1970; Kingman 1982): the pair merging at each step is uniform
among the current `(n - i).choose 2` pairs and independent of the earlier steps. Kingman (1982)
shows that this is the law of the tree topology of the coalescent.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.randomJoining`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#random-joining).

## Every ranked history is equally likely under random joining

Under random joining each history has probability `∏_{k=2}^n C(k, 2)⁻¹`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.randomJoining_singleton_eq_inv`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#random-joining-singleton-eq-inv).

## Each ranked labeled history has probability `2^{n-1} / (n! (n - 1)!)`

**Each ranked labeled history has probability `2^{n-1} / (n! (n - 1)!)`** under random
joining (Edwards 1970; Tajima 1983).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.randomJoining_singleton`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Topology.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html#random-joining-singleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ranked labeled histories of coalescent trees](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/ranked-labeled-histories-of-coalescent-trees)
