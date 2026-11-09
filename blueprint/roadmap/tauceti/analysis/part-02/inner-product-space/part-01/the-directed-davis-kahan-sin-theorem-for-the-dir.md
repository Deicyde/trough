---
declaration: theorem
origin: cited
lean: Submodule.mul_directedProjectionGap_le_norm_sub
statement: formalized
proof: formalized
---

# The directed Davis–Kahan `sin Θ` theorem for the directed gap

Let `U` be invariant
under `A` and `V` invariant under the symmetric operator `B`. If the quadratic form of `A` on `U`
is at least `c + g` and that of `B` on `Vᗮ` is at most `c`, then the directed gap
`‖P_{Vᗮ} P_U‖` from `U` to `V` satisfies `g ‖P_{Vᗮ} P_U‖ ≤ ‖B - A‖`.

```lean
Submodule.mul_directedProjectionGap_le_norm_sub.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {A B : E →L[𝕜] E} (U V : Submodule 𝕜 E)
  [U.HasOrthogonalProjection] [V.HasOrthogonalProjection] (hB : (↑B).IsSymmetric)
  (hU : ∀ x ∈ U, A x ∈ U) (hV : ∀ x ∈ V, B x ∈ V) {c g : ℝ}
  (hAU : ∀ x ∈ U, (c + g) * ‖x‖ ^ 2 ≤ RCLike.re (inner 𝕜 (A x) x))
  (hBV : ∀ x ∈ Vᗮ, RCLike.re (inner 𝕜 (B x) x) ≤ c * ‖x‖ ^ 2) :
  g * U.directedProjectionGap V ≤ ‖B - A‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dimension-free directed Davis–Kahan `sin Θ` theorem](the-dimension-free-directed-davis-kahan-sin-theo.md)

## Lean

Formalized in Tau Ceti as [`Submodule.mul_directedProjectionGap_le_norm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.html#Submodule.mul_directedProjectionGap_le_norm_sub).

## Sources

- [Tau Ceti documentation: `Submodule.mul_directedProjectionGap_le_norm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.html#Submodule.mul_directedProjectionGap_le_norm_sub)
- [Source of `Submodule.mul_directedProjectionGap_le_norm_sub` in TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Projection/SinTheta.lean#L135)
