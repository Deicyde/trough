---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BinaryBranching.leaves, Cslib.Algorithms.Lean.BinaryBranching.round, Cslib.Algorithms.Lean.BinaryBranching.leaves_length_pos, Cslib.Algorithms.Lean.BinaryBranching.round_nil_iterate, Cslib.Algorithms.Lean.BinaryBranching.round_iterate, Cslib.Algorithms.Lean.BinaryBranching.round_iterate_of_le, Cslib.Algorithms.Lean.BinaryBranching.sum_leaves, Cslib.Algorithms.Lean.BinaryBranching.leaves_map
statement: formalized
proof: formalized
---

# Traversal of implicit binary trees

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html).

## Depth-cut frontier of a binary branching step

The frontier below `s`, left to right, cut at depth `k`. At depth zero it is `[s]`,
even when `step s` branches. Duplicate occurrences are retained.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.leaves`, a definition declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#leaves).

## One depth-first round of binary branching

One depth-first round on `(stack, output)`. Terminal states are prepended to the output;
a branching state is replaced by its left child followed by its right child.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.round`, a definition declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#round).

## Depth-cut frontiers are nonempty

Every depth-cut frontier is nonempty.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.leaves_length_pos`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#leaves-length-pos).

## An empty work stack is fixed by every round

An empty work stack is fixed by any number of rounds.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.round_nil_iterate`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#round-nil-iterate).

## Exact round count for traversing a terminal frontier

If every frontier occurrence is terminal, exactly `2 * length - 1` rounds process
the tree below `s`, preserving the tail `r` and prepending its reversed frontier to `out`.
The terminal-frontier hypothesis is essential: a depth cut may contain branching states.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.round_iterate`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#round-iterate).

## Enough rounds empty the stack and collect the frontier

After at least `2 * length - 1` rounds from `[s]`, the stack is empty and all
terminal frontier occurrences have been collected in reverse order.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.round_iterate_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#round-iterate-of-le).

## Additive weight of the root is the sum over the frontier

A natural-valued weight additive across each branch equals the sum of the frontier
weights, even when the frontier is cut before termination.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.sum_leaves`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#sum-leaves).

## Commuting maps transport the ordered frontier

A map commuting with both steps transports the ordered frontier, preserving multiplicity.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.leaves_map`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#leaves-map).

## Commuting maps transport one depth-first round

A commuting node map transports one stack round and its accumulated output.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.round_map`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#round-map).

## Commuting maps transport any number of rounds

A commuting node map transports any number of rounds. No injectivity is required.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.round_iterate_map`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#round-iterate-map).

## Weight-counting depth-first round

One stack round accumulating natural weights rather than a list of terminal states.
The previous count is retained, and each terminal occurrence contributes its weight.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.roundCount`, a definition declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#round-count).

## Counting rounds project list-output rounds

Counting rounds are the projection of list-output rounds to the sum of output weights.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.roundCount_iterate`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#round-count-iterate).

## Final count of counting rounds is the frontier weight

With a terminal frontier and enough rounds, the final count is its total weight.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.roundCount_iterate_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#round-count-iterate-of-le).

## Binomial bound on the frontier size under depth and heavy budgets

With at most `d` further depth steps and `h` further heavy steps, the frontier has
at most `∑ j ∈ range (h + 1), d.choose j` occurrences. The source budget hypotheses
are retained, including the strict heavy-budget inequality.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.length_leaves_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#length-leaves-le).

## A large enough depth cut yields only terminal states

A depth allowance covering the remaining depth budget produces only terminal states.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.step_eq_none_of_mem_leaves`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#step-eq-none-of-mem-leaves).

## Frontier occurrences satisfy the resource invariant

Every frontier occurrence satisfies the resource invariant at some budgets.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.exists_of_mem_leaves`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#exists-of-mem-leaves).

## Branch-split properties hold at the root iff at some leaf

A property split by branches holds at the root iff it holds at some frontier occurrence.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.iff_exists_mem_leaves`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#iff-exists-mem-leaves).

## Depth budget bounds the depth-first stack size

The depth budget bounds the stack by `D + 1` at every round; each pending state
satisfies the resource invariant. This is a list-size bound, not a machine-space model.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.stack_bound`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#stack-bound).

## Invariant-restricted step transport of the frontier

Step transport restricted to a preserved invariant transports the frontier and
records that all its occurrences satisfy the invariant.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.leaves_sim`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#leaves-sim).

## A round does not decrease pending plus collected occurrences

One round does not decrease the combined number of pending and collected occurrences.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.total_le_round`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#total-le-round).

## Pending plus collected occurrences are bounded by the frontier length

With a terminal frontier, pending and collected occurrences together never exceed
its length, including before traversal is complete.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.total_le_leaves`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#total-le-leaves).

## Stack invariants hold for every collected leaf

A property of every state ever on the stack holds of each collected leaf.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.out_of_stack`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#out-of-stack).

## Deepening the cut past a terminal frontier changes nothing

Increasing a depth cut beyond a terminal frontier leaves the list unchanged.

Formalized by `Cslib.Algorithms.Lean.BinaryBranching.leaves_eq_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/BinaryBranching.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html#leaves-eq-of-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Traversal of implicit binary trees](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/traversal-of-implicit-binary-trees)
