---
declaration: section
origin: cited
lean: OAI.Barnette.main
statement: formalized
proof: formalized
---

# 180. Barnette’s Hamiltonian-cycle conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that every finite simple cubic bipartite planar 3-vertex-connected graph has a Hamiltonian cycle, resolving Barnette's conjecture. Equivalently, every three-edge path in a finite simple cubic 3-vertex-connected bipartite Pfaffian graph lies in a Hamiltonian cycle.

## Paired states and Hamiltonian cycles in cubic bipartite planar graphs

We prove Barnette's conjecture: every finite simple cubic bipartite planar 3-vertex-connected graph has a Hamiltonian cycle.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Barnette's conjecture states that every finite simple cubic bipartite planar graph that is 3-vertex-connected has a Hamiltonian cycle. The formalization proves this statement for every such graph. The selected result is the existence of a cycle visiting every vertex exactly once.

## Lean: Barnette's Hamiltonian-cycle conjecture

Stated in [BarnetteHamiltonian.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BarnetteHamiltonian.lean).

```lean
theorem main : MainStatement.{u}
```

Proved in [lean/OAI/Combinatorics/Hamiltonian/Main.lean, line 47](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Hamiltonian/Main.lean#L47).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/180.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/180.md)
