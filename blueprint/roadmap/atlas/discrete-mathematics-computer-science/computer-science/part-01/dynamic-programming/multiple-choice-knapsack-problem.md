---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.MultipleChoiceKnapsack.Item, Cslib.Algorithms.Lean.MultipleChoiceKnapsack.IsSelection, Cslib.Algorithms.Lean.MultipleChoiceKnapsack.totalWeight, Cslib.Algorithms.Lean.MultipleChoiceKnapsack.totalValue, Cslib.Algorithms.Lean.MultipleChoiceKnapsack.bestPacking, Cslib.Algorithms.Lean.MultipleChoiceKnapsack.bestCovering, Cslib.Algorithms.Lean.MultipleChoiceKnapsack.le_bestPacking, Cslib.Algorithms.Lean.MultipleChoiceKnapsack.exists_eq_of_bestPacking_eq_coe
statement: formalized
proof: formalized
---

# Multiple-choice knapsack problem

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html).

## Knapsack item with weight and value

A knapsack item with a natural weight and a value in `β`.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.Item`, a structure declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#item).

## Multiple-choice knapsack selection

A selection chooses exactly one item from each group, in group order.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.IsSelection`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#is-selection).

## Total weight of a knapsack selection

The total weight of a selection.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.totalWeight`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#total-weight).

## Total value of a knapsack selection

The total value of a selection.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.totalValue`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#total-value).

## Packing recurrence for multiple-choice knapsack

The packing recurrence: the best total value of a selection with total weight at most `c`,
`⊥` if none exists.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.bestPacking`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#best-packing).

## Covering recurrence for multiple-choice knapsack

The covering recurrence: the best total value of a selection with total weight at least
`L`, `⊥` if none exists. The residual target `L - weight` is truncated subtraction.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.bestCovering`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#best-covering).

## Packing recurrence bounds every feasible selection's value

The packing recurrence is an upper bound: every feasible selection's value is at most
`bestPacking`.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.le_bestPacking`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#le-best-packing).

## Packing recurrence is attained by a feasible selection

The packing recurrence is attained: a finite value is the value of a feasible selection.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.exists_eq_of_bestPacking_eq_coe`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#exists-eq-of-best-packing-eq-coe).

## Packing recurrence is bottom iff no selection fits the capacity

The packing recurrence is `⊥` exactly when no selection fits the capacity.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.bestPacking_eq_bot_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#best-packing-eq-bot-iff).

## Covering recurrence bounds every covering selection's value

The covering recurrence is an upper bound: every selection of total weight at least `L` has
value at most `bestCovering`.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.le_bestCovering`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#le-best-covering).

## Covering recurrence is attained by a covering selection

The covering recurrence is attained: a finite value is the value of a selection of total
weight at least `L`.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.exists_eq_of_bestCovering_eq_coe`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#exists-eq-of-best-covering-eq-coe).

## Covering recurrence is bottom iff no selection reaches the target

The covering recurrence is `⊥` exactly when no selection reaches the target.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.bestCovering_eq_bot_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#best-covering-eq-bot-iff).

## Bottom-up packing table for multiple-choice knapsack

The bottom-up packing table: for each suffix of the groups, the row of best values at
capacities `0, …, capacity`, each row computed from the next one by one scan of its group per
cell.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.packingTable`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#packing-table).

## Packing table computes the packing recurrence

The table computes the recurrence at every capacity `0, …, capacity`.

Formalized by `Cslib.Algorithms.Lean.MultipleChoiceKnapsack.packingTable_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleChoiceKnapsack.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html#packing-table-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiple-choice knapsack problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/dynamic-programming/multiple-choice-knapsack-problem)
