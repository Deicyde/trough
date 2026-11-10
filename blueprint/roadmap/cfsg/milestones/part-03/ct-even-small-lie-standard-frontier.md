---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ct_even_small_lie_standard_frontier, CFSG.Milestones.ct_even_small_lie_standard_frontier_models
statement: formalized
proof: formalized
---

# CT_even_small_Lie_standard_frontier

The milestone module `CFSG.Milestones.CT_even_small_Lie_standard_frontier`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CT_even_small_Lie_standard_frontier.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_even_small_Lie_standard_frontier.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ct_even_small_lie_standard_frontier` (theorem, [line 761](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_even_small_Lie_standard_frontier.lean#L761)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_even_small_lie_standard_frontier
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (L : Subgroup G) (hL : standardComponentIsStandard L)
    (hcore : ∀ t : G, orderOf t = 2 →
      standardComponentOddCore (Subgroup.centralizer ({t} : Set G)) = ⊥)
    (S : Sylow 2 (Subgroup.centralizer (L : Set G)))
    (hS : IsCyclic (S : Subgroup (Subgroup.centralizer (L : Set G))))
    (htype : Blueprint.Recognition.Exact.EvenStandardType (L ⧸ Subgroup.center L))
    (hexc : ¬ Blueprint.Recognition.Exact.EvenStandardException (L ⧸ Subgroup.center L))
    (hres : Blueprint.Recognition.Exact.EvenStandardResidual L)
    (hbcd : Blueprint.Recognition.Exact.ResidualB L ∨ Blueprint.Recognition.Exact.ResidualC L ∨
      Blueprint.Recognition.Exact.ResidualD L) :
    Nat.card G ∈ standardComponentEvenSporadicOrders
```

`CFSG.Milestones.ct_even_small_lie_standard_frontier_models` (theorem, [line 783](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_even_small_Lie_standard_frontier.lean#L783)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_even_small_lie_standard_frontier_models
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (L : Subgroup G) (hL : standardComponentIsStandard L)
    (hcore : ∀ t : G, orderOf t = 2 →
      standardComponentOddCore (Subgroup.centralizer ({t} : Set G)) = ⊥)
    (S : Sylow 2 (Subgroup.centralizer (L : Set G)))
    (hS : IsCyclic (S : Subgroup (Subgroup.centralizer (L : Set G))))
    (htype : Blueprint.Recognition.Exact.EvenStandardType (L ⧸ Subgroup.center L))
    (hexc : ¬ Blueprint.Recognition.Exact.EvenStandardException (L ⧸ Subgroup.center L))
    (hres : Blueprint.Recognition.Exact.EvenStandardResidual L)
    (hbcd : Blueprint.Recognition.Exact.ResidualB L ∨ Blueprint.Recognition.Exact.ResidualC L ∨
      Blueprint.Recognition.Exact.ResidualD L) :
    Blueprint.Recognition.EvenSporadicOutcome G
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [AT_alternating_automorphism_permutation](../part-01/at-alternating-automorphism-permutation.md)
- [CL_LIT_SQTK_simple_listBase](cl-lit-sqtk-simple-listbase.md)
- [CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition](cl-lit-stroth-leon-sims-baby-monster-recognition.md)
- [CT_catalog_nonabelian_type_partition](ct-catalog-nonabelian-type-partition.md)
- [LC_GL_local_rank_bounds](../part-05/lc-gl-local-rank-bounds.md)

## Sources

- [CFSG/Milestones/CT_even_small_Lie_standard_frontier.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_even_small_Lie_standard_frontier.lean)
