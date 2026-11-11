---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Phylogenetics.NeighborJoining.initialDist, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.qCriterion, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.joinDist, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.NJRun, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.IsBinaryPhylogeneticTree, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.side, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.splitGain, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.side_swap
statement: formalized
proof: formalized
---

# Neighbor joining

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html).

## The algorithm

## Initial cluster dissimilarity in neighbor joining

The dissimilarity between clusters at the start of neighbor joining: on singletons,
`initialDist d {x} {y} = d x y` (only singleton values are used).

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.initialDist`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#initial-dist).

## Neighbor-joining Q-criterion

The Studier–Keppler form of the neighbor-joining criterion on the cluster set `S`:
`Q(a, b) = (|S| - 2) D a b - ∑_{c ∈ S} D a c - ∑_{c ∈ S} D b c`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.qCriterion`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#q-criterion).

## Cluster dissimilarity after a neighbor-joining step

The cluster dissimilarity after joining `a` and `b`: the new cluster `a ∪ b` is at
`(D a c + D b c - D a b) / 2` from every other cluster `c`, and at `0` from itself; other
values are unchanged.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.joinDist`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#join-dist).

## Runs of neighbor joining

`NJRun d S D C`: some run of neighbor joining on the dissimilarity `d` reaches the cluster
set `S` with cluster dissimilarity `D`, having formed the clusters in `C`. A join is allowed
while at least four clusters remain, for any pair of distinct clusters minimizing
`qCriterion`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.NJRun`, an inductive type declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#njrun).

## Binary phylogenetic tree

`G` with the taxon placement `ι` is a **binary phylogenetic `X`-tree**: `G` is a tree,
`ι` is injective, the leaves (degree-one vertices) are exactly the taxa, and every other
vertex has degree three.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.IsBinaryPhylogeneticTree`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#is-binary-phylogenetic-tree).

## Taxa on one side of a tree edge

The taxa on the `a`-side of the edge `{a, b}`: those whose vertex is still joined to `a`
once the edge `{a, b}` is deleted.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.side`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#side).

## Contribution of a split to the neighbor-joining score

The contribution of one split `{A, Aᶜ}` to the neighbor-joining score of the pair `x, y`:
the number of taxa on the far side of the split when `x, y` lie on the same side, and `1`
when the split separates them.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.splitGain`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#split-gain).

## Two sides of a tree edge partition the taxa

In a tree, the two sides of an edge partition the taxa.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.side_swap`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#side-swap).

## Splits of two tree edges are compatible

In a tree, the splits of any two edges are compatible: one side of the first edge lies
inside one side of the second.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.side_compat`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#side-compat).

## Leaf side of a pendant edge

The leaf side of a pendant edge holds only the leaf's taxon.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.side_leaf`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#side-leaf).

## Every edge side of a binary phylogenetic tree is nonempty

Every side of every edge of a binary phylogenetic tree holds a taxon.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.side_nonempty`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#side-nonempty).

## Edge side at an internal vertex as a disjoint union

At an internal vertex `a` with neighbor `b`, the `a`-side of `{a, b}` is the disjoint union
of the far sides of the other two edges at `a`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.side_eq_union`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#side-eq-union).

## Split decomposition of a tree metric

The path length between two taxa is half the sum,
over the darts (oriented edges) of the tree, of the lengths of the edges whose split separates
them.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.dist_eq_sum_darts`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#dist-eq-sum-darts).

## Cherry lemma for split systems

For a compatible system of splits with positive weights,
containing every trivial split and binary (every side with at least two taxa is the disjoint
union of two sides), on at least four taxa, a pair maximizing the total `splitGain` is a
side of some split.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.exists_eq_pair_of_isMax`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 611](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L611). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#exists-eq-pair-of-is-max).

## Q-criterion of two singleton clusters

The Q-criterion of two singleton clusters at the start of neighbor joining:
`Q({x}, {y}) = (|X| - 2) d x y - ∑_z d x z - ∑_z d y z`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.qCriterion_singleton`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 788](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L788). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#q-criterion-singleton).

## The Q-criterion of a split-decomposed dissimilarity

If `d x y` is half the total
weight of the splits `A e` separating `x` and `y`, then
`(|X| - 2) d x y - ∑_z d x z - ∑_z d y z = -∑ e, w e * splitGain (A e) x y`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.sub_sum_sub_sum_eq_neg_sum_splitGain`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 821](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L821). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#sub-sum-sub-sum-eq-neg-sum-split-gain).

