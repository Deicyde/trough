---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ClassicalRep, CFSG.Milestones.fam_classical_model_membership_alltags, CFSG.Milestones.statedClassicalModel_tag_mem, CFSG.Milestones.fam_classical_model_membership
statement: formalized
proof: formalized
---

# FAM_classical_model_membership

The milestone module `CFSG.Milestones.FAM_classical_model_membership`, one of those CFSG/Milestones.lean imports.

It declares 4 results, quoted from [CFSG/Milestones/FAM_classical_model_membership.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_classical_model_membership.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ClassicalRep` (def, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_classical_model_membership.lean#L12)). A definition.

```lean
def ClassicalRep (G : Type) [Group G] : Prop
```

`CFSG.Milestones.fam_classical_model_membership_alltags` (theorem, [line 16](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_classical_model_membership.lean#L16)). Proved here.

```lean
theorem fam_classical_model_membership_alltags (G : Type) [Group G] :
    ClassicalRep G ↔ ∃ (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ),
      Assembly.LowTwoRank.StatedClassicalModel G t n p f
```

`CFSG.Milestones.statedClassicalModel_tag_mem` (theorem, [line 20](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_classical_model_membership.lean#L20)). Proved here.

```lean
theorem statedClassicalModel_tag_mem (G : Type) [Group G]
    (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (h : Assembly.LowTwoRank.StatedClassicalModel G t n p f) :
    t ∈ ({.PSL, .PSU, .PSp, .POmegaOdd, .POmegaPlus, .POmegaMinus} :
      Set Assembly.LowTwoRank.StatedLieTag)
```

`CFSG.Milestones.fam_classical_model_membership` (theorem, [line 35](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_classical_model_membership.lean#L35)). Proved here.

```lean
theorem fam_classical_model_membership (G : Type) [Group G] :
    ClassicalRep G ↔ ∃ t : Assembly.LowTwoRank.StatedLieTag,
      t ∈ ({.PSL, .PSU, .PSp, .POmegaOdd, .POmegaPlus, .POmegaMinus} :
        Set Assembly.LowTwoRank.StatedLieTag) ∧
      ∃ n p f : ℕ, Assembly.LowTwoRank.StatedClassicalModel G t n p f
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.low_two_rank`](../../case-division/case-hlow-lowtworankstatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/FAM_classical_model_membership.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_classical_model_membership.lean)
