---
declaration: theorem
origin: cited
lean: CFSG.Milestones.gw_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth
statement: formalized
proof: formalized
---

# GW_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth

The milestone module `CFSG.Milestones.GW_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/GW_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.gw_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth` (theorem, [line 13](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth.lean#L13)). Proved here.

```lean
theorem gw_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (d : OriginalData G)
     : d.Stationarity
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CLS_component_free_centralizer_quotient_characteristic_two](../part-01/cls-component-free-centralizer-quotient-characte.md)
- [OO_odd_order_solvable](../part-05/oo-odd-order-solvable.md)

## Sources

- [CFSG/Milestones/GW_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_post_proposition_sixteen_all_prime_stationarity_and_no_growth.lean)
