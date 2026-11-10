---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_monster_existence_griess_conway_1, CFSG.Milestones.cl_lit_monster_existence_griess_conway_2, CFSG.Milestones.cl_lit_monster_existence_griess_conway
statement: formalized
proof: formalized
---

# CL_LIT_Monster_existence_Griess_Conway

The milestone module `CFSG.Milestones.CL_LIT_Monster_existence_Griess_Conway`, one of those CFSG/Milestones.lean imports.

It declares 3 results, quoted from [CFSG/Milestones/CL_LIT_Monster_existence_Griess_Conway.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Monster_existence_Griess_Conway.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_monster_existence_griess_conway_1` (theorem, [line 16](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Monster_existence_Griess_Conway.lean#L16)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_monster_existence_griess_conway_1 :
    ∃ (G : Type) (_ : Group G) (_ : Finite G), IsSimpleGroup G ∧ Nat.card G = monsterOrder ∧
      ∃ a z : G, MonsterIsF1Type a z ∧ ¬ IsConj a z ∧
        ∀ t : G, orderOf t = 2 → IsConj a t ∨ IsConj z t
```

`CFSG.Milestones.cl_lit_monster_existence_griess_conway_2` (theorem, [line 29](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Monster_existence_Griess_Conway.lean#L29)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_monster_existence_griess_conway_2 :
    ∃ (G : Type) (_ : Group G) (_ : Finite G), IsSimpleGroup G ∧ Nat.card G = monsterOrder ∧
      ∃ a z : G, MonsterIsF1Type a z ∧ ¬ IsConj a z ∧
        (∀ t : G, orderOf t = 2 → IsConj a t ∨ IsConj z t) ∧ MonsterTwoAGraphData a z
```

`CFSG.Milestones.cl_lit_monster_existence_griess_conway` (theorem, [line 44](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Monster_existence_Griess_Conway.lean#L44)). Proved here.

```lean
theorem cl_lit_monster_existence_griess_conway :
    MonsterExistenceStatement MGriess
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [AT_alternating_automorphism_permutation](../part-01/at-alternating-automorphism-permutation.md)
- [CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition](../part-03/cl-lit-stroth-leon-sims-baby-monster-recognition.md)
- [FAM_Th_simplicity](../part-04/fam-th-simplicity.md)

## Sources

- [CFSG/Milestones/CL_LIT_Monster_existence_Griess_Conway.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Monster_existence_Griess_Conway.lean)
