---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.exists_isDarbouxBasis_eq_sum_smul_elliptic_of_posDef, TauCeti.SymplecticForm.exists_isDarbouxBasis_hamiltonianEnd_apply_eq_of_posDef
statement: formalized
proof: formalized
---

# Williamson's theorem

A positive definite quadratic form `Q` on a finite-dimensional
symplectic vector space `(V, ω)` is a sum of harmonic oscillators in suitable Darboux
coordinates: there are a Darboux basis `b = (q₁, p₁, …, qₙ, pₙ)` and positive frequencies
`ν₁, …, νₙ` with `Q = ∑ₖ νₖ Iₖ`, where `Iₖ = (xₖ² + yₖ²) / 2` are the elliptic blocks of `b`
(`TauCeti.SymplecticForm.elliptic`). Thus `Q v = ∑ₖ νₖ / 2 (xₖ² + yₖ²)` in the coordinates
`(x₁, y₁, …, xₙ, yₙ)` of `v` (`TauCeti.SymplecticForm.elliptic_apply`), and `Q` lies in the
span of the nondegenerate family `(Iₖ)`
(`TauCeti.SymplecticForm.IsDarbouxBasis.isNondegenerateQuadraticFamily_elliptic`).

```lean
TauCeti.SymplecticForm.exists_isDarbouxBasis_eq_sum_smul_elliptic_of_posDef.{u_1} {V : Type u_1}
  [AddCommGroup V] [_root_.Module ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V)
  {Q : QuadraticForm ℝ V} (hQ : QuadraticMap.PosDef Q) :
  ∃ n b ν,
    ω.IsDarbouxBasis b ∧
      (∀ (k : Fin n), 0 < ν k) ∧ Q = ∑ k, ν k • TauCeti.SymplecticForm.elliptic b k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_isDarbouxBasis_eq_sum_smul_elliptic_of_posDef`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson.html#TauCeti.SymplecticForm.exists_isDarbouxBasis_eq_sum_smul_elliptic_of_posDef).

## Other forms

**Williamson's theorem, Hamiltonian form.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_isDarbouxBasis_hamiltonianEnd_apply_eq_of_posDef`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson.html#TauCeti.SymplecticForm.exists_isDarbouxBasis_hamiltonianEnd_apply_eq_of_posDef).

```lean
TauCeti.SymplecticForm.exists_isDarbouxBasis_hamiltonianEnd_apply_eq_of_posDef.{u_1} {V : Type u_1}
  [AddCommGroup V] [_root_.Module ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V)
  {Q : QuadraticForm ℝ V} (hQ : QuadraticMap.PosDef Q) :
  ∃ n b ν,
    ω.IsDarbouxBasis b ∧
      (∀ (k : Fin n), 0 < ν k) ∧
        ∀ (k : Fin n),
          (ω.hamiltonianEnd Q) (b (k, 0)) = -ν k • b (k, 1) ∧
            (ω.hamiltonianEnd Q) (b (k, 1)) = ν k • b (k, 0)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.exists_isDarbouxBasis_eq_sum_smul_elliptic_of_posDef`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson.html#TauCeti.SymplecticForm.exists_isDarbouxBasis_eq_sum_smul_elliptic_of_posDef)
- [Source of `TauCeti.SymplecticForm.exists_isDarbouxBasis_eq_sum_smul_elliptic_of_posDef` in TauCeti/Geometry/Symplectic/Hamiltonian/Williamson.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Hamiltonian/Williamson.lean#L124)
