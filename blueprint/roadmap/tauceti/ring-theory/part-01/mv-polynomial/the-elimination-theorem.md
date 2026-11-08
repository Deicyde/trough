---
declaration: theorem
origin: cited
lean: MonomialOrder.IsGroebnerBasis.comap_rename
statement: formalized
proof: formalized
---

# The elimination theorem

Let `m` be an elimination order for the variables `e τ`: every
monomial below a monomial in these variables is again a monomial in these variables. If `G` is a
Gröbner basis of `I` for `m`, then the members of `G` in the variables `e τ` form a Gröbner basis
of the elimination ideal `I.comap (rename e)` for every monomial order `m'` on `τ` which `e`
carries to `m`.

```lean
MonomialOrder.IsGroebnerBasis.comap_rename.{u_1, u_2, u_3, u_4, u_5} {σ : Type u_1} {τ : Type u_2}
  {R : Type u_3} [CommSemiring R] {m : MonomialOrder σ} {m' : MonomialOrder τ} {e : τ → σ}
  {G : Set (MvPolynomial σ R)} {I : Ideal (MvPolynomial σ R)} (h : m.IsGroebnerBasis G I)
  (hm :
    ∀ (a b : τ →₀ ℕ),
      m'.toSyn a ≤ m'.toSyn b ↔ m.toSyn (Finsupp.mapDomain e a) ≤ m.toSyn (Finsupp.mapDomain e b))
  (helim :
    ∀ (a b : σ →₀ ℕ), m.toSyn a ≤ m.toSyn b → ↑b.support ⊆ Set.range e → ↑a.support ⊆ Set.range e) :
  m'.IsGroebnerBasis (⇑(MvPolynomial.rename e) ⁻¹' G) (Ideal.comap (MvPolynomial.rename e) I)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonomialOrder.IsGroebnerBasis.comap_rename`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Elimination.html#MonomialOrder.IsGroebnerBasis.comap_rename).

## Sources

- [Tau Ceti documentation: `MonomialOrder.IsGroebnerBasis.comap_rename`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Elimination.html#MonomialOrder.IsGroebnerBasis.comap_rename)
- [Source of `MonomialOrder.IsGroebnerBasis.comap_rename` in TauCeti/RingTheory/MvPolynomial/Groebner/Elimination.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPolynomial/Groebner/Elimination.lean#L63)
