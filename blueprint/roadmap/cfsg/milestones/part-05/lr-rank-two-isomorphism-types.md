---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lr_rank_two_isomorphism_types
statement: formalized
proof: formalized
---

# LR_rank_two_isomorphism_types

The milestone module `CFSG.Milestones.LR_rank_two_isomorphism_types`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/LR_rank_two_isomorphism_types.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_rank_two_isomorphism_types.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lr_rank_two_isomorphism_types` (theorem, [line 13](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_rank_two_isomorphism_types.lean#L13)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lr_rank_two_isomorphism_types
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hrank : twoRank G = 2) :
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ StatedClassicalModel G .PSL 2 p f) ∨
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ StatedClassicalModel G .PSL 3 p f) ∨
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ StatedClassicalModel G .PSU 3 p f) ∨
    StatedClassicalModel G .PSU 3 2 2 ∨
    Nonempty (G ≃* alternatingGroup (Fin 7)) ∨
    Nonempty (G ≃* StatedM11)
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.low_two_rank`](../../case-division/case-hlow-lowtworankstatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CLS_connectivity_MacWilliams_four_generator](../part-01/cls-connectivity-macwilliams-four-generator.md)
- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)
- [LR_Glauberman_Z_star_central_Sylow_involution](lr-glauberman-z-star-central-sylow-involution.md)
- [LR_dihedral_simple_recognition](lr-dihedral-simple-recognition.md)
- [OO_odd_order_solvable](oo-odd-order-solvable.md)
- [SE_simple_strong_embedding_models](../part-06/se-simple-strong-embedding-models.md)

## Sources

- [CFSG/Milestones/LR_rank_two_isomorphism_types.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_rank_two_isomorphism_types.lean)
