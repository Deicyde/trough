---
declaration: theorem
origin: cited
lean: TauCeti.inner_apply_add_integral_le
statement: formalized
proof: formalized
---

# The Lyapunov inequality near the end

Let `B` be symmetric with `α ‖v‖ ≤ ‖B v‖`. If
`‖A(s) - B‖ ≤ α / 2` for `s ≥ T`, then along a solution of `w' = -A(s) w`,
`⟪w s, B (w s)⟫ + α² ∫ₜˢ ‖w‖² ≤ ⟪w T, B (w T)⟫` for `s ≥ T`.

```lean
TauCeti.inner_apply_add_integral_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {A : ℝ → E →L[ℝ] E} {B : E →L[ℝ] E} {w : ℝ → E} {α T : ℝ}
  (hBsym : (↑B).IsSymmetric) (hBα : ∀ (v : E), α * ‖v‖ ≤ ‖B v‖)
  (hAB : ∀ (s : ℝ), T ≤ s → ‖A s - B‖ ≤ α / 2) (hw : ∀ (s : ℝ), HasDerivAt w (-(A s) (w s)) s)
  {s : ℝ} (hs : T ≤ s) :
  inner ℝ (w s) (B (w s)) + α ^ 2 * ∫ (τ : ℝ) in T..s, ‖w τ‖ ^ 2 ≤ inner ℝ (w T) (B (w T))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.inner_apply_add_integral_le`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/EnergyEstimate/HalfLine.html#TauCeti.inner_apply_add_integral_le).

## Sources

- [Tau Ceti documentation: `TauCeti.inner_apply_add_integral_le`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/EnergyEstimate/HalfLine.html#TauCeti.inner_apply_add_integral_le)
- [Source of `TauCeti.inner_apply_add_integral_le` in TauCeti/Analysis/ODE/EnergyEstimate/HalfLine.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/ODE/EnergyEstimate/HalfLine.lean#L79)
