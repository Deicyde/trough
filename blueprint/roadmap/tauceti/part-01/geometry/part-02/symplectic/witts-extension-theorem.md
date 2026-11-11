---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv, TauCeti.SymplecticForm.exists_isSymplectomorphism_extend, TauCeti.exists_continuousLinearEquiv_fix_inl_of_compContinuousLinearMap_inl_eq
statement: formalized
proof: formalized
---

# Witt's extension theorem

**Witt's extension theorem**, for a linear isomorphism `f : S ≃ₗ[ℝ] T` between subspaces of two
symplectic vector spaces of the same finite dimension: if `f` preserves the restricted forms, it
is the restriction of a linear symplectomorphism.

```lean
TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv.{u_1, u_2} {V : Type u_1}
  {W : Type u_2} [AddCommGroup V] [_root_.Module ℝ V] [AddCommGroup W] [_root_.Module ℝ W]
  [FiniteDimensional ℝ V] [FiniteDimensional ℝ W] (ω₁ : TauCeti.SymplecticForm V)
  (ω₂ : TauCeti.SymplecticForm W) (hdim : Module.finrank ℝ V = Module.finrank ℝ W)
  {S : Submodule ℝ V} {T : Submodule ℝ W} (f : ↥S ≃ₗ[ℝ] ↥T)
  (hω :
    ∀ (x y : ↥S),
      (fun v w => (ω₂.toBilinForm v) w) ↑(f x) ↑(f y) = (fun v w => (ω₁.toBilinForm v) w) ↑x ↑y) :
  ∃ e, ω₁.IsSymplectomorphism ω₂ e ∧ ∀ (x : ↥S), e ↑x = ↑(f x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/WittExtension.html#TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv).

## Other forms

**Witt's extension theorem for symplectic vector spaces.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_isSymplectomorphism_extend`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/WittExtension.html#TauCeti.SymplecticForm.exists_isSymplectomorphism_extend).

```lean
TauCeti.SymplecticForm.exists_isSymplectomorphism_extend.{u_1, u_2} {V : Type u_1} {W : Type u_2}
  [AddCommGroup V] [_root_.Module ℝ V] [AddCommGroup W] [_root_.Module ℝ W] [FiniteDimensional ℝ V]
  [FiniteDimensional ℝ W] (ω₁ : TauCeti.SymplecticForm V) (ω₂ : TauCeti.SymplecticForm W)
  (hdim : Module.finrank ℝ V = Module.finrank ℝ W) {S : Submodule ℝ V} (f : ↥S →ₗ[ℝ] W)
  (hf : Function.Injective ⇑f)
  (hω :
    ∀ (x y : ↥S),
      (fun v w => (ω₂.toBilinForm v) w) (f x) (f y) = (fun v w => (ω₁.toBilinForm v) w) ↑x ↑y) :
  ∃ e, ω₁.IsSymplectomorphism ω₂ e ∧ ∀ (x : ↥S), e ↑x = f x
```

**Witt's extension theorem for the zero section.** Formalized in Tau Ceti as [`TauCeti.exists_continuousLinearEquiv_fix_inl_of_compContinuousLinearMap_inl_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/ContinuousAlternatingMap.html#TauCeti.exists_continuousLinearEquiv_fix_inl_of_compContinuousLinearMap_inl_eq).

```lean
TauCeti.exists_continuousLinearEquiv_fix_inl_of_compContinuousLinearMap_inl_eq.{u_1, u_2}
  {E : Type u_1} {N : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup N] [NormedSpace ℝ N] [FiniteDimensional ℝ N]
  {a₀ a₁ : (E × N) [⋀^Fin 2]→L[ℝ] ℝ} (hnd₀ : ∀ (v : E × N), (∀ (w : E × N), a₀ ![v, w] = 0) → v = 0)
  (hnd₁ : ∀ (v : E × N), (∀ (w : E × N), a₁ ![v, w] = 0) → v = 0)
  (htan :
    a₁.compContinuousLinearMap (ContinuousLinearMap.inl ℝ E N) =
      a₀.compContinuousLinearMap (ContinuousLinearMap.inl ℝ E N)) :
  ∃ A, (∀ (v w : E × N), a₁ ![A v, A w] = a₀ ![v, w]) ∧ ∀ (q : E), A (q, 0) = (q, 0)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/WittExtension.html#TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv)
- [Source of `TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv` in TauCeti/Geometry/Symplectic/WittExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/WittExtension.lean#L213)
