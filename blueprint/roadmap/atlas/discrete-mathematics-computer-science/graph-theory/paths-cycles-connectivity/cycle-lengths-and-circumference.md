---
declaration: section
origin: cited
lean: SimpleGraph.cycleLengths, SimpleGraph.oddCycleLengths, SimpleGraph.Walk.IsLongestCycle
statement: formalized
proof: formalized
---

# Cycle lengths and circumference

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-lengths-and-circumference/index.html).

## Cycle lengths

For a simple graph $G$, the set of cycle lengths of $G$ is the set of
natural numbers $m$ such that $G$ contains a cycle of length $m$.

Formalized by `SimpleGraph.cycleLengths`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Circumference.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Circumference.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-lengths-and-circumference/index.html#cycle-lengths).

## Odd cycle lengths

For a simple graph $G$, the set of odd cycle lengths of $G$ is the set
of those cycle lengths of $G$ that are odd, that is, the odd natural numbers $m$ such that $G$
contains a cycle of length $m$.

Formalized by `SimpleGraph.oddCycleLengths`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Circumference.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Circumference.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-lengths-and-circumference/index.html#odd-cycle-lengths).

## Longest cycle in a graph

A cycle is globally longest if no cycle in the graph has more edges.

Formalized by `SimpleGraph.Walk.IsLongestCycle`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/LongestCycle.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/LongestCycle.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-lengths-and-circumference/index.html#is-longest-cycle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cycle lengths and circumference](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-lengths-and-circumference/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/cycle-lengths-and-circumference)
