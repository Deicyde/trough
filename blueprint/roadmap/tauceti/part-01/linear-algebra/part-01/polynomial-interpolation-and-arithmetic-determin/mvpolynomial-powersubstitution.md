---
declaration: def
origin: cited
lean: MvPolynomial.powerSubstitution
statement: formalized
---

# MvPolynomial.powerSubstitution

The power substitution `Z ↦ X`, `W ↦ X ^ B` on bivariate polynomials, with variable `0 = Z`
and variable `1 = W`: the evaluation homomorphism `F ↦ F(X, X ^ B)`.

```lean
MvPolynomial.powerSubstitution.{u_1} {R : Type u_1} [CommSemiring R] (B : ℕ) :
  MvPolynomial (Fin 2) R →ₐ[R] Polynomial R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.powerSubstitution`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/PowerSubstitution.html#MvPolynomial.powerSubstitution).

## Sources

- [Tau Ceti documentation: `MvPolynomial.powerSubstitution`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/PowerSubstitution.html#MvPolynomial.powerSubstitution)
- [Source of `MvPolynomial.powerSubstitution` in TauCeti/RingTheory/MvPolynomial/PowerSubstitution.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/PowerSubstitution.lean#L102)
- [Tau Ceti roadmap status: Polynomial interpolation and arithmetic determinants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ArithmeticInterpolationDeterminants/STATUS.md)
