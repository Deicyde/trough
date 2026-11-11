---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree, MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree.NonnegLengths, MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree.taxa, MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree.clusters, MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree.shape, MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.sum_tavareProb, MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tavareProb_nonneg, MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.mergeAlong
statement: formalized
proof: formalized
---

# Multispecies coalescent

76 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html).

## Species trees

## Rooted binary species tree with branch lengths

A rooted binary **species tree** on the species `Fin n` with branch lengths: `leaf i` is
species `i`, and `node l r t` is the ancestral species of the species below `l` and `r`, where
`t` is the length, in coalescent units (`2N` generations), of the branch above the node, i.e.
the time during which the ancestral population of `l` and `r` exists before it merges with a
sister population. The length stored at the root node is not used: the root population lasts
until all lineages have coalesced. Leaf branch lengths are not recorded, because one gene
lineage is sampled per species and a single lineage cannot coalesce. A species tree on the
species `Fin n` labels each species by exactly one leaf; the type does not enforce this, and
the theorems below are about concrete trees with this property. The type accepts any real
branch length; the probabilistic statements assume nonnegative lengths (`NonnegLengths`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree`, an inductive type declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#species-tree).

## Species tree with nonnegative branch lengths

Every branch length of the species tree, including the unused one stored at the root, is
nonnegative. On such trees `geneTreeProb` is a probability law; for a negative length it is
only a signed weight.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree.NonnegLengths`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#nonneg-lengths).

## Species below a node of a species tree

The species below a node.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree.taxa`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#taxa).

## Clusters of a species tree

The clusters (clades) of a species tree: the sets of species below its vertices, including
the singletons and the full set of species.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree.clusters`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#clusters).

## Topology of a species tree

The topology of a species tree, forgetting branch lengths, as a planar rooted binary tree.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.SpeciesTree.shape`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#shape).

## Tavaré's probabilities sum to one

From `m ≥ 1` lineages, the number of ancestors at
time `t` is one of `1, …, m`. (The rows of `exp (t • G)` restricted to the states `≥ 1` sum to
one because `G` kills the indicator of `{1, …, n}`; an identity for every real `t`.)

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.sum_tavareProb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#sum-tavare-prob).

## Tavaré's probabilities are nonnegative

**Tavaré's probabilities are nonnegative** for `t ≥ 0`: `exp (t • G)` is the entrywise limit
of powers of the Wright–Fisher transition matrix (`tendsto_wfLineageMatrix_pow_floor`), whose
entries are nonnegative. (For `t < 0` they can be negative or exceed one.)

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tavareProb_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#tavare-prob-nonneg).

## Lineages after the first coalescence events of a ranked history

The lineages after the first `t` coalescence events of the ranked history `h` (of `m`
lineages), starting from the lineages `bs`, each given as the set of sampled genes it is
ancestral to. Events follow the encoding of `RankedHistory`: the pair `{a, b}` with `a < b`
merges into position `a`, and position `b` is removed (`mergeBlocks`). With the singletons as
starting lineages this is `blocksAfter` (`mergeAlong_singletons`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.mergeAlong`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#merge-along).

## Merging lineages from singletons gives the ancestral blocks

Starting from the singletons, `mergeAlong` is `blocksAfter`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.mergeAlong_singletons`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#merge-along-singletons).

## Clusters formed along a ranked history

The clusters formed during the first `t` coalescence events of `h` from the lineages `bs`:
every lineage present at some step `u ≤ t`, as the set of sampled genes it is ancestral to.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.cladesAlong`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#clades-along).

## Coalescence along one branch of the species tree

One population of the multispecies coalescent along a branch of length `t`. It receives
`m` lineages `bs` (and the clusters `acc` formed below it). Under Kingman's coalescent the
number `j` of lineages left at the top of the branch has law `tavareProb m j t` (Tavaré's
formula, `exp_blockCountingGenerator_apply`), and, independently of the coalescence times, the
order of the `m - j` coalescences is the beginning of a random-joining history of the `m`
lineages (`randomJoining`). The continuation `k` receives the number of exiting lineages, the
lineages, and the clusters formed so far.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.branchStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#branch-step).

## Law of the lineages leaving a species-tree branch

The law of the lineages leaving the top of the branch above a vertex of the species tree,
in continuation-passing form: `exitLaw T k` is the expectation of `k m bs acc`, where `m` is
the number of exiting lineages, `bs` the lineages and `acc` the clusters formed below. The two
daughter populations evolve independently, and their lineages enter the ancestral population
together.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.exitLaw`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#exit-law).

## The multispecies coalescent

**The multispecies coalescent** (Pamilo & Nei 1988; Degnan & Salter 2005), one lineage
sampled per species: the probability that the gene tree, given by its set of clusters, lies in
the event `E`. Below the root, each branch population runs Kingman's coalescent for the
branch length (`branchStep`); in the root population all remaining lineages coalesce by
random joining. The definition accepts any real branch lengths; it is a probability law on
species trees with nonnegative branch lengths (`geneTreeProb_nonneg`, `geneTreeProb_or`,
`geneTreeProb_true`), and only a signed weight otherwise (with internal branch `-1`, the
matching three-species gene tree gets `1 - (2/3) e < 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob).

