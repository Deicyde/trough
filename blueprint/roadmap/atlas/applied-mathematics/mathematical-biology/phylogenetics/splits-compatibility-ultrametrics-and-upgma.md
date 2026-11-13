---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Phylogenetics.Splits.IsHierarchy, Cslib.Bioinformatics.Phylogenetics.Splits.IsBinaryHierarchy.isHierarchy, Cslib.Bioinformatics.Phylogenetics.Splits.isHierarchy_completion, Cslib.Bioinformatics.Phylogenetics.Splits.exists_isBinaryHierarchy_superset, Cslib.Bioinformatics.Phylogenetics.Splits.IsBinaryHierarchy.card_add_one, Cslib.Bioinformatics.Phylogenetics.Splits.Compatible, Cslib.Bioinformatics.Phylogenetics.Splits.Compatible.symm, Cslib.Bioinformatics.Phylogenetics.Splits.compatible_compl_left
statement: formalized
proof: formalized
---

# Splits, compatibility, ultrametrics and UPGMA

57 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html).

## Hierarchies

## Hierarchy on a finite set

A **hierarchy** on a finite set `S`: a family of nonempty subsets of `S` containing `S` and
every singleton, any two members nested or disjoint. These are the cluster systems of the rooted
phylogenetic trees on `S` (Semple & Steel 2003, Section 3.5).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.IsHierarchy`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#is-hierarchy).

## A binary hierarchy is a hierarchy

A binary hierarchy is a hierarchy.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.IsBinaryHierarchy.isHierarchy`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#is-hierarchy-2).

## Pairwise nested-or-disjoint clusters form a hierarchy

Adding `S` and the singletons to
a family of pairwise nested-or-disjoint nonempty subsets of a nonempty `S` gives a hierarchy.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.isHierarchy_completion`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#is-hierarchy-completion).

## Hierarchies are refined by binary trees

Every family of pairwise nested-or-disjoint
nonempty subsets of a nonempty `S` is contained in a binary hierarchy on `S`, the cluster set of
a rooted binary phylogenetic tree on `S` (Semple & Steel 2003, Proposition 3.5.2 and the
refinement of a rooted tree to a binary one).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.exists_isBinaryHierarchy_superset`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#exists-is-binary-hierarchy-superset).

## Number of members of a binary hierarchy

A binary hierarchy on `S` has `2 |S| - 1` members: the `|S|` singletons and `|S| - 1`
internal clusters (stated without subtraction).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.IsBinaryHierarchy.card_add_one`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#card-add-one).

## Compatible splits

The splits `A | Aᶜ` and `B | Bᶜ` are **compatible**: one of `A ∩ B`, `A ∩ Bᶜ`, `Aᶜ ∩ B`,
`Aᶜ ∩ Bᶜ` is empty (Semple & Steel 2003, Section 3.1).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.Compatible`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#compatible).

## Symmetry of split compatibility

Compatibility is symmetric.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.Compatible.symm`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#symm).

## Compatibility is unchanged by complementing the first split

Compatibility depends only on the split, not on the side used to store it.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.compatible_compl_left`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#compatible-compl-left).

## Compatibility is unchanged by complementing the second split

Compatibility depends only on the split, not on the side used to store it.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.compatible_compl_right`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#compatible-compl-right).

## Compatible clusters are nested or disjoint

For the sides not containing a fixed taxon `a`, compatibility is being nested or disjoint:
splits seen from a root are clusters.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.compatible_iff_nested_or_disjoint`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#compatible-iff-nested-or-disjoint).

## Four-gamete condition for binary characters

The binary characters `χ` and `ψ` show **all four gametes** `(0,0), (0,1), (1,0), (1,1)`
on the taxa.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.FourGametes`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#four-gametes).

## Split of a binary character

The split of a binary character: the taxa in state `true`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.charSplit`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#char-split).

## The four-gamete test

Two binary characters give compatible splits iff they do not
show all four gametes (Buneman 1971; Estabrook, Johnson & McMorris 1976).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.compatible_iff_not_fourGametes`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#compatible-iff-not-four-gametes).

## Split set of a tree computed from a leaf

The split set of `T` computed from the leaf `a`: both sides of every cluster of `T` seen
from `a`. It equals `edgeSplits T` for every `a` (`splitSet_eq_edgeSplits`).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.splitSet`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#split-set).

