---
declaration: theorem
origin: cited
lean: ContinuousLinearEquiv.IsMaxVolumeEllipsoid.exists_sum_rankOne_eq_id, TauCeti.exists_sum_smul_eq_of_finiteDimensional
statement: formalized
proof: formalized
---

# John's theorem

A maximal-volume ellipsoid `T : E ≃L[𝕜] F` decomposes the identity of the
inner product space `E` over its contact points: there are unit vectors `uᵢ` with `‖T uᵢ‖ = 1` and
positive weights `cᵢ` summing to the dimension of `E` such that `∑ cᵢ ⟪uᵢ, x⟫ uᵢ = x` for every
`x`.

In terms of the norm `x ↦ ‖T x‖` on `E`, whose closed unit ball is then in John's position, the
`uᵢ` are points of the Euclidean unit sphere on the boundary of that ball, and `re ⟪·, uᵢ⟫` is a
support functional of the ball at `uᵢ` (`ContinuousLinearMap.re_inner_le_norm_mul_norm_apply`).

```lean
ContinuousLinearEquiv.IsMaxVolumeEllipsoid.exists_sum_rankOne_eq_id.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [FiniteDimensional 𝕜 E] {T : E ≃L[𝕜] F}
  (hT : T.IsMaxVolumeEllipsoid) :
  ∃ m u c,
    (∀ (i : Fin m), ‖u i‖ = 1 ∧ ‖T (u i)‖ = 1) ∧
      (∀ (i : Fin m), 0 < c i) ∧
        ∑ i, c i = ↑(Module.finrank 𝕜 E) ∧
          ∑ i, ↑(c i) • ((InnerProductSpace.rankOne 𝕜) (u i)) (u i) = ContinuousLinearMap.id 𝕜 E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearEquiv.IsMaxVolumeEllipsoid.exists_sum_rankOne_eq_id`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/JohnEllipsoid.html#ContinuousLinearEquiv.IsMaxVolumeEllipsoid.exists_sum_rankOne_eq_id).

## Other forms

**John's theorem on the dual, read back in an `n`-dimensional normed space `F`.** Formalized in Tau Ceti as [`TauCeti.exists_sum_smul_eq_of_finiteDimensional`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/JohnEllipsoid.html#TauCeti.exists_sum_smul_eq_of_finiteDimensional).

```lean
TauCeti.exists_sum_smul_eq_of_finiteDimensional.{u_1, u_3} {𝕜 : Type u_1} {F : Type u_3} [RCLike 𝕜]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [FiniteDimensional 𝕜 F] :
  ∃ k c φ w,
    (∀ (i : Fin k), ‖w i‖ ≤ 1) ∧
      (∀ (z : F), ∑ i, (↑(c i) * (φ i) z) • w i = z) ∧
        ∀ (z : F) (b : Fin k → 𝕜) {B : ℝ},
          (∀ (i : Fin k), ‖b i‖ ≤ B) →
            ‖∑ i, ↑(c i) * b i * (φ i) z‖ ≤ √↑(Module.finrank 𝕜 F) * B * ‖z‖
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearEquiv.IsMaxVolumeEllipsoid.exists_sum_rankOne_eq_id`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/JohnEllipsoid.html#ContinuousLinearEquiv.IsMaxVolumeEllipsoid.exists_sum_rankOne_eq_id)
- [Source of `ContinuousLinearEquiv.IsMaxVolumeEllipsoid.exists_sum_rankOne_eq_id` in TauCeti/Analysis/InnerProductSpace/JohnEllipsoid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/JohnEllipsoid.lean#L375)
