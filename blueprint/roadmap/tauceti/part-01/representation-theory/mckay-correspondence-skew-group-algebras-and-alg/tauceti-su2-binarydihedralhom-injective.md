---
declaration: theorem
origin: cited
lean: TauCeti.SU2.binaryDihedralHom_injective
statement: formalized
proof: formalized
---

# TauCeti.SU2.binaryDihedralHom_injective

The binary dihedral representation of the dicyclic group is faithful.

```lean
TauCeti.SU2.binaryDihedralHom_injective (n : ℕ) [NeZero n] :
  Function.Injective ⇑(TauCeti.SU2.binaryDihedralHom n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SU2.binaryDihedralHom_injective`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/BinaryDihedral.html#TauCeti.SU2.binaryDihedralHom_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.SU2.binaryDihedralHom_injective`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/BinaryDihedral.html#TauCeti.SU2.binaryDihedralHom_injective)
- [Source of `TauCeti.SU2.binaryDihedralHom_injective` in TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean#L130)
- [Tau Ceti roadmap status: McKay correspondence, skew-group algebras and algebraic Weyl functors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/McKaySkewGroup/STATUS.md)
