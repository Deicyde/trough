---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_borel_tits_local_parabolic, CFSG.Milestones.cl_lit_borel_tits_local_parabolic_all_models
statement: formalized
proof: formalized
---

# CL_LIT_Borel_Tits_local_parabolic

The milestone module `CFSG.Milestones.CL_LIT_Borel_Tits_local_parabolic`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_Borel_Tits_local_parabolic.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Borel_Tits_local_parabolic.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_borel_tits_local_parabolic` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Borel_Tits_local_parabolic.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_borel_tits_local_parabolic
    (r k n : ℕ) [Fact r.Prime] (hk : 0 < k) (hn : 2 ≤ n) (hsmall : n = 2 → 4 ≤ r ^ k)
    (U : Subgroup PSL(n, GaloisField r k)) (hU : U ≠ ⊥) (hUr : IsPGroup r U) :
    ∃ (S : Sylow r PSL(n, GaloisField r k)) (P : Subgroup PSL(n, GaloisField r k)),
      P ≠ ⊤ ∧
      Subgroup.normalizer (U : Set PSL(n, GaloisField r k)) ≤ P ∧
      pCoreOf r (Subgroup.normalizer (U : Set PSL(n, GaloisField r k))) ≤ pCoreOf r P ∧
      Subgroup.normalizer ((S : Subgroup PSL(n, GaloisField r k)) :
        Set PSL(n, GaloisField r k)) ≤ P
```

`CFSG.Milestones.cl_lit_borel_tits_local_parabolic_all_models` (theorem, [line 29](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Borel_Tits_local_parabolic.lean#L29)). Proved here.

```lean
theorem cl_lit_borel_tits_local_parabolic_all_models
    (X : Type) [Group X] (t : Assembly.LowTwoRank.StatedLieTag) (n r f : ℕ)
    (hmodel : Blueprint.LieModel X t n r f)
    (U : Subgroup X) (hU : U ≠ ⊥) (hUr : IsPGroup r U) :
    ∃ (S : Sylow r X) (P : Subgroup X), P ≠ ⊤ ∧
      Subgroup.normalizer (U : Set X) ≤ P ∧
      Open.pCoreOf r (Subgroup.normalizer (U : Set X)) ≤ Open.pCoreOf r P ∧ U ≤ Open.pCoreOf r P ∧
      (t ≠ .Tits → Subgroup.normalizer ((S : Subgroup X) : Set X) ≤ P) ∧
      (t = .Tits → (S : Subgroup X) ≤ P)
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)

## Sources

- [CFSG/Milestones/CL_LIT_Borel_Tits_local_parabolic.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Borel_Tits_local_parabolic.lean)
