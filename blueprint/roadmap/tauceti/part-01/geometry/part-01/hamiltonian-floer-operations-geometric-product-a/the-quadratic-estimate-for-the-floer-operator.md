---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.exists_pos_forall_norm_floerOperator_sub_floerOperator_sub_floerLinearization_le
statement: formalized
proof: formalized
---

# The quadratic estimate for the Floer operator

Let `K` be a compact set of pairs `(p, y)`
of a parameter and a target point at which `J` is jointly `C²` and the Hamiltonians `Ks`, `Kt`
are jointly `C³`. There are `δ > 0` and `C` such that for every parameter map `φ : ℝ × ℝ → P` and
maps `w`, `ξ₁`, `ξ₂` differentiable at a domain point `z` with `(φ z, w z) ∈ K` and
`‖ξ₁ z‖, ‖ξ₂ z‖ ≤ δ`, the Floer operator with coefficients `J (φ z)`, `Ks (φ z)`, `Kt (φ z)`
satisfies
`‖F(w + ξ₁) - F(w + ξ₂) - D_w(ξ₁ - ξ₂)‖ ≤ C (max ‖ξ₁‖ ‖ξ₂‖ (1 + ‖∂t w - X_Kt(w)‖) ‖ξ₁ - ξ₂‖
  + ‖ξ₁ - ξ₂‖ ‖∂t ξ₁‖ + ‖ξ₂‖ ‖∂t ξ₁ - ∂t ξ₂‖)` at `z`. This is the Lipschitz bound on the
nonlinear part of the Floer operator used by the Newton iteration.

```lean
TauCeti.SymplecticForm.exists_pos_forall_norm_floerOperator_sub_floerOperator_sub_floerLinearization_le.{u,
    u_1}
  {V : Type u} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  (ω : TauCeti.SymplecticForm V) {P : Type u_1} [NormedAddCommGroup P] [NormedSpace ℝ P]
  {J : P → V → V →L[ℝ] V} {Ks Kt : P → V → ℝ} {K : Set (P × V)} (hK : IsCompact K)
  (hJ : ∀ q ∈ K, ContDiffAt ℝ 2 (Function.uncurry J) q)
  (hKs : ∀ q ∈ K, ContDiffAt ℝ 3 (Function.uncurry Ks) q)
  (hKt : ∀ q ∈ K, ContDiffAt ℝ 3 (Function.uncurry Kt) q) :
  ∃ δ > 0,
    ∃ C,
      ∀ (φ : ℝ × ℝ → P) (w ξ₁ ξ₂ : ℝ × ℝ → V) (z : ℝ × ℝ),
        DifferentiableAt ℝ w z →
          DifferentiableAt ℝ ξ₁ z →
            DifferentiableAt ℝ ξ₂ z →
              (φ z, w z) ∈ K →
                ‖ξ₁ z‖ ≤ δ →
                  ‖ξ₂ z‖ ≤ δ →
                    ‖ω.floerOperator (fun z => J (φ z)) (fun z => Ks (φ z)) (fun z => Kt (φ z))
                              (w + ξ₁) z -
                            ω.floerOperator (fun z => J (φ z)) (fun z => Ks (φ z))
                              (fun z => Kt (φ z)) (w + ξ₂) z -
                          ω.floerLinearization (fun z => J (φ z)) (fun z => Ks (φ z))
                            (fun z => Kt (φ z)) w (ξ₁ - ξ₂) z‖ ≤
                      C *
                        (max ‖ξ₁ z‖ ‖ξ₂ z‖ *
                                (1 +
                                  ‖(fderiv ℝ w z) TauCeti.stdComplexLineImag -
                                      ω.hamiltonianVectorField (Kt (φ z)) (w z)‖) *
                              ‖ξ₁ z - ξ₂ z‖ +
                            ‖ξ₁ z - ξ₂ z‖ * ‖(fderiv ℝ ξ₁ z) TauCeti.stdComplexLineImag‖ +
                          ‖ξ₂ z‖ *
                            ‖(fderiv ℝ ξ₁ z) TauCeti.stdComplexLineImag -
                                (fderiv ℝ ξ₂ z) TauCeti.stdComplexLineImag‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Uniform Lipschitz bound at a compact family of base points](../../../analysis/part-03/calculus/part-03/uniform-lipschitz-bound-at-a-compact-family-of-b.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_pos_forall_norm_floerOperator_sub_floerOperator_sub_floerLinearization_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/QuadraticEstimate.html#TauCeti.SymplecticForm.exists_pos_forall_norm_floerOperator_sub_floerOperator_sub_floerLinearization_le).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.exists_pos_forall_norm_floerOperator_sub_floerOperator_sub_floerLinearization_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/QuadraticEstimate.html#TauCeti.SymplecticForm.exists_pos_forall_norm_floerOperator_sub_floerOperator_sub_floerLinearization_le)
- [Source of `TauCeti.SymplecticForm.exists_pos_forall_norm_floerOperator_sub_floerOperator_sub_floerLinearization_le` in TauCeti/Geometry/Symplectic/Floer/QuadraticEstimate.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/QuadraticEstimate.lean#L327)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
