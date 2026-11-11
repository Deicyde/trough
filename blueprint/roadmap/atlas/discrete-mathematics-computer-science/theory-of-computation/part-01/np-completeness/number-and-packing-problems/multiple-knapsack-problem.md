---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MultipleKnapsack.MultipleKnapsackInstance, MetaMathlibExt.Complexity.NPComplete.MultipleKnapsack.MultipleKnapsackFeasible, MetaMathlibExt.Complexity.NPComplete.MultipleKnapsack.multipleKnapsackDec, MetaMathlibExt.Complexity.NPComplete.MultipleKnapsack.multipleKnapsack_npComplete
statement: formalized
---

# Multiple knapsack problem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiple-knapsack-problem/index.html).

## Multiple-knapsack instances

A multiple-knapsack instance consists of a finite list of
items, each a pair $(w, v)$ of natural numbers giving its weight $w$ and value $v$, a finite list
of natural-number knapsack capacities, and a natural-number target value.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultipleKnapsack.MultipleKnapsackInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MultipleKnapsackWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MultipleKnapsackWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiple-knapsack-problem/index.html#multiple-knapsack-instance).

## Feasible multiple-knapsack instances

Let a multiple-knapsack instance have items
$(w_0, v_0), \dots, (w_{k-1}, v_{k-1})$ (weight, value), knapsack capacities
$c_0, \dots, c_{m-1}$ and target $V$. The instance is feasible when there are
$a_0, \dots, a_{k-1} \in \{0, \dots, m\}$, where $a_j = b < m$ puts item $j$ in knapsack $b$
and $a_j = m$ leaves item $j$ out, such that for every $b < m$ the total weight
$\sum_{j : a_j = b} w_j$ is at most $c_b$, and the total value $\sum_{j : a_j < m} v_j$ is at
least $V$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultipleKnapsack.MultipleKnapsackFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MultipleKnapsackWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MultipleKnapsackWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiple-knapsack-problem/index.html#multiple-knapsack-feasible).

## MULTIPLE KNAPSACK as a decision problem

The decision problem MULTIPLE KNAPSACK accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a feasible
multiple-knapsack instance. Bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultipleKnapsack.multipleKnapsackDec`, a definition declared in [WantedExt/Complexity/NPComplete/MultipleKnapsackWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MultipleKnapsackWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiple-knapsack-problem/index.html#multiple-knapsack-dec).

## MULTIPLE KNAPSACK is NP-complete

The decision problem MULTIPLE KNAPSACK belongs to NP,
and every decision problem in NP has a polynomial-time many-one reduction to MULTIPLE KNAPSACK.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MULTIPLE KNAPSACK.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MultipleKnapsack.multipleKnapsack_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MultipleKnapsackWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MultipleKnapsackWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiple-knapsack-problem/index.html#multiple-knapsack-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiple knapsack problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiple-knapsack-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiple-knapsack-problem)
