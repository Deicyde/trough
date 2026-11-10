---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_gms_monster_uniqueness, CFSG.Milestones.cl_lit_gms_monster_uniqueness_of_two
statement: formalized
proof: formalized
---

# CL_LIT_GMS_Monster_uniqueness

The milestone module `CFSG.Milestones.CL_LIT_GMS_Monster_uniqueness`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_GMS_Monster_uniqueness.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GMS_Monster_uniqueness.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_gms_monster_uniqueness` (theorem, [line 17](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GMS_Monster_uniqueness.lean#L17)). Proved here.

```lean
theorem cl_lit_gms_monster_uniqueness
    (d₀ : B) (hd₀ : orderOf d₀ = 2)
    (hrank : Matrix.rank (d₀.val.val - 1) = 1860)
    (G : Type) [Group G] [Finite G] (a z : G) (hG : GMSF1Type d₀ a z) :
    Nonempty (G ≃* CFSG.Monster.Griess.AutO)
```

`CFSG.Milestones.cl_lit_gms_monster_uniqueness_of_two` (theorem, [line 27](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GMS_Monster_uniqueness.lean#L27)). Proved here.

```lean
theorem cl_lit_gms_monster_uniqueness_of_two
    (d₀ : B) (hd₀ : orderOf d₀ = 2)
    (hrank : Matrix.rank (d₀.val.val - 1) = 1860)
    (G H : Type) [Group G] [Group H] [Finite G] [Finite H] (a z : G) (b y : H)
    (hG : GMSF1Type d₀ a z) (hH : GMSF1Type d₀ b y) :
    Nonempty (G ≃* H)
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [AT_alternating_automorphism_permutation](../part-01/at-alternating-automorphism-permutation.md)
- [CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition](../part-03/cl-lit-stroth-leon-sims-baby-monster-recognition.md)
- [FAM_Th_simplicity](../part-04/fam-th-simplicity.md)

## Sources

- [CFSG/Milestones/CL_LIT_GMS_Monster_uniqueness.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GMS_Monster_uniqueness.lean)
