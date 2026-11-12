---
declaration: section
origin: cited
lean: OAI.OrdinaryCorrelations.binary_corrected_elliott, OAI.OrdinaryTwoPointCorrelations.liouville_log_saving, OAI.OrdinaryTwoPointCorrelations.binary_corrected_elliott, OAI.OrdinaryTwoPointCorrelations.affine_corrected_elliott
statement: formalized
proof: formalized
---

# 007. Ordinary two-point correlations and the corrected Elliott conjecture

1 manuscript and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the ordinary two-point Chowla conjecture, with a bound $O(X/(\log X)^c)$ for Liouville correlation sums along fixed nonproportional affine forms, where *c* > 0 is absolute. More generally, proves the binary corrected Elliott conjecture for complex multiplicative functions bounded by one when one factor is uniformly nonpretentious against each fixed Dirichlet character times $n^{it}$ for $|t|\le X$.

## Ordinary two-point correlations of multiplicative functions

We prove the ordinary two-point Chowla conjecture. For every fixed pair of nonproportional affine forms, the Liouville correlation has a power-of-logarithm saving at every cutoff, with an absolute exponent. We also prove the binary corrected Elliott conjecture for ordinary averages of complex multiplicative functions of modulus at most one, under uniform nonpretentiousness of at least one original factor. This qualitative conclusion holds in fixed residue classes and for fixed nonproportional affine forms.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves ordinary two-point cancellation for multiplicative functions. For the Liouville function on every fixed pair of nonproportional affine forms, the correlation sum up to $X$ is $O(X/(\log X)^c)$ for an absolute $c>0$, with the implied constant depending on the forms.

For two one-bounded multiplicative functions, if at least one is uniformly nonpretentious against all Dirichlet-character twists with frequency $|t|\le N$, then their shifted and nonproportional affine correlation sums divided by $N$ tend to zero. These are ordinary averages, with no logarithmic averaging.

## Lean: Ordinary Elliott cancellation under uniform nonpretentiousness

Stated in [OrdinaryElliott.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OrdinaryElliott.lean).

```lean
theorem binary_corrected_elliott
    (f₁ f₂ : ℕ → ℂ) (hf₁ : OneBounded f₁) (hf₂ : OneBounded f₂)
    (hm₁ : Multiplicative f₁) (hm₂ : Multiplicative f₂)
    (hNP : UniformlyNonpretentious f₁ ∨ UniformlyNonpretentious f₂)
    (h₁ h₂ : ℕ) (hne : h₁ ≠ h₂) :
    Tendsto (shiftAverage f₁ f₂ h₁ h₂) atTop (nhds 0)
```

Proved in [lean/OAI/NumberTheory/OrdinaryCorrelations/Elliott/BinaryCorrectedElliott.lean, line 37](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/OrdinaryCorrelations/Elliott/BinaryCorrectedElliott.lean#L37).

## Lean: Ordinary Liouville and multiplicative two-point correlations

Stated in [OrdinaryTwoPointCorrelations.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.lean).

```lean
theorem liouville_log_saving :
    ∃ c : ℝ, 0 < c ∧ ∀ a₁ a₂ b₁ b₂ : ℕ,
      0 < a₁ → 0 < a₂ → a₁ * b₂ ≠ a₂ * b₁ →
      ∃ C : ℝ, 0 < C ∧ ∀ X : ℝ, 3 ≤ X →
        ‖affineSum liouville liouville a₁ a₂ b₁ b₂ ⌊X⌋₊‖ ≤
          C * X / Real.rpow (Real.log X) c
```

Proved in [lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean#L10).

```lean
theorem binary_corrected_elliott :
    ∀ f₁ f₂ : ℕ → ℂ, Multiplicative f₁ → Multiplicative f₂ →
      OneBounded f₁ → OneBounded f₂ →
      (UniformlyNonpretentious f₁ ∨ UniformlyNonpretentious f₂) →
      ∀ h₁ h₂ : ℕ, h₁ ≠ h₂ →
        Tendsto (fun N : ℕ => correlationSum f₁ f₂ h₁ h₂ N / (N : ℂ)) atTop (nhds 0)
```

Proved in [lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean, line 18](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean#L18).

```lean
theorem affine_corrected_elliott :
    ∀ f₁ f₂ : ℕ → ℂ, Multiplicative f₁ → Multiplicative f₂ →
      OneBounded f₁ → OneBounded f₂ →
      (UniformlyNonpretentious f₁ ∨ UniformlyNonpretentious f₂) →
      ∀ a₁ a₂ b₁ b₂ : ℕ, 0 < a₁ → 0 < a₂ → a₁ * b₂ ≠ a₂ * b₁ →
        Tendsto (fun N : ℕ => affineSum f₁ f₂ a₁ a₂ b₁ b₂ N / (N : ℂ)) atTop (nhds 0)
```

Proved in [lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean, line 26](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean#L26).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/007.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/007.md)
