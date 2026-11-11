---
declaration: theorem
origin: cited
lean: CliffordAlgebra.existsUnique_pos_mul_of_surjective
statement: formalized
proof: formalized
---

# CliffordAlgebra.existsUnique_pos_mul_of_surjective

For a full endomorphism-algebra Clifford action, two positive definite compatible Hermitian
forms differ by a unique positive real scalar. This is
`CliffordAlgebra.existsUnique_pos_mul_inner_of_surjective` without a fixed inner product on `S`:
the reference form `H₀` takes its place.

```lean
CliffordAlgebra.existsUnique_pos_mul_of_surjective.{u_1, u_2} {V : Type u_1} {S : Type u_2}
  [AddCommGroup V] [_root_.Module ℝ V] {Q : QuadraticForm ℝ V} [AddCommGroup S] [_root_.Module ℂ S]
  [FiniteDimensional ℂ S] (ρ : CliffordAlgebra (QuadraticForm.baseChange ℂ Q) →ₐ[ℂ] Module.End ℂ S)
  [Nontrivial S] (hsurj : Function.Surjective ⇑ρ) (H₀ : S →ₗ⋆[ℂ] S →ₗ[ℂ] ℂ) (hH₀ : H₀.IsPosSemidef)
  (hdef₀ : ∀ (x : S), x ≠ 0 → (H₀ x) x ≠ 0)
  (hH₀ρ :
    ∀ (v : V) (x y : S),
      (H₀ ((ρ ((CliffordAlgebra.ι (QuadraticForm.baseChange ℂ Q)) (1 ⊗ₜ[ℝ] v))) x)) y =
        -(H₀ x) ((ρ ((CliffordAlgebra.ι (QuadraticForm.baseChange ℂ Q)) (1 ⊗ₜ[ℝ] v))) y))
  (H : S →ₗ⋆[ℂ] S →ₗ[ℂ] ℂ) (hpos : H.IsNonneg) (hdef : ∀ (x : S), x ≠ 0 → (H x) x ≠ 0)
  (hH :
    ∀ (v : V) (x y : S),
      (H ((ρ ((CliffordAlgebra.ι (QuadraticForm.baseChange ℂ Q)) (1 ⊗ₜ[ℝ] v))) x)) y =
        -(H x) ((ρ ((CliffordAlgebra.ι (QuadraticForm.baseChange ℂ Q)) (1 ⊗ₜ[ℝ] v))) y)) :
  ∃! r, 0 < r ∧ ∀ (x y : S), (H x) y = ↑r * (H₀ x) y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.existsUnique_pos_mul_of_surjective`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Hermitian/Complex.html#CliffordAlgebra.existsUnique_pos_mul_of_surjective).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.existsUnique_pos_mul_of_surjective`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Hermitian/Complex.html#CliffordAlgebra.existsUnique_pos_mul_of_surjective)
- [Source of `CliffordAlgebra.existsUnique_pos_mul_of_surjective` in TauCeti/LinearAlgebra/CliffordAlgebra/Hermitian/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Hermitian/Complex.lean#L136)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
