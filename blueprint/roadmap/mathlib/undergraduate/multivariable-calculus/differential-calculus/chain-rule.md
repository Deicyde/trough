# Chain rule

Mathlib states this as `fderiv_comp`.

```lean
fderiv_comp.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  {G : Type u_4} [AddCommGroup G] [TopologicalSpace G] [_root_.Module 𝕜 G] [ContinuousAdd G]
  [ContinuousSMul 𝕜 G] {f : E → F} (x : E) [T2Space G] {g : F → G} (hg : DifferentiableAt 𝕜 g (f x))
  (hf : DifferentiableAt 𝕜 f x) : fderiv 𝕜 (g ∘ f) x = fderiv 𝕜 g (f x) ∘SL fderiv 𝕜 f x
```

## Depends on

- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](differentials-linear-tangent-functions.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Derivative of a composition of functions (Analysis)](../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)

## Sources

- [Mathlib documentation: `fderiv_comp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Comp.html#fderiv_comp)
- [Source of `fderiv_comp` in Mathlib/Analysis/Calculus/FDeriv/Comp.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/FDeriv/Comp.lean#L166)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L462)
