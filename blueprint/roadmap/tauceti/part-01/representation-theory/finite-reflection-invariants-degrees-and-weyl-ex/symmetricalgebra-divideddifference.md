---
declaration: def
origin: cited
lean: SymmetricAlgebra.dividedDifference
statement: formalized
---

# SymmetricAlgebra.dividedDifference

The **divided-difference operator** `p ↦ (p - σ p) / ℓ` on the symmetric algebra, for a linear
endomorphism `σ` of `M` such that `m - σ m` is a multiple of `ℓ` for every `m`, and an element
`ℓ` that is a nonzerodivisor in `Sym M`. It is characterized by
`ι ℓ * dividedDifference σ ℓ hσ hℓ p = p - σ p` (`SymmetricAlgebra.dividedDifference_eq_iff`).

```lean
SymmetricAlgebra.dividedDifference.{u_1, u_2} {R : Type u_1} {M : Type u_2} [CommRing R]
  [AddCommGroup M] [_root_.Module R M] (σ : M →ₗ[R] M) (ℓ : M) (hσ : ∀ (m : M), m - σ m ∈ R ∙ ℓ)
  (hℓ : IsLeftRegular ((SymmetricAlgebra.ι R M) ℓ)) :
  SymmetricAlgebra R M →ₗ[R] SymmetricAlgebra R M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SymmetricAlgebra.dividedDifference`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SymmetricAlgebra/DividedDifference.html#SymmetricAlgebra.dividedDifference).

## Sources

- [Tau Ceti documentation: `SymmetricAlgebra.dividedDifference`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SymmetricAlgebra/DividedDifference.html#SymmetricAlgebra.dividedDifference)
- [Source of `SymmetricAlgebra.dividedDifference` in TauCeti/LinearAlgebra/SymmetricAlgebra/DividedDifference.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/SymmetricAlgebra/DividedDifference.lean#L90)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
