---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_le_eLpNorm_deriv_of_support_subset_Icc, TauCeti.lintegral_enorm_rpow_le_of_support_subset_Icc
statement: formalized
proof: formalized
---

# The one-dimensional Poincaré inequality

a `C¹` function on `ℝ` supported in an interval
of length `b - a` obeys `‖g‖_p ≤ (b - a) ‖g'‖_p` for every `1 ≤ p ≤ ∞`. The endpoints may
be in either order: an empty or degenerate interval carries only the zero function.

The interval hypothesis is essential; `TauCeti.not_exists_eLpNorm_le_const_mul_eLpNorm_fderiv`
shows no such bound holds uniformly over all compactly supported functions.

```lean
TauCeti.eLpNorm_le_eLpNorm_deriv_of_support_subset_Icc.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  {g : ℝ → F} {a b : ℝ} [NormedSpace ℝ F] {g' : ℝ → F} (hg : ∀ (t : ℝ), HasDerivAt g (g' t) t)
  (hg' : Continuous g') (hsupp : Function.support g ⊆ Set.Icc a b) {p : ENNReal} (hp : 1 ≤ p) :
  MeasureTheory.eLpNorm g p MeasureTheory.volume ≤
    ENNReal.ofReal (b - a) * MeasureTheory.eLpNorm g' p MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for the integral of a product](../../../../measure-theory/function/holders-inequality-for-the-integral-of-a-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_eLpNorm_deriv_of_support_subset_Icc`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Slab.html#TauCeti.eLpNorm_le_eLpNorm_deriv_of_support_subset_Icc).

## Other forms

**The one-dimensional Poincaré inequality, in the `∫⁻` form the Fubini argument below consumes.** Formalized in Tau Ceti as [`TauCeti.lintegral_enorm_rpow_le_of_support_subset_Icc`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Slab.html#TauCeti.lintegral_enorm_rpow_le_of_support_subset_Icc).

```lean
TauCeti.lintegral_enorm_rpow_le_of_support_subset_Icc.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  {g : ℝ → F} {a b : ℝ} [NormedSpace ℝ F] {g' : ℝ → F} (hg : ∀ (t : ℝ), HasDerivAt g (g' t) t)
  (hg' : Continuous g') (hsupp : Function.support g ⊆ Set.Icc a b) {r : ℝ} (hr : 1 ≤ r) :
  ∫⁻ (t : ℝ), ‖g t‖ₑ ^ r ≤ ENNReal.ofReal ((b - a) ^ r) * ∫⁻ (t : ℝ), ‖g' t‖ₑ ^ r
```

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_eLpNorm_deriv_of_support_subset_Icc`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Slab.html#TauCeti.eLpNorm_le_eLpNorm_deriv_of_support_subset_Icc)
- [Source of `TauCeti.eLpNorm_le_eLpNorm_deriv_of_support_subset_Icc` in TauCeti/Analysis/Sobolev/Poincare/Slab.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Poincare/Slab.lean#L186)
