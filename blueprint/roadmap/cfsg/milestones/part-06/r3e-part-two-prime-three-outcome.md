---
declaration: theorem
origin: cited
lean: CFSG.Milestones.r3e_part_two_prime_three_outcome
statement: formalized
proof: formalized
---

# R3E_part_two_prime_three_outcome

The milestone module `CFSG.Milestones.R3E_part_two_prime_three_outcome`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/R3E_part_two_prime_three_outcome.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/R3E_part_two_prime_three_outcome.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.r3e_part_two_prime_three_outcome` (theorem, [line 3141](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/R3E_part_two_prime_three_outcome.lean#L3141)). Proved here.

```lean
theorem _root_.CFSG.Milestones.r3e_part_two_prime_three_outcome
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hchar : IsCharTwoType G)
    (he : evenRank G = 3) (hq : ∀ q : ℕ, q.Prime → 3 < q → localRank q G < 3) :
    IIModel G ∨ AschCoreLocal G 2
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CFSG.Assembly.component_type](../../case-division/case-hcomp-componentstatement.md)
- [CAT_native_realization](../part-01/cat-native-realization.md)
- [CLS_low_two_rank_classification](../part-02/cls-low-two-rank-classification.md)
- [CL_LIT_Timmesfeld_1978_large_extraspecial](../part-03/cl-lit-timmesfeld-1978-large-extraspecial.md)

## Sources

- [CFSG/Milestones/R3E_part_two_prime_three_outcome.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/R3E_part_two_prime_three_outcome.lean)
