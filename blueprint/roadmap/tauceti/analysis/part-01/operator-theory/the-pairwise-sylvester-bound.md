---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply, TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply_of_mem
statement: formalized
proof: formalized
---

# The pairwise Sylvester bound

Let `A` and `B` be symmetric operators on finite-dimensional
inner product spaces. If every eigenvalue of `A` is at distance at least `δ` from every eigenvalue
of `B`, then `δ N(X) ≤ (π / 2) N(A X - X B)` for every unitarily invariant seminorm `N`. In
particular every solution of the Sylvester equation `A X - X B = C` satisfies
`δ N(X) ≤ (π / 2) N(C)`.

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {A : E →L[𝕜] E} {B : F →L[𝕜] F} {δ : ℝ}
  (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 F E) (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric)
  (h : Module.End.PointSpectraSeparated ↑A ⊤ ↑B ⊤ δ) (X : F →L[𝕜] E) :
  δ * N ↑X ≤ Real.pi / 2 * N ↑((A.sylvester B) X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Courant–Fischer, lower direction](../../part-02/inner-product-space/part-01/courant-fischer-lower-direction.md)
- [Ky Fan's maximum principle, attainment](../../part-02/inner-product-space/part-02/ky-fans-maximum-principle-attainment.md)
- [The simultaneous Ky Fan estimate for the Sylvester equation](the-simultaneous-ky-fan-estimate-for-the-sylvest.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Pairwise.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply).

## Other forms

**The pairwise Sylvester bound on invariant subspaces.** Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply_of_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Pairwise.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply_of_mem).

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply_of_mem.{u_1, u_2,
    u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {A : E →L[𝕜] E} {B : F →L[𝕜] F} {δ : ℝ}
  (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 F E) (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric)
  {S : Submodule 𝕜 E} {T : Submodule 𝕜 F} (hS : ∀ x ∈ S, A x ∈ S) (hT : ∀ y ∈ T, B y ∈ T)
  (h : Module.End.PointSpectraSeparated (↑A) S (↑B) T δ) {X : F →L[𝕜] E} (hXS : ∀ (y : F), X y ∈ S)
  (hXT : ∀ y ∈ Tᗮ, X y = 0) : δ * N ↑X ≤ Real.pi / 2 * N ↑((A.sylvester B) X)
```

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Pairwise.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_map_le_pi_div_two_mul_map_sylvester_apply` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Pairwise.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Pairwise.lean#L259)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorTheory/STATUS.md)
