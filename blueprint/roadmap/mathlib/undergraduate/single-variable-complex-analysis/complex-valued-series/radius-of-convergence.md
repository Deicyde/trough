# Radius of convergence

The radius of a formal multilinear series is the largest `r` such that the sum `Σ ‖pₙ‖ ‖y‖ⁿ`
converges for all `‖y‖ < r`. This implies that `Σ pₙ yⁿ` converges for all `‖y‖ < r`, but these
definitions are *not* equivalent in general.

```lean
FormalMultilinearSeries.radius.{u_1, u_3, u_4} {𝕜 : Type u_1} {E : Type u_3} {F : Type u_4}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] (p : FormalMultilinearSeries 𝕜 E F) : ENNReal
```

## Depends on

- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Multilinear map](../../../overview/linear-algebra/fundamentals/multilinear-map.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `FormalMultilinearSeries.radius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Analytic/ConvergenceRadius.html#FormalMultilinearSeries.radius)
- [Source of `FormalMultilinearSeries.radius` in Mathlib/Analysis/Analytic/ConvergenceRadius.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Analytic/ConvergenceRadius.lean#L106)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L369)
