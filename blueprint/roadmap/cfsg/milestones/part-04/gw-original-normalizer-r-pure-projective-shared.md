---
declaration: theorem
origin: cited
lean: CFSG.Milestones.gw_original_normalizer_r_pure_projective_shared_fourgroup_and_index_divisor
statement: formalized
proof: formalized
---

# GW_original_normalizer_R_pure_projective_shared_fourgroup_and_index_divisor

The milestone module `CFSG.Milestones.GW_original_normalizer_R_pure_projective_shared_fourgroup_and_index_divisor`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/GW_original_normalizer_R_pure_projective_shared_fourgroup_and_index_divisor.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_normalizer_R_pure_projective_shared_fourgroup_and_index_divisor.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.gw_original_normalizer_r_pure_projective_shared_fourgroup_and_index_divisor` (theorem, [line 14](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_normalizer_R_pure_projective_shared_fourgroup_and_index_divisor.lean#L14)). Proved here.

```lean
theorem gw_original_normalizer_r_pure_projective_shared_fourgroup_and_index_divisor (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (d : OriginalData G)
    (hs : d.Stationarity) (hc : d.CanonicalNormalizers) (hm : d.MaximalOddKernel)
    (hR : d.R ≠ ⊥) (hCN : d.C < d.N) : d.PureProjectiveNormalizer
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CLS_component_free_centralizer_quotient_characteristic_two](../part-01/cls-component-free-centralizer-quotient-characte.md)

## Sources

- [CFSG/Milestones/GW_original_normalizer_R_pure_projective_shared_fourgroup_and_index_divisor.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_normalizer_R_pure_projective_shared_fourgroup_and_index_divisor.lean)
