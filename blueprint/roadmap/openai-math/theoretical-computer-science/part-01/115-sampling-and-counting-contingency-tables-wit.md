---
declaration: section
origin: cited
lean: OAI.ContingencyTables.boundedSampling, OAI.ContingencyTables.exactSampling, OAI.ContingencyTables.counting
statement: formalized
proof: formalized
---

# 115. Sampling and counting contingency tables with arbitrary margins

2 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For nonnegative integer matrices with prescribed row and column sums, gives exact uniform sampling in expected polynomial bit time and almost-uniform sampling in worst-case polynomial bit time. The dimensions and binary-encoded margins are unrestricted. Also gives a fully polynomial randomized approximation scheme for counting such tables with arbitrary individual cell bounds, including structural zeros, with polynomial cost on every execution.

## Exact Uniform Sampling of Contingency Tables with Arbitrary Margins

We give an exact uniform sampler for nonnegative integer contingency tables with arbitrary prescribed margins. It terminates almost surely and has expected bit complexity polynomial in both dimensions and the binary length of the margins. No positivity, balance, sparsity, or fixed-dimension assumption is required.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/main.pdf); the Lean below formalizes results from it.

## An FPRAS for Cell-Bounded Contingency Tables

We give a fully polynomial randomized approximation scheme for counting nonnegative integer matrices with prescribed row sums, column sums, and individual entry bounds. Both dimensions vary, all numerical data are encoded in binary, and zero bounds are allowed. The algorithm uses only unbiased random bits and has a polynomial bound on its bit operations on every execution.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives an exact uniform sampler for nonnegative integer contingency tables with arbitrary prescribed row and column sums having equal totals. It terminates almost surely, every halted output is feasible, and each table has exactly the uniform limiting probability. Expected bit complexity is polynomial in the dimensions and the binary length of the margins.

It also gives a sampler with a fixed polynomial time bound on every execution whose total-variation error is at most $2^{-k}$ for requested precision $k\ge1$. The same Comparator file includes the companion approximation scheme for counting tables with individual cell bounds.

The formalization gives a fully polynomial randomized approximation scheme for counting nonnegative integer matrices with prescribed row sums, column sums, and individual entry bounds. Both dimensions may vary, the margins and bounds are binary encoded, and zero entry bounds are allowed. For rational $0<\varepsilon,\delta<1$, the algorithm returns a nonnegative estimate with relative error at most $\varepsilon$ with probability at least $1-\delta$, and returns zero on every execution when no table exists.

The running time is polynomial in the encoded input size, $\varepsilon^{-1}$, and $\log(\delta^{-1})$ on every random tape. The same Comparator file also contains the companion sampling results for tables without cell bounds.

## Lean: Exact and bounded-time sampling of contingency tables

```lean
theorem boundedSampling : Algorithms.BoundedSamplingStatement
```

Stated in [ContingencyTables.lean, line 211](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContingencyTables.lean#L211). Proved in [lean/OAI/Combinatorics/ContingencyTables/UnconditionalMain.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/ContingencyTables/UnconditionalMain.lean#L19).

```lean
theorem exactSampling : Algorithms.ExactSamplingStatement
```

Stated in [ContingencyTables.lean, line 214](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContingencyTables.lean#L214). Proved in [lean/OAI/Combinatorics/ContingencyTables/UnconditionalMain.lean, line 24](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/ContingencyTables/UnconditionalMain.lean#L24).

```lean
theorem counting : Algorithms.CountingStatement
```

Stated in [ContingencyTables.lean, line 217](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContingencyTables.lean#L217). Proved in [lean/OAI/Combinatorics/ContingencyTables/UnconditionalMain.lean, line 29](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/ContingencyTables/UnconditionalMain.lean#L29).

## Lean: Randomized approximate counting of cell-bounded contingency tables

States the `OAI.ContingencyTables.boundedSampling` quoted above. Stated in [ContingencyTables.lean, line 211](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContingencyTables.lean#L211).

States the `OAI.ContingencyTables.exactSampling` quoted above. Stated in [ContingencyTables.lean, line 214](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContingencyTables.lean#L214).

States the `OAI.ContingencyTables.counting` quoted above. Stated in [ContingencyTables.lean, line 217](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContingencyTables.lean#L217).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/115.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/115.md)
