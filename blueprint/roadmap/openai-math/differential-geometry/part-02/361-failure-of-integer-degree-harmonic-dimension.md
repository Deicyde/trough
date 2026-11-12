---
declaration: section
origin: cited
lean: OAI.HarmonicCounterexample.main
statement: formalized
proof: formalized
---

# 361. Failure of integer-degree harmonic dimension comparison

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves Yau's proposed Euclidean dimension bound for harmonic functions of integer growth on manifolds with nonnegative Ricci curvature. For every sufficiently large integer *k*, a complete smooth metric on ℝ$^{3}$ has at least $(k+2)^2$ independent harmonic functions of growth at most *k*, exceeding the Euclidean count $(k+1)^2$. The metric may depend on *k*.

## A counterexample to integer-degree harmonic dimension comparison

For some even *n* ≥ 8 and integer *k* ≥ 2, we construct a complete smooth metric on ℝ$^{n}$ with nonnegative Ricci curvature whose space of real harmonic functions of pointwise polynomial growth at most *k* has dimension larger than the Euclidean harmonic-polynomial dimension. The metric is Euclidean near the origin, has asymptotic volume ratio strictly between zero and one, and has nonunique tangent cones at infinity. This answers the integer-degree form of Yau's dimension comparison question in the negative.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## A Three-Dimensional Counterexample to Integer-Degree Harmonic Dimension Comparison

For every $4/9\lt v\lt 1$ and $1\lt c\lt 9v/4$, all sufficiently large integers *k* admit a complete smooth metric on ℝ$^{3}$ with nonnegative Ricci curvature, asymptotic volume ratio *v*, and at least $c(k+1)^2$ linearly independent real harmonic functions of pointwise growth at most *k*. This answers Yau's integer-degree dimension comparison question negatively in dimension three, with a fixed-factor excess over the Euclidean count. For each $1\lt c\lt 9/4$, these metrics can be chosen arbitrarily close to the Euclidean metric in global bi-Lipschitz distance. The metric may depend on *k*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/paper.pdf).

## The Lean formalization

The formalized result disproves the proposed Euclidean upper comparison for dimensions of harmonic functions with integer polynomial growth. It constructs one complete smooth metric with nonnegative Ricci curvature on an even-dimensional Euclidean space, Euclidean near the origin and with asymptotic volume ratio strictly between zero and one, admitting more independent harmonic functions of the prescribed growth degree than the Euclidean count. The construction uses dimension $16$ and degree $50000$. Separate tangent-cone and cone-spectrum conclusions are not included.

## Lean: Counterexample to harmonic dimension comparison

Stated in [HarmonicGrowth.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HarmonicGrowth.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main : MainClaim
```

Proved in [lean/OAI/Geometry/HarmonicGrowth/Main.lean, line 475](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/HarmonicGrowth/Main.lean#L475).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/361.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/361.md)
