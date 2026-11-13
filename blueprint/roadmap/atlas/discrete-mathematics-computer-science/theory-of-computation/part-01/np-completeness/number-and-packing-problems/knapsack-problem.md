---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.Knapsack.KnapsackInstance, MetaMathlibExt.Complexity.NPComplete.Knapsack.KnapsackFeasible, MetaMathlibExt.Complexity.NPComplete.Knapsack.knapsackDec, MetaMathlibExt.Complexity.NPComplete.Knapsack.knapsack_npComplete
statement: formalized
---

# Knapsack problem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/knapsack-problem/index.html).

## Knapsack instances

A 0/1 knapsack instance is a triple $(I, C, T)$ of a list $I$ of items,
each a pair $(w, v)$ of natural numbers giving its weight $w$ and value $v$, a natural-number
capacity $C$, and a natural-number target value $T$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Knapsack.KnapsackInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/KnapsackWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/KnapsackWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/knapsack-problem/index.html#knapsack-instance).

## Feasible knapsack instances

A knapsack instance $(I, C, T)$, with item list $I$, capacity
$C$ and target value $T$, is feasible when some subsequence of $I$, possibly empty, has total
weight at most $C$ and total value at least $T$. Repeated items in $I$ are distinct occurrences
that can be selected separately.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Knapsack.KnapsackFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/KnapsackWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/KnapsackWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/knapsack-problem/index.html#knapsack-feasible).

## The KNAPSACK decision problem

KNAPSACK is the decision problem that accepts a bitstring
$x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a knapsack instance
$(I, C, T)$ for which some subsequence of the item list $I$, possibly empty, has total weight at
most $C$ and total value at least $T$. Bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Knapsack.knapsackDec`, a definition declared in [WantedExt/Complexity/NPComplete/KnapsackWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/KnapsackWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/knapsack-problem/index.html#knapsack-dec).

## KNAPSACK is NP-complete

The KNAPSACK decision problem is in NP, and every decision
problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), KNAPSACK (MP9).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.Knapsack.knapsack_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/KnapsackWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/KnapsackWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/knapsack-problem/index.html#knapsack-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Knapsack problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/knapsack-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/knapsack-problem)
