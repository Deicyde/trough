# Schwarz lemma

The **Schwarz Lemma**.
Let `f : E → F` be a complex analytic on an open ball with center at the origin.
If `f` sends this ball to the closed ball with center `0` of the same radius and `f 0 = 0`,
then for any point `z` of this disk we have `‖f z‖ ≤ ‖z‖`.

```lean
Complex.norm_le_norm_of_mapsTo_ball.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [NormedAddCommGroup F] [NormedSpace ℂ F] {R : ℝ} {f : E → F} {z : E}
  (hd : DifferentiableOn ℂ f (Metric.ball 0 R))
  (h_maps : Set.MapsTo f (Metric.ball 0 R) (Metric.closedBall 0 R)) (h₀ : f 0 = 0) (hz : ‖z‖ < R) :
  ‖f z‖ ≤ ‖z‖
```

## Depends on

- [Ball](../../topology/metric-spaces/ball.md)
- [Complex number](../../general-algebra/numbers/complex-number.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Affine function](../../geometry/affine-and-euclidean-geometry/affine-function.md)
- [Cauchy integral formula](cauchy-integral-formula.md)
- [Hahn-Banach theorem](../normed-vector-spaces-banach-spaces/hahn-banach-theorem.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Removable singularity](removable-singularity.md)

## Sources

- [Mathlib documentation: `Complex.norm_le_norm_of_mapsTo_ball`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Schwarz.html#Complex.norm_le_norm_of_mapsTo_ball)
- [Source of `Complex.norm_le_norm_of_mapsTo_ball` in Mathlib/Analysis/Complex/Schwarz.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Complex/Schwarz.lean#L230)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L372)
