---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_stroth_leon_sims_baby_monster_recognition, CFSG.Milestones.cl_lit_stroth_leon_sims_baby_monster_recognition_models
statement: formalized
proof: formalized
---

# CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition

The milestone module `CFSG.Milestones.CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_stroth_leon_sims_baby_monster_recognition` (theorem, [line 17](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition.lean#L17)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_stroth_leon_sims_baby_monster_recognition :
    ∃ (B : Type) (_ : Group B) (_ : Finite B), IsSimpleGroup B ∧
      Nat.card B = sporadicOrderBabyMonster ∧
      ∃ d₀ : B, orderOf d₀ = 2 ∧
        Nat.card (Subgroup.centralizer ({d₀} : Set B)) = 4 * sporadicOrderTwistedE6Two ∧
        ∀ (G : Type) [Group G] [Finite G], IsSimpleGroup G →
          ∀ d : G, orderOf d = 2 →
            Nonempty (Subgroup.centralizer ({d} : Set G) ≃*
              Subgroup.centralizer ({d₀} : Set B)) →
            Nonempty (G ≃* B)
```

`CFSG.Milestones.cl_lit_stroth_leon_sims_baby_monster_recognition_models` (theorem, [line 36](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition.lean#L36)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_stroth_leon_sims_baby_monster_recognition_models
    (d₀ : Blueprint.NativeSporadic.B) (hd₀ : orderOf d₀ = 2)
    (hrank : Matrix.rank (d₀.val.val - 1) = 1860)
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (d : G) (hd : orderOf d = 2)
    (hcentralizer : Nonempty (Subgroup.centralizer ({d} : Set G) ≃*
      Subgroup.centralizer ({d₀} : Set Blueprint.NativeSporadic.B))) :
    Nonempty (G ≃* Blueprint.NativeSporadic.B)
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CL_LIT_Goldschmidt_strongly_closed_abelian](../part-02/cl-lit-goldschmidt-strongly-closed-abelian.md)

## Sources

- [CFSG/Milestones/CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition.lean)
