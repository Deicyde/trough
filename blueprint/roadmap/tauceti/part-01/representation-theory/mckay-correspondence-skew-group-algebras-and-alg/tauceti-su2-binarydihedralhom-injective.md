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
- [Source of `TauCeti.SU2.binaryDihedralHom_injective` in TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean#L130)
- [Tau Ceti roadmap status: McKay correspondence, skew-group algebras and algebraic Weyl functors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/McKaySkewGroup/STATUS.md)
