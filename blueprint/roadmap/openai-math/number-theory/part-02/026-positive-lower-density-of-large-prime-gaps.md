---
declaration: section
origin: cited
lean: OAI.Problem344.large_gaps_and_ratio_density
statement: formalized
proof: formalized
---

# 026. Positive lower density of large prime gaps

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For every fixed *C* > 0, a positive proportion of consecutive prime gaps exceed $C\log p_n$, throughout every sufficiently large initial segment of the primes. The proportion may depend on *C*. Consequently, the indices where $p_n/n$ increases have positive lower density, answering Erdős and Prachar.

## Positive lower density of large prime gaps

For every fixed *C* > 0, we prove that a positive proportion of consecutive prime gaps exceed $C\log p$, where *p* is the smaller prime. The proportion is bounded below for every sufficiently large initial segment of the prime sequence, with a constant depending on *C*. It follows that the indices at which $p_n/n$ increases have positive lower asymptotic density, answering a question of Erdős and Prachar.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized supplement proves that the indices $n$ for which $p_n/n<p_{n+1}/(n+1)$ have positive lower asymptotic density, where $p_n$ is the $n$th prime. Thus the normalized prime sequence has a positive-density set of increases. This is the prime-ratio corollary associated with the paper's theorem on a positive lower density of large prime gaps.

## Lean: Positive lower density of prime-ratio increases

```lean
theorem large_gaps_and_ratio_density :
    (∀ C : ℝ, 0 < C →
      ∃ c : ℝ, 0 < c ∧ ∃ N₀ : ℕ, ∀ N : ℕ, N₀ ≤ N →
        c * (N : ℝ) ≤ ((LargePrimeGaps.largeGapIndices C N).card : ℝ)) ∧
    0 < lowerAsymptoticDensity ratioIncreaseIndices
```

Stated in [PrimeGaps.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PrimeGaps.lean#L36). Proved in [lean/OAI/NumberTheory/PrimeGaps/RatioCorollary.lean, line 30](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/PrimeGaps/RatioCorollary.lean#L30).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/026.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/026.md)
