---
declaration: theorem
origin: cited
lean: CFSG.Milestones.gw_original_q_five_index_three_character_kernel_order_contradiction, CFSG.Milestones.gw_original_q_five_index_three_character_kernel_order_contradiction_full
statement: formalized
proof: formalized
---

# GW_original_q_five_index_three_character_kernel_order_contradiction

The milestone module `CFSG.Milestones.GW_original_q_five_index_three_character_kernel_order_contradiction`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/GW_original_q_five_index_three_character_kernel_order_contradiction.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_q_five_index_three_character_kernel_order_contradiction.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.gw_original_q_five_index_three_character_kernel_order_contradiction` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_q_five_index_three_character_kernel_order_contradiction.lean#L12)). Proved here.

```lean
theorem gw_original_q_five_index_three_character_kernel_order_contradiction (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (d : OriginalData G)
    (hs : d.Stationarity) (hc : d.CanonicalNormalizers) (hm : d.MaximalOddKernel)
    (hp : d.PureProjectiveNormalizer) (hb : d.CosetBounds)
    (hn : d.n = 3) (hR : d.R ≠ ⊥) (hCN : d.C < d.N)
    (w : CoordinateWitness (d.N ⧸ CFSG.Assembly.oddCore d.N)) (hq : Nat.card w.K = 5)
    (hindex : (d.commonE.subgroupOf d.R).index = 3) (horder : d.ConditionalOrder) : d.CharacterKernelConclusion
```

`CFSG.Milestones.gw_original_q_five_index_three_character_kernel_order_contradiction_full` (theorem, [line 28](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_q_five_index_three_character_kernel_order_contradiction.lean#L28)). Proved here.

```lean
theorem gw_original_q_five_index_three_character_kernel_order_contradiction_full (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (d : OriginalData G)
    (hs : d.Stationarity) (hc : d.CanonicalNormalizers) (hm : d.MaximalOddKernel)
    (hp : d.PureProjectiveNormalizer) (hb : d.CosetBounds)
    (hn : d.n = 3) (hR : d.R ≠ ⊥) (hCN : d.C < d.N)
    (w : CoordinateWitness (d.N ⧸ CFSG.Assembly.oddCore d.N)) (hq : Nat.card w.K = 5)
    (hindex : (d.commonE.subgroupOf d.R).index = 3) (horder : d.ConditionalOrderFull) : d.CharacterKernelConclusion
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/GW_original_q_five_index_three_character_kernel_order_contradiction.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_q_five_index_three_character_kernel_order_contradiction.lean)
