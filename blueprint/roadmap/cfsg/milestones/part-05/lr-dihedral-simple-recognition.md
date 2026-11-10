---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lr_dihedral_simple_recognition
statement: formalized
proof: formalized
---

# LR_dihedral_simple_recognition

The milestone module `CFSG.Milestones.LR_dihedral_simple_recognition`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/LR_dihedral_simple_recognition.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_dihedral_simple_recognition.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lr_dihedral_simple_recognition` (theorem, [line 13](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_dihedral_simple_recognition.lean#L13)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lr_dihedral_simple_recognition (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (S : Sylow 2 G) (n : ℕ) (hn : 2 ≤ n)
    (hS : Nonempty ((S : Subgroup G) ≃* DihedralGroup (2 ^ (n - 1)))) :
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ LowTwoRank.StatedClassicalModel G .PSL 2 p f) ∨
      Nonempty (G ≃* alternatingGroup (Fin 7))
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.low_two_rank`](../../case-division/case-hlow-lowtworankstatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/LR_dihedral_simple_recognition.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_dihedral_simple_recognition.lean)
