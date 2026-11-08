---
declaration: theorem
origin: cited
lean: Representation.asAlgebraHom_surjective_of_isIrreducible
statement: formalized
proof: formalized
---

# Burnside density theorem

The monoid algebra of a finite-dimensional irreducible
representation over an algebraically closed field exhausts the full endomorphism algebra.

Jacobson density gives all endomorphisms linear over the representation's commuting endomorphism
ring. Schur's lemma identifies that ring with the base field, so these are exactly the
`k`-linear endomorphisms.

```lean
Representation.asAlgebraHom_surjective_of_isIrreducible.{u_1, u_2, u_3} {k : Type u_1}
  {G : Type u_2} {V : Type u_3} [Field k] [Monoid G] [AddCommGroup V] [_root_.Module k V]
  [IsAlgClosed k] [FiniteDimensional k V] (ρ : Representation k G V) (hρ : ρ.IsIrreducible) :
  Function.Surjective ⇑ρ.asAlgebraHom
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schur's lemma, vanishing form](../../ring-theory/part-02/semisimple/schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`Representation.asAlgebraHom_surjective_of_isIrreducible`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Irreducible.html#Representation.asAlgebraHom_surjective_of_isIrreducible).

## Sources

- [Tau Ceti documentation: `Representation.asAlgebraHom_surjective_of_isIrreducible`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Irreducible.html#Representation.asAlgebraHom_surjective_of_isIrreducible)
- [Source of `Representation.asAlgebraHom_surjective_of_isIrreducible` in TauCeti/RepresentationTheory/Irreducible.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Irreducible.lean#L236)
