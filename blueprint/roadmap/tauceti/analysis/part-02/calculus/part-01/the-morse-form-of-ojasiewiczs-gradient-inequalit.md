---
declaration: theorem
origin: cited
lean: TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_gradient_sq, TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_fderiv_sq
statement: formalized
proof: formalized
---

# The Morse form of Łojasiewicz's gradient inequality

Near a nondegenerate critical point
the absolute energy difference is bounded by a multiple of the squared norm of the gradient;
equivalently the Łojasiewicz inequality holds there with exponent `1 / 2`.
Smoothness alone does not guarantee such an inequality, and a gradient trajectory can spiral
forever without converging.

```lean
TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_gradient_sq.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [CompleteSpace E] {f : E → ℝ} {x : E}
  (h : TauCeti.IsNondegenerateCriticalPoint f x) :
  ∃ lam > 0, ∀ᶠ (y : E) in nhds x, lam * |f y - f x| ≤ ‖gradient f y‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_gradient_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Linearization.html#TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_gradient_sq).

## Other forms

**The Morse form of Łojasiewicz's gradient inequality on a normed space.** Formalized in Tau Ceti as [`TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_fderiv_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Basic.html#TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_fderiv_sq).

```lean
TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_fderiv_sq.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {f : E → ℝ} {x : E}
  (h : TauCeti.IsNondegenerateCriticalPoint f x) :
  ∃ lam > 0, ∀ᶠ (y : E) in nhds x, lam * |f y - f x| ≤ ‖fderiv ℝ f y‖ ^ 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_gradient_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Linearization.html#TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_gradient_sq)
- [Source of `TauCeti.IsNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_gradient_sq` in TauCeti/Analysis/Calculus/Morse/Linearization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Morse/Linearization.lean#L420)
