---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_component_free_involution_odd_cores_trivial
statement: formalized
proof: formalized
---

# CLS_component_free_involution_odd_cores_trivial

The milestone module `CFSG.Milestones.CLS_component_free_involution_odd_cores_trivial`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_component_free_involution_odd_cores_trivial.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_free_involution_odd_cores_trivial.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_component_free_involution_odd_cores_trivial` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_free_involution_odd_cores_trivial.lean#L11)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_component_free_involution_odd_cores_trivial (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hrank : 3 ≤ twoRank G)
    (hcomp : ¬ IsComponentType G) (hse : ∀ M : Subgroup G, ¬ dichotomyStronglyEmbedded M)
    (t : G) (ht : orderOf t = 2) :
    oddCore (Subgroup.centralizer ({t} : Set G)) = ⊥
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.component_dichotomy`](../../case-division/case-hdich-dichotomystatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CLS_component_free_centralizer_quotient_characteristic_two](cls-component-free-centralizer-quotient-characte.md)
- [OO_odd_order_solvable](../part-05/oo-odd-order-solvable.md)

## Sources

- [CFSG/Milestones/CLS_component_free_involution_odd_cores_trivial.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_free_involution_odd_cores_trivial.lean)
