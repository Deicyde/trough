---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ct_odd_standard_recognition_frontier, CFSG.Milestones.ct_odd_standard_recognition_frontier_models
statement: formalized
proof: formalized
---

# CT_odd_standard_recognition_frontier

The milestone module `CFSG.Milestones.CT_odd_standard_recognition_frontier`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CT_odd_standard_recognition_frontier.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_odd_standard_recognition_frontier.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ct_odd_standard_recognition_frontier` (theorem, [line 3450](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_odd_standard_recognition_frontier.lean#L3450)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_odd_standard_recognition_frontier
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (L : Subgroup G) (hL : standardComponentIsStandard L)
    (htype : Blueprint.Recognition.Exact.OddStandardType (L ⧸ Subgroup.center L)) :
    (∃ n : ℕ, 9 ≤ n ∧ Nonempty (G ≃* alternatingGroup (Fin n))) ∨
      (∃ p : ℕ, p.Prime ∧ p ≠ 2 ∧ Nat.card G ∈ lieOrdersChar p) ∨
      Nat.card G ∈ standardComponentOddSporadicOrders
```

`CFSG.Milestones.ct_odd_standard_recognition_frontier_models` (theorem, [line 3481](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_odd_standard_recognition_frontier.lean#L3481)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_odd_standard_recognition_frontier_models
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (L : Subgroup G) (hL : standardComponentIsStandard L)
    (htype : Blueprint.Recognition.Exact.OddStandardType (L ⧸ Subgroup.center L)) :
    (∃ n : ℕ, 9 ≤ n ∧ Nonempty (G ≃* alternatingGroup (Fin n))) ∨ Blueprint.OddLieType G ∨
      (Blueprint.NativeSporadic.IsSporadic G .M12 ∨ Blueprint.NativeSporadic.IsSporadic G .J1 ∨
        Blueprint.NativeSporadic.IsSporadic G .J2 ∨ Blueprint.NativeSporadic.IsSporadic G .HS ∨
        Blueprint.NativeSporadic.IsSporadic G .McL ∨ Blueprint.NativeSporadic.IsSporadic G .Ly ∨
        Blueprint.NativeSporadic.IsSporadic G .Suz ∨ Blueprint.NativeSporadic.IsSporadic G .He ∨
        Blueprint.NativeSporadic.IsSporadic G .ONan)
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CL_LIT_Gorenstein_Walter_L_balance](../part-02/cl-lit-gorenstein-walter-l-balance.md)
- [CTSS_sporadic_standard_centerless_M12_J2_and_other_quotients_frontier](ctss-sporadic-standard-centerless-m12-j2-and-oth.md)
- [CTU_KProper_simple_unbalanced_recognition](ctu-kproper-simple-unbalanced-recognition.md)
- [CT_rank_two_standard_recognition_frontier](ct-rank-two-standard-recognition-frontier.md)

## Sources

- [CFSG/Milestones/CT_odd_standard_recognition_frontier.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_odd_standard_recognition_frontier.lean)
