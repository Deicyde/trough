---
declaration: def
origin: cited
lean: MonomialOrder.IsGroebnerBasis.basisMapWeightedHomogeneousSubmodule
statement: formalized
---

# The graded standard monomial basis

For an ideal `I` which is homogeneous for the grading
by the weight `w`, the images of the standard monomials of `I` of weight `n` form a basis of the
image in `MvPolynomial σ R ⧸ I` of the weighted homogeneous polynomials of weight `n`.

```lean
MonomialOrder.IsGroebnerBasis.basisMapWeightedHomogeneousSubmodule.{u_1, u_2, u_3, u_4}
  {σ : Type u_1} {R : Type u_2} {M : Type u_3} [AddCommMonoid M] {m : MonomialOrder σ} {w : σ → M}
  [CommRing R] [DecidableEq M] {G : Set (MvPolynomial σ R)} {I : Ideal (MvPolynomial σ R)}
  (h : m.IsGroebnerBasis G I) (hG : ∀ g ∈ G, g ≠ 0 → IsUnit (m.leadingCoeff g))
  (hI : Ideal.IsHomogeneous (MvPolynomial.weightedHomogeneousSubmodule R w) I) (n : M) :
  Module.Basis (↑(m.standardMonomials I ∩ {c | (Finsupp.weight w) c = n})) R
    ↥(Submodule.map (Ideal.Quotient.mkₐ R I).toLinearMap
        (MvPolynomial.weightedHomogeneousSubmodule R w n))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonomialOrder.IsGroebnerBasis.basisMapWeightedHomogeneousSubmodule`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Homogeneous.html#MonomialOrder.IsGroebnerBasis.basisMapWeightedHomogeneousSubmodule).

## Sources

- [Tau Ceti documentation: `MonomialOrder.IsGroebnerBasis.basisMapWeightedHomogeneousSubmodule`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Homogeneous.html#MonomialOrder.IsGroebnerBasis.basisMapWeightedHomogeneousSubmodule)
- [Source of `MonomialOrder.IsGroebnerBasis.basisMapWeightedHomogeneousSubmodule` in TauCeti/RingTheory/MvPolynomial/Groebner/Homogeneous.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Groebner/Homogeneous.lean#L250)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
