---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub
statement: formalized
proof: formalized
---

# The pairwise `π / 2` Davis–Kahan `sin Θ` theorem

Let `A` and `B` be symmetric operators
on a finite-dimensional inner product space, let `U` be invariant under `A` and `V` invariant
under `B`. If every eigenvalue of `A` on `U` is at distance at least `δ` from every eigenvalue of
`B` on `Vᗮ`, then the directed sine map `P_{Vᗮ} P_U` from `U` towards `V` satisfies
`δ N(P_{Vᗮ} P_U) ≤ (π / 2) N(B - A)` for every unitarily invariant seminorm `N`.

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub.{u_1,
    u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] {δ : ℝ} (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 E E) {A B : E →L[𝕜] E}
  (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric) {U V : Submodule 𝕜 E} (hU : ∀ x ∈ U, A x ∈ U)
  (hV : ∀ x ∈ V, B x ∈ V) (h : Module.End.PointSpectraSeparated (↑A) U (↑B) Vᗮ δ) :
  δ * N ↑(Vᗮ.starProjection ∘SL U.starProjection) ≤ Real.pi / 2 * N (↑B - ↑A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Courant–Fischer, lower direction](../../part-03/inner-product-space/part-01/courant-fischer-lower-direction.md)
- [Ky Fan's maximum principle, attainment](../../part-03/inner-product-space/part-02/ky-fans-maximum-principle-attainment.md)
- [The pairwise Sylvester bound](../../part-03/inner-product-space/part-02/the-pairwise-sylvester-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Pairwise.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Pairwise.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Pairwise.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Pairwise.lean#L54)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorTheory/STATUS.md)
