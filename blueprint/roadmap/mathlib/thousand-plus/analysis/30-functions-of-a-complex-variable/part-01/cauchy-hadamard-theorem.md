---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: FormalMultilinearSeries.radius_inv_eq_limsup
mathlib_file: Mathlib/Analysis/Analytic/RadiusLiminf.lean
---

# Cauchy–Hadamard theorem

The **Cauchy-Hadamard theorem** for formal multilinear series: The inverse of the radius
is equal to $\limsup_{n\to\infty} \sqrt[n]{‖p n‖}$.

```lean
FormalMultilinearSeries.radius_inv_eq_limsup.{u_1, u_2, u_3} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] (p : FormalMultilinearSeries 𝕜 E F) :
  p.radius⁻¹ = Filter.limsup (fun n => ↑(‖p n‖₊ ^ (1 / ↑n))) Filter.atTop
```

## Depends on

- [Power functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)
- [Radius of convergence](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Array](../../../../overview/data-structures/list-like-structures/array.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)

## Sources

- [Mathlib documentation: `FormalMultilinearSeries.radius_inv_eq_limsup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Analytic/RadiusLiminf.html#FormalMultilinearSeries.radius_inv_eq_limsup)
- [Source of `FormalMultilinearSeries.radius_inv_eq_limsup` in Mathlib/Analysis/Analytic/RadiusLiminf.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Analytic/RadiusLiminf.lean#L64)
- [1000+ theorems list: Q859122](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1000)
- [1000+ theorems project: Q859122](https://1000-plus.github.io/?length=-1#Q859122)
- [Wikipedia: Cauchy–Hadamard theorem](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Hadamard_theorem)
- [Wikidata: Q859122](https://www.wikidata.org/wiki/Q859122)