## Clusters seen from a leaf omit that leaf

The clusters seen from `a` do not contain `a`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.notMem_of_mem_clusterSet`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#not-mem-of-mem-cluster-set).

## Side of a tree edge containing a vertex

The side of the edge `p – v` containing `v`: the taxa whose leaf is closer to `v` than to
`p`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.edgeSide`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#edge-side).

## Edge splits of a tree

The **edge splits** of `T`: the sides of all its edges (both sides of every edge).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.edgeSplits`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#edge-splits).

## The two sides of a tree edge are complementary

The two sides of an edge are complementary.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.compl_edgeSide`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#compl-edge-side).

## Clusters seen from a leaf are edge sides

The cluster of a vertex `v` seen from `a` is the side of `v` of the edge from `v` to its
neighbor `p` toward `a`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.cluster_eq_edgeSide`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#cluster-eq-edge-side).

## Split set from any leaf equals the edge splits

The split set computed from any leaf is the set of edge splits.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.splitSet_eq_edgeSplits`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#split-set-eq-edge-splits).

## The split set does not depend on the leaf used to compute it

**The split set does not depend on the leaf used to compute it.**

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.splitSet_eq_splitSet`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#split-set-eq-split-set).

## Splits computed from a leaf are pairwise compatible

Any two splits of one tree are compatible.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.compatible_of_mem_splitSet`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 647](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L647). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#compatible-of-mem-split-set).

## Edge splits of a tree are pairwise compatible

Any two splits of one tree are compatible.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.compatible_of_mem_edgeSplits`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 699](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L699). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#compatible-of-mem-edge-splits).

## Splits-equivalence theorem

**Splits-equivalence theorem**, binary form (Buneman 1971; Semple & Steel 2003, Theorem
3.1.4): on at least two taxa, a family `F` of proper splits (both sides nonempty) is contained in
the split set of some unrooted binary phylogenetic tree iff its members are pairwise compatible.
The tree is a binary refinement of the tree whose splits are exactly `F` and the trivial ones.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.splits_equivalence`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 711](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L711). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#splits-equivalence).

## Perfect phylogeny for a binary character matrix

`T` is a **perfect phylogeny** for the binary character matrix `M` (taxa by characters):
the split of every non-constant column is a split of `T`, i.e. every character changes state
on exactly one edge.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.IsPerfectPhylogeny`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 724](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L724). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#is-perfect-phylogeny).

## Perfect phylogeny and the four-gamete condition

**Perfect phylogeny and the four-gamete condition** (Estabrook, Johnson & McMorris 1976;
Gusfield 1991): a binary character matrix on at least two taxa has a perfect phylogeny iff no
two of its columns show all four gametes.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.exists_perfectPhylogeny_iff`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#exists-perfect-phylogeny-iff).

## Robinson–Foulds distance

The **Robinson–Foulds distance**: the number of splits in exactly one of the two trees.
Each split is counted once, by its side away from the leaf `a` (its cluster seen from `a`);
trivial splits are common to all trees and cancel. The value does not depend on `a`
(`rfDist_eq_rfDist`).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.rfDist`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 780](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L780). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#rf-dist).

## Robinson–Foulds distance as half the split symmetric difference

Each split is counted twice in the symmetric difference of the split sets (once per side),
so the Robinson–Foulds distance is half of it.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.two_mul_rfDist`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 785](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L785). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#two-mul-rf-dist).

## Robinson–Foulds distance is independent of the base leaf

The Robinson–Foulds distance does not depend on the leaf used to compute it.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.rfDist_eq_rfDist`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 834](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L834). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#rf-dist-eq-rf-dist).

## Robinson–Foulds distance from a tree to itself is zero

The Robinson–Foulds distance from a tree to itself is zero.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.rfDist_self`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 842](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L842). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#rf-dist-self).

## Symmetry of the Robinson–Foulds distance

The Robinson–Foulds distance is symmetric.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.rfDist_comm`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 846](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L846). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#rf-dist-comm).

## Triangle inequality for the Robinson–Foulds distance

The Robinson–Foulds distance satisfies the triangle inequality.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.rfDist_triangle`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 850](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L850). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#rf-dist-triangle).

