---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.NonnegWeights, Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.argmaxState, Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.le_argmaxState, Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.sup'_eq_argmaxState, Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.maxPrune, Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.traceback, Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.maxPrune_nonneg, Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.weight_traceback
statement: formalized
proof: formalized
---

# Maximum-likelihood ancestral reconstruction

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html).

## Nonnegative transition weights on a tree

All transition weights in the tree are nonnegative.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.NonnegWeights`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#nonneg-weights).

## State maximizing a function

A state maximizing `f` (ties broken by choice).

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.argmaxState`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#argmax-state).

## The argmax state maximizes the function

`argmaxState f` maximizes `f`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.le_argmaxState`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#le-argmax-state).

## Value at the argmax state is the maximum

The value at `argmaxState f` is the maximum `univ.sup'` of `f`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.sup'_eq_argmaxState`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#sup-eq-argmax-state).

## Max-product pruning recursion

The max-product (Viterbi) form of Felsenstein's pruning recursion: the largest weight of a
labeling of the subtree `t` given state `s` at its root.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.maxPrune`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#max-prune).

## Pupko's traceback

Pupko's traceback: given the state `s` of the root of `t`, label each child with a state
maximizing the transition weight times the child's `maxPrune`, and recurse.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.traceback`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#traceback).

## Nonnegativity of max-product pruning

With nonnegative weights, `maxPrune` is nonnegative.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.maxPrune_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#max-prune-nonneg).

## The traced labeling attains `maxPrune`

No sign condition is needed.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.weight_traceback`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#weight-traceback).

## Nonnegativity of labeling weights

With nonnegative weights, every labeling has nonnegative weight.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.weight_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#weight-nonneg).

## `maxPrune` bounds the weight of every labeling

**`maxPrune` bounds the weight of every labeling** (nonnegative weights).

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.weight_le_maxPrune`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#weight-le-max-prune).

## The max-product recursion computes the maximal labeling weight

`maxPrune obs t s` is the
maximum over all labelings `z` of the non-root nodes of `weight obs t s z`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.maxPrune_eq_sup'`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#max-prune-eq-sup).

## Root state of Pupko's reconstruction

The root state of Pupko's reconstruction: it maximizes `π s * maxPrune obs t s`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.jointRoot`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#joint-root).

## Pupko's joint reconstruction

The root state `jointRoot` and the traced labeling.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.pupko`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#pupko).

## Likelihood of Pupko's joint reconstruction

The likelihood of Pupko's reconstruction is `max_s π s * maxPrune obs t s`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.jointLik_pupko`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#joint-lik-pupko).

## Pupko et al. (2000): joint maximum likelihood

With nonnegative root, transition and leaf
weights, no root state `s` and labeling `z` of the non-root nodes has larger joint likelihood
`π s * weight obs t s z` than Pupko's reconstruction.

Formalized by `Cslib.Bioinformatics.Phylogenetics.AncestralReconstruction.pupko_isJointML`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/AncestralReconstruction.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html#pupko-is-joint-ml).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum-likelihood ancestral reconstruction](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/maximum-likelihood-ancestral-reconstruction)
