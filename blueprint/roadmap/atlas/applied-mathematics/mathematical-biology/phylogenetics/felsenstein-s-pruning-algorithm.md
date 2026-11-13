---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.Tree, Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.Tree.numInternal, Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.Tree.numLeaves, Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.Labeling, Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.card_labeling, Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.weight, Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.bruteLik, Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.likelihood
statement: formalized
proof: formalized
---

# Felsenstein's pruning algorithm

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html).

## Rooted binary tree with transition weights

A rooted binary tree with leaf labels `L`; an internal node `node P l Q r` carries the
transition weights `P` and `Q` (from the node's state to the child's state) on the edges to its
left child `l` and right child `r`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.Tree`, an inductive type declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#tree).

## Number of internal nodes of a tree

The number of internal nodes.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.Tree.numInternal`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#num-internal).

## Number of leaves of a tree

The number of leaves.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.Tree.numLeaves`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#num-leaves).

## Labeling of the non-root nodes of a tree

A labeling of the non-root nodes of a tree by states: at every internal node, the states of
its two children and labelings of the two subtrees.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.Labeling`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#labeling).

## Number of labelings of a tree

There are `|S| ^ (2 · #internal nodes)` labelings (one state for each non-root node), so the
brute-force sum `bruteLik` has exponentially many terms.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.card_labeling`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#card-labeling).

## Weight of a tree labeling

The weight of a labeling given root state `s`: the product over all edges of the transition
weight from the parent's state to the child's state, times the leaf weight `obs l` at the state
of every leaf `l`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.weight`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#weight).

## Brute-force likelihood given the root state

The likelihood of the leaf data conditioned on root state `s`, by brute force: the sum of
the weights of all labelings of the non-root nodes.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.bruteLik`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#brute-lik).

## Site likelihood of a phylogenetic tree

The site likelihood with root distribution `π`: `∑ s, π s * bruteLik obs t s`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.likelihood`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#likelihood).

## Felsenstein's pruning recursion

Felsenstein's pruning recursion: the partial likelihood of the subtree `t` given state `s`
at its root.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.prune`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#prune).

## Brute-force likelihood at a leaf

At a leaf, the brute-force likelihood is the leaf weight.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.bruteLik_leaf`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#brute-lik-leaf).

## Brute-force likelihood factors over subtrees

The brute-force likelihood factors over the two subtrees of the root (the distributive law
behind pruning).

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.bruteLik_node`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#brute-lik-node).

## Felsenstein's pruning algorithm computes the likelihood conditioned on the root state

**Felsenstein's pruning algorithm computes the likelihood conditioned on the root state.**

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.prune_eq_bruteLik`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#prune-eq-brute-lik).

## The site likelihood by pruning

`likelihood obs t π = ∑ s, π s * prune obs t s`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.likelihood_eq_sum_prune`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#likelihood-eq-sum-prune).

## Tabulated Felsenstein pruning algorithm

Felsenstein's pruning algorithm, tabulated on the states `Fin n`: the vector of partial
likelihoods of each subtree is computed once, with `O(n²)` operations per internal node.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.pruneTab`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#prune-tab).

## Tabulated pruning computes the pruning recursion

The tabulated algorithm computes the pruning recursion.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.pruneTab_get`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#prune-tab-get).

## Site likelihood from tabulated partial likelihoods

The site likelihood from the tabulated partial likelihoods at the root.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.likelihood_eq_sum_pruneTab`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#likelihood-eq-sum-prune-tab).

## Independent sites

For an alignment whose sites `k : ι` evolve independently along the
same tree with leaf data `obs k`, the joint likelihood (the sum over all choices of a root state
and a labeling at every site of the product of the per-site weights) is the product of the
per-site likelihoods.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinPruning.sum_prod_siteWeight_eq_prod_likelihood`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinPruning.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html#sum-prod-site-weight-eq-prod-likelihood).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Felsenstein's pruning algorithm](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/felsenstein-s-pruning-algorithm)
