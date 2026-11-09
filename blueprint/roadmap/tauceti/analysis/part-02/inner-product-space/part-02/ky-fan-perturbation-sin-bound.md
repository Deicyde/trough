---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_starProjection_le_kyFan_sub
statement: formalized
proof: formalized
---

# Ky Fan perturbation `sin Θ` bound

For every `k`, interval/exterior
spectral separation implies `δ Kₖ(P_{Vᗮ} P_U) ≤ Kₖ(B - A)`.

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_starProjection_le_kyFan_sub.{u_1,
    u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] {a b δ : ℝ} (k : ℕ) {A B : E →L[𝕜] E} (hA : (↑A).IsSymmetric)
  (hB : (↑B).IsSymmetric) {U V : Submodule 𝕜 E} (hU : ∀ x ∈ U, A x ∈ U) (hV : ∀ x ∈ V, B x ∈ V)
  (h : Module.End.PointIntervalExteriorGap (↑A) U (↑B) Vᗮ a b δ) :
  δ * (TauCeti.UnitarilyInvariantSeminorm.kyFan 𝕜 E E k) ↑(Vᗮ.starProjection ∘SL U.starProjection) ≤
    (TauCeti.UnitarilyInvariantSeminorm.kyFan 𝕜 E E k) (↑B - ↑A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ky Fan's maximum principle, attainment](ky-fans-maximum-principle-attainment.md)
- [The perturbation Davis–Kahan `sin Θ` theorem](../../../part-01/operator-theory/the-perturbation-davis-kahan-sin-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_starProjection_le_kyFan_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Corollaries.html#TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_starProjection_le_kyFan_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_starProjection_le_kyFan_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Corollaries.html#TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_starProjection_le_kyFan_sub)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_starProjection_le_kyFan_sub` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Corollaries.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Corollaries.lean#L109)
