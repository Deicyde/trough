---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.abs_sub_sub_fderiv_le_of_norm_hamiltonianVectorField_sub_le
statement: formalized
proof: formalized
---

# Second-order Taylor bound for a Hamiltonian

If the Hamiltonian vector field of a
differentiable function `G` satisfies `‖X_G(z) - X_G(y₀)‖ ≤ L ‖z - y₀‖` on the closed ball of
radius `r` about `y₀`, then `|G(y) - G(y₀) - dG(y₀)(y - y₀)| ≤ ‖ω‖ L ‖y - y₀‖²` for
`‖y - y₀‖ ≤ r`, where `‖ω‖` is the operator norm of the form.

```lean
TauCeti.SymplecticForm.abs_sub_sub_fderiv_le_of_norm_hamiltonianVectorField_sub_le.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  (ω : TauCeti.SymplecticForm V) {G : V → ℝ} (hG : Differentiable ℝ G) {y₀ y : V} {L r : ℝ}
  (hL : 0 ≤ L)
  (hX :
    ∀ z ∈ Metric.closedBall y₀ r,
      ‖ω.hamiltonianVectorField G z - ω.hamiltonianVectorField G y₀‖ ≤ L * ‖z - y₀‖)
  (hy : ‖y - y₀‖ ≤ r) :
  |G y - G y₀ - (fderiv ℝ G y₀) (y - y₀)| ≤
    ‖LinearMap.toContinuousBilinearMap ω.toBilinForm‖ * L * ‖y - y₀‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.abs_sub_sub_fderiv_le_of_norm_hamiltonianVectorField_sub_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Basic.html#TauCeti.SymplecticForm.abs_sub_sub_fderiv_le_of_norm_hamiltonianVectorField_sub_le).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.abs_sub_sub_fderiv_le_of_norm_hamiltonianVectorField_sub_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Basic.html#TauCeti.SymplecticForm.abs_sub_sub_fderiv_le_of_norm_hamiltonianVectorField_sub_le)
- [Source of `TauCeti.SymplecticForm.abs_sub_sub_fderiv_le_of_norm_hamiltonianVectorField_sub_le` in TauCeti/Geometry/Symplectic/Hamiltonian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Hamiltonian/Basic.lean#L264)
