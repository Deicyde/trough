---
declaration: section
origin: cited
lean: OAI.common_bases_fpras
statement: formalized
proof: formalized
---

# 114. Approximate counting of common integer polymatroid bases

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives a fully polynomial randomized approximation scheme for counting common integer bases of two integral polymatroids of equal total rank, supplied by exact rank-value oracles. Capacities are binary-encoded, each integer vector counts once, and oracle calls and bit operations outside the oracles are polynomial on every execution. For matroids presented by independence oracles, the results also cover common independent sets of prescribed, unrestricted, or maximum cardinality, even when the ranks differ.

## An FPRAS for Common Integer Polymatroid Bases with Binary Capacities

We give a fully polynomial randomized approximation scheme for counting common integer bases of two polymatroids with the same total rank, supplied by exact rank-value oracles. The total rank and capacities are encoded in binary, and each integer vector is counted once. On every execution, the number of oracle calls and the bit work outside the oracles are bounded by a fixed polynomial in the ground-set size, the binary input length, the inverse relative-error tolerance, and the logarithm of the inverse failure probability. The algorithm handles binary capacities directly, without expanding them into labelled copies.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf).

## Approximate counting of common bases of two matroids

We give a fully polynomial randomized approximation scheme for counting the common bases of two arbitrary matroids of the same rank, supplied by independence oracles. The algorithm requires no explicit representation of either matroid and has polynomial bounds on both oracle calls and bit operations on every execution.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result gives a fully polynomial randomized approximation scheme for the number of common bases of two equal-rank matroids on an enumerated finite ground set, using independence oracles. For rational $0<\varepsilon,\delta<1$, the nonnegative rational output has relative error at most $\varepsilon$ with probability at least $1-\delta$. A zero count produces zero on every execution. Oracle calls and bit operations have polynomial bounds on every random tape in the input size, $\varepsilon^{-1}$, and $\log(\delta^{-1})$.

## Lean: FPRAS for common matroid bases

Stated in [CommonBasesFPRAS.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CommonBasesFPRAS.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem common_bases_fpras : CommonBasesFPRAS.MainTheorem
```

Proved in [lean/OAI/Combinatorics/MatroidCounting/CommonBases.lean, line 26093](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/MatroidCounting/CommonBases.lean#L26093).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/114.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/114.md)
