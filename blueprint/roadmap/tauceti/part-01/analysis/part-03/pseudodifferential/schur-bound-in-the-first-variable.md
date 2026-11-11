---
declaration: theorem
origin: cited
lean: TauCeti.Symbol.lintegral_enorm_quantizationKernel_left_le, TauCeti.Symbol.lintegral_enorm_quantizationKernel_right_le
statement: formalized
proof: formalized
---

# Schur bound in the first variable

Under the bounds of
`TauCeti.Symbol.lintegral_enorm_quantizationKernel_right_le` at every position,
`∫ ‖K_a(x, y)‖ dx ≤ C_n A Rⁿ` for every `y`.

```lean
TauCeti.Symbol.lintegral_enorm_quantizationKernel_left_le.{u_1, u_2} {n : ℕ} {m : ℝ} {V : Type u_1}
  {W : Type u_2} [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup W] [NormedSpace ℂ W]
  (a : TauCeti.Symbol n V W m) (hm : m < -↑n) {A R : ℝ} (hR : 0 < R)
  (h₀ :
    ∀ (x : TauCeti.CoordinateSpace n),
      ∫ (ξ : TauCeti.CoordinateSpace n), ‖a.coefficient (x, ξ)‖ ≤ A)
  (h₁ :
    ∀ (x : TauCeti.CoordinateSpace n) (j : Fin n),
      ∫ (ξ : TauCeti.CoordinateSpace n),
          ‖TauCeti.mixedDeriv [] (List.replicate (n + 1) j) a.coefficient x ξ‖ ≤
        A * R ^ (n + 1))
  (y : TauCeti.CoordinateSpace n) :
  ∫⁻ (x : TauCeti.CoordinateSpace n), ‖TauCeti.quantizationKernel a.coefficient x y‖ₑ ≤
    ENNReal.ofReal
      ((2 ^ (n + 1) * (1 + √↑n ^ (n + 1)) * ((2 * Real.pi) ^ n)⁻¹ * A *
          ∫ (w : TauCeti.CoordinateSpace n), ((1 + ‖w‖) ^ (n + 1))⁻¹) *
        R ^ n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.lintegral_enorm_quantizationKernel_left_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Lp.html#TauCeti.Symbol.lintegral_enorm_quantizationKernel_left_le).

## Other forms

**Schur bound in the second variable.** Formalized in Tau Ceti as [`TauCeti.Symbol.lintegral_enorm_quantizationKernel_right_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Lp.html#TauCeti.Symbol.lintegral_enorm_quantizationKernel_right_le).

```lean
TauCeti.Symbol.lintegral_enorm_quantizationKernel_right_le.{u_1, u_2} {n : ℕ} {m : ℝ} {V : Type u_1}
  {W : Type u_2} [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup W] [NormedSpace ℂ W]
  (a : TauCeti.Symbol n V W m) (hm : m < -↑n) {x : TauCeti.CoordinateSpace n} {A R : ℝ} (hR : 0 < R)
  (h₀ : ∫ (ξ : TauCeti.CoordinateSpace n), ‖a.coefficient (x, ξ)‖ ≤ A)
  (h₁ :
    ∀ (j : Fin n),
      ∫ (ξ : TauCeti.CoordinateSpace n),
          ‖TauCeti.mixedDeriv [] (List.replicate (n + 1) j) a.coefficient x ξ‖ ≤
        A * R ^ (n + 1)) :
  ∫⁻ (y : TauCeti.CoordinateSpace n), ‖TauCeti.quantizationKernel a.coefficient x y‖ₑ ≤
    ENNReal.ofReal
      ((2 ^ (n + 1) * (1 + √↑n ^ (n + 1)) * ((2 * Real.pi) ^ n)⁻¹ * A *
          ∫ (w : TauCeti.CoordinateSpace n), ((1 + ‖w‖) ^ (n + 1))⁻¹) *
        R ^ n)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.lintegral_enorm_quantizationKernel_left_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Lp.html#TauCeti.Symbol.lintegral_enorm_quantizationKernel_left_le)
- [Source of `TauCeti.Symbol.lintegral_enorm_quantizationKernel_left_le` in TauCeti/Analysis/Pseudodifferential/Lp.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Pseudodifferential/Lp.lean#L85)
