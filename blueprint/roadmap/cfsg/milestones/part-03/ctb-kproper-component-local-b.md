---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ctb_kproper_component_local_b
statement: formalized
proof: formalized
---

# CTB_KProper_component_local_B

The milestone module `CFSG.Milestones.CTB_KProper_component_local_B`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CTB_KProper_component_local_B.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTB_KProper_component_local_B.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ctb_kproper_component_local_b` (theorem, [line 2431](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTB_KProper_component_local_B.lean#L2431)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctb_kproper_component_local_b
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper CFSG.Blueprint.Catalog G)
    (hcomp : IsComponentType G) : oddCore G = ⊥ ∧ LocalBProperty G
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CL_LIT_Curtis_Tits_presentation_theorem](../part-02/cl-lit-curtis-tits-presentation-theorem.md)
- [CL_LIT_Fischer_three_transposition_theorem](../part-02/cl-lit-fischer-three-transposition-theorem.md)
- [CL_LIT_GMS_Monster_uniqueness](../part-02/cl-lit-gms-monster-uniqueness.md)
- [CL_LIT_Monster_existence_Griess_Conway](../part-02/cl-lit-monster-existence-griess-conway.md)
- [CL_LIT_classical_involution_theorem](cl-lit-classical-involution-theorem.md)
- [FAM_sporadic_converse](../part-04/fam-sporadic-converse.md)

## Sources

- [CFSG/Milestones/CTB_KProper_component_local_B.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTB_KProper_component_local_B.lean)
