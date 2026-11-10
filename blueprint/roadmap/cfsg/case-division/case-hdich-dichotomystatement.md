---
declaration: theorem
origin: cited
lean: CFSG.Assembly.component_dichotomy
statement: formalized
proof: formalized
---

# CFSG.Assembly.component_dichotomy

The case `hdich : DichotomyStatement` of [`CFSG.Assembly.classification`](reduction.md). What it asserts, defined in [CFSG/Assembly/Reduction.lean, line 30](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L30):

```lean
@[expose] def DichotomyStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    3 ≤ twoRank G → (involutionGraph G).Connected → IsComponentType G ∨ IsCharTwoType G
```

The theorem the top theorem's proof gives for it, quoted from [CFSG/Assembly/Dichotomy.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Dichotomy.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Assembly.component_dichotomy` (theorem, [line 75](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Dichotomy.lean#L75)). Proved here.

```lean
theorem component_dichotomy (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hrank : 3 ≤ twoRank G)
    (hconn : (involutionGraph G).Connected) : IsComponentType G ∨ IsCharTwoType G
```

Its file imports, directly or through other files, 4 milestone modules: [CLS_component_free_centralizer_quotient_characteristic_two](../milestones/part-01/cls-component-free-centralizer-quotient-characte.md), [CLS_component_free_involution_odd_cores_trivial](../milestones/part-01/cls-component-free-involution-odd-cores-trivial.md), [CLS_involution_centralizers_characteristic_two_transfer](../milestones/part-01/cls-involution-centralizers-characteristic-two-t.md), [OO_odd_order_solvable](../milestones/part-05/oo-odd-order-solvable.md).

## Depends on

- [CLS_component_free_involution_odd_cores_trivial](../milestones/part-01/cls-component-free-involution-odd-cores-trivial.md)
- [CLS_involution_centralizers_characteristic_two_transfer](../milestones/part-01/cls-involution-centralizers-characteristic-two-t.md)

## Sources

- [CFSG/Assembly/Dichotomy.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Dichotomy.lean#L75)
