---
declaration: def
origin: cited
lean: Representation.symmetricAlgebraReynolds
statement: formalized
---

# Representation.symmetricAlgebraReynolds

The **Reynolds operator** `p ↦ #G⁻¹ • ∑ g, g • p`, from `Sym M` onto the invariant subalgebra.
It is linear over the invariant subalgebra and restricts to the identity on it, but it is
generally not multiplicative.

```lean
Representation.symmetricAlgebraReynolds.{u_1, u_2, u_3} {R : Type u_1} {G : Type u_2} {M : Type u_3}
  [CommRing R] [Group G] [AddCommMonoid M] [_root_.Module R M] (ρ : Representation R G M)
  [Fintype G] [Invertible ↑(Fintype.card G)] :
  SymmetricAlgebra R M →ₗ[↥ρ.symmetricAlgebraInvariants] ↥ρ.symmetricAlgebraInvariants
```

## Depends on

- [Representation.symmetricAlgebraInvariants](representation-symmetricalgebrainvariants.md)

## Lean

Formalized in Tau Ceti as [`Representation.symmetricAlgebraReynolds`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Reynolds.html#Representation.symmetricAlgebraReynolds).

## Sources

- [Tau Ceti documentation: `Representation.symmetricAlgebraReynolds`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Reynolds.html#Representation.symmetricAlgebraReynolds)
- [Source of `Representation.symmetricAlgebraReynolds` in TauCeti/RepresentationTheory/SymmetricAlgebra/Reynolds.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SymmetricAlgebra/Reynolds.lean#L60)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
