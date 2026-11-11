---
declaration: theorem
origin: cited
lean: Submodule.mul_projectionGap_le_norm_sub
statement: formalized
proof: formalized
---

# The dimension-free Davis–Kahan `sin Θ` theorem for the gap

Let `U` be invariant under
the symmetric operator `A` and `V` invariant under the symmetric operator `B`. Suppose that the
quadratic form of `A` on `U` is at least `c + g` while that of `B` on `Vᗮ` is at most `c`, and
that the quadratic form of `B` on `V` is at least `c' + g` while that of `A` on `Uᗮ` is at
most `c'`. Then the gap between `U` and `V` satisfies `g ‖P_U - P_V‖ ≤ ‖B - A‖`.

```lean
Submodule.mul_projectionGap_le_norm_sub.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {A B : E →L[𝕜] E} (U V : Submodule 𝕜 E)
  [U.HasOrthogonalProjection] [V.HasOrthogonalProjection] (hA : (↑A).IsSymmetric)
  (hB : (↑B).IsSymmetric) (hU : ∀ x ∈ U, A x ∈ U) (hV : ∀ x ∈ V, B x ∈ V) {c c' g : ℝ}
  (hAU : ∀ x ∈ U, (c + g) * ‖x‖ ^ 2 ≤ RCLike.re (inner 𝕜 (A x) x))
  (hBV : ∀ x ∈ Vᗮ, RCLike.re (inner 𝕜 (B x) x) ≤ c * ‖x‖ ^ 2)
  (hBV' : ∀ x ∈ V, (c' + g) * ‖x‖ ^ 2 ≤ RCLike.re (inner 𝕜 (B x) x))
  (hAU' : ∀ x ∈ Uᗮ, RCLike.re (inner 𝕜 (A x) x) ≤ c' * ‖x‖ ^ 2) : g * U.projectionGap V ≤ ‖B - A‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The directed Davis–Kahan `sin Θ` theorem for the directed gap](the-directed-davis-kahan-sin-theorem-for-the-dir.md)

## Lean

Formalized in Tau Ceti as [`Submodule.mul_projectionGap_le_norm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.html#Submodule.mul_projectionGap_le_norm_sub).

## Sources

- [Tau Ceti documentation: `Submodule.mul_projectionGap_le_norm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.html#Submodule.mul_projectionGap_le_norm_sub)
- [Source of `Submodule.mul_projectionGap_le_norm_sub` in TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.lean#L162)
