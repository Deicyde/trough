---
declaration: theorem
origin: cited
lean: TauCeti.spectralFlow_eq_sum
statement: formalized
proof: formalized
---

# Phillips' partition formula

For a partition `a = p 0 ≤ p 1 ≤ ⋯ ≤ p n = b` and a spectral
cut `c k` of `A` on each `[p k, p (k + 1)]`, the spectral flow is the sum of the changes of the
counts of eigenvalues in `[0, c k]` over the pieces.

```lean
TauCeti.spectralFlow_eq_sum.{u_1, u_2} {𝕜 : Type u_1} {H : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H] [NormedAlgebra ℝ (H →L[𝕜] H)]
  [IsometricContinuousFunctionalCalculus ℝ (H →L[𝕜] H) IsSelfAdjoint] {A : ℝ → H →L[𝕜] H}
  [IsScalarTower ℝ 𝕜 (H →L[𝕜] H)] {a b : ℝ} (hA : ContinuousOn A (Set.Icc a b))
  (hsa : ∀ t ∈ Set.Icc a b, IsSelfAdjoint (A t)) (hF : ∀ t ∈ Set.Icc a b, (A t).IsFredholm) {n : ℕ}
  {p : ℕ → ℝ} (hp : Monotone p) (hp0 : p 0 = a) (hpn : p n = b) {c : ℕ → ℝ}
  (hc : ∀ k < n, TauCeti.IsSpectralCutOn A (c k) (Set.Icc (p k) (p (k + 1)))) :
  TauCeti.spectralFlow A a b =
    ∑ k ∈ Finset.range n,
      (↑(TauCeti.spectralCount (c k) (A (p (k + 1)))) - ↑(TauCeti.spectralCount (c k) (A (p k))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riesz's lemma, translated form](../normed/part-02/rieszs-lemma-translated-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.spectralFlow_eq_sum`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/Spectral/Flow.html#TauCeti.spectralFlow_eq_sum).

## Sources

- [Tau Ceti documentation: `TauCeti.spectralFlow_eq_sum`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/Spectral/Flow.html#TauCeti.spectralFlow_eq_sum)
- [Source of `TauCeti.spectralFlow_eq_sum` in TauCeti/Analysis/Fredholm/Spectral/Flow.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fredholm/Spectral/Flow.lean#L544)
