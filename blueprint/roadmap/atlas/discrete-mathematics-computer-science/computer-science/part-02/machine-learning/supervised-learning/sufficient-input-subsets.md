---
declaration: section
origin: cited
lean: Cslib.MachineLearning.SufficientInputSubsets.IsGreedy, Cslib.MachineLearning.SufficientInputSubsets.exists_isGreedy, Cslib.MachineLearning.SufficientInputSubsets.chain, Cslib.MachineLearning.SufficientInputSubsets.findSIS, Cslib.MachineLearning.SufficientInputSubsets.chain_of_nonempty, Cslib.MachineLearning.SufficientInputSubsets.chain_of_not_nonempty, Cslib.MachineLearning.SufficientInputSubsets.subset_of_mem_chain, Cslib.MachineLearning.SufficientInputSubsets.mem_chain_self
statement: formalized
proof: formalized
---

# Sufficient input subsets

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html).

## Greedy backward-selection rule

`pick` is a greedy backward-selection rule for `g`: from a nonempty remaining set `R` it
masks a feature `i ∈ R` maximizing `g (R.erase i)`.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.IsGreedy`, a definition declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#is-greedy).

## Existence of greedy backward-selection rules

Greedy rules exist for every `g`.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.exists_isGreedy`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#exists-is-greedy).

## Backward-selection chain of remaining feature sets

Backward selection: the list of remaining sets `R₀ = R, R₁, …, ∅`, where `R_{t+1}` is
`R_t` with the feature chosen by `pick` masked.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.chain`, a definition declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#chain).

## FindSIS procedure for sufficient input subsets

`FindSIS`: un-mask features in reverse order of masking (start from `∅`) and return the
first set on which the prediction reaches the threshold, or `none`. The paper's procedure does
not test `∅` itself; the two agree whenever `g ∅ < τ`, the case the paper considers.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.findSIS`, a definition declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#find-sis).

## Backward-selection chain at a nonempty set

Unfolding `chain` at a nonempty set.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.chain_of_nonempty`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#chain-of-nonempty).

## Backward-selection chain at the empty set

Unfolding `chain` at the empty set (the chain stops).

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.chain_of_not_nonempty`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#chain-of-not-nonempty).

## Sets in the backward-selection chain are subsets of the start

Every set in the backward-selection chain is a subset of the starting set.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.subset_of_mem_chain`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#subset-of-mem-chain).

## Starting set begins the backward-selection chain

The starting set is the first set of the chain.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.mem_chain_self`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#mem-chain-self).

## FindSIS returns a set when the start reaches the threshold

If the prediction on the starting set reaches the threshold, `findSIS` returns a set.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.findSIS_isSome`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#find-sis-is-some).

## FindSIS returns a sufficient subset of the features

Criterion (1): the returned SIS is a subset of the starting features and is sufficient.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.findSIS_sufficient`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#find-sis-sufficient).

## Proposition 1 (first part)

**Proposition 1 (first part)** of Carter et al.: no feature of the returned SIS can be
additionally masked while keeping the prediction at or above the threshold.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.findSIS_erase_lt`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#find-sis-erase-lt).

## Proposition 1 (second part)

**Proposition 1 (second part)** of Carter et al.: among the sets met during backward
selection, the returned SIS has the smallest cardinality among the sufficient ones.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.findSIS_card_le`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#find-sis-card-le).

## Minimality of FindSIS for monotone set functions

For a monotone set function (masking more features never raises the prediction), the
returned SIS is inclusion-minimal: no proper subset is sufficient. (Derived; the paper states
only Proposition 1.)

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.findSIS_minimal_of_monotone`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#find-sis-minimal-of-monotone).

## SIS-collection procedure

`SIScollection`: while the remaining features `R` are sufficient (`τ ≤ g R`), find a SIS
among them, record it and mask it. Stops if `findSIS` returns an empty set (only possible
when `τ ≤ g ∅`).

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.sisCollection`, a definition declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#sis-collection).

## Sets of the SIS-collection are nonempty and sufficient

Every set of the SIS-collection is a nonempty sufficient subset of the starting features.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.sisCollection_sufficient`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#sis-collection-sufficient).

## Sets of the SIS-collection are pairwise disjoint

The sets of the SIS-collection are pairwise disjoint.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.sisCollection_pairwiseDisjoint`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#sis-collection-pairwise-disjoint).

## Proposition 2

**Proposition 2** of Carter et al.: if the fully masked input is below the threshold,
masking every set of the SIS-collection leaves the prediction below the threshold.

Formalized by `Cslib.MachineLearning.SufficientInputSubsets.sisCollection_remaining_lt`, a theorem declared in [CSLibExt/MachineLearning/SufficientInputSubsets.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/SufficientInputSubsets.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html#sis-collection-remaining-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sufficient input subsets](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/sufficient-input-subsets)
