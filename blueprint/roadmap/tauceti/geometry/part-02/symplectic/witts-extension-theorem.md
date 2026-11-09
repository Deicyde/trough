---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv, TauCeti.SymplecticForm.exists_isSymplectomorphism_extend
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

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/WittExtension.html#TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv)
- [Source of `TauCeti.SymplecticForm.exists_isSymplectomorphism_extend_linearEquiv` in TauCeti/Geometry/Symplectic/WittExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/WittExtension.lean#L209)
