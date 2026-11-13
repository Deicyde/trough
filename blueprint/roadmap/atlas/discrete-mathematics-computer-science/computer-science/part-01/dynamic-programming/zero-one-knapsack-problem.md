---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.Knapsack.Item, Cslib.Algorithms.Lean.TimeM.Knapsack.Result, Cslib.Algorithms.Lean.TimeM.Knapsack.totalWeight, Cslib.Algorithms.Lean.TimeM.Knapsack.totalValue, Cslib.Algorithms.Lean.TimeM.Knapsack.Feasible, Cslib.Algorithms.Lean.TimeM.Knapsack.solve, Cslib.Algorithms.Lean.TimeM.Knapsack.solve_correct, Cslib.Algorithms.Lean.TimeM.Knapsack.solve_time
statement: formalized
proof: formalized
---

# Zero-one knapsack problem

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html).

## Knapsack item

A zero-one knapsack item consists of a weight $w \in \mathbb{N}$ and a value
$v \in \mathbb{N}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.Knapsack.Item`, a structure declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html#item).

## Knapsack result

For a list of $n$ knapsack items, a knapsack result consists of a set
$S \subseteq \{0, \dots, n - 1\}$ of item indices, the chosen items, and a natural number, the
reported total value.

Formalized by `Cslib.Algorithms.Lean.TimeM.Knapsack.Result`, a structure declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html#result).

## Total weight of a knapsack selection

For knapsack items $x_0, \dots, x_{n-1}$ with weights
$w_i$ and a set $S \subseteq \{0, \dots, n - 1\}$ of item indices, the total weight of $S$ is
$\sum_{i \in S} w_i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.Knapsack.totalWeight`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html#total-weight).

## Total value of a knapsack selection

For knapsack items $x_0, \dots, x_{n-1}$ with values
$v_i$ and a set $S \subseteq \{0, \dots, n - 1\}$ of item indices, the total value of $S$ is
$\sum_{i \in S} v_i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.Knapsack.totalValue`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html#total-value).

## Feasible knapsack selection

For knapsack items $x_0, \dots, x_{n-1}$ with weights $w_i$
and a capacity $W \in \mathbb{N}$, a set $S \subseteq \{0, \dots, n - 1\}$ of item indices is
feasible when its total weight $\sum_{i \in S} w_i$ is at most $W$.

Formalized by `Cslib.Algorithms.Lean.TimeM.Knapsack.Feasible`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html#feasible).

## Bottom-up zero-one knapsack algorithm

Given knapsack items $x_0, \dots, x_{n-1}$ with
weights $w_i$ and values $v_i$ and a capacity $W \in \mathbb{N}$, the algorithm fills a table
$V(i, c)$ for $0 \le i \le n$ and $0 \le c \le W$ by $V(0, c) = 0$ and, for $i < n$,
$V(i + 1, c) = \max(V(i, c), V(i, c - w_i) + v_i)$ if $w_i \le c$ and $V(i + 1, c) = V(i, c)$
otherwise. Starting from $c = W$, it then inspects the rows $i = n, n - 1, \dots, 1$: if
$V(i, c) = V(i - 1, c)$ it skips item $i - 1$, and otherwise it selects index $i - 1$ and
replaces $c$ by $c - w_{i-1}$. It returns the selected index set together with the value
$V(n, W)$. Each of the $n(W + 1)$ cells of rows $1, \dots, n$ costs one tick, and each of the
$n$ inspected rows costs one tick.

Formalized by `Cslib.Algorithms.Lean.TimeM.Knapsack.solve`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html#solve).

## Correctness of the zero-one knapsack algorithm

For every list of knapsack items and every
capacity $W \in \mathbb{N}$, let $S$ and $v$ be the index set and the reported value returned by
the bottom-up knapsack algorithm. Then $S$ is feasible for $W$, $v$ is the total value of $S$,
and every feasible set $T$ of item indices has total value at most $v$.

Formalized by `Cslib.Algorithms.Lean.TimeM.Knapsack.solve_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html#solve-correct).

## Exact cost of the knapsack algorithm

For every list of $n$ knapsack items and every
capacity $W \in \mathbb{N}$, the bottom-up knapsack algorithm costs exactly $n(W + 1) + n$ ticks:
one for each of the $n(W + 1)$ table cells it computes and one for each of the $n$ item rows it
inspects during reconstruction.

Formalized by `Cslib.Algorithms.Lean.TimeM.Knapsack.solve_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html#solve-time).

## Pseudo-polynomial cost bound for knapsack

For every list of $n$ knapsack items and every
capacity $W \in \mathbb{N}$ with $W \ge 1$, the bottom-up knapsack algorithm costs at most $3nW$
ticks.

Formalized by `Cslib.Algorithms.Lean.TimeM.Knapsack.solve_time_le_three_mul`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/Knapsack.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html#solve-time-le-three-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zero-one knapsack problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/dynamic-programming/zero-one-knapsack-problem)