## Robinson–Foulds distance vanishes exactly on isomorphic trees

The Robinson–Foulds distance vanishes exactly on isomorphic trees (Robinson & Foulds 1981).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.rfDist_eq_zero_iff`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 857](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L857). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#rf-dist-eq-zero-iff).

## Isomorphism invariance of the Robinson–Foulds distance

The Robinson–Foulds distance is invariant under isomorphism, so it is a metric on the trees
up to isomorphism.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.rfDist_congr`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 869](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L869). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#rf-dist-congr).

## Maximum of the Robinson–Foulds distance

On `n ≥ 3` taxa it is at most `2 (n - 3)`, the
number of nontrivial splits of two binary trees (Robinson & Foulds 1981).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.rfDist_le`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 875](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L875). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#rf-dist-le).

## Majority splits of a family of trees

The **majority splits** of a finite family of trees `T i`: the clusters, seen from `a`, of
more than half of the trees (repetitions in the family count).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.majoritySplits`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 928](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L928). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#majority-splits).

## Majority splits are compatible

**Majority splits are compatible** (Margush & McMorris 1981): two clusters each in more than
half of the trees are both clusters of a common tree (pigeonhole), hence nested or disjoint.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.nested_or_disjoint_of_mem_majoritySplits`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 935](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L935). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#nested-or-disjoint-of-mem-majority-split).

## The majority-rule consensus tree

The majority splits are clusters of one unrooted
binary phylogenetic tree (a binary refinement of the majority-rule consensus tree).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.exists_tree_majoritySplits_subset`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 952](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L952). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#exists-tree-majority-splits-subset).

## Bootstrap support

**Bootstrap support** (Felsenstein 1985) of the split with side `A` away from `a`, for a
tree estimator `est` and an alignment `M` of `m` sites: the fraction of the `m ^ m` site
resamplings with replacement `w : Fin m → Fin m` (uniform draws, whose site counts are
multinomial) for which the tree estimated from the resampled alignment `M ∘ w` has the
cluster `A`. This is the exact bootstrap proportion; Felsenstein's procedure estimates it from a
sample of resamplings.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.bootstrapSupport`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 973](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L973). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#bootstrap-support).

## Bootstrap support lies in the unit interval

Bootstrap support is a frequency: it lies in `[0, 1]`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.bootstrapSupport_mem_Icc`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 980](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L980). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#bootstrap-support-mem-icc).

## Bootstrap support above one half means a majority split

A split has bootstrap support above one half iff it is a majority split of the bootstrap
replicate trees; so the splits with support above one half are pairwise compatible and form
one tree (`exists_tree_majoritySplits_subset`).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.one_half_lt_bootstrapSupport_iff`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 995](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L995). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#one-half-lt-bootstrap-support-iff).

## Ultrametric on taxa

`d` is an **ultrametric** on the taxa: symmetric, zero exactly on the diagonal, and
satisfying the **three-point condition** `d x z ≤ max (d x y) (d y z)` (equivalently, of the
three distances among any three taxa the two largest are equal).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.IsUltrametric`, a structure declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1029](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1029). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#is-ultrametric).

## Metric of a dated rooted tree

`d` is the metric of a **dated rooted tree**, encoded by its clusters: a hierarchy `H` on
the taxa with dates `h` (`0` at the leaves, strictly increasing from a cluster to any cluster
strictly containing it) such that `d x y` is the date of the smallest cluster containing `x`
and `y` (their most recent common ancestor). With edge lengths `(h D - h C) / 2` from each
cluster `C` to its parent `D`, `d x y` is the path length from `x` to `y` and all leaves are
equidistant from the root (Semple & Steel 2003, Section 7.2).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.IsDatedTreeMetric`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1045](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1045). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#is-dated-tree-metric).

## Ultrametrics satisfy the four-point condition

**Ultrametrics satisfy the four-point condition** (Semple & Steel 2003, Section 7.2), so
every ultrametric on a finite set is a tree metric (`IsUltrametric.isTreeMetric`).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.IsUltrametric.fourPointCondition`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1072](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1072). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#four-point-condition).

## Every ultrametric is a tree metric

