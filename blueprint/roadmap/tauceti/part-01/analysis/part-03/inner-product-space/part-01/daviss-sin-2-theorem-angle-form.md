---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.sin_two_arccos_le, LinearMap.IsSymmetric.sin_two_theta_le_of_mem, LinearMap.IsSymmetric.sin_two_theta_le
statement: formalized
proof: formalized
---

# Davis's sin 2θ theorem, angle form

Under the hypotheses of
`sin_two_theta_le`, with `θ = arccos ‖P x‖` the angle between the unit
eigenvector `x` and the invariant subspace `U`,

`(b - a) * sin (2θ) ≤ 2 * ε`, with no division by `b-a`.

```lean
LinearMap.IsSymmetric.sin_two_arccos_le.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {T H : E →ₗ[𝕜] E} (hT : T.IsSymmetric)
  (hH : H.IsSymmetric) {U : Submodule 𝕜 E} [U.HasOrthogonalProjection] (hUinv : ∀ u ∈ U, T u ∈ U)
  {a b ε : ℝ} (hb : ∀ u ∈ U, b * ‖u‖ ^ 2 ≤ RCLike.re (inner 𝕜 (T u) u))
  (ha : ∀ w ∈ Uᗮ, RCLike.re (inner 𝕜 (T w) w) ≤ a * ‖w‖ ^ 2) (hε : ∀ (v : E), ‖H v‖ ≤ ε * ‖v‖)
  {x : E} (hx : ‖x‖ = 1) {μ : ℝ} (hμ : T x + H x = ↑μ • x) :
  (b - a) * Real.sin (2 * Real.arccos ‖U.starProjection x‖) ≤ 2 * ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sin_two_arccos_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Vector.html#LinearMap.IsSymmetric.sin_two_arccos_le).

## Other forms

**Davis's sin 2θ theorem, orthogonal-decomposition form.** Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sin_two_theta_le_of_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Vector.html#LinearMap.IsSymmetric.sin_two_theta_le_of_mem).

```lean
LinearMap.IsSymmetric.sin_two_theta_le_of_mem.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {T H : E →ₗ[𝕜] E} (hT : T.IsSymmetric)
  (hH : H.IsSymmetric) {U : Submodule 𝕜 E} (hUinv : ∀ u ∈ U, T u ∈ U) {a b ε : ℝ}
  (hb : ∀ u ∈ U, b * ‖u‖ ^ 2 ≤ RCLike.re (inner 𝕜 (T u) u))
  (ha : ∀ w ∈ Uᗮ, RCLike.re (inner 𝕜 (T w) w) ≤ a * ‖w‖ ^ 2) (hε : ∀ (v : E), ‖H v‖ ≤ ε * ‖v‖)
  {y z : E} (hyU : y ∈ U) (hzU : z ∈ Uᗮ) (hx : ‖y + z‖ = 1) {μ : ℝ}
  (hμ : T (y + z) + H (y + z) = ↑μ • (y + z)) : (b - a) * (‖y‖ * ‖z‖) ≤ ε
```

**Davis's sin 2θ theorem, per-eigenvector product form.** Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sin_two_theta_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Vector.html#LinearMap.IsSymmetric.sin_two_theta_le).

```lean
LinearMap.IsSymmetric.sin_two_theta_le.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {T H : E →ₗ[𝕜] E} (hT : T.IsSymmetric)
  (hH : H.IsSymmetric) {U : Submodule 𝕜 E} [U.HasOrthogonalProjection] (hUinv : ∀ u ∈ U, T u ∈ U)
  {a b ε : ℝ} (hb : ∀ u ∈ U, b * ‖u‖ ^ 2 ≤ RCLike.re (inner 𝕜 (T u) u))
  (ha : ∀ w ∈ Uᗮ, RCLike.re (inner 𝕜 (T w) w) ≤ a * ‖w‖ ^ 2) (hε : ∀ (v : E), ‖H v‖ ≤ ε * ‖v‖)
  {x : E} (hx : ‖x‖ = 1) {μ : ℝ} (hμ : T x + H x = ↑μ • x) :
  (b - a) * (‖U.starProjection x‖ * ‖x - U.starProjection x‖) ≤ ε
```

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.sin_two_arccos_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Vector.html#LinearMap.IsSymmetric.sin_two_arccos_le)
- [Source of `LinearMap.IsSymmetric.sin_two_arccos_le` in TauCeti/Analysis/InnerProductSpace/DoubleAngle/Vector.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Vector.lean#L226)
