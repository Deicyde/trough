---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_le_map_sylvester_apply
statement: formalized
proof: formalized
---

# The residual Davis–Kahan `sin Θ` theorem

Let `A` and `M` be symmetric operators on
finite-dimensional inner product spaces `E` and `F`, let `U` be invariant under `A`, and let
`X : F → E` be linear. If the eigenvalues of `M` lie in `[a, b]` and those of `A` on `Uᗮ` lie
outside `(a - δ, b + δ)`, then `δ N(P_{Uᗮ} X) ≤ N(A X - X M)` for every unitarily invariant
seminorm `N`.

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_le_map_sylvester_apply.{u_1, u_2,
    u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {a b δ : ℝ} (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 F E) {A : E →L[𝕜] E}
  {M : F →L[𝕜] F} (hA : (↑A).IsSymmetric) (hM : (↑M).IsSymmetric) {U : Submodule 𝕜 E}
  (hU : ∀ x ∈ U, A x ∈ U) (h : Module.End.PointIntervalExteriorGap ↑M ⊤ (↑A) Uᗮ a b δ)
  (X : F →L[𝕜] E) : δ * N ↑(Uᗮ.starProjection ∘SL X) ≤ N ↑((A.sylvester M) X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fan dominance](../part-01/fan-dominance.md)
- [The interval/exterior Sylvester bound](../part-01/the-interval-exterior-sylvester-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_le_map_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_le_map_sylvester_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_le_map_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_le_map_sylvester_apply)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_le_map_sylvester_apply` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Basic.lean#L84)
