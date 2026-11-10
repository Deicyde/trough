---
declaration: theorem
origin: cited
lean: CFSG.Milestones.gw_original_maximal_odd_s_invariant_r_and_normalizer_core
statement: formalized
proof: formalized
---

# GW_original_maximal_odd_S_invariant_R_and_normalizer_core

The milestone module `CFSG.Milestones.GW_original_maximal_odd_S_invariant_R_and_normalizer_core`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/GW_original_maximal_odd_S_invariant_R_and_normalizer_core.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_maximal_odd_S_invariant_R_and_normalizer_core.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.gw_original_maximal_odd_s_invariant_r_and_normalizer_core` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_maximal_odd_S_invariant_R_and_normalizer_core.lean#L11)). Proved here.

```lean
theorem gw_original_maximal_odd_s_invariant_r_and_normalizer_core (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (d : OriginalData G)
    (hs : d.Stationarity) (hc : d.CanonicalNormalizers) : d.MaximalOddKernel
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/GW_original_maximal_odd_S_invariant_R_and_normalizer_core.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_maximal_odd_S_invariant_R_and_normalizer_core.lean)
