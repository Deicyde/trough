---
declaration: theorem
origin: cited
lean: TauCeti.Comodule.exists_basis_coefficientMatrix_mem_unitary
statement: formalized
proof: formalized
---

# Algebraic unitarization

Over a complex Hopf star algebra with a nonzero positive right
invariant integral, every comodule with a finite basis has a basis, indexed by the same type,
whose coefficient matrix is unitary.

```lean
TauCeti.Comodule.exists_basis_coefficientMatrix_mem_unitary.{u_1, u_2, u_3} {A : Type u_1}
  {M : Type u_2} {ι : Type u_3} [Ring A] [StarRing A] [AddCommGroup M] [_root_.Module ℂ M]
  [Fintype ι] [HopfAlgebra ℂ A] [StarModule ℂ A] [TauCeti.StarCoalgebra ℂ A]
  [TauCeti.Comodule ℂ A M] [DecidableEq ι] {h : A →ₗ[ℂ] ℂ} (hh : h.IsRightInvariantIntegral)
  (h0 : h ≠ 0) (hpos : ∀ (a : A), 0 ≤ h (star a * a)) (b : Module.Basis ι ℂ M) :
  ∃ c, TauCeti.Comodule.coefficientMatrix c ∈ unitary (Matrix ι ι A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Comodule.exists_basis_coefficientMatrix_mem_unitary`](https://taucetiproject.org/docs/TauCeti/Algebra/Coalgebra/Comodule/Unitarization.html#TauCeti.Comodule.exists_basis_coefficientMatrix_mem_unitary).

## Sources

- [Tau Ceti documentation: `TauCeti.Comodule.exists_basis_coefficientMatrix_mem_unitary`](https://taucetiproject.org/docs/TauCeti/Algebra/Coalgebra/Comodule/Unitarization.html#TauCeti.Comodule.exists_basis_coefficientMatrix_mem_unitary)
- [Source of `TauCeti.Comodule.exists_basis_coefficientMatrix_mem_unitary` in TauCeti/Algebra/Coalgebra/Comodule/Unitarization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Coalgebra/Comodule/Unitarization.lean#L213)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumGroups/STATUS.md)
