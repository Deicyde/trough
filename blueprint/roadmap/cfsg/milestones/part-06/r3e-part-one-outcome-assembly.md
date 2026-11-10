---
declaration: theorem
origin: cited
lean: CFSG.Milestones.r3e_part_one_outcome_assembly
statement: formalized
proof: formalized
---

# R3E_part_one_outcome_assembly

The milestone module `CFSG.Milestones.R3E_part_one_outcome_assembly`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/R3E_part_one_outcome_assembly.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/R3E_part_one_outcome_assembly.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.r3e_part_one_outcome_assembly` (theorem, [line 1901](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/R3E_part_one_outcome_assembly.lean#L1901)). Proved here.

```lean
theorem _root_.CFSG.Milestones.r3e_part_one_outcome_assembly
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hchar : IsCharTwoType G)
    (he : evenRank G = 3) (hq : ∃ q : ℕ, q.Prime ∧ 3 < q ∧ localRank q G = 3) :
    IModel G ∨ AschCoreLocal G 2
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CL_LIT_GH74_sectional_two_rank_four](../part-02/cl-lit-gh74-sectional-two-rank-four.md)

## Sources

- [CFSG/Milestones/R3E_part_one_outcome_assembly.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/R3E_part_one_outcome_assembly.lean)