## Root branch length does not affect gene-tree probabilities

The branch length stored at the root of a species tree does not affect the gene tree.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_node_length`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-node-length).

## Exit law of a constant continuation

If a continuation takes the constant value `c` whenever at least one lineage exits, then
so does `exitLaw` (Tavaré's probabilities sum to one and random joining is a probability).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.exitLaw_eq_const`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#exit-law-eq-const).

## Normalization

For every species tree, the event "any gene tree" has weight one (an
identity for every real branch length). With `geneTreeProb_nonneg` and `geneTreeProb_or` this
makes `geneTreeProb T` a probability law when `T.NonnegLengths`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_true`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-true).

## Total gene-tree probability is one

An event containing every gene tree has weight one, for every species tree.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_eq_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-eq-one).

## Nonnegativity of the exit law

On a species tree with nonnegative branch lengths, `exitLaw` of a continuation that is
nonnegative whenever at least one lineage exits is nonnegative (Tavaré's probabilities are
nonnegative, `tavareProb_nonneg`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.exitLaw_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#exit-law-nonneg).

## Gene-tree probabilities are nonnegative

**Gene-tree probabilities are nonnegative** on species trees with nonnegative branch
lengths. (For a negative branch length they need not be.)

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-nonneg).

## Expectation under random joining as an average over histories

An expectation under random joining is the average over the `∏_{k=2}^m C(k, 2)` ranked
histories.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.integral_randomJoining`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#integral-random-joining).

## Rational-valued expectation under random joining

`integral_randomJoining` for a rational-valued function, with a rational result (used to
evaluate random-joining probabilities by computation).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.integral_randomJoining_ratCast`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#integral-random-joining-rat-cast).

## Random-joining probability as a fraction of ranked histories

The probability of an event under random joining is the fraction of ranked histories in it.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.randomJoining_real`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#random-joining-real).

## Additivity of the exit law

`exitLaw` is additive in the continuation.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.exitLaw_add`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#exit-law-add).

## Additivity

The probabilities of two disjoint events of gene trees add up. With
`geneTreeProb_nonneg` and `geneTreeProb_true`, `geneTreeProb T` is a probability law when
`T.NonnegLengths`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_or`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-or).

## Gene-tree probabilities are at most one

On a species tree with nonnegative branch lengths, every gene-tree probability is at most
one.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_le_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-le-one).

## Two lineages remain distinct with probability $e^{-t}$

