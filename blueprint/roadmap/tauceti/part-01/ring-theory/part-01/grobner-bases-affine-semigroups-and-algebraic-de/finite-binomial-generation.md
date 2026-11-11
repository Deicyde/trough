---
declaration: theorem
origin: cited
lean: TauCeti.exists_finset_toricIdeal_eq_span
statement: formalized
proof: formalized
---

# Finite binomial generation

For finitely many exponents `a i`, there are finitely many
pairs `(u, v)` with `∑ i, u i • a i = ∑ i, v i • a i` whose binomials `X^u - X^v` generate the
toric ideal over every commutative ring. The pairs are chosen over `ℤ`, where the polynomial ring
is noetherian, and the generators are transported by change of coefficients.

```lean
TauCeti.exists_finset_toricIdeal_eq_span.{u, u_1, u_2} {ι : Type u_1} {M : Type u_2}
  [AddCommMonoid M] [Finite ι] (a : ι → M) :
  ∃ P,
    (∀ p ∈ P, (Finsupp.linearCombination ℕ a) p.1 = (Finsupp.linearCombination ℕ a) p.2) ∧
      ∀ (R : Type u) [inst : CommRing R],
        TauCeti.toricIdeal R a =
          Ideal.span
            ((fun p => (MvPolynomial.monomial p.1) 1 - (MvPolynomial.monomial p.2) 1) '' ↑P)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Binomial generation of toric ideals](binomial-generation-of-toric-ideals.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_finset_toricIdeal_eq_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/ToricIdeal/Basic.html#TauCeti.exists_finset_toricIdeal_eq_span).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_finset_toricIdeal_eq_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/ToricIdeal/Basic.html#TauCeti.exists_finset_toricIdeal_eq_span)
- [Source of `TauCeti.exists_finset_toricIdeal_eq_span` in TauCeti/RingTheory/MvPolynomial/ToricIdeal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/ToricIdeal/Basic.lean#L255)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
