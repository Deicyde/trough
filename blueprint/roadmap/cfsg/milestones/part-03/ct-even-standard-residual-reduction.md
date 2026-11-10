---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ct_even_standard_residual_reduction
statement: formalized
proof: formalized
---

# CT_even_standard_residual_reduction

The milestone module `CFSG.Milestones.CT_even_standard_residual_reduction`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CT_even_standard_residual_reduction.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_even_standard_residual_reduction.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ct_even_standard_residual_reduction` (theorem, [line 1044](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_even_standard_residual_reduction.lean#L1044)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_even_standard_residual_reduction
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (L : Subgroup G) (hL : standardComponentIsStandard L)
    (hcore : ∀ t : G, orderOf t = 2 →
      standardComponentOddCore (Subgroup.centralizer ({t} : Set G)) = ⊥)
    (S : Sylow 2 (Subgroup.centralizer (L : Set G)))
    (hS : IsCyclic (S : Subgroup (Subgroup.centralizer (L : Set G))))
    (htype : Blueprint.Recognition.Exact.EvenStandardType (L ⧸ Subgroup.center L))
    (hexc : ¬ Blueprint.Recognition.Exact.EvenStandardException (L ⧸ Subgroup.center L)) :
    Blueprint.Recognition.Exact.EvenStandardResidual L
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CFSG.Assembly.disconnected_involution_graph](../../case-division/case-hdisc-disconnectedstatement.md)
- [CLS_component_dichotomy](../part-01/cls-component-dichotomy.md)
- [CT_Seitz_centerless_reduction_frontier](ct-seitz-centerless-reduction-frontier.md)
- [LR_Brauer_Suzuki_central_involution](../part-05/lr-brauer-suzuki-central-involution.md)
- [LR_semidihedral_simple_recognition](../part-05/lr-semidihedral-simple-recognition.md)

## Sources

- [CFSG/Milestones/CT_even_standard_residual_reduction.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_even_standard_residual_reduction.lean)
