---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.AdmixtureGraph, MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.Edge, MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit, MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.weight, MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.pathProb, MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.paths, MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit_eq, MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit_self
statement: formalized
proof: formalized
---

# Admixture graphs

28 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html).

## Population Genetics

## Admixture graph

An admixture graph on the nodes `V` (Patterson et al. 2012): a rooted directed acyclic
graph in which every non-root node has one or two parents, with admixture proportions.

* `parents X` are the parents of `X`, the root has none, every other node has one or two;
* `prop X Y` is the probability that a lineage in `X` descends from parent `Y`: nonnegative,
  summing to `1` over the parents of a non-root node, and `0` off the parent set;
* the parent relation is well founded, i.e. the graph is acyclic (`V` is finite in all
  results).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph`, a structure declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#admixture-graph).

## Edges of an admixture graph

The edges `(child, parent)` of the graph.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.Edge`, an abbreviation declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#edge).

## Probability that a lineage passes through a node

`visit X c` is the probability that the lineage of a gene sampled in `X`, traced toward the
root with parents chosen according to the admixture proportions, passes through `c`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#visit).

## Lineage weight of an edge in an admixture graph

`weight X e` is the probability that the lineage of a gene sampled in `X` traverses the edge
`e = (c, p)`: it reaches `c` and then descends from `p`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.weight`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#weight).

## Probability of a root-ward path in an admixture graph

The probability of a root-ward path `[v₀, v₁, …, v_k]`: the product of the proportions
`prop vᵢ vᵢ₊₁`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.pathProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#path-prob).

## Root-ward paths from a node of an admixture graph

The root-ward paths from `X`: the lists `[X = v₀, v₁, …, v_k = root]` with each `vᵢ₊₁` a
parent of `vᵢ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.paths`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#paths).

## First-step equation for visit probabilities

First-step equation for `visit`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#visit-eq).

## A lineage visits its own node with probability one

A lineage passes through its own node with probability `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit_self`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#visit-self).

## Nonnegativity of visit probabilities

Visit probabilities are nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#visit-nonneg).

## Visit probabilities are at most one

Visit probabilities are at most `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit_le_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#visit-le-one).

## Every lineage reaches the root

Every lineage reaches the root.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit_root`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#visit-root).

## First-step equation for root-ward paths

First-step equation for `paths`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.paths_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#paths-eq).

## Admixture proportions are at most one

Admixture proportions are at most `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.prop_le_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#prop-le-one).

## A lineage from a parent never passes through its child

Acyclicity: a lineage from a parent `Y` of `X` never passes through `X`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit_eq_zero_of_mem_parents`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#visit-eq-zero-of-mem-parents).

## Nonnegativity of lineage weights

Lineage weights are nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.weight_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#weight-nonneg).

## Lineage weights are at most one

Lineage weights are at most `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.weight_le_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#weight-le-one).

## First-step recursion for lineage weights

First-step recursion for lineage weights: a lineage from `X` traverses `e` either as its
first step (if `e` starts at `X`) or after moving to a parent `Y`, chosen with probability
`prop X Y`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.weight_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#weight-eq).

## Lineage weight recursion at an admixture node

The recursion at an admixture node `X` with parents `A ≠ B`: with `α = prop X A`,
`w X = α w A + (1 - α) w B + w₀`, where `w₀` puts weight `α` on the edge `(X, A)`,
`1 - α` on `(X, B)` and `0` elsewhere.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.weight_admixture`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#weight-admixture).

## Lineage weight recursion at a tree node

The recursion at a tree node `X` with the single parent `Y`: `w X = w Y + 1_{(X, Y)}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.weight_tree`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#weight-tree).

## Path-sum formula for lineage weights

Path-sum form of the lineage weights (Patterson et al. 2012): `weight X e` is the sum, over
the root-ward paths from `X` that traverse `e`, of the products of the admixture proportions
along the path.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.weight_eq_sum_paths`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#weight-eq-sum-paths).

## Tree-shaped admixture graph

The graph is a tree: no node has two parents.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.IsTree`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#is-tree).

## Visit probabilities on a tree are zero or one

On a tree every visit probability is `0` or `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.visit_eq_zero_or_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#visit-eq-zero-or-one).

## Lineage weights on a tree are zero or one

On a tree every lineage weight is `0` or `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.weight_eq_zero_or_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#weight-eq-zero-or-one).

## Drift model of an admixture graph

The drift model of an admixture graph: the populations are the nodes, the root frequency is
`root`, the edge increments are `incr` (square integrable and pairwise uncorrelated), the drift
length of an edge is the second moment of its increment, and the weights are the lineage
weights of the graph.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.driftModel`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#drift-model).

## A tree-shaped admixture graph has binary loadings

A tree-shaped admixture graph induces a drift model with binary loadings (all weights `0` or
`1`).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.hasBinaryLoadings_of_isTree`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#has-binary-loadings-of-is-tree).

## Three-population test is nonnegative on a tree

The three-population test on a tree-shaped admixture graph: `f3 C A B ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.f3_nonneg_of_isTree`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#f3-nonneg-of-is-tree).

## Three-population statistic at an admixture node

The three-population statistic at an admixture node `X` with parents `A ≠ B`, proportions
`α = prop X A` and `β = prop X B` (`α + β = 1`), in a drift model with the graph's weights:
`f3 X A B = α² ℓ_{XA} + β² ℓ_{XB} - α β f2 A B`, where `ℓ_{XA}`, `ℓ_{XB}` are the drift
lengths of the two admixture edges.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.f3_admixture`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#f3-admixture).

## Three-population statistic at an admixture node without edge drift

With no drift on the admixture edges, an admixture node `X` with parents `A ≠ B` and
proportion `α = prop X A` has `f3 X A B = -α (1 - α) f2 A B` (the hypothesis of the seed's
`DriftModel.f3_admixture`, here derived from the graph).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureGraph.f3_admixture_of_len_eq_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureGraph.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html#f3-admixture-of-len-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Admixture graphs](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-structure/admixture-graphs)
