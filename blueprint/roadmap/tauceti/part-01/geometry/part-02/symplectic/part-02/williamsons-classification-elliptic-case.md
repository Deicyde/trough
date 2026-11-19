---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.IsNondegenerateQuadraticFamily.exists_isDarbouxBasis_span_eq_span_elliptic, TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff
statement: formalized
proof: formalized
---

# Williamson's classification, elliptic case

If the span of a nondegenerate family `Q` of
quadratic forms contains a positive definite form, then there is a Darboux basis whose elliptic
blocks `Iₖ = (xₖ² + yₖ²) / 2` span the same space as `Q`.

```lean
TauCeti.SymplecticForm.IsNondegenerateQuadraticFamily.exists_isDarbouxBasis_span_eq_span_elliptic.{u_1,
    u_2}
  {V : Type u_1} [AddCommGroup V] [_root_.Module ℝ V] [FiniteDimensional ℝ V]
  {ω : TauCeti.SymplecticForm V} {P : QuadraticForm ℝ V} {ι : Type u_2} {Q : ι → QuadraticForm ℝ V}
  (h : ω.IsNondegenerateQuadraticFamily Q) (hP : P ∈ Submodule.span ℝ (Set.range Q))
  (hPpos : QuadraticMap.PosDef P) :
  ∃ n b,
    ω.IsDarbouxBasis b ∧
      Submodule.span ℝ (Set.range Q) =
        Submodule.span ℝ (Set.range (TauCeti.SymplecticForm.elliptic b))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Williamson's theorem](williamsons-theorem.md)
- [Witt's extension theorem](witts-extension-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.IsNondegenerateQuadraticFamily.exists_isDarbouxBasis_span_eq_span_elliptic`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson/Elliptic.html#TauCeti.SymplecticForm.IsNondegenerateQuadraticFamily.exists_isDarbouxBasis_span_eq_span_elliptic).

## Other forms

**Williamson's classification on a symplectic plane.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson/Plane.html#TauCeti.SymplecticForm.exists_isSymplectomorphism_forall_apply_eq_iff).

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

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.IsNondegenerateQuadraticFamily.exists_isDarbouxBasis_span_eq_span_elliptic`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson/Elliptic.html#TauCeti.SymplecticForm.IsNondegenerateQuadraticFamily.exists_isDarbouxBasis_span_eq_span_elliptic)
- [Source of `TauCeti.SymplecticForm.IsNondegenerateQuadraticFamily.exists_isDarbouxBasis_span_eq_span_elliptic` in TauCeti/Geometry/Symplectic/Hamiltonian/Williamson/Elliptic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson/Elliptic.lean#L147)
