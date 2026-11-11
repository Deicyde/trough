---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff
statement: formalized
proof: formalized
---

# Williamson's classification on a symplectic plane

Two elements `A` and `B` of the
symplectic Lie algebras of symplectic planes `(V, ω)` and `(W, ω')` are conjugate by a linear
symplectomorphism exactly when their squares are the same homothety and their Hamiltonians
`v ↦ ω(A v, v)` and `w ↦ ω'(B w, w)` take positive values together and negative values
together.

```lean
TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff.{u_1, u_2} {V : Type u_1}
  {W : Type u_2} [AddCommGroup V] [_root_.Module ℝ V] [AddCommGroup W] [_root_.Module ℝ W]
  {ω : TauCeti.SymplecticForm V} {ω' : TauCeti.SymplecticForm W} (hV : Module.finrank ℝ V = 2)
  (hW : Module.finrank ℝ W = 2) {A : Module.End ℝ V} {B : Module.End ℝ W}
  (hA : A ∈ skewAdjointLieSubalgebra ω.toBilinForm)
  (hB : B ∈ skewAdjointLieSubalgebra ω'.toBilinForm) :
  (∃ e, ω.IsSymplectomorphism ω' e ∧ ∀ (v : V), e (A v) = B (e v)) ↔
    (∀ (κ : ℝ), A * A = κ • 1 ↔ B * B = κ • 1) ∧
      ((∃ v, 0 < (fun v w => (ω.toBilinForm v) w) (A v) v) ↔
          ∃ w, 0 < (fun v w => (ω'.toBilinForm v) w) (B w) w) ∧
        ((∃ v, (fun v w => (ω.toBilinForm v) w) (A v) v < 0) ↔
          ∃ w, (fun v w => (ω'.toBilinForm v) w) (B w) w < 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Witt's extension theorem](witts-extension-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson/Plane.html#TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson/Plane.html#TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff)
- [Source of `TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff` in TauCeti/Geometry/Symplectic/Hamiltonian/Williamson/Plane.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson/Plane.lean#L177)
