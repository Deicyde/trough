---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lc_gl_standard_type_lie_char_two_recognition_rank_four, CFSG.Milestones.lc_gl_standard_type_recognition_rank_four
statement: formalized
proof: formalized
---

# LC_GL_standard_type_recognition_rank_four

The milestone module `CFSG.Milestones.LC_GL_standard_type_recognition_rank_four`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/LC_GL_standard_type_recognition_rank_four.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_standard_type_recognition_rank_four.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lc_gl_standard_type_lie_char_two_recognition_rank_four` (theorem, [line 240](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_standard_type_recognition_rank_four.lean#L240)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lc_gl_standard_type_lie_char_two_recognition_rank_four
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hchar : IsCharTwoType G)
    (he : 4 ≤ evenRank G) (p : ℕ) (hp : p ∈ LargeEvenBeta 4 G) (B : Subgroup G) (x : G)
    (L : Subgroup G) (hS : LargeEvenSStar p B x L) (hst : LargeEvenStandardType p B x L) :
    InLieTypeCharTwoCatalog G
```

`CFSG.Milestones.lc_gl_standard_type_recognition_rank_four` (theorem, [line 264](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_standard_type_recognition_rank_four.lean#L264)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lc_gl_standard_type_recognition_rank_four
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hchar : IsCharTwoType G)
    (he : 4 ≤ evenRank G) (p : ℕ) (hp : p ∈ LargeEvenBeta 4 G) (B : Subgroup G) (x : G)
    (L : Subgroup G) (hS : LargeEvenSStar p B x L) (hst : LargeEvenStandardType p B x L) :
    InCatalog G
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CAT_native_realization](../part-01/cat-native-realization.md)
- [CL_LIT_GH74_sectional_two_rank_four](../part-02/cl-lit-gh74-sectional-two-rank-four.md)
- [CL_LIT_Gorenstein_Walter_L_balance](../part-02/cl-lit-gorenstein-walter-l-balance.md)
- [FAM_sporadic_converse](../part-04/fam-sporadic-converse.md)

## Sources

- [CFSG/Milestones/LC_GL_standard_type_recognition_rank_four.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_standard_type_recognition_rank_four.lean)
