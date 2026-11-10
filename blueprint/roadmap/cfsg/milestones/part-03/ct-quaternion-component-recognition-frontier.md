---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ct_quaternion_component_recognition_frontier
statement: formalized
proof: formalized
---

# CT_quaternion_component_recognition_frontier

The milestone module `CFSG.Milestones.CT_quaternion_component_recognition_frontier`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CT_quaternion_component_recognition_frontier.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_quaternion_component_recognition_frontier.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ct_quaternion_component_recognition_frontier` (theorem, [line 1795](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_quaternion_component_recognition_frontier.lean#L1795)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_quaternion_component_recognition_frontier
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G)
    (z : G) (hz : orderOf z = 2)
    (J : Subgroup G) (hJ : IsComponentOf J (Subgroup.centralizer ({z} : Set G)))
    (hzJ : z ∈ J) (S : Sylow 2 J)
    (hS : ∃ r : ℕ, 3 ≤ r ∧ Nonempty ((S : Subgroup J) ≃* QuaternionGroup (2 ^ (r - 2)))) :
    OddLieType G ∨ Nonempty (G ≃* M11)
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CL_LIT_GH74_sectional_two_rank_four](../part-02/cl-lit-gh74-sectional-two-rank-four.md)

## Sources

- [CFSG/Milestones/CT_quaternion_component_recognition_frontier.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_quaternion_component_recognition_frontier.lean)
