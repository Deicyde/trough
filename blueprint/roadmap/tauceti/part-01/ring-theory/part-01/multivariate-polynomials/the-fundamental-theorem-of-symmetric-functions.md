---
declaration: def
origin: cited
lean: TauCeti.SymmetricFunction.esymmAlgEquiv
statement: formalized
---

# The fundamental theorem of symmetric functions

the ring of symmetric functions over a
commutative ring `R` is the polynomial ring over `R` on the elementary symmetric functions
`e₁, e₂, …`, the variable `X r` representing `e_(r + 1)`.

```lean
TauCeti.SymmetricFunction.esymmAlgEquiv.{u_1} (R : Type u_1) [CommRing R] :
  MvPolynomial ℕ R ≃ₐ[R] TauCeti.SymmetricFunction R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymmetricFunction.esymmAlgEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/Generators.html#TauCeti.SymmetricFunction.esymmAlgEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.SymmetricFunction.esymmAlgEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/Generators.html#TauCeti.SymmetricFunction.esymmAlgEquiv)
- [Source of `TauCeti.SymmetricFunction.esymmAlgEquiv` in TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/Generators.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/Generators.lean#L204)
