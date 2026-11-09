---
declaration: theorem
origin: cited
lean: TauCeti.mlieDerivFormWithin_eq_interior_mextDerivWithin_add, TauCeti.mlieDerivForm_apply_eq_mextDeriv_add, TauCeti.mlieDerivForm_eq_interior_mextDeriv_add, TauCeti.mlieDerivForm_eq_interior_mextDeriv_add_apply
statement: formalized
proof: formalized
---

# Cartan's magic formula

**Cartan's magic formula** within a set, `L_V φ = ι_V dφ + d (ι_V φ)`, for a form and a vector
field differentiable within the set at the point.

```lean
TauCeti.mlieDerivFormWithin_eq_interior_mextDerivWithin_add.{u_1, u_2, u_3, u_4} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ} {V : (x : M) → TangentSpace I x} {s : Set M}
  {x : M} [IsManifold I 1 M] {φ : TauCeti.RoughForm I M F (k + 1)}
  (hφ : (MDiffAt[s] fun y => ⟨y, φ y⟩) x) (hV : (MDiffAt[s] fun y => ⟨y, V y⟩) x)
  (hs : UniqueMDiffAt[s] x) :
  TauCeti.mlieDerivFormWithin V φ s x =
    TauCeti.RoughForm.interior V (TauCeti.mextDerivWithin φ s) x +
      TauCeti.mextDerivWithin (TauCeti.RoughForm.interior V φ) s x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's formula](../../../../analysis/part-02/calculus/part-01/cartans-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mlieDerivFormWithin_eq_interior_mextDerivWithin_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/LieDeriv.html#TauCeti.mlieDerivFormWithin_eq_interior_mextDerivWithin_add).

## Other forms

**Cartan's magic formula for a one-form `φ`, evaluated on a tangent vector.** Formalized in Tau Ceti as [`TauCeti.mlieDerivForm_apply_eq_mextDeriv_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/LieDeriv.html#TauCeti.mlieDerivForm_apply_eq_mextDeriv_add).

```lean
TauCeti.mlieDerivForm_apply_eq_mextDeriv_add.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {V : (x : M) → TangentSpace I x} {x : M} [IsManifold I 1 M]
  {φ : TauCeti.RoughForm I M F 1} {f : M → F} (hf : ∀ (y : M), (φ y) ![V y] = f y)
  (hφ : (MDiffAt fun y => ⟨y, φ y⟩) x) (hV : (MDiffAt fun y => ⟨y, V y⟩) x) (v : TangentSpace I x) :
  (TauCeti.mlieDerivForm V φ x) ![v] = (TauCeti.mextDeriv φ x) ![V x, v] + (d% f x) v
```

**Cartan's magic formula.** Formalized in Tau Ceti as [`TauCeti.mlieDerivForm_eq_interior_mextDeriv_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/LieDeriv.html#TauCeti.mlieDerivForm_eq_interior_mextDeriv_add).

```lean
TauCeti.mlieDerivForm_eq_interior_mextDeriv_add.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {k : ℕ} {V : (x : M) → TangentSpace I x} [IsManifold I 1 M]
  {φ : TauCeti.RoughForm I M F (k + 1)} (hφ : MDiff fun y => ⟨y, φ y⟩)
  (hV : MDiff fun y => ⟨y, V y⟩) :
  TauCeti.mlieDerivForm V φ =
    TauCeti.RoughForm.interior V (TauCeti.mextDeriv φ) +
      TauCeti.mextDeriv (TauCeti.RoughForm.interior V φ)
```

**Cartan's magic formula.** Formalized in Tau Ceti as [`TauCeti.mlieDerivForm_eq_interior_mextDeriv_add_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/LieDeriv.html#TauCeti.mlieDerivForm_eq_interior_mextDeriv_add_apply).

```lean
TauCeti.mlieDerivForm_eq_interior_mextDeriv_add_apply.{u_1, u_2, u_3, u_4} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ} {V : (x : M) → TangentSpace I x} {x : M}
  [IsManifold I 1 M] {φ : TauCeti.RoughForm I M F (k + 1)} (hφ : (MDiffAt fun y => ⟨y, φ y⟩) x)
  (hV : (MDiffAt fun y => ⟨y, V y⟩) x) :
  TauCeti.mlieDerivForm V φ x =
    TauCeti.RoughForm.interior V (TauCeti.mextDeriv φ) x +
      TauCeti.mextDeriv (TauCeti.RoughForm.interior V φ) x
```

## Sources

- [Tau Ceti documentation: `TauCeti.mlieDerivFormWithin_eq_interior_mextDerivWithin_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/LieDeriv.html#TauCeti.mlieDerivFormWithin_eq_interior_mextDerivWithin_add)
- [Source of `TauCeti.mlieDerivFormWithin_eq_interior_mextDerivWithin_add` in TauCeti/Geometry/Manifold/DifferentialForm/LieDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/LieDeriv.lean#L248)
