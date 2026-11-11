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
- [Source of `TauCeti.SU2.mem_binaryDihedralSubgroup_iff` in TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SU2/BinaryDihedral.lean#L275)
- [Tau Ceti roadmap status: McKay correspondence, skew-group algebras and algebraic Weyl functors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/McKaySkewGroup/STATUS.md)
