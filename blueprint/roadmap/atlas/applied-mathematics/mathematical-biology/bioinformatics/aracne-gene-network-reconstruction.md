---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.GeneNetworks.Aracne.aracne, Cslib.Bioinformatics.GeneNetworks.Aracne.le_aracne_of_isAcyclic, Cslib.Bioinformatics.GeneNetworks.Aracne.aracne_le_of_isTree, Cslib.Bioinformatics.GeneNetworks.Aracne.aracne_eq_of_isTree, Cslib.Bioinformatics.GeneNetworks.Aracne.le_aracne_of_isMaxWeightSpanningTree
statement: formalized
proof: formalized
---

# ARACNE gene network reconstruction

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/aracne-gene-network-reconstruction/index.html).

## ARACNE gene network reconstruction

The network ARACNE reconstructs from symmetric pairwise mutual informations `I` with
independence threshold `I₀` and DPI tolerance zero (Margolin et al. 2006): `{i, k}` is an edge
iff `i ≠ k`, `I₀ < I i k`, and no third gene `j` with `I₀ < I i j` and `I₀ < I j k` has
`I i k < min (I i j) (I j k)`.

Formalized by `Cslib.Bioinformatics.GeneNetworks.Aracne.aracne`, a definition declared in [CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/aracne-gene-network-reconstruction/index.html#aracne).

## No false negatives

If the true network `T` is a forest whose edges all carry mutual
information above `I₀`, and `I a b ≤ min (I a c) (I c b)` whenever `c` separates `a` from `b` in
`T` (every walk from `a` to `b` visits `c`), then ARACNE keeps every edge of `T`.

Formalized by `Cslib.Bioinformatics.GeneNetworks.Aracne.le_aracne_of_isAcyclic`, a theorem declared in [CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/aracne-gene-network-reconstruction/index.html#le-aracne-of-is-acyclic).

## No false positives

If the true network `T` is a tree and `I a b < min (I a c) (I c b)`
whenever `c` separates `a` from `b` in `T`, then every edge ARACNE keeps is an edge of `T`.

Formalized by `Cslib.Bioinformatics.GeneNetworks.Aracne.aracne_le_of_isTree`, a theorem declared in [CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/aracne-gene-network-reconstruction/index.html#aracne-le-of-is-tree).

## ARACNE recovers tree networks exactly

**ARACNE recovers tree networks exactly** (Margolin et al. 2006, Theorem 1): if the true
network `T` is a tree whose edges all carry mutual information above `I₀`, and the strict
data-processing inequality holds on every separated triple, then ARACNE returns `T`. Strictness
is the explicit form of the paper's exclusion of exact cancellations; with equality ARACNE can
keep an indirect edge (see the tests).

Formalized by `Cslib.Bioinformatics.GeneNetworks.Aracne.aracne_eq_of_isTree`, a theorem declared in [CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/aracne-gene-network-reconstruction/index.html#aracne-eq-of-is-tree).

## Chow–Liu trees survive ARACNE

**Chow–Liu trees survive ARACNE** (Margolin et al. 2006, Theorem 2): a spanning tree `T` of
maximum total weight `∑_{{i, k} ∈ T} I i k` among all spanning trees, whose edges all carry
mutual information above `I₀`, is a subnetwork of the ARACNE network.

Formalized by `Cslib.Bioinformatics.GeneNetworks.Aracne.le_aracne_of_isMaxWeightSpanningTree`, a theorem declared in [CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/GeneNetworks/Aracne.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/aracne-gene-network-reconstruction/index.html#le-aracne-of-is-max-weight-spanning-tree).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: ARACNE gene network reconstruction](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/aracne-gene-network-reconstruction/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/aracne-gene-network-reconstruction)
