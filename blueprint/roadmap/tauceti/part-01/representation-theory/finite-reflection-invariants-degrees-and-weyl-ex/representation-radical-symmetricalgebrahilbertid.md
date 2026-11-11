---
declaration: theorem
origin: cited
lean: Representation.radical_symmetricAlgebraHilbertIdeal_of_isReduced
statement: formalized
proof: formalized
---

# Representation.radical_symmetricAlgebraHilbertIdeal_of_isReduced

For a finite group over a reduced base, the radical of the Hilbert ideal is the irrelevant
ideal.

```lean
Representation.radical_symmetricAlgebraHilbertIdeal_of_isReduced.{u_1, u_2, u_3} {R : Type u_1}
  {G : Type u_2} {M : Type u_3} [CommRing R] [Group G] [Finite G] [AddCommMonoid M]
  [_root_.Module R M] (ρ : Representation R G M) [IsReduced R] :
  ρ.symmetricAlgebraHilbertIdeal.radical =
    (HomogeneousIdeal.irrelevant (TauCeti.SymmetricAlgebra.homogeneousSubmodule R M)).toIdeal
```

## Depends on

- [Representation.symmetricAlgebraInvariants](representation-symmetricalgebrainvariants.md)

## Lean

Formalized in Tau Ceti as [`Representation.radical_symmetricAlgebraHilbertIdeal_of_isReduced`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/HilbertIdeal.html#Representation.radical_symmetricAlgebraHilbertIdeal_of_isReduced).

## Sources

- [Tau Ceti documentation: `Representation.radical_symmetricAlgebraHilbertIdeal_of_isReduced`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/HilbertIdeal.html#Representation.radical_symmetricAlgebraHilbertIdeal_of_isReduced)
- [Source of `Representation.radical_symmetricAlgebraHilbertIdeal_of_isReduced` in TauCeti/RepresentationTheory/SymmetricAlgebra/HilbertIdeal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SymmetricAlgebra/HilbertIdeal.lean#L282)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
