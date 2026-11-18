---
declaration: theorem
origin: cited
lean: TauCeti.BesovSpace.lowPass_smul_lowPass
statement: formalized
proof: formalized
---

# Bony's decomposition

For every gap `N`, the product of the low-frequency cut-offs
`S_M u · S_M v = ∑_{k, l < M} Δₖ u · Δₗ v` splits into the truncated paraproducts
`∑_{j < M} S_{j-N} u · Δⱼ v` (the pairs with `k + N < l`) and `∑_{j < M} Δⱼ u · S_{j-N} v` (the
pairs with `l + N < k`) and the truncated resonant part, the pairs with `|k - l| ≤ N`.

```lean
TauCeti.BesovSpace.lowPass_smul_lowPass.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F] {φ : ContDiffBump 0}
  {s : ℝ} {q : ENNReal} {s' : ℝ} {q' p₁ p₂ r : ENNReal} [Fact (1 ≤ p₁)] [Fact (1 ≤ p₂)]
  [p₁.HolderTriple p₂ r] (N M : ℕ) (u : TauCeti.BesovSpace ℂ φ s p₁ q)
  (v : TauCeti.BesovSpace F φ s' p₂ q') :
  u.lowPass M • v.lowPass M =
    ∑ j ∈ Finset.range M, u.lowPass (j - N) • v.block j +
        ∑ j ∈ Finset.range M, u.block j • v.lowPass (j - N) +
      ∑ j ∈ Finset.range M, u.block j • ∑ k ∈ Finset.range M with k ≤ j + N ∧ j ≤ k + N, v.block k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BesovSpace.lowPass_smul_lowPass`](https://taucetiproject.org/docs/TauCeti/Analysis/FunctionalSpaces/BesovSpace/Paraproduct.html#TauCeti.BesovSpace.lowPass_smul_lowPass).

## Sources

- [Tau Ceti documentation: `TauCeti.BesovSpace.lowPass_smul_lowPass`](https://taucetiproject.org/docs/TauCeti/Analysis/FunctionalSpaces/BesovSpace/Paraproduct.html#TauCeti.BesovSpace.lowPass_smul_lowPass)
- [Source of `TauCeti.BesovSpace.lowPass_smul_lowPass` in TauCeti/Analysis/FunctionalSpaces/BesovSpace/Paraproduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/FunctionalSpaces/BesovSpace/Paraproduct.lean#L330)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PDE/STATUS.md)
