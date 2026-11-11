---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosureStages, Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure, Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosureStages_zero_cell, Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosureStages_succ_cell, Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_initializations, Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_stage_assignments, Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_transition_assignments, Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosureStages_cell_eq_true_iff
statement: formalized
proof: formalized
---

# Transitive closure

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html).

## Staged transitive-closure computation

Let $A$ be a Boolean adjacency matrix on the
vertices $0, \dots, n-1$ and let $k \le n$. The computation first builds the $n \times n$ Boolean
matrix $T^{(0)}$ whose entry $(i, j)$ is true exactly when $i = j$ or $A_{ij}$ is true. Then, for
$p = 0, \dots, k - 1$, it builds a new matrix $T^{(p+1)}$ from the saved matrix $T^{(p)}$ by
$T^{(p+1)}_{ij} = T^{(p)}_{ij} \lor (T^{(p)}_{ip} \land T^{(p)}_{pj})$, and it returns $T^{(k)}$.
One time unit is charged for each cell assignment.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosureStages`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-stages).

## Saved-matrix transitive-closure algorithm

Given a Boolean adjacency matrix $A$ on the
vertices $0, 1, \dots, n-1$, the algorithm first builds the matrix $t^{(0)}$ with $t^{(0)}_{ij}$
true exactly when $i = j$ or $A_{ij}$ is true. Then, for $k = 0, 1, \dots, n-1$ in turn, it
builds a new matrix $t^{(k+1)}$ with
$t^{(k+1)}_{ij} = t^{(k)}_{ij} \lor (t^{(k)}_{ik} \land t^{(k)}_{kj})$ for all $i, j$, reading
every operand from the saved matrix $t^{(k)}$, and it returns $t^{(n)}$. One time unit is
charged for each cell assignment; reads, Boolean operations and matrix allocation are free.

This is the saved-matrix recurrence of CLRS for the reflexive transitive closure.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure).

## Initial matrix of the transitive-closure computation

Let $A$ be a Boolean adjacency
matrix on the vertices $0, \dots, n-1$. For all vertices $i$ and $j$, the entry $(i, j)$ of the
matrix produced by the staged transitive-closure computation with no pivot stages is true if and
only if $i = j$ or $A_{ij}$ is true.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosureStages_zero_cell`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-stages-zero-cell).

## Transition recurrence of the transitive-closure stages

Let $A$ be a Boolean adjacency
matrix on the vertices $0, \dots, n-1$, and for $m \le n$ let $T^{(m)}$ be the matrix produced by
the staged transitive-closure computation on $A$ after its first $m$ pivot stages. For every
$k < n$ and all vertices $i$ and $j$,

$$T^{(k+1)}_{ij} = T^{(k)}_{ij} \lor \bigl(T^{(k)}_{ik} \land T^{(k)}_{kj}\bigr).$$

Every operand of stage $k + 1$ is read from the complete matrix saved after stage $k$.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosureStages_succ_cell`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-stages-succ-cell).

## Cost of initializing the transitive-closure matrix

For every Boolean adjacency matrix on
$n$ vertices, the staged transitive-closure computation with no pivot stages (only the
initialization of the $n \times n$ matrix) charges exactly $n^2$ time units, one for each cell
assignment.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_initializations`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-initializations).

## Cost of one transition stage

For every Boolean adjacency matrix on $n$ vertices and every
$k < n$, the time charged by the staged transitive-closure computation with $k + 1$ pivot stages
minus the time charged with $k$ pivot stages equals $n^2$: one time unit for each cell assignment
of the new stage.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_stage_assignments`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-stage-assignments).

## Cost of the transition stages of transitive closure

Charge one time unit for each cell
assignment. For every Boolean adjacency matrix on $n$ vertices, let $a$ be the cost of running the
initialization of the saved-matrix transitive-closure algorithm followed by all $n$ of its
stages, and let $b$ be the cost of running the initialization alone. Then $a - b = n^3$, where the
subtraction is subtraction of natural numbers, truncated at $0$. That is, the $n$ transition
stages together perform exactly $n^3$ cell assignments.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_transition_assignments`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-transition-assignment).

## Invariant of the transitive-closure stages

Let $A$ be a Boolean adjacency matrix of a
directed graph on the vertices $0, \dots, n-1$ and let $k \le n$. For all vertices $i$ and $j$, the
entry $(i, j)$ of the matrix produced by the staged transitive-closure computation after its first
$k$ pivot stages is true if and only if there are vertices $i = v_0, v_1, \dots, v_m = j$ with
$m \ge 0$ such that each $A_{v_t v_{t+1}}$ is true and every intermediate vertex
$v_1, \dots, v_{m-1}$ is less than $k$.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosureStages_cell_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-stages-cell-eq-true-i).

## Correctness of the transitive-closure algorithm

Let $A$ be a Boolean adjacency matrix
of a directed graph on the vertices $0, \dots, n-1$. For all vertices $i$ and $j$, the entry
$(i, j)$ of the matrix returned by the transitive-closure algorithm on $A$ is true if and only if
$j$ is reachable from $i$ by a sequence of zero or more edges of the graph.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_cell_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-cell-eq-true-iff).

## Running time of the transitive-closure algorithm

For every Boolean adjacency matrix on
$n$ vertices, the transitive-closure algorithm charges exactly $n^2 + n^3$ time units: $n^2$ cell
assignments to initialize the matrix and $n^2$ in each of the $n$ transition stages.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 538](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L538). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-time).

## Cost of transitive closure on the empty graph

For the graph with no vertices, the
transitive-closure algorithm charges $0$ time units: it performs no cell assignments.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_time_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-time-zero).

## Cost of transitive closure on one vertex

For every Boolean adjacency matrix on a single
vertex, the transitive-closure algorithm charges exactly $2$ time units: one cell assignment for
the initialization and one for the single transition stage.

Formalized by `Cslib.Algorithms.Lean.TransitiveClosure.transitiveClosure_time_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TransitiveClosure.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html#transitive-closure-time-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transitive closure](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/transitive-closure)
