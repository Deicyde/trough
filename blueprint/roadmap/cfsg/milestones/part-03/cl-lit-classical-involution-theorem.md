---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_classical_involution_theorem_models, CFSG.Milestones.cl_lit_classical_involution_theorem
statement: formalized
proof: formalized
---

# CL_LIT_classical_involution_theorem

The milestone module `CFSG.Milestones.CL_LIT_classical_involution_theorem`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_classical_involution_theorem.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_classical_involution_theorem.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_classical_involution_theorem_models` (theorem, [line 1806](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_classical_involution_theorem.lean#L1806)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_classical_involution_theorem_models
    (G : Type) [Group G] [Finite G]
    [IsSimpleGroup (genFittingFStar G)]
    (hFnonab : ∃ a b : genFittingFStar G, a * b ≠ b * a)
    (z : G) (hz : orderOf z = 2)
    (J : Subgroup G) (hzJ : z ∈ J) (hJ : IsSubnormal J (Subgroup.centralizer ({z} : Set G)))
    (S : Sylow 2 J)
    (hS : ∃ r : ℕ, 3 ≤ r ∧ Nonempty ((S : Subgroup J) ≃* QuaternionGroup (2 ^ (r - 2)))) :
    (classicalInvolutionWitness J → Blueprint.OddLieType (genFittingFStar G) ∨
      Blueprint.NativeSporadic.IsSporadic (genFittingFStar G) .M11) ∧
    (classicalInvolutionTightlyEmbedded J → Blueprint.OddLieType (genFittingFStar G) ∨
      Blueprint.NativeSporadic.IsSporadic (genFittingFStar G) .M11 ∨
      Blueprint.NativeSporadic.IsSporadic (genFittingFStar G) .M12)
```

`CFSG.Milestones.cl_lit_classical_involution_theorem` (theorem, [line 1828](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_classical_involution_theorem.lean#L1828)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_classical_involution_theorem
    (G : Type) [Group G] [Finite G]
    (F : Subgroup G) [F.Normal] [IsSimpleGroup F]
    (hFnonab : ∃ a b : F, a * b ≠ b * a)
    (hFstar : Subgroup.centralizer (F : Set G) = ⊥)
    (z : G) (hz : orderOf z = 2)
    (J : Subgroup G) (hzJ : z ∈ J) (hJ : IsSubnormal J (Subgroup.centralizer ({z} : Set G)))
    (S : Sylow 2 J)
    (hS : ∃ r : ℕ, 3 ≤ r ∧ Nonempty ((S : Subgroup J) ≃* QuaternionGroup (2 ^ (r - 2)))) :
    (classicalInvolutionWitness J →
      (∃ p : ℕ, p.Prime ∧ p ≠ 2 ∧ Nat.card F ∈ lieOrdersChar p) ∨ Nonempty (F ≃* M11)) ∧
    (classicalInvolutionTightlyEmbedded J →
      (∃ p : ℕ, p.Prime ∧ p ≠ 2 ∧ Nat.card F ∈ lieOrdersChar p) ∨ Nonempty (F ≃* M11) ∨
        Nonempty (F ≃* classicalInvolutionM12))
```

The files of 3 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CL_LIT_GH74_sectional_two_rank_four](../part-02/cl-lit-gh74-sectional-two-rank-four.md)

## Sources

- [CFSG/Milestones/CL_LIT_classical_involution_theorem.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_classical_involution_theorem.lean)
