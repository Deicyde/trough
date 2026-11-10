---
declaration: theorem
origin: cited
lean: CFSG.Milestones.gw_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility
statement: formalized
proof: formalized
---

# GW_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility

The milestone module `CFSG.Milestones.GW_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/GW_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.gw_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility.lean#L12)). Proved here.

```lean
theorem gw_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (d : OriginalData G)
    (hs : d.Stationarity) (hc : d.CanonicalNormalizers) (hm : d.MaximalOddKernel)
    (hp : d.PureProjectiveNormalizer) (hR : d.R ≠ ⊥) (hCN : d.C < d.N) : d.CosetBounds
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/GW_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/GW_original_normalizer_coset_involution_fixedpoints_secondary_torus_divisibility.lean)
