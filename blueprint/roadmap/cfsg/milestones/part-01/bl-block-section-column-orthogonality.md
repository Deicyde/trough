---
declaration: theorem
origin: cited
lean: CFSG.Milestones.block_section_orthogonality
statement: formalized
proof: formalized
---

# BL_block_section_column_orthogonality

The milestone module `CFSG.Milestones.BL_block_section_column_orthogonality`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/BL_block_section_column_orthogonality.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/BL_block_section_column_orthogonality.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.block_section_orthogonality` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/BL_block_section_column_orthogonality.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.block_section_orthogonality (p : ℕ) (hp : p.Prime) (m : Ideal BlocksAlgInt) (hm : m.IsMaximal)
    (hpm : (p : BlocksAlgInt) ∈ m)
    (G : Type) [Group G] [Finite G] (B : Set (G → ℂ)) (hB : BlocksIsBlock m G B)
    (x y xp yp : G) (hx : BlocksIsPPart p x xp) (hy : BlocksIsPPart p y yp)
    (hxy : ¬ IsConj xp yp) :
    ∑ᶠ χ ∈ B, χ x * starRingEnd ℂ (χ y) = 0
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/BL_block_section_column_orthogonality.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/BL_block_section_column_orthogonality.lean)
