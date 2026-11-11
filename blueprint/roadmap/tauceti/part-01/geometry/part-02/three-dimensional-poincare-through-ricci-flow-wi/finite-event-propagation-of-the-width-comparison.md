---
declaration: theorem
origin: cited
lean: TauCeti.ricciWidth_normalized_le_of_forward_le_of_jump_le
statement: formalized
proof: formalized
---

# Finite-event propagation of the width comparison

Let `τ 0 < τ 1 < ⋯ < τ n` be event
times, with `0 ≤ τ 0`, and let `τ (n + 1)` bound the final epoch. On each epoch
`[τ k, τ (k + 1))` the function `W` is continuous and satisfies the upper forward width
inequality. At the event time `τ (k + 1)` its value exceeds the upper limit of `W` from the left
by at most `e k`. Then every later value obeys the normalized bound in which each event error
enters with the weight `(1 + 4 τ (k + 1)) ^ (-3/4)`. With no events (`n = 0`) this is the
regular-slab comparison on `[τ 0, τ 1)`.

```lean
TauCeti.ricciWidth_normalized_le_of_forward_le_of_jump_le {W : ℝ → ℝ} {τ e : ℕ → ℝ} {n : ℕ}
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
  (t : ℝ) :
  t ∈ Set.Ico (τ n) (τ (n + 1)) →
    (1 + 4 * t) ^ (-3 / 4) * W t ≤
      (1 + 4 * τ 0) ^ (-3 / 4) * W (τ 0) +
          ∑ k ∈ Finset.range n, (1 + 4 * τ (k + 1)) ^ (-3 / 4) * e k -
        2 * Real.pi * ((1 + 4 * t) ^ (1 / 4) - (1 + 4 * τ 0) ^ (1 / 4))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.ricciWidthProfile](tauceti-ricciwidthprofile.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ricciWidth_normalized_le_of_forward_le_of_jump_le`](https://taucetiproject.org/docs/TauCeti/Geometry/RicciFlow/WidthComparison.html#TauCeti.ricciWidth_normalized_le_of_forward_le_of_jump_le).

## Sources

- [Tau Ceti documentation: `TauCeti.ricciWidth_normalized_le_of_forward_le_of_jump_le`](https://taucetiproject.org/docs/TauCeti/Geometry/RicciFlow/WidthComparison.html#TauCeti.ricciWidth_normalized_le_of_forward_le_of_jump_le)
- [Source of `TauCeti.ricciWidth_normalized_le_of_forward_le_of_jump_le` in TauCeti/Geometry/RicciFlow/WidthComparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RicciFlow/WidthComparison.lean#L237)
- [Tau Ceti roadmap status: Three-dimensional Poincaré through Ricci flow with surgery](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Poincare3D/STATUS.md)
