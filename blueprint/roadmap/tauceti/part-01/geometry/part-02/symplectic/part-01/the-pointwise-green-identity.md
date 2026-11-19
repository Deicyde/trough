---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.apply_floerLinearization_eq_floerLinearizationAdjoint_apply_add
statement: formalized
proof: formalized
---

# The pointwise Green identity

For a map `ξ`, a covector field `η` and `w ↦ J(w, u w)`
differentiable at `z`,
`η(D ξ) = (D^* η)(ξ) + ∂s (η(ξ)) + ∂t ((η ∘ J)(ξ))`.

```lean
TauCeti.SymplecticForm.apply_floerLinearization_eq_floerLinearizationAdjoint_apply_add.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  {ω : TauCeti.SymplecticForm V} {J : ℝ × ℝ → V → V →L[ℝ] V} {Ks Kt : ℝ × ℝ → V → ℝ}
  {u ξ : ℝ × ℝ → V} {η : ℝ × ℝ → V →L[ℝ] ℝ} {z : ℝ × ℝ} (hξ : DifferentiableAt ℝ ξ z)
  (hη : DifferentiableAt ℝ η z) (hJu : DifferentiableAt ℝ (fun w => J w (u w)) z) :
  (η z) (ω.floerLinearization J Ks Kt u ξ z) =
    (ω.floerLinearizationAdjoint J Ks Kt u η z) (ξ z) +
        (fderiv ℝ (fun w => (η w) (ξ w)) z) TauCeti.stdComplexLineReal +
      (fderiv ℝ (fun w => (η w ∘SL J w (u w)) (ξ w)) z) TauCeti.stdComplexLineImag
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.apply_floerLinearization_eq_floerLinearizationAdjoint_apply_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Linearization/Adjoint.html#TauCeti.SymplecticForm.apply_floerLinearization_eq_floerLinearizationAdjoint_apply_add).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.apply_floerLinearization_eq_floerLinearizationAdjoint_apply_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Linearization/Adjoint.html#TauCeti.SymplecticForm.apply_floerLinearization_eq_floerLinearizationAdjoint_apply_add)
- [Source of `TauCeti.SymplecticForm.apply_floerLinearization_eq_floerLinearizationAdjoint_apply_add` in TauCeti/Geometry/Symplectic/Floer/Linearization/Adjoint.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/Linearization/Adjoint.lean#L226)
