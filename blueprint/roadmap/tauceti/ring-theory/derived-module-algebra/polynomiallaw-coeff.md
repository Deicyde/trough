---
declaration: def
origin: cited
lean: PolynomialLaw.coeff
statement: formalized
---

# PolynomialLaw.coeff

The coefficients of polynomial laws `M →ₚₗ[R] N` at the generic combination `∑ⱼ Xⱼ ⊗ mⱼ`:
`coeff m f k` is the coefficient of the monomial `Xᵏ` in `f (∑ⱼ Xⱼ ⊗ mⱼ)`, computed over the
polynomial ring `R[Xⱼ]`.

```lean
PolynomialLaw.coeff.{u, u_1, u_2, u_3} (R : Type u) [CommSemiring R] {M : Type u_1} (N : Type u_2)
  [AddCommMonoid M] [_root_.Module R M] [AddCommMonoid N] [_root_.Module R N] {ι : Type u_3}
  [Fintype ι] (m : ι → M) : (M →ₚₗ[R] N) →ₗ[R] (ι →₀ ℕ) →₀ N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PolynomialLaw.coeff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PolynomialLaw/Coeff.html#PolynomialLaw.coeff).

## Sources

- [Tau Ceti documentation: `PolynomialLaw.coeff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PolynomialLaw/Coeff.html#PolynomialLaw.coeff)
- [Source of `PolynomialLaw.coeff` in TauCeti/RingTheory/PolynomialLaw/Coeff.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PolynomialLaw/Coeff.lean#L78)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