Two lineages are still distinct after time `t` with probability `e^{-t}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tavareProb_two_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#tavare-prob-two-two).

## Two lineages coalesce with probability $1 - e^{-t}$

Two lineages have coalesced within time `t` with probability `1 - e^{-t}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tavareProb_two_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#tavare-prob-two-one).

## Three lineages remain distinct with probability $e^{-3t}$

Three lineages are still distinct after time `t` with probability `e^{-3t}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tavareProb_three_three`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#tavare-prob-three-three).

## Three lineages have two ancestors at time $t$

Three lineages have two ancestors at time `t` with probability `(3/2)(e^{-t} - e^{-3t})`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tavareProb_three_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#tavare-prob-three-two).

## Three lineages have one ancestor at time $t$

Three lineages have one ancestor at time `t` with probability
`1 - (3/2) e^{-t} + (1/2) e^{-3t}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tavareProb_three_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#tavare-prob-three-one).

## Three-species tree ((0, 1), 2)

The three-species tree `((0, 1), 2)` with internal branch length `t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.triple`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#triple).

## Three-gene tree with a given cherry

The gene tree on three genes with cherry `c` (a pair of genes), as a set of clusters.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tripleTree`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 554](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L554). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#triple-tree).

## Clusters of the three-species tree

The species tree `((0, 1), 2)` has the clusters of the gene tree with cherry `{0, 1}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.clusters_triple`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#clusters-triple).

## Three-species concordance

**Three-species concordance** (Hudson 1983; Pamilo & Nei 1988): with one lineage per
species and internal branch length `t`, the gene tree matches the species tree with
probability `1 - (2/3) e^{-t}`. (An identity for every real `t`; branch lengths are `t ≥ 0`.)

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_triple_matching`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 564](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L564). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-triple-matching).

## Probability of the discordant three-species gene tree with cherry \{0, 2}

Each discordant three-species gene tree has probability `(1/3) e^{-t}`: cherry `{0, 2}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_triple_cherry_02`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 578](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L578). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-triple-cherry-02).

## Probability of the discordant three-species gene tree with cherry \{1, 2}

Each discordant three-species gene tree has probability `(1/3) e^{-t}`: cherry `{1, 2}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_triple_cherry_12`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-triple-cherry-12).

## No anomalous gene trees for three species

**No anomalous gene trees for three species** (Degnan & Rosenberg 2006): for a positive
internal branch, each discordant gene tree is strictly less probable than the matching one.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.triple_no_anomaly`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#triple-no-anomaly).

## Wright–Fisher limit of the no-coalescence probability

The three-species probabilities come from the Wright–Fisher model: in a population of `M`
gene copies, the lineages of species `0` and `1` have distinct parents in each of the
`⌊t M⌋` generations of the internal branch (`t ≥ 0` coalescent units) with probability
`noCoalProb M 2 ^ ⌊t M⌋`, which tends to `tavareProb 2 2 t = e^{-t}`, the weight of the case
in which three lineages reach the root population.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tendsto_noCoalProb_pow_floor_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#tendsto-no-coal-prob-pow-floor-two).

## Caterpillar four-species tree

The asymmetric (caterpillar) species tree `(((0, 1), 2), 3)`: `x` is the length of the
deeper internal branch (above the ancestor of `0, 1, 2`) and `y` that of the shallower one
(above the ancestor of `0, 1`), as in Degnan & Rosenberg (2006).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.caterpillar`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#caterpillar).

## Balanced four-species tree

The symmetric (balanced) species tree `((0, 1), (2, 3))` with internal branch lengths `y₁`
(above the ancestor of `0, 1`) and `y₂` (above the ancestor of `2, 3`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.balanced`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#balanced).

## Caterpillar four-gene tree

The asymmetric gene tree `(((a, b), c), d)` on four genes, as a set of clusters.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.caterpillarTree`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#caterpillar-tree).

## Balanced four-gene tree

The symmetric gene tree `((a, b), (c, d))` on four genes, as a set of clusters.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.balancedTree`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 645](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L645). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#balanced-tree).

