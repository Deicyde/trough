---
declaration: def
origin: cited
lean: TauCeti.SU2.binaryDihedralEquiv
statement: formalized
---

# TauCeti.SU2.binaryDihedralEquiv

The binary dihedral subgroup is isomorphic to the dicyclic group `QuaternionGroup n`.

```lean
TauCeti.SU2.binaryDihedralEquiv (n : ℕ) [NeZero n] :
  QuaternionGroup n ≃* ↥(TauCeti.SU2.binaryDihedralSubgroup n)
```

## Depends on

- [The binary dihedral subgroup of `SU(2)` of order `4n`](the-binary-dihedral-subgroup-of-su-2-of-order-4n.md)
- [TauCeti.SU2.binaryDihedralHom_injective](tauceti-su2-binarydihedralhom-injective.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SU2.binaryDihedralEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/BinaryDihedral.html#TauCeti.SU2.binaryDihedralEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.SU2.binaryDihedralEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/BinaryDihedral.html#TauCeti.SU2.binaryDihedralEquiv)
- [Source of `TauCeti.SU2.binaryDihedralEquiv` in TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean#L251)
- [Tau Ceti roadmap status: McKay correspondence, skew-group algebras and algebraic Weyl functors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/McKaySkewGroup/STATUS.md)
