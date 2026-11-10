---
declaration: theorem
origin: cited
lean: CFSG.Milestones.r3e_rank_three_core_uniqueness_exclusion
statement: formalized
proof: formalized
---

# R3E_rank_three_core_uniqueness_exclusion

The milestone module `CFSG.Milestones.R3E_rank_three_core_uniqueness_exclusion`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/R3E_rank_three_core_uniqueness_exclusion.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/R3E_rank_three_core_uniqueness_exclusion.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.r3e_rank_three_core_uniqueness_exclusion` (theorem, [line 3615](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/R3E_rank_three_core_uniqueness_exclusion.lean#L3615)). Proved here.

```lean
theorem _root_.CFSG.Milestones.r3e_rank_three_core_uniqueness_exclusion
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hchar : IsCharTwoType G)
    (he : evenRank G = 3) : ¬ AschCoreLocal G 2
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CL_LIT_Aschbacher_1983_uniqueness_case_rank_three](../part-02/cl-lit-aschbacher-1983-uniqueness-case-rank-thre.md)
- [CL_LIT_GL83_Theorem_C_preuniqueness_rank_three](../part-02/cl-lit-gl83-theorem-c-preuniqueness-rank-three.md)

## Sources

- [CFSG/Milestones/R3E_rank_three_core_uniqueness_exclusion.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/R3E_rank_three_core_uniqueness_exclusion.lean)
