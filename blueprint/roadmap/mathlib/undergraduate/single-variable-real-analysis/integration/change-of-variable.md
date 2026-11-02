---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: intervalIntegral.integral_deriv_smul_comp
mathlib_file: Mathlib/MeasureTheory/Integral/IntervalIntegral/IntegrationByParts.lean
---

# Change of variable

Change of variables, most common version. If `f` has continuous derivative `f'` on `[a, b]`,
and `g` is continuous, then we can substitute `u = f x` to get
`∫ x in a..b, f' x • (g ∘ f) x = ∫ u in f a..f b, g u`.

If the function `f` is monotone or antitone, see also `integral_deriv_smul_comp_of_deriv_nonneg`
and `integral_deriv_smul_comp_of_deriv_nonpos` dropping all assumptions on `g`.

```lean
intervalIntegral.integral_deriv_smul_comp.{u_1} {a b : ℝ} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {f f' : ℝ → ℝ} {g : ℝ → E} (h : ∀ x ∈ Set.uIcc a b, HasDerivAt f (f' x) x)
  (h' : ContinuousOn f' (Set.uIcc a b)) (hg : Continuous g) :
  ∫ (x : ℝ) in a..b, f' x • (g ∘ f) x = ∫ (x : ℝ) in f a..f b, g x
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Derivative at a point](../differentiability/derivative-at-a-point.md)
- [Lebesgue measure](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Proof depends on

- [Fundamental Theorem of Integral Calculus](../../../hundred-theorems/part-01/fundamental-theorem-of-integral-calculus.md)
- [Image of a segment](../real-valued-functions-defined-on-a-subset-of/image-of-a-segment.md)

## Sources

- [Mathlib documentation: `intervalIntegral.integral_deriv_smul_comp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/IntegrationByParts.html#intervalIntegral.integral_deriv_smul_comp)
- [Source of `intervalIntegral.integral_deriv_smul_comp` in Mathlib/MeasureTheory/Integral/IntervalIntegral/IntegrationByParts.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/IntegrationByParts.lean#L309)
- [Mathlib undergraduate list: Single Variable Real Analysis › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L343)
