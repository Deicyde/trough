---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_aschbacher_proper_two_generated_core
statement: formalized
proof: formalized
---

# CL_LIT_Aschbacher_proper_two_generated_core

The milestone module `CFSG.Milestones.CL_LIT_Aschbacher_proper_two_generated_core`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CL_LIT_Aschbacher_proper_two_generated_core.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Aschbacher_proper_two_generated_core.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_aschbacher_proper_two_generated_core` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Aschbacher_proper_two_generated_core.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_aschbacher_proper_two_generated_core
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (S : Sylow 2 G) (hrank : 3 ≤ pRank 2 (S : Subgroup G))
    (hcore : properTwoGenCoreGamma (S : Subgroup G) 2 ≠ ⊤) :
    properTwoGenCoreGamma (S : Subgroup G) 1 ≠ ⊤ ∨ Nonempty (G ≃* properTwoGenCoreJ1)
```

The files of 3 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CFSG.Assembly.disconnected_involution_graph](../../case-division/case-hdisc-disconnectedstatement.md)
- [CFSG.Assembly.low_two_rank](../../case-division/case-hlow-lowtworankstatement.md)
- [CLS_component_free_centralizer_quotient_characteristic_two](../part-01/cls-component-free-centralizer-quotient-characte.md)

## Sources

- [CFSG/Milestones/CL_LIT_Aschbacher_proper_two_generated_core.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Aschbacher_proper_two_generated_core.lean)
