---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub, Submodule.mul_norm_sinThetaMap_le_pi_div_two_mul_norm_sub
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

- [The pairwise Sylvester bound](../../part-03/inner-product-space/part-02/the-pairwise-sylvester-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Pairwise.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub).

## Other forms

**The pairwise `π / 2` Davis–Kahan `sin Θ` theorem in operator norm.** Formalized in Tau Ceti as [`Submodule.mul_norm_sinThetaMap_le_pi_div_two_mul_norm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Pairwise.html#Submodule.mul_norm_sinThetaMap_le_pi_div_two_mul_norm_sub).

```lean
Submodule.mul_norm_sinThetaMap_le_pi_div_two_mul_norm_sub.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  (U V : Submodule 𝕜 E) {A B : E →L[𝕜] E} (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric)
  (hU : ∀ x ∈ U, A x ∈ U) (hV : ∀ x ∈ V, B x ∈ V) {δ : ℝ}
  (h : Module.End.PointSpectraSeparated (↑A) U (↑B) Vᗮ δ) :
  δ * ‖U.sinThetaMap V‖ ≤ Real.pi / 2 * ‖B - A‖
```

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Pairwise.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_pi_div_two_mul_map_sub` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Pairwise.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Pairwise.lean#L61)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OperatorTheory/STATUS.md)
