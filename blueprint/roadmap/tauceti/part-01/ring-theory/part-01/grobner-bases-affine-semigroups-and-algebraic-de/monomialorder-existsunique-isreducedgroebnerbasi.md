---
declaration: theorem
origin: cited
lean: MonomialOrder.existsUnique_isReducedGroebnerBasis
statement: formalized
proof: formalized
---

# MonomialOrder.existsUnique_isReducedGroebnerBasis

Over a field, every ideal has exactly one reduced monic Gröbner basis.

```lean
MonomialOrder.existsUnique_isReducedGroebnerBasis.{u_1, u_3, u_4} {σ : Type u_1} {k : Type u_3}
  [Field k] (m : MonomialOrder σ) (I : Ideal (MvPolynomial σ k)) :
  ∃! G, m.IsReducedGroebnerBasis G I
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonomialOrder.existsUnique_isReducedGroebnerBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Reduced.html#MonomialOrder.existsUnique_isReducedGroebnerBasis).

## Sources

- [Tau Ceti documentation: `MonomialOrder.existsUnique_isReducedGroebnerBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Reduced.html#MonomialOrder.existsUnique_isReducedGroebnerBasis)
- [Source of `MonomialOrder.existsUnique_isReducedGroebnerBasis` in TauCeti/RingTheory/MvPolynomial/Groebner/Reduced.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Groebner/Reduced.lean#L229)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
