---
declaration: section
origin: cited
lean: OAI.ErdosGallai.erdos_gallai
statement: formalized
proof: formalized
---

# 181. The Erdős–Gallai cycle-decomposition conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that the edges of every finite simple undirected graph on *n* vertices can be partitioned into at most $Cn$ simple cycles and single edges, for an absolute constant *C*. This resolves the Erdős–Gallai cycle-decomposition conjecture, bounding the number of pieces linearly even for dense graphs.

## A linear cycle-and-edge decomposition of every graph

We prove that every finite simple undirected graph on *n* vertices has an edge partition into at most $Cn$ simple cycles and single edges, for an absolute constant *C*. This resolves the Erdős–Gallai cycle decomposition conjecture positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Erdős–Gallai cycle-decomposition conjecture asks for a linear bound on the number of cycles and single edges needed to partition a graph's edges. The formalized result gives one absolute constant $C>0$ such that every finite simple graph on $n$ vertices has an edge-disjoint decomposition into at most $Cn$ cycles or singleton edges. Edgeless and small graphs are included. The optimal value of $C$ is not determined.

## Lean: Linear cycle-and-edge decomposition

Stated in [CycleDecomposition.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CycleDecomposition.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem erdos_gallai : MainStatement
```

Proved in [lean/OAI/Combinatorics/CycleDecomposition/Main.lean, line 207](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/CycleDecomposition/Main.lean#L207).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/181.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/181.md)
