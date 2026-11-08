---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub, TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub_swap
statement: formalized
proof: formalized
---

# The perturbation Davis–Kahan `sin Θ` theorem

Let `A` and `B` be symmetric operators on a
finite-dimensional inner product space, let `U` be invariant under `A` and `V` invariant under
`B`. If the eigenvalues of `A` on `U` lie in `[a, b]` and those of `B` on `Vᗮ` lie outside
`(a - δ, b + δ)`, then the directed sine map `P_{Vᗮ} P_U` from `U` towards `V` satisfies
`δ N(P_{Vᗮ} P_U) ≤ N(B - A)` for every unitarily invariant seminorm `N`.

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub.{u_1, u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] {a b δ : ℝ} (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 E E)
  {A B : E →L[𝕜] E} (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric) {U V : Submodule 𝕜 E}
  (hU : ∀ x ∈ U, A x ∈ U) (hV : ∀ x ∈ V, B x ∈ V)
  (h : Module.End.PointIntervalExteriorGap (↑A) U (↑B) Vᗮ a b δ) :
  δ * N ↑(Vᗮ.starProjection ∘SL U.starProjection) ≤ N (↑B - ↑A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Courant–Fischer, lower direction](../../part-02/inner-product-space/part-01/courant-fischer-lower-direction.md)
- [Fan dominance](fan-dominance.md)
- [The interval/exterior Sylvester bound](../../part-02/inner-product-space/part-01/the-interval-exterior-sylvester-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub).

## Other forms

**The perturbation Davis–Kahan `sin Θ` theorem, reversed orientation.** Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub_swap`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub_swap).

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub_swap.{u_1,
    u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] {a b δ : ℝ} (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 E E)
  {A B : E →L[𝕜] E} (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric) {U V : Submodule 𝕜 E}
  (hU : ∀ x ∈ U, A x ∈ U) (hV : ∀ x ∈ V, B x ∈ V)
  (h : Module.End.PointIntervalExteriorGap (↑B) Vᗮ (↑A) U a b δ) :
  δ * N ↑(Vᗮ.starProjection ∘SL U.starProjection) ≤ N (↑B - ↑A)
```

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_map_starProjection_comp_starProjection_le_map_sub` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/Basic.lean#L130)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorTheory/STATUS.md)