## Clusters of the caterpillar species tree

The species tree `(((0, 1), 2), 3)` has the clusters of the gene tree `(((0, 1), 2), 3)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.clusters_caterpillar`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#clusters-caterpillar).

## Degnan–Rosenberg probability of the matching caterpillar gene tree

Degnan & Rosenberg (2006), eq. (1): `f(x, y)`, the probability of the matching gene tree
`(((A, B), C), D)` on the caterpillar species tree.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.drF`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#dr-f).

## Degnan–Rosenberg formula g for the gene tree ((A, C), (B, D))

Degnan & Rosenberg (2006), eq. (2): `g(x, y)`, the probability of the gene tree
`((A, C), (B, D))` (and of `((A, D), (B, C))`) on the caterpillar species tree.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.drG`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#dr-g).

## Degnan–Rosenberg formula h for the gene tree ((A, B), (C, D))

Degnan & Rosenberg (2006), eq. (3): `h(x, y)`, the probability of the gene tree
`((A, B), (C, D))` on the caterpillar species tree.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.drH`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 665](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L665). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#dr-h).

## The matching gene tree

**The matching gene tree** on the caterpillar species tree has probability `f(x, y)`
(Degnan & Rosenberg 2006, eq. (1)). An identity for all real `x, y`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_caterpillar_matching`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-caterpillar-matching).

## Probability of the gene tree ((A, C), (B, D)) on the caterpillar

The symmetric gene tree `((A, C), (B, D))` on the caterpillar species tree has probability
`g(x, y)` (Degnan & Rosenberg 2006, eq. (2)).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_caterpillar_AC_BD`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 701](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-caterpillar-ac-bd).

## Probability of the gene tree ((A, D), (B, C)) on the caterpillar

The symmetric gene tree `((A, D), (B, C))` on the caterpillar species tree has probability
`g(x, y)`, the same as `((A, C), (B, D))` (Degnan & Rosenberg 2006).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_caterpillar_AD_BC`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 715](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L715). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-caterpillar-ad-bc).

## Probability of the gene tree ((A, B), (C, D)) on the caterpillar

The symmetric gene tree `((A, B), (C, D))` on the caterpillar species tree has probability
`h(x, y)` (Degnan & Rosenberg 2006, eq. (3)).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_caterpillar_AB_CD`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 729](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L729). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-caterpillar-ab-cd).

## Boundary of the four-species anomaly zone

Degnan & Rosenberg (2006), eq. (4): the boundary `a(x)` of the four-species anomaly zone,
for a deeper internal branch of length `x > 0` (at `x = 0` the denominator vanishes and Lean's
`a / 0 = 0` gives the junk value `log (2/3 - 0)`; `a(x) → ∞` as `x → 0⁺`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.anomalyA`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#anomaly-a).

## Boundary for three anomalous gene trees

Degnan & Rosenberg (2006), eq. (5): the boundary `b(x)` below which the caterpillar species
tree has three anomalous gene trees (defined for `x ≥ 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.anomalyB`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 749](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L749). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#anomaly-b).

## $g(x, y) < h(x, y)$ for a positive shallower branch

For a positive shallower branch, the symmetric gene tree `((A, B), (C, D))` is strictly more
probable than `((A, C), (B, D))`: `g(x, y) < h(x, y)` (Degnan & Rosenberg 2006).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.drG_lt_drH`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#dr-g-lt-dr-h).

## The boundary `a(x)` of the anomaly zone

**The boundary `a(x)` of the anomaly zone** (Degnan & Rosenberg 2006): for a deeper
internal branch `x > 0`, the symmetric gene tree `((A, B), (C, D))` is more probable than the
matching gene tree, `f(x, y) < h(x, y)`, if and only if `y < a(x)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.drF_lt_drH_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 767](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L767). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#dr-f-lt-dr-h-iff).

## Degnan–Rosenberg criterion: $f(x, y) < g(x, y)$ iff $y < b(x)$

