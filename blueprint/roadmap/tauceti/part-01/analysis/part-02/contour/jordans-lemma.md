---
declaration: theorem
origin: cited
lean: TauCeti.Contour.norm_integral_semicircle_exp_mul_le
statement: formalized
proof: formalized
---

# Jordan's lemma

If `‖f‖ ≤ M` on the upper semicircle of radius `R`, then for `a > 0`
the arc contribution of `f z · e^{iaz}` is at most `π M / a` in norm — a bound independent of
`R`, obtained without assuming any decay of `f`.

No integrability hypothesis is imposed on the integrand, matching the Mathlib norm-of-integral
idiom (`intervalIntegral.norm_integral_le_of_norm_le` constrains only the dominating function).
When the parameterized integrand fails to be integrable the interval integral totalizes to `0`
and the bound reads `0 ≤ π M / a`, which holds since `0 ≤ M`; the content of the lemma is
therefore unchanged, and callers are not obliged to discharge integrability.

```lean
TauCeti.Contour.norm_integral_semicircle_exp_mul_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {f : ℂ → E} {a R M : ℝ} (ha : 0 < a) (hR : 0 ≤ R)
  (hM : ∀ θ ∈ Set.Icc 0 Real.pi, ‖f (circleMap 0 R θ)‖ ≤ M) :
  ‖∫ (θ : ℝ) in 0..Real.pi,
        (Complex.exp (Complex.I * ↑a * circleMap 0 R θ) * deriv (circleMap 0 R) θ) •
          f (circleMap 0 R θ)‖ ≤
    Real.pi * M / a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jordan's integral bound](../../part-03/special-functions/jordans-integral-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.norm_integral_semicircle_exp_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/JordanLemma.html#TauCeti.Contour.norm_integral_semicircle_exp_mul_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.norm_integral_semicircle_exp_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/JordanLemma.html#TauCeti.Contour.norm_integral_semicircle_exp_mul_le)
- [Source of `TauCeti.Contour.norm_integral_semicircle_exp_mul_le` in TauCeti/Analysis/Contour/JordanLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/JordanLemma.lean#L66)
