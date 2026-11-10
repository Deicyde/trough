---
declaration: theorem
origin: cited
lean: TauCeti.BoundedHolomorphicFunctions.dist_apply_le_of_ball_subset, TauCeti.norm_fderiv_le_of_forall_mem_ball_norm_le, TauCeti.norm_deriv_le_of_forall_mem_closedBall_norm_le, TauCeti.norm_deriv_le_of_forall_mem_closedBall_two_mul_norm_le
statement: formalized
proof: formalized
---

# Cauchy estimate

On a ball of radius `R` inside `U`, a bounded holomorphic map `f` is
Lipschitz at the centre with constant `2 * ‖f‖ / R`.

```lean
TauCeti.BoundedHolomorphicFunctions.dist_apply_le_of_ball_subset.{u_1, u_2} {V : Type u_1}
  {E : Type u_2} [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup E] [NormedSpace ℂ E]
  {U : TopologicalSpace.Opens V} (f : ↥(TauCeti.boundedHolomorphicFunctions E U)) {x z : ↥U} {R : ℝ}
  (hR : Metric.ball (↑x) R ⊆ ↑U) (hz : dist z x < R) : dist (↑f z) (↑f x) ≤ 2 * ‖f‖ / R * dist z x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BoundedHolomorphicFunctions.dist_apply_le_of_ball_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/HolomorphicFunctions/Bounded.html#TauCeti.BoundedHolomorphicFunctions.dist_apply_le_of_ball_subset).

## Other forms

**Cauchy's estimate on a ball in a complex normed space.** Formalized in Tau Ceti as [`TauCeti.norm_fderiv_le_of_forall_mem_ball_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UniformLimit.html#TauCeti.norm_fderiv_le_of_forall_mem_ball_norm_le).

```lean
TauCeti.norm_fderiv_le_of_forall_mem_ball_norm_le.{u_1, u_2} {V : Type u_1} {E : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup E] [NormedSpace ℂ E] {f : V → E}
  {c : V} {r M : ℝ} (hd : DifferentiableOn ℂ f (Metric.ball c r)) (hr : 0 < r)
  (hM : ∀ y ∈ Metric.ball c r, ‖f y‖ ≤ M) : ‖fderiv ℂ f c‖ ≤ 2 * M / r
```

**Cauchy's estimate on a closed ball.** Formalized in Tau Ceti as [`TauCeti.norm_deriv_le_of_forall_mem_closedBall_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/NormalFamilies.html#TauCeti.norm_deriv_le_of_forall_mem_closedBall_norm_le).

```lean
TauCeti.norm_deriv_le_of_forall_mem_closedBall_norm_le.{u_2} {E : Type u_2} {U : Set ℂ} {f : ℂ → E}
  [NormedAddCommGroup E] [NormedSpace ℂ E] (hf : DifferentiableOn ℂ f U) {c : ℂ} {r M : ℝ}
  (hr : 0 < r) (hsub : Metric.closedBall c r ⊆ U) (hM : ∀ w ∈ Metric.closedBall c r, ‖f w‖ ≤ M) :
  ‖deriv f c‖ ≤ M / r
```

**Cauchy's estimate, uniformly on a ball.** Formalized in Tau Ceti as [`TauCeti.norm_deriv_le_of_forall_mem_closedBall_two_mul_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/NormalFamilies.html#TauCeti.norm_deriv_le_of_forall_mem_closedBall_two_mul_norm_le).

```lean
TauCeti.norm_deriv_le_of_forall_mem_closedBall_two_mul_norm_le.{u_2} {E : Type u_2} {U : Set ℂ}
  {f : ℂ → E} [NormedAddCommGroup E] [NormedSpace ℂ E] (hf : DifferentiableOn ℂ f U) {c : ℂ}
  {r M : ℝ} (hr : 0 < r) (hsub : Metric.closedBall c (2 * r) ⊆ U)
  (hM : ∀ w ∈ Metric.closedBall c (2 * r), ‖f w‖ ≤ M) {z : ℂ} (hz : z ∈ Metric.ball c r) :
  ‖deriv f z‖ ≤ M / r
```

## Sources

- [Tau Ceti documentation: `TauCeti.BoundedHolomorphicFunctions.dist_apply_le_of_ball_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/HolomorphicFunctions/Bounded.html#TauCeti.BoundedHolomorphicFunctions.dist_apply_le_of_ball_subset)
- [Source of `TauCeti.BoundedHolomorphicFunctions.dist_apply_le_of_ball_subset` in TauCeti/Analysis/Complex/HolomorphicFunctions/Bounded.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/HolomorphicFunctions/Bounded.lean#L188)
