---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Phylogenetics.Parsimony.Cost, Cslib.Bioinformatics.Phylogenetics.Parsimony.edgeCost, Cslib.Bioinformatics.Phylogenetics.Parsimony.Agrees, Cslib.Bioinformatics.Phylogenetics.Parsimony.leafObs, Cslib.Bioinformatics.Phylogenetics.Parsimony.untrop_weight, Cslib.Bioinformatics.Phylogenetics.Parsimony.sankoff, Cslib.Bioinformatics.Phylogenetics.Parsimony.sankoff_eq_inf, Cslib.Bioinformatics.Phylogenetics.Parsimony.sankoff_le_edgeCost
statement: formalized
proof: formalized
---

# Small parsimony problem

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html).

## Min-plus cost semiring

The cost semiring: `MinTropical (WithTop ℕ)`, with `min` as addition and `+` as
multiplication.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.Cost`, an abbreviation declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#cost).

## Total substitution cost of a labeling

The total substitution cost of a labeling `x` of the non-root vertices of `t` with root
state `s`: the sum over all edges of the cost `untrop (P a b)` from the parent's state `a` to
the child's state `b`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.edgeCost`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#edge-cost).

## Labeling agrees with the observed leaf states

The labeling `x` (with root state `s`) agrees with the observed states `σ` at every leaf.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.Agrees`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#agrees).

## Tropical leaf weights of observed states

The leaf weights of the observed states `σ`: the tropical one (cost `0`) at the observed
state and the tropical zero (cost `⊤`) at every other state.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.leafObs`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#leaf-obs).

## Tropical weight of a labeling equals its edge cost

The weight of a labeling in the tropical semiring is its edge cost if it agrees with the
leaf states and `⊤` otherwise.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.untrop_weight`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#untrop-weight).

## Sankoff's algorithm

The minimum cost of the subtree `t` given the state `s` at its
root, computed by Felsenstein's pruning recursion over the tropical semiring.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.sankoff`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#sankoff).

## Sankoff's algorithm computes the small-parsimony cost

`sankoff σ t s` is the minimum
total edge cost over all labelings of the non-root vertices that agree with the observed states
at the leaves (with root state `s`).

## Sources

- Sankoff (1975).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.sankoff_eq_inf`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#sankoff-eq-inf).

## Sankoff's cost is a lower bound

Sankoff's cost is a lower bound for the cost of every labeling that agrees with the leaf
states.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.sankoff_le_edgeCost`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#sankoff-le-edge-cost).

## Sankoff's cost is attained

Sankoff's cost is attained: if it is finite, some labeling that agrees with the leaf states
has exactly this cost. (It is `⊤` exactly when every agreeing labeling uses a forbidden change,
or when `t` is a single leaf whose observed state is not `s`.)

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.exists_edgeCost_eq_sankoff`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#exists-edge-cost-eq-sankoff).

## Sankoff's recursion at a leaf

Sankoff's recursion at a leaf: cost `0` at the observed state, `⊤` elsewhere.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.sankoff_leaf`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#sankoff-leaf).

## Sankoff's recursion at an internal vertex

Sankoff's recursion at an internal vertex: the cost of state `s` is the sum, over the two
children, of the minimum over the child's state `a` of the edge cost from `s` to `a` plus the
child's cost at `a`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.sankoff_node`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#sankoff-node).

## Unit substitution cost

The unit cost: `0` for no change and `1` for a change of state.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.unitCost`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#unit-cost).

## Tree with unit costs on every edge

Every edge of the tree carries the unit cost.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.IsUnitCost`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#is-unit-cost).

## Fitch's algorithm

The set of candidate states at the root of the subtree and the number
of changes counted so far. The edge weights of the tree are ignored. Each child is evaluated
once per node, so the recursion makes one call per vertex.

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.fitch`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#fitch).

## Fitch's algorithm computes the small-parsimony score

On a binary tree with unit costs,
Fitch's count equals the minimum, over root states, of Sankoff's cost.

## Sources

- Fitch (1971); Hartigan (1973).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.fitch_score_eq`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#fitch-score-eq).

## Fitch's root set is the set of optimal root states

On a binary tree with unit costs, a
root state is in Fitch's set if and only if Sankoff's cost at that state is the minimum.

## Sources

- Hartigan (1973).

Formalized by `Cslib.Bioinformatics.Phylogenetics.Parsimony.fitch_set_eq`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/Parsimony.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html#fitch-set-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Small parsimony problem](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/small-parsimony-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/phylogenetics/small-parsimony-problem)
