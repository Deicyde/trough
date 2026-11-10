---
declaration: theorem
origin: cited
lean: CFSG.Assembly.low_two_rank
statement: formalized
proof: formalized
---

# CFSG.Assembly.low_two_rank

The case `hlow : LowTwoRankStatement` of [`CFSG.Assembly.classification`](reduction.md). What it asserts, defined in [CFSG/Assembly/Reduction.lean, line 26](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L26):

```lean
@[expose] def LowTwoRankStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    Even (Nat.card G) → twoRank G ≤ 2 → C G
```

The theorem the top theorem's proof gives for it, quoted from [CFSG/Assembly/LowTwoRank.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/LowTwoRank.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Assembly.low_two_rank` (theorem, [line 51](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/LowTwoRank.lean#L51)). Proved here.

```lean
theorem low_two_rank
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (heven : Even (Nat.card G))
    (hrank : twoRank G ≤ 2) : InCatalog G
```

Its file imports, directly or through other files, 8 milestone modules: [CLS_connectivity_MacWilliams_four_generator](../milestones/part-01/cls-connectivity-macwilliams-four-generator.md), [FAM_classical_model_membership](../milestones/part-04/fam-classical-model-membership.md), [LC_GL_local_rank_bounds](../milestones/part-05/lc-gl-local-rank-bounds.md), [LR_Glauberman_Z_star_central_Sylow_involution](../milestones/part-05/lr-glauberman-z-star-central-sylow-involution.md), [LR_dihedral_simple_recognition](../milestones/part-05/lr-dihedral-simple-recognition.md), [LR_rank_two_isomorphism_types](../milestones/part-05/lr-rank-two-isomorphism-types.md), [OO_odd_order_solvable](../milestones/part-05/oo-odd-order-solvable.md), [SE_simple_strong_embedding_models](../milestones/part-06/se-simple-strong-embedding-models.md).

## Depends on

- [LC_GL_local_rank_bounds](../milestones/part-05/lc-gl-local-rank-bounds.md)
- [LR_rank_two_isomorphism_types](../milestones/part-05/lr-rank-two-isomorphism-types.md)

## Sources

- [CFSG/Assembly/LowTwoRank.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/LowTwoRank.lean#L51)
