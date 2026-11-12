---
declaration: section
origin: cited
lean: OAI.LargeIndependentSets.mainTheoremReal
statement: formalized
proof: formalized
---

# 106. Hardness of coloring three-colorable graphs

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

It is NP-hard to color a three-colorable graph using any fixed number *c* ≥ 3 of colors. More strongly, for every fixed $0\lt \delta\lt 1/3$, a deterministic polynomial-time reduction from 3SAT produces simple unweighted graphs that are three-colorable in the satisfiable case and have no independent set of size $\delta n$ otherwise, where *n* is the number of vertices.

## Hardness of finding large independent sets in three-colorable graphs

We prove that, for every fixed $0\lt \delta\lt 1/3$, it is NP-hard to distinguish three-colorable graphs from graphs in which every independent set has fewer than *δ* times the number of vertices. Consequently, for every fixed integer *c* ≥ 3, finding a proper *c*-coloring of a three-colorable graph is NP-hard.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result shows hardness of finding large independent sets even under a three-colorability promise. For every fixed $0<\delta<1/3$, a deterministic polynomial-time reduction maps binary 3SAT formulas to nonempty finite simple graphs. Satisfiable formulas produce three-colorable graphs; unsatisfiable formulas produce graphs whose largest independent set has fewer than $\delta$ times the number of vertices. The complete adjacency-matrix output is included in the runtime bound.

## Lean: Independent-set hardness in three-colorable graphs

Stated in [IndependentSets.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IndependentSets.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem mainTheoremReal :
    ∀ δ : ℝ, 0 < δ → δ < 1 / 3 → Nonempty (RealGraphReduction δ)
```

Proved in [lean/OAI/Combinatorics/IndependentSets/Main.lean, line 124](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/IndependentSets/Main.lean#L124).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/106.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/106.md)
