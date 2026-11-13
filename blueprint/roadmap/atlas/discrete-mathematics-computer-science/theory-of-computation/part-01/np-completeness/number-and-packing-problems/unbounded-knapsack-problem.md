---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.UnboundedKnapsack.UnboundedKnapsackInstance, MetaMathlibExt.Complexity.NPComplete.UnboundedKnapsack.UnboundedKnapsackFeasible, MetaMathlibExt.Complexity.NPComplete.UnboundedKnapsack.unboundedKnapsackDec, MetaMathlibExt.Complexity.NPComplete.UnboundedKnapsack.unboundedKnapsack_npComplete
statement: formalized
---

# Unbounded knapsack problem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/unbounded-knapsack-problem/index.html).

## Unbounded knapsack instances

An instance of the unbounded knapsack problem is a triple
$(I, C, K)$ of a finite list $I = ((s_1, v_1), \dots, (s_m, v_m))$ of items, where item $j$ has
weight $s_j \in \mathbb{N}$ and value $v_j \in \mathbb{N}$, a capacity $C \in \mathbb{N}$ and a
target value $K \in \mathbb{N}$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.UnboundedKnapsack.UnboundedKnapsackInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/UnboundedKnapsackWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/UnboundedKnapsackWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/unbounded-knapsack-problem/index.html#unbounded-knapsack-instance).

## Feasible unbounded knapsack instances

An unbounded knapsack instance with items
$(s_1, v_1), \dots, (s_m, v_m)$, capacity $C$ and target value $K$ is feasible when there are
multiplicities $c_1, \dots, c_m \in \mathbb{N}$ with $\sum_{j=1}^{m} c_j s_j \le C$ and
$\sum_{j=1}^{m} c_j v_j \ge K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.UnboundedKnapsack.UnboundedKnapsackFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/UnboundedKnapsackWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/UnboundedKnapsackWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/unbounded-knapsack-problem/index.html#unbounded-knapsack-feasible).

## Unbounded knapsack as a decision problem

The unbounded knapsack problem is the decision
problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding of unbounded knapsack instances, to a feasible instance. Bitstrings that fail to decode
are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.UnboundedKnapsack.unboundedKnapsackDec`, a definition declared in [WantedExt/Complexity/NPComplete/UnboundedKnapsackWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/UnboundedKnapsackWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/unbounded-knapsack-problem/index.html#unbounded-knapsack-dec).

## UNBOUNDED KNAPSACK is NP-complete

The unbounded knapsack decision problem belongs to NP,
and every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), UNBOUNDED KNAPSACK.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.UnboundedKnapsack.unboundedKnapsack_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/UnboundedKnapsackWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/UnboundedKnapsackWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/unbounded-knapsack-problem/index.html#unbounded-knapsack-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unbounded knapsack problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/unbounded-knapsack-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/unbounded-knapsack-problem)
