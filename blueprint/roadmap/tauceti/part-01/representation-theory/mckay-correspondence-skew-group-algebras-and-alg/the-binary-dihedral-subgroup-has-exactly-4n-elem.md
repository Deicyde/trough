---
declaration: theorem
origin: cited
lean: TauCeti.SU2.natCard_binaryDihedralSubgroup
statement: formalized
proof: formalized
---

# The binary dihedral subgroup has exactly `4n` elements

```lean
TauCeti.SU2.natCard_binaryDihedralSubgroup (n : ℕ) [NeZero n] :
  Nat.card ↥(TauCeti.SU2.binaryDihedralSubgroup n) = 4 * n
```

## Depends on

- [The binary dihedral subgroup of `SU(2)` of order `4n`](the-binary-dihedral-subgroup-of-su-2-of-order-4n.md)

## Proof depends on

- [TauCeti.SU2.binaryDihedralEquiv](tauceti-su2-binarydihedralequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SU2.natCard_binaryDihedralSubgroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/BinaryDihedral.html#TauCeti.SU2.natCard_binaryDihedralSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.SU2.natCard_binaryDihedralSubgroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/BinaryDihedral.html#TauCeti.SU2.natCard_binaryDihedralSubgroup)
- [Source of `TauCeti.SU2.natCard_binaryDihedralSubgroup` in TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean#L261)
- [Tau Ceti roadmap status: McKay correspondence, skew-group algebras and algebraic Weyl functors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/McKaySkewGroup/STATUS.md)