Every ultrametric on a finite set is a tree metric (via Buneman's four-point theorem).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.IsUltrametric.isTreeMetric`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1086](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1086). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#is-tree-metric).

## Ultrametrics are dated tree metrics

**Ultrametrics are dated tree metrics** (Semple & Steel 2003, Theorem 7.2.5): on a
nonempty finite set of taxa, a dissimilarity satisfies the three-point condition (and is a
metric) iff it is the metric of a dated rooted tree.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.isUltrametric_iff_isDatedTreeMetric`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#is-ultrametric-iff-is-dated-tree-metric).

## Average linkage between clusters

The **average linkage** between two clusters: the mean of `d x y` over `x ∈ C`, `y ∈ D`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.avgDist`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#avg-dist).

## States reachable by UPGMA

The states reachable by **UPGMA** (Sokal & Michener 1958) on `d`: a partition `P` of the
taxa into blocks and the heights `c x y` recorded so far. It starts from the singletons; each
step merges two distinct blocks `C`, `D` of least average linkage (ties broken arbitrarily) and
records `avgDist d C D` as the height at which every `x ∈ C` and `y ∈ D` are joined (the
distance between them in the output tree; their common ancestor sits at half of it).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.UpgmaReaches`, an inductive type declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#upgma-reaches).

## UPGMA is exact on ultrametrics

In every UPGMA run on an ultrametric, the recorded
height of two taxa in the same block is their distance. In particular a completed run (one
block) reconstructs `d`, i.e. the dated tree, exactly (Semple & Steel 2003, Section 7.2).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.upgma_exact`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#upgma-exact).

## UPGMA always completes

UPGMA always completes: from the singletons it reaches the single block `univ`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.exists_upgmaReaches_univ`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1439](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#exists-upgma-reaches-univ).

## Rooted triplet

A **rooted triplet** `xy|z`: `x` and `y` are closer to each other than to `z`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.Triplet`, a structure declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1494](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#triplet).

## Cluster system displaying a triplet

The cluster system `H` **displays** the triplet `xy|z`: some cluster contains `x` and `y`
but not `z`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.DisplaysTriplet`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#displays-triplet).

## Cut in the Aho graph

The **Aho graph** of the triplets `R` on `S'` (vertices `S'`, an edge `x y` for each
`xy|z ∈ R` with `x, y, z ∈ S'`) has a cut: a partition of `S'` into two nonempty parts with no
edge across, i.e. the graph is disconnected.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.HasAhoCut`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#has-aho-cut).

## A rooted binary tree is determined by its triplets

**A rooted binary tree is determined by its triplets** (Semple & Steel 2003, Theorem
6.4.1): two binary hierarchies on `S` displaying the same triplets are equal.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.eq_of_displaysTriplet_iff`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1587](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1587). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#eq-of-displays-triplet-iff).

## Correctness of BUILD

**Correctness of BUILD** (Aho, Sagiv, Szymanski & Ullman 1981; Semple & Steel 2003,
Section 6.4): a set `R` of triplets on a nonempty `S`, none of the degenerate form `xx|x` (which
no tree displays and no cut detects), is displayed by a rooted binary phylogenetic tree on `S`
iff for every subset `S'` of at least two taxa the Aho graph of `R` on `S'` is disconnected.
BUILD splits along the components and recurses; the converse direction builds the tree this
way, splitting along any cut.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.build_spec`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1599](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#build-spec).

## Tree displaying a quartet

`T` **displays the quartet** `xy|zw`: some edge split of `T` has `x, y` on one side and
`z, w` on the other.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.DisplaysQuartet`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1709](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1709). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#displays-quartet).

## An unrooted binary tree is determined by its quartets

**An unrooted binary tree is determined by its quartets** (Semple & Steel 2003, Corollary
6.3.8): two trees displaying the same quartets are isomorphic. Already the quartets containing
the taxon `a` suffice; they are the rooted triplets seen from `a`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Splits.iso_of_displaysQuartet_iff`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Splits.lean, line 1715](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/Splits.lean#L1715). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html#iso-of-displays-quartet-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Splits, compatibility, ultrametrics and UPGMA](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/splits-compatibility-ultrametrics-and-upgma)
