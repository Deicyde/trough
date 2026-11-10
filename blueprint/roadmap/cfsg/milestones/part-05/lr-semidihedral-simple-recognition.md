---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lr_semidihedral_simple_recognition_1, CFSG.Milestones.lr_semidihedral_simple_recognition_2
statement: formalized
proof: formalized
---

# LR_semidihedral_simple_recognition

The milestone module `CFSG.Milestones.LR_semidihedral_simple_recognition`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/LR_semidihedral_simple_recognition.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_semidihedral_simple_recognition.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lr_semidihedral_simple_recognition_1` (theorem, [line 60](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_semidihedral_simple_recognition.lean#L60)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lr_semidihedral_simple_recognition_1
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hsd : ∃ (S : Sylow 2 G) (n : ℕ), 4 ≤ n ∧
      Nonempty ((S : Subgroup G) ≃* SemidihedralGroup n)) :
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ p ^ f % 4 = 3 ∧
        StatedClassicalModel G .PSL 3 p f) ∨
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ p ^ f % 4 = 1 ∧
        StatedClassicalModel G .PSU 3 p f) ∨
    Nonempty (G ≃* StatedM11)
```

`CFSG.Milestones.lr_semidihedral_simple_recognition_2` (theorem, [line 78](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_semidihedral_simple_recognition.lean#L78)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lr_semidihedral_simple_recognition_2
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (P : Sylow 2 G)
    (hsd : ∃ n : ℕ, 4 ≤ n ∧ Nonempty ((P : Subgroup G) ≃* SemidihedralGroup n)) :
    (∃ p k : ℕ, ∃ _hp : Fact p.Prime, 0 < k ∧ p ^ k % 4 = 3 ∧
        Nonempty (G ≃* PSL(3, GaloisField p k))) ∨
    (∃ p k : ℕ, ∃ _hp : Fact p.Prime, 0 < k ∧ p ^ k % 4 = 1 ∧
        Nonempty (G ≃* PSU3 p k)) ∨
    Nonempty (G ≃* M11)
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)
- [LR_Glauberman_Z_star_central_Sylow_involution](lr-glauberman-z-star-central-sylow-involution.md)
- [LR_dihedral_simple_recognition](lr-dihedral-simple-recognition.md)
- [OO_odd_order_solvable](oo-odd-order-solvable.md)

## Sources

- [CFSG/Milestones/LR_semidihedral_simple_recognition.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_semidihedral_simple_recognition.lean)
