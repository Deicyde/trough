---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Phylogenetics.NeighborJoining.exists_eq_pair_of_qCriterion_min_of_abs_sub_lt, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.exists_adj_adj_of_qCriterion_min_of_abs_sub_lt, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.NJRun.exists_adj_adj_of_join_init_of_abs_sub_lt, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.NJRun.exists_avg, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.qCriterion_eq_sub_of_shift, Cslib.Bioinformatics.Phylogenetics.NeighborJoining.njRun_splits_of_abs_sub_lt
statement: formalized
proof: formalized
---

# Atteson's theorem on neighbor joining

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/atteson-s-theorem-on-neighbor-joining/index.html).

## Split systems

## Robust cherry lemma for split systems

The selection step of Atteson's theorem
(Atteson 1999), with a proof after Mihaescu, Levy & Pachter (2009, Theorem 16).
Let `A e` (`e : E`) be a compatible binary system of splits with positive weights `w`,
containing every trivial split and closed under complement, on at least four taxa, and let
`d x y` be half the total weight of the indices whose side separates `x` and `y`. Let `μ` be
a lower bound on the weight of every internal split (both sides with at least two taxa). If
`D` is symmetric, vanishes on the diagonal, and `|D x y - d x y| < μ / 2` for all distinct
`x, y`, then a pair of distinct taxa minimizing the Q-criterion
`(|X| - 2) D x y - ∑_z D x z - ∑_z D y z` is a side of the split system.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.exists_eq_pair_of_qCriterion_min_of_abs_sub_lt`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/atteson-s-theorem-on-neighbor-joining/index.html#exists-eq-pair-of-q-criterion-min-of-abs).

## Robust cherry lemma for neighbor joining

The selection step of Atteson's theorem
(Atteson 1999), with a proof after Mihaescu, Levy & Pachter (2009, Theorem 16). Let `d` be
the path-length metric of a binary phylogenetic `X`-tree `(G, ι)` with positive edge lengths
`w` and at least four taxa, and let `μ` be a lower bound on the lengths of the internal edges
(edges with no taxon at either end). Let `D` be a symmetric dissimilarity with zero diagonal
such that `|D x y - d x y| < μ / 2` for all distinct taxa.
If the distinct taxa `x, y` minimize the Q-criterion of `D` over all pairs of distinct
singleton clusters at the start of neighbor joining, then `ι x` and `ι y` have a common
neighbor: they form a cherry. The bound is sharp: with `≤ μ / 2` a non-cherry can tie
(see the tests).

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.exists_adj_adj_of_qCriterion_min_of_abs_sub_lt`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean, line 866](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean#L866). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/atteson-s-theorem-on-neighbor-joining/index.html#exists-adj-adj-of-q-criterion-min-of-abs).

## The first join of neighbor joining on a perturbed tree metric joins a cherry

Under the
hypotheses of `exists_adj_adj_of_qCriterion_min_of_abs_sub_lt`, any pair of clusters that
neighbor joining run on `D` may join from the initial singletons consists of two taxa with a
common neighbor.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.NJRun.exists_adj_adj_of_join_init_of_abs_sub_lt`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean, line 906](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean#L906). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/atteson-s-theorem-on-neighbor-joining/index.html#exists-adj-adj-of-join-init-of-abs-sub-l).

## Neighbor joining averages up to row shifts

Along every run of neighbor joining on a
symmetric dissimilarity `d` with zero diagonal there are weights `α s` (nonnegative, supported
on `s`, summing to `1`) and row terms `κ s` such that the cluster dissimilarity vanishes on the
diagonal and `D s t = ∑ x, ∑ y, α s x * α t y * d x y - κ s - κ t` for distinct current
clusters. Joining `a, b` takes `α (a ∪ b) = (α a + α b) / 2` and
`κ (a ∪ b) = (κ a + κ b + D a b) / 2`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.NJRun.exists_avg`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean, line 938](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean#L938). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/atteson-s-theorem-on-neighbor-joining/index.html#exists-avg).

## The shifting lemma

**The shifting lemma** (Mihaescu, Levy & Pachter 2009, Lemma 4): if `D'` agrees with `D` on
the diagonal of `S` and `D' s t = D s t + f s + f t` for distinct `s, t ∈ S`, then the
Q-criterion of every pair of distinct clusters drops by the same amount `2 ∑_{c ∈ S} f c`, so
both have the same minimizing pairs.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.qCriterion_eq_sub_of_shift`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean, line 1039](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean#L1039). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/atteson-s-theorem-on-neighbor-joining/index.html#q-criterion-eq-sub-of-shift).

## Atteson's theorem: neighbor joining has `ℓ∞` radius `1/2`

**Atteson's theorem: neighbor joining has `ℓ∞` radius `1/2`** (Atteson 1999). Let `d` be
the path-length metric of a binary phylogenetic `X`-tree `(G, ι)` with positive edge lengths
`w`, let `μ` be a lower bound on the lengths of its internal edges (edges with no taxon at
either end), and let `D` be a symmetric dissimilarity with zero diagonal such that
`|D x y - d x y| < μ / 2` for all distinct taxa. Then every complete run of neighbor joining on
`D` (stopped with at most three clusters) forms exactly the splits of the internal edges of the
tree: a set of taxa `A` or its complement is a formed cluster if and only if `A` is the set of
taxa on the `a`-side of an edge `{a, b}` with both endpoints internal.

## Sources

- Atteson (1999); stated as Theorem 2 of Mihaescu, Levy and Pachter (2009). `NJRun` uses the Studier–Keppler update. The proof was written for this formalization: up to row shifts, which do not change the pairs neighbor joining selects, the cluster dissimilarity of a run is an average of `D` (`NJRun.exists_avg`), so its errors against the tree metric of the current clusters stay below `μ / 2`, and the cherry step `exists_eq_pair_of_qCriterion_min_of_abs_sub_lt` applies at every join.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoining.njRun_splits_of_abs_sub_lt`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean, line 1173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningRobustness.lean#L1173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/atteson-s-theorem-on-neighbor-joining/index.html#nj-run-splits-of-abs-sub-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Atteson's theorem on neighbor joining](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/atteson-s-theorem-on-neighbor-joining/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/atteson-s-theorem-on-neighbor-joining)
