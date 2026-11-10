---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lc_gl_embedding_theorem_d2_rank_four
statement: formalized
proof: formalized
---

# LC_GL_embedding_theorem_D2_rank_four

The milestone module `CFSG.Milestones.LC_GL_embedding_theorem_D2_rank_four`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/LC_GL_embedding_theorem_D2_rank_four.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_embedding_theorem_D2_rank_four.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lc_gl_embedding_theorem_d2_rank_four` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_embedding_theorem_D2_rank_four.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lc_gl_embedding_theorem_d2_rank_four
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : IsKProper G) (hchar : IsCharTwoType G) (he : 4 ≤ evenRank G)
    (hδ₁ : GLBDeltaOne G) (hδ₂ : GLBDeltaTwo G)
    (p : ℕ) (hp : p ∈ GLBBetaFour G) (P : Sylow p G)
    (M : Subgroup G) (hM : GLBIsMaxTwoLocal M) (hPM : GLBCore p 2 (P : Subgroup G) ≤ M)
    (Q : Subgroup G) (hQ : IsPGroup p Q) (hQrank : pRank p Q = 2) (hQM : GLBCore p 1 Q ≤ M)
    (H : Subgroup G) (hH : IsTwoLocal H) (hQH : Q ≤ H) :
    H ≤ M
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [LC_GL_embedding_theorem_D1_rank_four](lc-gl-embedding-theorem-d1-rank-four.md)

## Sources

- [CFSG/Milestones/LC_GL_embedding_theorem_D2_rank_four.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_embedding_theorem_D2_rank_four.lean)
