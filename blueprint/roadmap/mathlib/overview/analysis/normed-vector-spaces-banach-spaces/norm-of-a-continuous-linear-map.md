# Norm of a continuous linear map

Construct a continuous linear map from a linear map and a bound on this linear map.
The fact that the norm of the continuous linear map is then controlled is given in
`LinearMap.mkContinuous_norm_le`.

```lean
LinearMap.mkContinuous.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {𝕜₂ : Type u_2} {E : Type u_3}
  {F : Type u_4} [Ring 𝕜] [Ring 𝕜₂] [SeminormedAddCommGroup E] [SeminormedAddCommGroup F]
  [_root_.Module 𝕜 E] [_root_.Module 𝕜₂ F] {σ : 𝕜 →+* 𝕜₂} (f : E →ₛₗ[σ] F) (C : ℝ)
  (h : ∀ (x : E), ‖f x‖ ≤ C * ‖x‖) : E →SL[σ] F
```

## Depends on

- [Bornology](../topological-vector-spaces/bornology.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Sources

- [Mathlib documentation: `LinearMap.mkContinuous`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Operator/ContinuousLinearMap.html#LinearMap.mkContinuous)
- [Source of `LinearMap.mkContinuous` in Mathlib/Analysis/Normed/Operator/ContinuousLinearMap.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Operator/ContinuousLinearMap.lean#L52)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L284)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L430)
