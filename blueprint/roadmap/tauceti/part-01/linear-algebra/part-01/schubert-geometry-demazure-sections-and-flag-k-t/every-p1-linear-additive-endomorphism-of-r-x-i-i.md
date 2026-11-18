---
declaration: theorem
origin: cited
lean: TauCeti.MvPolynomial.existsUnique_eq_frobeniusTrace_mul
statement: formalized
proof: formalized
---

# Every `p⁻¹`-linear additive endomorphism of `R[X_i]` is `f ↦ frobeniusTrace p (h * f)` for a unique polynomial `h`

This is the affine-space case of `Hom(F_* O, O) ≅ F_* (ω ^ (1 - p))`;
the polynomial is `TauCeti.MvPolynomial.frobeniusTraceDual p φ`.

```lean
TauCeti.MvPolynomial.existsUnique_eq_frobeniusTrace_mul.{u_1, u_2} {σ : Type u_1} {R : Type u_2}
  [CommSemiring R] {p : ℕ} [ExpChar R p] [PerfectRing R p] [Finite σ]
  (φ : MvPolynomial σ R →+ MvPolynomial σ R)
  (hφ : ∀ (g f : MvPolynomial σ R), φ (g ^ p * f) = g * φ f) :
  ∃! h, ∀ (f : MvPolynomial σ R), φ f = (MvPolynomial.frobeniusTrace σ R p) (h * f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPolynomial.existsUnique_eq_frobeniusTrace_mul`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Cartier.html#TauCeti.MvPolynomial.existsUnique_eq_frobeniusTrace_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPolynomial.existsUnique_eq_frobeniusTrace_mul`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Cartier.html#TauCeti.MvPolynomial.existsUnique_eq_frobeniusTrace_mul)
- [Source of `TauCeti.MvPolynomial.existsUnique_eq_frobeniusTrace_mul` in TauCeti/RingTheory/MvPolynomial/Cartier.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/Cartier.lean#L412)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
