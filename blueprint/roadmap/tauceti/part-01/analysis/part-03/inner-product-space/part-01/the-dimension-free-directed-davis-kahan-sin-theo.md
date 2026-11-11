---
declaration: theorem
origin: cited
lean: Submodule.mul_norm_starProjection_comp_starProjection_le_norm_sub
statement: formalized
proof: formalized
---

# The dimension-free directed Davis–Kahan `sin Θ` theorem

Let `U` be invariant under `A`
and `W` invariant under the symmetric operator `B`. If the quadratic form of `A` on `U` is at
least `c + g` and that of `B` on `W` is at most `c`, then `g ‖P_W P_U‖ ≤ ‖B - A‖`. For `g > 0`
this bounds `‖P_W P_U‖` by `‖B - A‖ / g`. Neither completeness nor finite dimension is assumed.

```lean
Submodule.mul_norm_starProjection_comp_starProjection_le_norm_sub.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {A B : E →L[𝕜] E}
  (U W : Submodule 𝕜 E) [U.HasOrthogonalProjection] [W.HasOrthogonalProjection]
  (hB : (↑B).IsSymmetric) (hU : ∀ x ∈ U, A x ∈ U) (hW : ∀ x ∈ W, B x ∈ W) {c g : ℝ}
  (hAU : ∀ x ∈ U, (c + g) * ‖x‖ ^ 2 ≤ RCLike.re (inner 𝕜 (A x) x))
  (hBW : ∀ x ∈ W, RCLike.re (inner 𝕜 (B x) x) ≤ c * ‖x‖ ^ 2) :
  g * ‖W.starProjection ∘SL U.starProjection‖ ≤ ‖B - A‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The reverse separated Sylvester bound](../part-03/the-reverse-separated-sylvester-bound.md)

## Lean

Formalized in Tau Ceti as [`Submodule.mul_norm_starProjection_comp_starProjection_le_norm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.html#Submodule.mul_norm_starProjection_comp_starProjection_le_norm_sub).

## Sources

- [Tau Ceti documentation: `Submodule.mul_norm_starProjection_comp_starProjection_le_norm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.html#Submodule.mul_norm_starProjection_comp_starProjection_le_norm_sub)
- [Source of `Submodule.mul_norm_starProjection_comp_starProjection_le_norm_sub` in TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.lean#L74)
