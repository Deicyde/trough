---
declaration: theorem
origin: cited
lean: CFSG.Blueprint.suzukiModel_admissible, CFSG.Blueprint.oddLieType_or_evenLieType_of_lieModel, CFSG.Milestones.ct_catalog_nonabelian_type_partition_converse, CFSG.Milestones.ct_catalog_nonabelian_type_partition
statement: formalized
proof: formalized
---

# CT_catalog_nonabelian_type_partition

The milestone module `CFSG.Milestones.CT_catalog_nonabelian_type_partition`, one of those CFSG/Milestones.lean imports.

It declares 4 results, quoted from [CFSG/Milestones/CT_catalog_nonabelian_type_partition.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_catalog_nonabelian_type_partition.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Blueprint.suzukiModel_admissible` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_catalog_nonabelian_type_partition.lean#L11)). Proved here.

```lean
theorem suzukiModel_admissible {G : Type} [Group G] {p f : ℕ} (h : SuzukiModel G p f) :
    StatedLieAdmissible .twistedB2 0 p f
```

`CFSG.Blueprint.oddLieType_or_evenLieType_of_lieModel` (theorem, [line 16](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_catalog_nonabelian_type_partition.lean#L16)). Proved here.

```lean
theorem oddLieType_or_evenLieType_of_lieModel {X : Type} [Group X] {t : StatedLieTag}
    {n p f : ℕ} (hadm : StatedLieAdmissible t n p f) (h : LieModel X t n p f) :
    OddLieType X ∨ EvenLieType X
```

`CFSG.Milestones.ct_catalog_nonabelian_type_partition_converse` (theorem, [line 35](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_catalog_nonabelian_type_partition.lean#L35)). Proved here.

```lean
theorem ct_catalog_nonabelian_type_partition_converse (X : Type) [Group X]
    (h : (∃ n : ℕ, 5 ≤ n ∧ Nonempty (X ≃* alternatingGroup (Fin n))) ∨
      OddLieType X ∨ EvenLieType X ∨ NativeSporadic.SporadicRep X) : Catalog X
```

`CFSG.Milestones.ct_catalog_nonabelian_type_partition` (theorem, [line 44](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_catalog_nonabelian_type_partition.lean#L44)). Proved here.

```lean
theorem ct_catalog_nonabelian_type_partition (X : Type) [Group X]
    (hnonab : ∃ a b : X, a * b ≠ b * a) :
    Catalog X ↔
      (∃ n : ℕ, 5 ≤ n ∧ Nonempty (X ≃* alternatingGroup (Fin n))) ∨
        OddLieType X ∨ EvenLieType X ∨ NativeSporadic.SporadicRep X
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)

## Sources

- [CFSG/Milestones/CT_catalog_nonabelian_type_partition.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_catalog_nonabelian_type_partition.lean)
