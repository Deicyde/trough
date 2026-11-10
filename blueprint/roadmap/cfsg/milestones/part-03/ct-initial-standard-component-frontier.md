---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ct_initial_standard_component_frontier
statement: formalized
proof: formalized
---

# CT_initial_standard_component_frontier

The milestone module `CFSG.Milestones.CT_initial_standard_component_frontier`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CT_initial_standard_component_frontier.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_initial_standard_component_frontier.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ct_initial_standard_component_frontier` (theorem, [line 16](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_initial_standard_component_frontier.lean#L16)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_initial_standard_component_frontier
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper CFSG.Blueprint.Catalog G)
    (hrank : 3 ≤ twoRank G)
    (hcomp : IsComponentType G) (hB : LocalBProperty G) :
    (∃ t : G, orderOf t = 2 ∧ ∃ L : Subgroup G,
        IsComponentOf L (Subgroup.centralizer ({t} : Set G)) ∧ IsStandardSubgroup L) ∨
      (∃ z : G, orderOf z = 2 ∧ ∃ J : Subgroup G,
        IsComponentOf J (Subgroup.centralizer ({z} : Set G)) ∧ z ∈ J ∧
          ∃ r : ℕ, 3 ≤ r ∧ ∃ S : Sylow 2 J,
            Nonempty ((S : Subgroup J) ≃* QuaternionGroup (2 ^ (r - 2))))
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [AT_alternating_automorphism_permutation](../part-01/at-alternating-automorphism-permutation.md)
- [CL_LIT_Aschbacher_component_type_theorem_5](../part-02/cl-lit-aschbacher-component-type-theorem-5.md)
- [CT_catalog_nonabelian_type_partition](ct-catalog-nonabelian-type-partition.md)
- [LC_GL_local_rank_bounds](../part-05/lc-gl-local-rank-bounds.md)

## Sources

- [CFSG/Milestones/CT_initial_standard_component_frontier.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_initial_standard_component_frontier.lean)
