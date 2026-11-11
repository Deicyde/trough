---
declaration: theorem
origin: cited
lean: Representation.adjoin_range_eq_top_of_le_span_sup_sq, Representation.span_range_eq_top_of_span_range_mk_eq_top
statement: formalized
proof: formalized
---

# Graded Nakayama lemma for polynomial invariants

Homogeneous invariants of positive degree
whose classes span `A₊ ⧸ A₊²`, where `A₊` is the ideal of invariants with zero constant term,
generate the invariant algebra `Sym(M)^G` as an `R`-algebra.

```lean
Representation.adjoin_range_eq_top_of_le_span_sup_sq.{u_1, u_3, u_4, u_5} {R : Type u_1}
  {G : Type u_3} {M : Type u_4} {ι : Type u_5} [CommSemiring R] [Monoid G] [AddCommMonoid M]
  [_root_.Module R M] (ρ : Representation R G M) (f : ι → ↥ρ.symmetricAlgebraInvariants) (d : ι → ℕ)
  (hd : ∀ (i : ι), 0 < d i)
  (hf : ∀ (i : ι), ↑(f i) ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule R M (d i))
  (hspan :
    Ideal.under (↥ρ.symmetricAlgebraInvariants)
        (HomogeneousIdeal.irrelevant (TauCeti.SymmetricAlgebra.homogeneousSubmodule R M)).toIdeal ≤
      Ideal.span (Set.range f) ⊔
        Ideal.under (↥ρ.symmetricAlgebraInvariants)
            (HomogeneousIdeal.irrelevant
                (TauCeti.SymmetricAlgebra.homogeneousSubmodule R M)).toIdeal ^
          2) :
  Algebra.adjoin R (Set.range f) = ⊤
```

## Depends on

- [Representation.symmetricAlgebraInvariants](../finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrainvariants.md)

## Proof depends on

- [The graded Nakayama lemma for generators](../../ring-theory/part-02/other-results/part-01/the-graded-nakayama-lemma-for-generators.md)

## Lean

Formalized in Tau Ceti as [`Representation.adjoin_range_eq_top_of_le_span_sup_sq`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Generators.html#Representation.adjoin_range_eq_top_of_le_span_sup_sq).

## Other forms

**Graded Nakayama lemma for the coinvariant algebra.** Formalized in Tau Ceti as [`Representation.span_range_eq_top_of_span_range_mk_eq_top`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Free.html#Representation.span_range_eq_top_of_span_range_mk_eq_top).

```lean
Representation.span_range_eq_top_of_span_range_mk_eq_top.{u_1, u_2, u_3, u_4} {R : Type u_1}
  {G : Type u_2} {M : Type u_3} [CommRing R] [Monoid G] [AddCommMonoid M] [_root_.Module R M]
  (ρ : Representation R G M) {ι : Type u_4} (b : ι → SymmetricAlgebra R M)
  (hb : ∀ (i : ι), ∃ d, b i ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule R M d)
  (hspan :
    Submodule.span R (Set.range (⇑(Ideal.Quotient.mkₐ R ρ.symmetricAlgebraHilbertIdeal) ∘ b)) = ⊤) :
  Submodule.span (↥ρ.symmetricAlgebraInvariants) (Set.range b) = ⊤
```

## Sources

- [Tau Ceti documentation: `Representation.adjoin_range_eq_top_of_le_span_sup_sq`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Generators.html#Representation.adjoin_range_eq_top_of_le_span_sup_sq)
- [Source of `Representation.adjoin_range_eq_top_of_le_span_sup_sq` in TauCeti/RepresentationTheory/SymmetricAlgebra/Generators.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SymmetricAlgebra/Generators.lean#L73)
