---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.cherryCoeff, Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.cherryLength, Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.cherryLength_eq, Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.qCriterion_le_iff_cherryLength_le, Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.NJRun.symm_diag, Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.NJRun.isMin_qCriterion_iff_cherryLength, Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.cherryLength_eq_length
statement: formalized
proof: formalized
---

# Neighbor joining and balanced minimum evolution

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution/index.html).

## Generalized Pauplin coefficient of a cherry tree

The generalized Pauplin coefficient of the pair of clusters `u, v` in the tree `T_ab`
obtained from the star on `S` by joining `a` and `b`: `1/2` for `{a, b}`; `1/(2(|S| - 2))` when
one of `u, v` is `a` or `b` and the other is not; `1/(|S| - 2)` when neither is. Values on the
diagonal `u = v` are never used.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.cherryCoeff`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution/index.html#cherry-coeff).

## Balanced minimum-evolution length of a cherry tree

The balanced minimum-evolution length of `T_ab` for the dissimilarity `D`:
half the sum over ordered pairs of distinct clusters of `cherryCoeff S a b u v * D u v`, which
is `∑_{u<v} cherryCoeff S a b u v * D u v` when `D` is symmetric.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.cherryLength`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution/index.html#cherry-length).

## The BME length of a join in terms of the Q-criterion

For `D` symmetric and zero on the
diagonal of `S`, `|S| ≥ 3` and distinct `a, b ∈ S`:
`cherryLength S D a b = (∑_{u ≠ v ∈ S} D u v + Q(a, b)) / (2 (|S| - 2))`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.cherryLength_eq`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution/index.html#cherry-length-eq).

## Minimizing `Q` is minimizing the local star BME length of the join

The BME length
of `T_ab` on the current clusters for the current cluster dissimilarity `D`. This is the
local star identity; it is not the full Gascuel–Steel comparison on all taxa.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.qCriterion_le_iff_cherryLength_le`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution/index.html#q-criterion-le-iff-cherry-length-le).

## Neighbor joining preserves symmetry and zero diagonal

Along a run of neighbor joining on a symmetric `d` with zero diagonal, the cluster
dissimilarity stays symmetric and vanishes on every current cluster.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.NJRun.symm_diag`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution/index.html#symm-diag).

## Q-minimality is cherry-length minimality at a run state

At every state of a run on a
symmetric dissimilarity with zero diagonal and at least three clusters, a pair of distinct
clusters minimizes the Q-criterion (the pairs NJ may join) if and only if joining it gives
the smallest `cherryLength`, the BME length of the join tree `T_ab` on the current clusters
for the current cluster dissimilarity `D`. This is the local star identity only: it does not
compare partially resolved trees on all taxa under the original dissimilarity `d`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.NJRun.isMin_qCriterion_iff_cherryLength`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution/index.html#is-min-q-criterion-iff-cherry-length).

## The coefficients give the tree length

Let `T_ab` carry real edge lengths: `ℓ c` on the
pendant edge of each cluster `c ∈ S` and `m` on the edge between `u` and the center. If `D` is
its path-length dissimilarity (`D a b = ℓ a + ℓ b`, `D x c = ℓ x + m + ℓ c` for `x ∈ {a, b}` and
`c` another cluster, `D c c' = ℓ c + ℓ c'` for two other distinct clusters), then
`cherryLength S D a b = ∑_{c ∈ S} ℓ c + m`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.NeighborJoiningBME.cherryLength_eq_length`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/NeighborJoiningBME.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution/index.html#cherry-length-eq-length).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Neighbor joining and balanced minimum evolution](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/neighbor-joining-and-balanced-minimum-evolution)
