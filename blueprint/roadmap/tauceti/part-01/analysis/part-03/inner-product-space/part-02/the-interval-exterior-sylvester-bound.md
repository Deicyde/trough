---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap, TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_of_mem, TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_swap_of_mem, TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_swap
statement: formalized
proof: formalized
---

# The interval/exterior Sylvester bound

Let `A` and `B` be symmetric operators on
finite-dimensional inner product spaces. If the eigenvalues of `A` lie in `[a, b]` and those of `B`
outside `(a - δ, b + δ)`, then `δ N(X) ≤ N(A X - X B)` for every unitarily invariant seminorm `N`.
In particular every solution of the Sylvester equation `A X - X B = C` satisfies
`δ N(X) ≤ N(C)`.

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap.{u_1,
    u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {A : E →L[𝕜] E} {B : F →L[𝕜] F} {a b δ : ℝ}
  (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 F E) (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric)
  (h : Module.End.PointIntervalExteriorGap ↑A ⊤ ↑B ⊤ a b δ) (X : F →L[𝕜] E) :
  δ * N ↑X ≤ N ↑((A.sylvester B) X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Courant–Fischer, lower direction](../part-01/courant-fischer-lower-direction.md)
- [Ky Fan's maximum principle, attainment](ky-fans-maximum-principle-attainment.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap).

## Other forms

**The interval/exterior Sylvester bound on invariant subspaces.** Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_of_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_of_mem).

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_of_mem.{u_1,
    u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {A : E →L[𝕜] E} {B : F →L[𝕜] F} {a b δ : ℝ}
  (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 F E) (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric)
  {S : Submodule 𝕜 E} {T : Submodule 𝕜 F} (hS : ∀ x ∈ S, A x ∈ S) (hT : ∀ y ∈ T, B y ∈ T)
  (h : Module.End.PointIntervalExteriorGap (↑A) S (↑B) T a b δ) {X : F →L[𝕜] E}
  (hXS : ∀ (y : F), X y ∈ S) (hXT : ∀ y ∈ Tᗮ, X y = 0) : δ * N ↑X ≤ N ↑((A.sylvester B) X)
```

**The interval/exterior Sylvester bound on invariant subspaces, reversed orientation.** Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_swap_of_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_swap_of_mem).

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_swap_of_mem.{u_1,
    u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {A : E →L[𝕜] E} {B : F →L[𝕜] F} {a b δ : ℝ}
  (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 F E) (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric)
  {S : Submodule 𝕜 E} {T : Submodule 𝕜 F} (hS : ∀ x ∈ S, A x ∈ S) (hT : ∀ y ∈ T, B y ∈ T)
  (h : Module.End.PointIntervalExteriorGap (↑B) T (↑A) S a b δ) {X : F →L[𝕜] E}
  (hXS : ∀ (y : F), X y ∈ S) (hXT : ∀ y ∈ Tᗮ, X y = 0) : δ * N ↑X ≤ N ↑((A.sylvester B) X)
```

**The interval/exterior Sylvester bound, reversed orientation.** Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_swap`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_swap).

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap_swap.{u_1,
    u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {A : E →L[𝕜] E} {B : F →L[𝕜] F} {a b δ : ℝ}
  (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 F E) (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric)
  (h : Module.End.PointIntervalExteriorGap ↑B ⊤ ↑A ⊤ a b δ) (X : F →L[𝕜] E) :
  δ * N ↑X ≤ N ↑((A.sylvester B) X)
```

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_pointIntervalExteriorGap` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.lean#L260)
