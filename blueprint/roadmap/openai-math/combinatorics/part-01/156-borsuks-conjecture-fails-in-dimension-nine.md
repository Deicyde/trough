---
declaration: section
origin: cited
lean: OAI.BorsukNine.main_theorem
statement: formalized
proof: formalized
---

# 156. Borsuk's conjecture fails in dimension nine

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a compact subset of ℝ$^{9}$ that cannot be covered by ten sets of strictly smaller diameter, disproving Borsuk's covering assertion already in dimension nine. The example consists of rank-one orthogonal projectors onto lines in ℝ$^{4}$, with the Frobenius metric.

## A nine-dimensional counterexample to Borsuk's covering assertion

The compact set of rank-one orthogonal projectors on ℝ$^{4}$, with the Frobenius metric, cannot be covered by ten sets of strictly smaller diameter. It therefore gives a counterexample to Borsuk's conjecture in dimension nine.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Borsuk's conjecture predicts that every bounded subset of $\mathbb R^d$ can be covered by $d+1$ sets of strictly smaller diameter. The formalized counterexample is the compact set of rank-one orthogonal projectors onto lines in $\mathbb R^4$, with the Frobenius metric. It lies in the nine-dimensional affine space of trace-one symmetric matrices, has diameter $\sqrt2$, and cannot be covered by ten arbitrary sets of smaller diameter.

## Lean: Nine-dimensional Borsuk counterexample

```lean
theorem main_theorem :
    IsCompact projectorSet ∧
    projectorSet ⊆ traceOneSymmetric ∧
    Metric.diam projectorSet = Real.sqrt 2 ∧
    ¬ HasTenSmallCover
```

Stated in [BorsukNine.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BorsukNine.lean#L25). Proved in [lean/OAI/Geometry/Borsuk/Counterexample.lean, line 49](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/Borsuk/Counterexample.lean#L49). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/156.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/156.md)
