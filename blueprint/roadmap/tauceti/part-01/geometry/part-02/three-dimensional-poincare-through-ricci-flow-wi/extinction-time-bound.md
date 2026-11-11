---
declaration: theorem
origin: cited
lean: TauCeti.ricciWidth_time_le_of_forward_le_of_jump_le
statement: formalized
proof: formalized
---

# Extinction-time bound

Under the hypotheses of finite-event propagation, suppose the
total weighted event error is at most `E`. Then every time `t` of the final epoch at which the
width is still nonnegative satisfies `t ≤ ((q₀ + (N₀ W(τ 0) + E) / (2π))^4 - 1) / 4`, where
`q₀ = (1 + 4 τ 0)^(1/4)` and `N₀ = (1 + 4 τ 0)^(-3/4)`.

```lean
TauCeti.ricciWidth_time_le_of_forward_le_of_jump_le {W : ℝ → ℝ} {τ e : ℕ → ℝ} {n : ℕ} {E : ℝ}
  (hτ₀ : 0 ≤ τ 0) (hτ : ∀ k < n, τ k < τ (k + 1))
  (hW : ∀ k ≤ n, ContinuousOn W (Set.Ico (τ k) (τ (k + 1))))
  (hforward :
    ∀ k ≤ n,
      ∀ t ∈ Set.Ico (τ k) (τ (k + 1)),
        ∀ η > 0,
          ∃ δ > 0,
            ∀ (h : ℝ),
              0 < h →
                h < δ →
                  t + h < τ (k + 1) →
                    (W (t + h) - W t) / h ≤ -2 * Real.pi + 3 * W t / (1 + 4 * t) + η)
  (hjump :
    ∀ k < n,
      ∀ η > 0,
        ∃ᶠ (s : ℝ) in nhdsWithin (τ (k + 1)) (Set.Iio (τ (k + 1))), W (τ (k + 1)) ≤ W s + e k + η)
  (hE : ∑ k ∈ Finset.range n, (1 + 4 * τ (k + 1)) ^ (-3 / 4) * e k ≤ E) {t : ℝ}
  (ht : t ∈ Set.Ico (τ n) (τ (n + 1))) (hWt : 0 ≤ W t) :
  t ≤
    (((1 + 4 * τ 0) ^ (1 / 4) + ((1 + 4 * τ 0) ^ (-3 / 4) * W (τ 0) + E) / (2 * Real.pi)) ^ 4 - 1) /
      4
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Finite-event propagation of the width comparison](finite-event-propagation-of-the-width-comparison.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ricciWidth_time_le_of_forward_le_of_jump_le`](https://taucetiproject.org/docs/TauCeti/Geometry/RicciFlow/WidthComparison.html#TauCeti.ricciWidth_time_le_of_forward_le_of_jump_le).

## Sources

- [Tau Ceti documentation: `TauCeti.ricciWidth_time_le_of_forward_le_of_jump_le`](https://taucetiproject.org/docs/TauCeti/Geometry/RicciFlow/WidthComparison.html#TauCeti.ricciWidth_time_le_of_forward_le_of_jump_le)
- [Source of `TauCeti.ricciWidth_time_le_of_forward_le_of_jump_le` in TauCeti/Geometry/RicciFlow/WidthComparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RicciFlow/WidthComparison.lean#L287)
- [Tau Ceti roadmap status: Three-dimensional Poincaré through Ricci flow with surgery](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Poincare3D/STATUS.md)
