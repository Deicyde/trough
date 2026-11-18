---
declaration: def
origin: cited
lean: MonomialOrder.IsGroebnerBasis.basisQuotient
statement: formalized
---

# The standard monomial basis

Given a Gröbner basis of `I` whose nonzero members have unit
leading coefficients, the images of the standard monomials of `I` form an `R`-basis of
`MvPolynomial σ R ⧸ I`.

```lean
MonomialOrder.IsGroebnerBasis.basisQuotient.{u_1, u_2, u_3} {σ : Type u_1} {R : Type u_2}
  {m : MonomialOrder σ} [CommRing R] {I : Ideal (MvPolynomial σ R)} {G : Set (MvPolynomial σ R)}
  (h : m.IsGroebnerBasis G I) (hG : ∀ g ∈ G, g ≠ 0 → IsUnit (m.leadingCoeff g)) :
  Module.Basis (↑(m.standardMonomials I)) R (MvPolynomial σ R ⧸ I)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonomialOrder.IsGroebnerBasis.basisQuotient`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/NormalForm.html#MonomialOrder.IsGroebnerBasis.basisQuotient).

## Sources

- [Tau Ceti documentation: `MonomialOrder.IsGroebnerBasis.basisQuotient`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/NormalForm.html#MonomialOrder.IsGroebnerBasis.basisQuotient)
- [Source of `MonomialOrder.IsGroebnerBasis.basisQuotient` in TauCeti/RingTheory/MvPolynomial/Groebner/NormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/Groebner/NormalForm.lean#L174)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
