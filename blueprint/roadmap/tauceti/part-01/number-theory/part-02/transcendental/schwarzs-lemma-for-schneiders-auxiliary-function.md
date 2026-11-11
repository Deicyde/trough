---
declaration: theorem
origin: cited
lean: TauCeti.norm_schneider_auxiliary_le
statement: formalized
proof: formalized
---

# Schwarz's lemma for Schneider's auxiliary function

Let `β ∈ ℂ` be irrational and let
`F(z) = ∑_{i < D₁, j < D₂} a_{ij} z ^ i exp (j λ z)` vanish at `u + v β` for `1 ≤ u, v ≤ L`. If
`‖a_{ij}‖ ≤ A`, `L (1 + ‖β‖) ≤ R`, `3 R ≤ T` and `1 ≤ T`, then on the disc `‖z‖ ≤ R`
`‖F z‖ ≤ D₁ D₂ A T ^ D₁ exp (D₂ ‖λ‖ T) (3 R / T) ^ (L ^ 2)`.

```lean
TauCeti.norm_schneider_auxiliary_le {β : ℂ} (hβ : ∀ (q : ℚ), ↑q ≠ β) {l : ℂ} {L D₁ D₂ : ℕ}
  {a : Fin D₁ → Fin D₂ → ℂ} {A R T : ℝ} (ha : ∀ (i : Fin D₁) (j : Fin D₂), ‖a i j‖ ≤ A)
  (hzero :
    ∀ (u v : ℕ),
      1 ≤ u →
        u ≤ L →
          1 ≤ v →
            v ≤ L →
              ∑ i, ∑ j, a i j * (↑u + ↑v * β) ^ ↑i * Complex.exp (↑↑j * l * (↑u + ↑v * β)) = 0)
  (hR : ↑L * (1 + ‖β‖) ≤ R) (hRT : 3 * R ≤ T) (hT : 1 ≤ T) {z : ℂ} (hz : ‖z‖ ≤ R) :
  ‖∑ i, ∑ j, a i j * z ^ ↑i * Complex.exp (↑↑j * l * z)‖ ≤
    ↑D₁ * ↑D₂ * A * T ^ D₁ * Real.exp (↑D₂ * ‖l‖ * T) * (3 * R / T) ^ L ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schwarz's lemma with prescribed zeros](../../../analysis/part-02/complex/part-03/schwarzs-lemma-with-prescribed-zeros.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_schneider_auxiliary_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/AnalyticBound.html#TauCeti.norm_schneider_auxiliary_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_schneider_auxiliary_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/AnalyticBound.html#TauCeti.norm_schneider_auxiliary_le)
- [Source of `TauCeti.norm_schneider_auxiliary_le` in TauCeti/NumberTheory/Transcendental/GelfondSchneider/AnalyticBound.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Transcendental/GelfondSchneider/AnalyticBound.lean#L89)
