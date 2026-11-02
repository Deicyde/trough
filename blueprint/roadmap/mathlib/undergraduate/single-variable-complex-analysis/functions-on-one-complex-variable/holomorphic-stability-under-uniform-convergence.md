---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: TendstoLocallyUniformlyOn.differentiableOn
mathlib_file: Mathlib/Analysis/Complex/LocallyUniformLimit.lean
---

# Holomorphic stability under uniform convergence

A locally uniform limit of holomorphic functions on an open domain of the complex plane is
holomorphic (the derivatives converge locally uniformly to that of the limit, which is proved
as `TendstoLocallyUniformlyOn.deriv`).

```lean
TendstoLocallyUniformlyOn.differentiableOn.{u_1, u_2} {E : Type u_1} {ι : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {U : Set ℂ} {φ : Filter ι} {F : ι → ℂ → E} {f : ℂ → E}
  [CompleteSpace E] [φ.NeBot] (hf : TendstoLocallyUniformlyOn F f φ U)
  (hF : ∀ᶠ (n : ι) in φ, DifferentiableOn ℂ (F n) U) (hU : IsOpen U) : DifferentiableOn ℂ f U
```

## Depends on

- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Holomorphic functions](holomorphic-functions.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Cauchy formulas](cauchy-formulas.md)
- [Uniform convergence](../../../overview/topology/uniform-notions/uniform-convergence.md)

## Sources

- [Mathlib documentation: `TendstoLocallyUniformlyOn.differentiableOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/LocallyUniformLimit.html#TendstoLocallyUniformlyOn.differentiableOn)
- [Source of `TendstoLocallyUniformlyOn.differentiableOn` in Mathlib/Analysis/Complex/LocallyUniformLimit.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/LocallyUniformLimit.lean#L133)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L400)
