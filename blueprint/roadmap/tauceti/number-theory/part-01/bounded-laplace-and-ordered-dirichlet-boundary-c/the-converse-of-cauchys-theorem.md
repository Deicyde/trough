---
declaration: theorem
origin: cited
lean: TauCeti.Contour.isExactOn_of_forall_closed_integral_eq_zero
statement: formalized
proof: formalized
---

# The converse of Cauchy's theorem

A continuous function on an open set `U` whose contour
integral vanishes along every closed piecewise-`C¹` curve in `U` has a primitive on `U`.

```lean
TauCeti.Contour.isExactOn_of_forall_closed_integral_eq_zero.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {U : Set ℂ} {f : ℂ → E} [CompleteSpace E] (hU : IsOpen U)
  (hf : ContinuousOn f U)
  (h :
    ∀ (γ : ℝ → ℂ) (a b : ℝ),
      TauCeti.IsPiecewiseC1On γ a b →
        Set.MapsTo γ (Set.uIcc a b) U → γ a = γ b → ∫ (t : ℝ) in a..b, deriv γ t • f (γ t) = 0) :
  Complex.IsExactOn f U
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.isExactOn_of_forall_closed_integral_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Primitive.html#TauCeti.Contour.isExactOn_of_forall_closed_integral_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.isExactOn_of_forall_closed_integral_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Primitive.html#TauCeti.Contour.isExactOn_of_forall_closed_integral_eq_zero)
- [Source of `TauCeti.Contour.isExactOn_of_forall_closed_integral_eq_zero` in TauCeti/Analysis/Contour/Primitive.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Primitive.lean#L181)
