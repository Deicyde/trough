---
declaration: abbrev
origin: cited
lean: TauCeti.SignedSym
statement: formalized
---

# TauCeti.SignedSym

The tensor algebra modulo signed swaps of homogeneous generators.

```lean
TauCeti.SignedSym.{u, v} {R : Type u} [CommRing R] {V : Type v} [AddCommGroup V] [_root_.Module R V]
  (G : TauCeti.InternalGrading R V ℤ) : Type (max v u)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SignedSym`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.html#TauCeti.SignedSym).

## Sources

- [Tau Ceti documentation: `TauCeti.SignedSym`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.html#TauCeti.SignedSym)
- [Source of `TauCeti.SignedSym` in TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.lean#L45)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
