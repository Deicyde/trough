---
declaration: def
origin: cited
lean: Representation.symmetricAlgebraInvariants
statement: formalized
---

# Representation.symmetricAlgebraInvariants

The invariant subalgebra `Sym(M)^G`: the elements of `Sym M` fixed by the induced action of
every element of `G`, that is, the fixed subalgebra `FixedPoints.subalgebra` of the bundled
action.

```lean
Representation.symmetricAlgebraInvariants.{u_1, u_2, u_3} {R : Type u_1} {G : Type u_2}
  {M : Type u_3} [CommSemiring R] [Monoid G] [AddCommMonoid M] [_root_.Module R M]
  (ρ : Representation R G M) : Subalgebra R (SymmetricAlgebra R M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Representation.symmetricAlgebraInvariants`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Basic.html#Representation.symmetricAlgebraInvariants).

## Sources

- [Tau Ceti documentation: `Representation.symmetricAlgebraInvariants`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Basic.html#Representation.symmetricAlgebraInvariants)
- [Source of `Representation.symmetricAlgebraInvariants` in TauCeti/RepresentationTheory/SymmetricAlgebra/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SymmetricAlgebra/Basic.lean#L226)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