## A singleton side is a pendant leaf side

A side holding a single taxon `z` is the leaf side of `z`'s pendant edge.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.eq_of_side_eq_singleton`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 1630](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L1630). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#eq-of-side-eq-singleton).

## A two-taxon side forms a cherry

If a side of the edge `{a, b}` is the pair `{x, y}`, then `a` is a common neighbor of the
leaves `ι x` and `ι y`: they form a cherry.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.adj_adj_of_side_eq_pair`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 1648](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L1648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#adj-adj-of-side-eq-pair).

## On a tree metric, a pair of taxa minimizing the Q-criterion is a cherry

(Saitou & Nei 1987; Studier & Keppler 1988; Bryant 2005). Let `d` be the path-length metric
of a binary phylogenetic `X`-tree `(G, ι)` with positive edge lengths `w` and at least four
taxa. If the distinct taxa `x, y` minimize the Q-criterion over all pairs of distinct
singleton clusters at the start of neighbor joining, then `ι x` and `ι y` have a common
neighbor.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.exists_adj_adj_of_qCriterion_min`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 1730](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L1730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#exists-adj-adj-of-q-criterion-min).

## The first join of neighbor joining on a tree metric joins a cherry

On the path-length
metric of a binary phylogenetic `X`-tree with positive edge lengths and at least four taxa,
any pair of clusters that neighbor joining may join from the initial singletons consists of
two taxa with a common neighbor.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.NJRun.exists_adj_adj_of_join_init`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 1762](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L1762). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#exists-adj-adj-of-join-init).

## The path metric on a partition into sides

Let `S` partition the taxa of a binary
phylogenetic `X`-tree `(G, ι)` with positive edge lengths `w` and path-length metric `d` into
sides of edges. Then there is a system of splits `A e` (`e : E`) of the set of clusters with
positive weights `w' e`, closed under complement, pairwise compatible, binary, and containing
every trivial split, such that
* the weight of every internal split (both sides with at least two clusters) is the length of an
  edge with both endpoints internal;
* a split whose side is `{s, t}` comes from an edge with side `s ∪ t`;
* for taxa `x ∈ s` and `y ∈ t` of distinct clusters, `d x y` is half the total weight of the
  splits separating `s` from `t`, plus a term `ρ s x` depending only on `s` and `x` and a term
  `ρ t y`.
In the construction, the splits are those of the edges that cut no cluster.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.exists_splitSystem_of_partition`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 1854](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L1854). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#exists-split-system-of-partition).

## Neighbor joining is exact on tree metrics

Let `d` be the path-length metric of a
binary phylogenetic `X`-tree `(G, ι)` with positive edge lengths `w`. Then every complete run
of neighbor joining (stopped with at most three clusters) forms exactly the splits of the
internal edges of the tree: a set of taxa `A` or its complement is a formed cluster if and
only if `A` is the set of taxa on the `a`-side of an edge `{a, b}` with both endpoints
internal.

## Sources

- Saitou & Nei (1987); Studier & Keppler (1988); Gascuel (1994); Bryant (2005). Proves the deferred entry `njRun_splits`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.njRun_splits`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 1982](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L1982). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#nj-run-splits).

## Neighbor joining forms the splits of a tree when every join forms a side

Let `(G, ι)`
be a binary phylogenetic `X`-tree and `D` any dissimilarity. Suppose that whenever a run of
neighbor joining on `D` has reached a partition `S` of the taxa into sides of edges of the tree
(with at least four clusters) and joins two of its clusters, their union is again a side of an
edge. Then every complete run of neighbor joining on `D` (stopped with at most three clusters)
forms exactly the splits of the internal edges of the tree. This reduces the correctness of
neighbor joining on `D` to its selection step.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.njRun_splits_of_join`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean, line 2002](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoining.lean#L2002). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html#nj-run-splits-of-join).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Neighbor joining](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/phylogenetics/neighbor-joining)