Degnan & Rosenberg (2006): for `x ≥ 0`, the gene tree `((A, C), (B, D))` (equivalently
`((A, D), (B, C))`) is more probable than the matching gene tree, `f(x, y) < g(x, y)`, if and
only if `y < b(x)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.drF_lt_drG_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 804](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L804). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#dr-f-lt-dr-g-iff).

## Value $\log(7/6)$ of the three-anomaly boundary at zero

`b(0) = log (7/6)` (Degnan & Rosenberg 2006): if `y ≥ log (7/6)`, then `y ≥ b(x)` for every
`x ≥ 0` (`anomalyB_le_anomalyB_zero`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.anomalyB_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 838](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L838). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#anomaly-b-zero).

## Three-anomaly boundary is maximal at zero

`b` is maximal at `0`: `b(x) ≤ log (7/6)` for `x ≥ 0`, so for `y ≥ log (7/6)` at most one
gene tree is anomalous.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.anomalyB_le_anomalyB_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 844](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L844). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#anomaly-b-le-anomaly-b-zero).

## Anomaly-zone boundary blows up for short deep branches

`a(x) → ∞` as `x → 0⁺` (Degnan & Rosenberg 2006): very short deep branches produce an
anomalous gene tree however long the shallower branch is.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.tendsto_anomalyA`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 861](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L861). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#tendsto-anomaly-a).

## Anomalous gene tree on four species

**Anomalous gene tree on four species** (Degnan & Rosenberg 2006): on the caterpillar
species tree with deeper branch `x > 0` and shallower branch `y`, the symmetric gene tree
`((A, B), (C, D))` is more probable than the gene tree matching the species tree if and only
if `y < a(x)`. With `caterpillar_le_matching` this gives `caterpillar_exists_anomalous_iff`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.caterpillar_anomalous_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 887](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L887). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#caterpillar-anomalous-iff).

## Anomaly of ((A, C), (B, D)) and ((A, D), (B, C)) on the caterpillar

On the caterpillar species tree with `x ≥ 0`, the gene trees `((A, C), (B, D))` and
`((A, D), (B, C))` are more probable than the matching gene tree if and only if `y < b(x)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.caterpillar_anomalous_AC_BD_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 895](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L895). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#caterpillar-anomalous-ac-bd-iff).

## Balanced gene tree on four genes

`G` is one of the three balanced (symmetric) gene trees on four genes.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.IsBalancedGeneTree`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 902](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L902). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#is-balanced-gene-tree).

## Only balanced gene trees can be anomalous on the caterpillar

On the caterpillar species tree with nonnegative branch lengths, no asymmetric gene tree is
more probable than the matching one (Degnan & Rosenberg 2006): only the three balanced gene
trees can be anomalous.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.caterpillar_le_matching`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 910](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L910). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#caterpillar-le-matching).

## $g(x, y) \le h(x, y)$ for a nonnegative shallower branch

`g(x, y) ≤ h(x, y)` for a nonnegative shallower branch (equality at `y = 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.drG_le_drH`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 928](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L928). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#dr-g-le-dr-h).

## The four-species anomaly zone

**The four-species anomaly zone** (Degnan & Rosenberg 2006, Definition 1 and Figure 2): the
caterpillar species tree with deeper branch `x > 0` and shallower branch `y ≥ 0` has an
anomalous gene tree, one strictly more probable than the gene tree matching the species
tree, if and only if `y < a(x)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.caterpillar_exists_anomalous_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 941](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L941). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#caterpillar-exists-anomalous-iff).

## No anomalous gene trees on the balanced four-species tree

