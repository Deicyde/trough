---
declaration: section
origin: cited
lean: OAI.CoboundaryExpanders.main
statement: formalized
proof: formalized
---

# 177. Bounded-degree coboundary expanders

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs arbitrarily large finite *d*-dimensional simplicial complexes, for every *d* ≥ 3, with uniformly bounded vertex degrees and uniform 𝔽$_{2}$ coboundary expansion in every degree below *d*. Together with the known graph and two-dimensional cases, this establishes the existence of such expanders in every positive dimension.

## Bounded-degree coboundary expanders in every dimension

For every integer *d* ≥ 3, we construct arbitrarily large finite *d*-dimensional simplicial complexes with uniformly bounded vertex degrees and uniform 𝔽$_{2}$ coboundary expansion in every degree below *d*. Together with the known graph and two-dimensional cases, this establishes the existence of bounded-degree 𝔽$_{2}$ coboundary expanders in every positive dimension.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization constructs bounded-degree $\mathbb F_2$ coboundary expanders in every dimension $d\ge3$. For each such $d$, it gives finite pure connected $d$-dimensional simplicial complexes with vertex counts tending to infinity, one uniform bound on top-dimensional degree at each vertex, and one positive coboundary-expansion constant in every degree below $d$. The constants may depend on $d$. The graph and two-dimensional cases used for the paper's all-positive-dimensions conclusion are separate.

## Lean: Bounded-degree coboundary expanders in dimensions at least three

```lean
theorem main : MainStatement
```

Stated in [CoboundaryExpanders.lean, line 91](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CoboundaryExpanders.lean#L91). Proved in [lean/OAI/Combinatorics/Coboundary/Main.lean, line 88](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Coboundary/Main.lean#L88).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/177.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/177.md)
