---
declaration: section
origin: cited
lean: OAI.SeymourSecondNeighborhood.exists_goodVertex
statement: formalized
proof: formalized
---

# 173. Seymour’s second-neighborhood conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Seymour's second-neighborhood conjecture: every nonempty finite oriented graph has a vertex with at least as many vertices at directed distance exactly two as at directed distance one. Oriented graphs may be arbitrary apart from the exclusion of loops and oppositely directed edge pairs.

## A proof of Seymour’s second-neighborhood conjecture

We prove that every nonempty finite oriented graph has a vertex with at least as many vertices at directed distance two as at directed distance one. This resolves Seymour's second neighborhood conjecture positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Seymour's second-neighborhood conjecture asserts that every nonempty finite oriented graph has a vertex with at least as many second out-neighbors as first out-neighbors. The formalized result proves this assertion, where the second neighborhood consists of vertices at directed distance exactly two. The initial vertex and first neighbors are excluded from that count, and sinks are included.

## Lean: Seymour's second-neighborhood conjecture

Stated in [SeymourSecondNeighborhood.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SeymourSecondNeighborhood.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem exists_goodVertex (r : V → V → Prop) (hr : IsOriented r) :
    ∃ v, GoodVertex r v
```

Proved in [lean/OAI/Combinatorics/SecondNeighborhood/Main.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/SecondNeighborhood/Main.lean#L11).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/173.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/173.md)
