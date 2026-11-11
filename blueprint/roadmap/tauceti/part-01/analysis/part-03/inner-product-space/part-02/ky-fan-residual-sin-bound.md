---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_le_kyFan_sylvester_apply
statement: formalized
proof: formalized
---

# Ky Fan residual `sin Θ` bound

Under interval/exterior spectral separation,
`δ Kₖ(P_{Uᗮ} X) ≤ Kₖ(A X - X M)` for every trial map `X` and every `k`.

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_le_kyFan_sylvester_apply.{u_1, u_2,
    u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {a b δ : ℝ} (k : ℕ) {A : E →L[𝕜] E} {M : F →L[𝕜] F}
  (hA : (↑A).IsSymmetric) (hM : (↑M).IsSymmetric) {U : Submodule 𝕜 E} (hU : ∀ x ∈ U, A x ∈ U)
  (h : Module.End.PointIntervalExteriorGap ↑M ⊤ (↑A) Uᗮ a b δ) (X : F →L[𝕜] E) :
  δ * (TauCeti.UnitarilyInvariantSeminorm.kyFan 𝕜 F E k) ↑(Uᗮ.starProjection ∘SL X) ≤
    (TauCeti.UnitarilyInvariantSeminorm.kyFan 𝕜 F E k) ↑((A.sylvester M) X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ky Fan's maximum principle, attainment](ky-fans-maximum-principle-attainment.md)
- [The residual Davis–Kahan `sin Θ` theorem](../part-03/the-residual-davis-kahan-sin-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_le_kyFan_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Corollaries.html#TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_le_kyFan_sylvester_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_le_kyFan_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Corollaries.html#TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_le_kyFan_sylvester_apply)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_kyFan_starProjection_comp_le_kyFan_sylvester_apply` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Corollaries.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Corollaries.lean#L98)
