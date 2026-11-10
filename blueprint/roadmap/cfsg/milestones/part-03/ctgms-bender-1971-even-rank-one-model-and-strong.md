---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_1, CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_2, CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_3, CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_4
statement: formalized
proof: formalized
---

# CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input

The milestone module `CFSG.Milestones.CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input`, one of those CFSG/Milestones.lean imports.

It declares 4 results, quoted from [CFSG/Milestones/CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_1` (theorem, [line 16](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input.lean#L16)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_1 (f : ℕ) (hf : 2 ≤ f) :
    fusionBenderBorel PSL(2, GaloisField 2 f) (2 ^ f) 1
```

`CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_2` (theorem, [line 26](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input.lean#L26)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_2 (f : ℕ) (hf : 2 ≤ f) :
    fusionBenderBorel (PSU3 2 f) (2 ^ f) 3
```

`CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_3` (theorem, [line 36](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input.lean#L36)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_3
    (X : Type) [Group X] [Finite X] (H : Subgroup X) (hH : fusionStronglyEmbedded H) :
    (∀ S : Sylow 2 X, IsCyclic (S : Subgroup X) ∨
        ∃ r : ℕ, 3 ≤ r ∧ Nonempty ((S : Subgroup X) ≃* QuaternionGroup (2 ^ (r - 2)))) ∨
    ∃ (M N : Subgroup X) (_ : M.Normal) (_ : N.Normal) (_ : (M.subgroupOf N).Normal),
      M ≤ N ∧ Odd (Nat.card M) ∧ Odd N.index ∧ fusionIsBenderGroup (N ⧸ M.subgroupOf N)
```

`CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_4` (theorem, [line 50](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input.lean#L50)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctgms_bender_1971_even_rank_one_model_and_strong_embedding_input_4 (a : ℕ) (ha : 1 ≤ a) :
    fusionBenderBorel (Sz a) (2 ^ (2 * a + 1)) 2
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input.lean)
