---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ctu_relativeU_catalog, CFSG.Milestones.ctu_kproper_simple_unbalanced_recognition, CFSG.Milestones.ctu_kproper_simple_unbalanced_recognition_models
statement: formalized
proof: formalized
---

# CTU_KProper_simple_unbalanced_recognition

The milestone module `CFSG.Milestones.CTU_KProper_simple_unbalanced_recognition`, one of those CFSG/Milestones.lean imports.

It declares 3 results, quoted from [CFSG/Milestones/CTU_KProper_simple_unbalanced_recognition.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTU_KProper_simple_unbalanced_recognition.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ctu_relativeU_catalog` (theorem, [line 2436](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTU_KProper_simple_unbalanced_recognition.lean#L2436)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctu_relativeU_catalog
    :
    CFSG.ComponentClassification.KProperRelativeB.RelativeU CFSG.Blueprint.Catalog
```

`CFSG.Milestones.ctu_kproper_simple_unbalanced_recognition` (theorem, [line 2458](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTU_KProper_simple_unbalanced_recognition.lean#L2458)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctu_kproper_simple_unbalanced_recognition
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (z : G) (hz : orderOf z = 2)
    (hunbal : CFSG.oddCore (Subgroup.centralizer ({z} : Set G)) ≠ ⊥) :
    CFSG.Blueprint.OddLieType G ∨
      ∃ n : ℕ, 7 ≤ n ∧ n % 4 = 3 ∧ Nonempty (G ≃* alternatingGroup (Fin n))
```

`CFSG.Milestones.ctu_kproper_simple_unbalanced_recognition_models` (theorem, [line 2469](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTU_KProper_simple_unbalanced_recognition.lean#L2469)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctu_kproper_simple_unbalanced_recognition_models
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (z : G) (hz : orderOf z = 2)
    (hunbal : CFSG.oddCore (Subgroup.centralizer ({z} : Set G)) ≠ ⊥) :
    (CFSG.Blueprint.OddLieType G ∨
      ∃ n : ℕ, 7 ≤ n ∧ n % 4 = 3 ∧ Nonempty (G ≃* alternatingGroup (Fin n))) ∧
      CFSG.Blueprint.Catalog G
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CL_LIT_Curtis_Tits_presentation_theorem](../part-02/cl-lit-curtis-tits-presentation-theorem.md)
- [CL_LIT_Fischer_three_transposition_theorem](../part-02/cl-lit-fischer-three-transposition-theorem.md)
- [CL_LIT_GMS_Monster_uniqueness](../part-02/cl-lit-gms-monster-uniqueness.md)
- [CL_LIT_Monster_existence_Griess_Conway](../part-02/cl-lit-monster-existence-griess-conway.md)
- [CL_LIT_classical_involution_theorem](cl-lit-classical-involution-theorem.md)
- [FAM_sporadic_converse](../part-04/fam-sporadic-converse.md)

## Sources

- [CFSG/Milestones/CTU_KProper_simple_unbalanced_recognition.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTU_KProper_simple_unbalanced_recognition.lean)
