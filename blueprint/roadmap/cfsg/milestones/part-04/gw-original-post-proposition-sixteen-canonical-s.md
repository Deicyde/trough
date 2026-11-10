---
declaration: theorem
origin: cited
lean: CFSG.Milestones.gw_original_post_proposition_sixteen_canonical_stationary_prime_normalizers, CFSG.Milestones.gw_original_post_proposition_sixteen_canonical_stationary_prime_normalizers_full
statement: formalized
proof: formalized
---

# GW_original_post_proposition_sixteen_canonical_stationary_prime_normalizers

The milestone module `CFSG.Milestones.GW_original_post_proposition_sixteen_canonical_stationary_prime_normalizers`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/GW_original_post_proposition_sixteen_canonical_stationary_prime_normalizers.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_post_proposition_sixteen_canonical_stationary_prime_normalizers.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.gw_original_post_proposition_sixteen_canonical_stationary_prime_normalizers` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_post_proposition_sixteen_canonical_stationary_prime_normalizers.lean#L11)). Proved here.

```lean
theorem gw_original_post_proposition_sixteen_canonical_stationary_prime_normalizers (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (d : OriginalData G)
    (hs : d.Stationarity) : d.CanonicalNormalizers
```

`CFSG.Milestones.gw_original_post_proposition_sixteen_canonical_stationary_prime_normalizers_full` (theorem, [line 22](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_post_proposition_sixteen_canonical_stationary_prime_normalizers.lean#L22)). Proved here.

```lean
theorem gw_original_post_proposition_sixteen_canonical_stationary_prime_normalizers_full (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (d : OriginalData G)
    (hs : d.Stationarity) : d.CanonicalNormalizersFull
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CLS_component_free_centralizer_quotient_characteristic_two](../part-01/cls-component-free-centralizer-quotient-characte.md)

## Sources

- [CFSG/Milestones/GW_original_post_proposition_sixteen_canonical_stationary_prime_normalizers.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_post_proposition_sixteen_canonical_stationary_prime_normalizers.lean)
