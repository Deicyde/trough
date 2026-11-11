---
declaration: theorem
origin: cited
lean: ENNReal.tsum_sum_Ico_mul_le
statement: formalized
proof: formalized
---

# Cauchy–Schwarz for a banded double sum

Summing `a j * b k` over the pairs of natural
numbers with `|j - k| < L` gives at most `2 L (∑ a²)^{1/2} (∑ b²)^{1/2}`, since each index
occurs in fewer than `2 L` of these pairs. No summability hypotheses are needed; both sides may be
infinite.

```lean
ENNReal.tsum_sum_Ico_mul_le (L : ℕ) (a b : ℕ → ENNReal) :
  ∑' (j : ℕ), ∑ k ∈ Finset.Ico (j + 1 - L) (j + L), a j * b k ≤
    2 * ↑L * ((∑' (j : ℕ), a j ^ 2) ^ 2⁻¹ * (∑' (k : ℕ), b k ^ 2) ^ 2⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ENNReal.tsum_sum_Ico_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/MeanInequalities.html#ENNReal.tsum_sum_Ico_mul_le).

## Sources

- [Tau Ceti documentation: `ENNReal.tsum_sum_Ico_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/MeanInequalities.html#ENNReal.tsum_sum_Ico_mul_le)
- [Source of `ENNReal.tsum_sum_Ico_mul_le` in TauCeti/Analysis/MeanInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/MeanInequalities.lean#L222)
