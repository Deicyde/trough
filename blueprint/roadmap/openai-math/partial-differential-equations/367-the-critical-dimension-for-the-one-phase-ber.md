---
declaration: section
origin: cited
lean: OAI.Bernoulli.nonflat_in_seven
statement: formalized
proof: formalized
---

# 367. The critical dimension for the one-phase Bernoulli problem

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Establishes seven as the first dimension admitting a nonflat, one-homogeneous global minimizer of the one-phase Bernoulli energy. Consequently, minimizing free boundaries are smooth through dimension six, and their singular sets have dimension at most $n-7$ in higher dimensions.

## The critical dimension for one-phase Bernoulli minimizers

We prove that seven is the critical dimension for the one-phase Bernoulli problem: every nonzero one-homogeneous global minimizer in dimensions at most six is flat, while a nonflat one-homogeneous global minimizer exists in dimension seven. It follows that the interior free boundary of a local minimizer is smooth in dimensions at most six. In dimension *n* ≥ 7, its singular set has Hausdorff dimension at most $n-7$, and this bound is sharp. In dimension seven, the singular set is locally finite.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The paper identifies seven as the critical dimension for nonflat one-homogeneous global minimizers of the one-phase Bernoulli problem. The linked formalization proves the existence side: in dimension seven there is a nonzero one-homogeneous global minimizer that is not a half-space solution.

The flatness classification in dimensions at most six and the resulting regularity and singular-set bounds are outside this selected statement.

## Lean: A nonflat one-homogeneous Bernoulli minimizer in dimension seven

```lean
theorem nonflat_in_seven : ∃ u : Space 7 → ℝ,
    GlobalMinimizer u ∧ Nonzero u ∧ OneHomogeneous u ∧ ¬ Flat u
```

Stated in [BernoulliNonflatInSeven.lean, line 78](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BernoulliNonflatInSeven.lean#L78). Proved in [lean/OAI/Analysis/BernoulliCone/Main.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/BernoulliCone/Main.lean#L10).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/367.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/367.md)
