---
declaration: theorem
origin: cited
lean: TauCeti.norm_deriv_lt_div_of_not_injOn, TauCeti.norm_deriv_lt_one_of_not_injOn
statement: formalized
proof: formalized
---

# Strict Schwarz lemma

A holomorphic map of `ball c R₁` into `closedBall (g c) R₂` that is
**not** injective has `‖deriv g c‖ < R₂ / R₁`.

Both radii must be positive: for `R₂ = 0` the map is constant, so it is not injective and the
strict bound fails.

```lean
TauCeti.norm_deriv_lt_div_of_not_injOn.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [StrictConvexSpace ℝ E] {g : ℂ → E} {c : ℂ} {R₁ R₂ : ℝ} (hR₁ : 0 < R₁) (hR₂ : 0 < R₂)
  (hgd : DifferentiableOn ℂ g (Metric.ball c R₁))
  (hgm : Set.MapsTo g (Metric.ball c R₁) (Metric.closedBall (g c) R₂))
  (hgi : ¬Set.InjOn g (Metric.ball c R₁)) : ‖deriv g c‖ < R₂ / R₁
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_deriv_lt_div_of_not_injOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Schwarz.html#TauCeti.norm_deriv_lt_div_of_not_injOn).

## Other forms

**Strict Schwarz lemma, equal radii.** Formalized in Tau Ceti as [`TauCeti.norm_deriv_lt_one_of_not_injOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Schwarz.html#TauCeti.norm_deriv_lt_one_of_not_injOn).

```lean
TauCeti.norm_deriv_lt_one_of_not_injOn.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [StrictConvexSpace ℝ E] {g : ℂ → E} {c : ℂ} {R : ℝ} (hR : 0 < R)
  (hgd : DifferentiableOn ℂ g (Metric.ball c R))
  (hgm : Set.MapsTo g (Metric.ball c R) (Metric.closedBall (g c) R))
  (hgi : ¬Set.InjOn g (Metric.ball c R)) : ‖deriv g c‖ < 1
```

## Sources

- [Tau Ceti documentation: `TauCeti.norm_deriv_lt_div_of_not_injOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Schwarz.html#TauCeti.norm_deriv_lt_div_of_not_injOn)
- [Source of `TauCeti.norm_deriv_lt_div_of_not_injOn` in TauCeti/Analysis/Complex/Conformal/Schwarz.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Schwarz.lean#L47)