**No anomalous gene trees on the balanced four-species tree** (Degnan & Rosenberg 2006):
for nonnegative branch lengths, no gene tree is more probable than the one matching the
species tree `((0, 1), (2, 3))`. Given the numbers of lineages entering the root population,
the matching tree is already the most probable outcome of random joining.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.balanced_no_anomaly`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 962](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L962). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#balanced-no-anomaly).

## Gene tree displaying a quartet split

A rooted gene tree on four genes `G` (a set of clusters) **displays the quartet split**
`ab | cd`, where `{c, d}` is the complement of `{a, b}`: forgetting the root, the internal edge
separates `{a, b}` from `{c, d}`; equivalently `{a, b}` or `{c, d}` is a cluster.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.DisplaysSplit`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 984](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L984). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#displays-split).

## No anomalous unrooted quartets, caterpillar species tree

**No anomalous unrooted quartets, caterpillar species tree** (Allman, Degnan & Rhodes 2011):
the unrooted gene quartet matches the species quartet `01 | 23` with probability
`1 - (2/3) e^{-y}`, where `y` is the length of the internal edge of the unrooted species
quartet (the shallower internal branch).

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_caterpillar_split_01`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 994](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L994). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-caterpillar-split-01).

## Probability of quartet split 02|13 on the caterpillar tree

On the caterpillar species tree the discordant unrooted gene quartet `02 | 13` has
probability `(1/3) e^{-y}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_caterpillar_split_02`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 1008](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L1008). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-caterpillar-split-02).

## Probability of quartet split 03|12 on the caterpillar tree

On the caterpillar species tree the discordant unrooted gene quartet `03 | 12` has
probability `(1/3) e^{-y}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_caterpillar_split_03`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 1022](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L1022). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-caterpillar-split-03).

## No anomalous unrooted quartets, balanced species tree

**No anomalous unrooted quartets, balanced species tree** (Allman, Degnan & Rhodes 2011):
on `((0, 1), (2, 3))` the unrooted gene quartet matches `01 | 23` with probability
`1 - (2/3) e^{-(y₁ + y₂)}`, where `y₁ + y₂` is the internal edge of the unrooted species
quartet.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_balanced_split_01`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 1053](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L1053). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-balanced-split-01).

## Probability of quartet split 02|13 on the balanced tree

On the balanced species tree the discordant unrooted gene quartet `02 | 13` has
probability `(1/3) e^{-(y₁ + y₂)}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_balanced_split_02`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 1066](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L1066). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-balanced-split-02).

## Probability of quartet split 03|12 on the balanced tree

On the balanced species tree the discordant unrooted gene quartet `03 | 12` has
probability `(1/3) e^{-(y₁ + y₂)}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.geneTreeProb_balanced_split_03`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 1079](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L1079). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#gene-tree-prob-balanced-split-03).

## The species quartet maximizes quartet support

**The species quartet maximizes quartet support** (Allman, Degnan & Rhodes 2011; Mirarab
et al. 2014): for a positive internal edge, the unrooted gene quartet matching the species
quartet is strictly the most probable of the three, on both four-species shapes. Since the
expected quartet support of a candidate four-species tree (one quartet) is the probability
of its quartet, the species tree maximizes it.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.split_01_most_probable`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 1095](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L1095). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#split-01-most-probable).

## Clade of a ranked history

The set `S` of sampled genes is a **clade** of the ranked history `h`: it is a block of one
of the ancestral partitions of `h`, i.e. the set of descendants of some lineage.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.IsClade`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 1116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L1116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#is-clade).

## Clade probability

**Clade probability** (Rosenberg 2003): under random joining, a fixed set of `k` among `m`
genes, `1 ≤ k < m`, is a clade with probability `2m / (k (k + 1) C(m, k))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.randomJoining_isClade`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 1703](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L1703). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#random-joining-is-clade).

## Clade probability under random joining for at most five genes

The case `m ≤ 5` of `randomJoining_isClade`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MultispeciesCoalescent.randomJoining_isClade_of_le_five`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean, line 1751](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/MultispeciesCoalescent.lean#L1751). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html#random-joining-is-clade-of-le-five).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multispecies coalescent](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/multispecies-coalescent/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/multispecies-coalescent)
