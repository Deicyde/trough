---
declaration: theorem
origin: cited
lean: Polynomial.taylorExp_smul_derivative'
statement: formalized
proof: formalized
---

# Taylor's formula for polynomials

Over a `ℚ`-algebra, the Taylor exponential of the
scaled derivative `r • d / dX` is the Taylor shift `p ↦ p (X + r)`.

```lean
Polynomial.taylorExp_smul_derivative'.{u_1} {R : Type u_1} [CommRing R] [Algebra ℚ R] (r : R) :
  (r • Polynomial.derivative').taylorExp ⋯ = Polynomial.taylorAlgHom r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.taylorExp_smul_derivative'`](https://taucetiproject.org/docs/TauCeti/RingTheory/Derivation/TaylorExp.html#Polynomial.taylorExp_smul_derivative').

## Sources

- [Tau Ceti documentation: `Polynomial.taylorExp_smul_derivative'`](https://taucetiproject.org/docs/TauCeti/RingTheory/Derivation/TaylorExp.html#Polynomial.taylorExp_smul_derivative')
- [Source of `Polynomial.taylorExp_smul_derivative'` in TauCeti/RingTheory/Derivation/TaylorExp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Derivation/TaylorExp.lean#L244)
