---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_map_sinTwoAngleOperator_le_two_mul_map_sub
statement: formalized
proof: formalized
---

# The Davis–Kahan `sin 2Θ` theorem

Let `A` and `B` be symmetric operators on a
finite-dimensional inner product space, let `U` be invariant under `A` and `V` invariant under
`B`. If `re ⟪A z, z⟫ ≤ a ‖z‖²` on `Uᗮ` and `b ‖y‖² ≤ re ⟪A y, y⟫` on `U`, then the double-angle
operator `2 P_{Uᗮ} P_V P_U` satisfies `(b - a) N(2 P_{Uᗮ} P_V P_U) ≤ 2 N(B - A)` for every
unitarily invariant seminorm `N`. No spectral hypothesis is placed on `B`.

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_sinTwoAngleOperator_le_two_mul_map_sub.{u_1, u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 E E) {A B : E →L[𝕜] E}
  (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric) {U V : Submodule 𝕜 E} (hU : ∀ x ∈ U, A x ∈ U)
  (hV : ∀ x ∈ V, B x ∈ V) {a b : ℝ} (ha : ∀ z ∈ Uᗮ, RCLike.re (inner 𝕜 (A z) z) ≤ a * ‖z‖ ^ 2)
  (hb : ∀ y ∈ U, b * ‖y‖ ^ 2 ≤ RCLike.re (inner 𝕜 (A y) y)) :
  (b - a) * N ↑(U.sinTwoAngleOperator V) ≤ 2 * N (↑B - ↑A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Courant–Fischer, lower direction](courant-fischer-lower-direction.md)
- [Fan dominance](../../../part-01/operator-theory/fan-dominance.md)
- [The interval/exterior Sylvester bound](the-interval-exterior-sylvester-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_sinTwoAngleOperator_le_two_mul_map_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/DoubleAngle.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_sinTwoAngleOperator_le_two_mul_map_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_map_sinTwoAngleOperator_le_two_mul_map_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/DoubleAngle.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_sinTwoAngleOperator_le_two_mul_map_sub)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_map_sinTwoAngleOperator_le_two_mul_map_sub` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/DoubleAngle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/SinTheta/DoubleAngle.lean#L69)
