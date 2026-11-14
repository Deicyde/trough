---
declaration: section
origin: cited
lean: OAI.ThresholdParallelRepetition.threshold_parallel_repetition
statement: formalized
proof: formalized
---

# 277. Threshold repetition for entangled games

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves exponential threshold repetition for every finite two-player one-round game: if its entangled value is *v* < 1, the probability of winning at least a fraction $v+\delta$ of *k* independent repetitions decays exponentially in *k*, for $0\lt \delta\lt 1-v$. Arbitrary joint finite-dimensional entangled strategies and correlated question distributions are allowed.

## Threshold parallel repetition for finite-dimensional entangled games

For every finite two-player game with entangled value *v* < 1, we prove exponential decay for the probability of winning at least a $v+\delta$ fraction of *k* independent repetitions, uniformly over all finite-dimensional joint strategies. The result allows arbitrary correlated question distributions and holds for every $0\lt \delta\lt 1-v$ and *k* ≥ 1. Its universal rate is proportional to $\delta^5/(1+\log(|\mathcal A||\mathcal B|))$, where $\mathcal A,\mathcal B$ are the answer alphabets. For each fixed question distribution, we also obtain an explicit cubic rate in *δ*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives exponential threshold parallel repetition for every finite two-player game with arbitrary correlated questions. If its finite-dimensional entangled value is $v<1$, its answer sets are $A,B$, and $0<\delta<1-v$, then the probability of winning at least the fraction $v+\delta$ of $k$ repetitions is at most $\exp(-\kappa\delta^{13}k/(1+\log(|A||B|)))$ for one universal $\kappa>0$. The bound applies to every joint finite-dimensional strategy and to their supremum, without assuming attainment. The separate distribution-dependent cubic bound is outside this scope.

## Lean: Threshold parallel repetition for entangled games

```lean
theorem threshold_parallel_repetition :
    ∃ κ₀ : ℝ, 0 < κ₀ ∧
      ∀ (x y a b : ℕ) (G : Game x y a b), entangledValue G < 1 →
      ∀ (δ : ℝ), 0 < δ → δ < 1 - entangledValue G →
      ∀ (k : ℕ), 1 ≤ k →
        (∀ S : RepeatedStrategy x y a b k,
          thresholdProbability G δ S ≤
            Real.exp (-κ₀ * δ ^ 13 / (1 + Real.log (((a + 1) * (b + 1) : ℕ) : ℝ)) * k)) ∧
        thresholdValue (k := k) G δ ≤
          Real.exp (-κ₀ * δ ^ 13 / (1 + Real.log (((a + 1) * (b + 1) : ℕ) : ℝ)) * k)
```

Stated in [EntangledGames.lean, line 64](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EntangledGames.lean#L64). Proved in [lean/OAI/Probability/EntangledGames/Main.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/EntangledGames/Main.lean#L9). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/277.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/277.md)
