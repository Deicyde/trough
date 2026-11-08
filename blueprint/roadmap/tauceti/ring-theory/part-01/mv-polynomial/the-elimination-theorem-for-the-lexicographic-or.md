---
declaration: theorem
origin: cited
lean: MonomialOrder.IsGroebnerBasis.comap_rename_lex
statement: formalized
proof: formalized
---

# The elimination theorem for the lexicographic order

If `e : τ → σ` is strictly monotone
with image an upper set of variables, then the members of a lexicographic Gröbner basis of `I` in
the variables `e τ` form a lexicographic Gröbner basis of the elimination ideal.

```lean
MonomialOrder.IsGroebnerBasis.comap_rename_lex.{u_1, u_2, u_3} {σ : Type u_1} {τ : Type u_2}
  {R : Type u_3} [CommSemiring R] {e : τ → σ} [LinearOrder σ] [WellFoundedGT σ] [LinearOrder τ]
  [WellFoundedGT τ] {G : Set (MvPolynomial σ R)} {I : Ideal (MvPolynomial σ R)}
  (h : MonomialOrder.lex.IsGroebnerBasis G I) (he : StrictMono e) (hup : IsUpperSet (Set.range e)) :
  MonomialOrder.lex.IsGroebnerBasis (⇑(MvPolynomial.rename e) ⁻¹' G)
    (Ideal.comap (MvPolynomial.rename e) I)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The elimination theorem](the-elimination-theorem.md)

## Lean

Formalized in Tau Ceti as [`MonomialOrder.IsGroebnerBasis.comap_rename_lex`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Elimination.html#MonomialOrder.IsGroebnerBasis.comap_rename_lex).

## Sources

- [Tau Ceti documentation: `MonomialOrder.IsGroebnerBasis.comap_rename_lex`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Groebner/Elimination.html#MonomialOrder.IsGroebnerBasis.comap_rename_lex)
- [Source of `MonomialOrder.IsGroebnerBasis.comap_rename_lex` in TauCeti/RingTheory/MvPolynomial/Groebner/Elimination.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPolynomial/Groebner/Elimination.lean#L110)
