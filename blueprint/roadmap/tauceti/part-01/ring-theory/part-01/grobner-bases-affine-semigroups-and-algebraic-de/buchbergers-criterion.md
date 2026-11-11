---
declaration: theorem
origin: cited
lean: MonomialOrder.isGroebnerBasis_span_iff_isRemainder_sPolynomial_zero, MonomialOrder.isGroebnerBasis_iff_span_eq_and_isRemainder_sPolynomial_zero, MonomialOrder.isGroebnerBasis_span_of_isRemainder_sPolynomial_zero
statement: formalized
proof: formalized
---

# Buchberger's criterion

A set `G` whose nonzero members have unit leading coefficients is a
Gröbner basis of the ideal it generates if and only if the S-polynomial of any two members of `G`
has remainder `0` on division by `G`.

```lean
MonomialOrder.isGroebnerBasis_span_iff_isRemainder_sPolynomial_zero.{u_1, u_2, u_3} {σ : Type u_1}
  {R : Type u_2} {m : MonomialOrder σ} [CommRing R] {G : Set (MvPolynomial σ R)}
  (hG : ∀ g ∈ G, g ≠ 0 → IsUnit (m.leadingCoeff g)) :
  m.IsGroebnerBasis G (Ideal.span G) ↔ ∀ g₁ ∈ G, ∀ g₂ ∈ G, m.IsRemainder (m.sPolynomial g₁ g₂) G 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonomialOrder.isGroebnerBasis_span_iff_isRemainder_sPolynomial_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Buchberger.html#MonomialOrder.isGroebnerBasis_span_iff_isRemainder_sPolynomial_zero).

## Other forms

**Buchberger's criterion.** Formalized in Tau Ceti as [`MonomialOrder.isGroebnerBasis_iff_span_eq_and_isRemainder_sPolynomial_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Buchberger.html#MonomialOrder.isGroebnerBasis_iff_span_eq_and_isRemainder_sPolynomial_zero).

```lean
MonomialOrder.isGroebnerBasis_iff_span_eq_and_isRemainder_sPolynomial_zero.{u_1, u_2, u_3}
  {σ : Type u_1} {R : Type u_2} {m : MonomialOrder σ} [CommRing R] {G : Set (MvPolynomial σ R)}
  {I : Ideal (MvPolynomial σ R)} (hG : ∀ g ∈ G, g ≠ 0 → IsUnit (m.leadingCoeff g)) :
  m.IsGroebnerBasis G I ↔
    Ideal.span G = I ∧ ∀ g₁ ∈ G, ∀ g₂ ∈ G, m.IsRemainder (m.sPolynomial g₁ g₂) G 0
```

**Buchberger's criterion.** Formalized in Tau Ceti as [`MonomialOrder.isGroebnerBasis_span_of_isRemainder_sPolynomial_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Buchberger.html#MonomialOrder.isGroebnerBasis_span_of_isRemainder_sPolynomial_zero).

```lean
MonomialOrder.isGroebnerBasis_span_of_isRemainder_sPolynomial_zero.{u_1, u_2, u_3} {σ : Type u_1}
  {R : Type u_2} {m : MonomialOrder σ} [CommRing R] {G : Set (MvPolynomial σ R)}
  (hG : ∀ g ∈ G, g ≠ 0 → IsUnit (m.leadingCoeff g))
  (hS : ∀ g₁ ∈ G, ∀ g₂ ∈ G, m.IsRemainder (m.sPolynomial g₁ g₂) G 0) :
  m.IsGroebnerBasis G (Ideal.span G)
```

## Sources

- [Tau Ceti documentation: `MonomialOrder.isGroebnerBasis_span_iff_isRemainder_sPolynomial_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Buchberger.html#MonomialOrder.isGroebnerBasis_span_iff_isRemainder_sPolynomial_zero)
- [Source of `MonomialOrder.isGroebnerBasis_span_iff_isRemainder_sPolynomial_zero` in TauCeti/RingTheory/MvPolynomial/Groebner/Buchberger.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Groebner/Buchberger.lean#L292)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
