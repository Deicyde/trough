---
declaration: theorem
origin: cited
lean: TauCeti.SU2.mem_binaryDihedralSubgroup_iff
statement: formalized
proof: formalized
---

# Normal forms in the binary dihedral subgroup

Every element is `r ^ j` or `s r ^ j` for
some `j < 2n`.

```lean
TauCeti.SU2.mem_binaryDihedralSubgroup_iff (n : ℕ) [NeZero n] {g : TauCeti.SU2} :
  g ∈ TauCeti.SU2.binaryDihedralSubgroup n ↔
    ∃ j < 2 * n,
      g = TauCeti.SU2.binaryDihedralRotation n ^ j ∨
        g = TauCeti.SU2.weylElement⁻¹ * TauCeti.SU2.binaryDihedralRotation n ^ j
```

## Depends on

- [The binary dihedral subgroup of `SU(2)` of order `4n`](the-binary-dihedral-subgroup-of-su-2-of-order-4n.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SU2.mem_binaryDihedralSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/BinaryDihedral.html#TauCeti.SU2.mem_binaryDihedralSubgroup_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.SU2.mem_binaryDihedralSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/BinaryDihedral.html#TauCeti.SU2.mem_binaryDihedralSubgroup_iff)
- [Source of `TauCeti.SU2.mem_binaryDihedralSubgroup_iff` in TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean#L275)
- [Tau Ceti roadmap status: McKay correspondence, skew-group algebras and algebraic Weyl functors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/McKaySkewGroup/STATUS.md)
