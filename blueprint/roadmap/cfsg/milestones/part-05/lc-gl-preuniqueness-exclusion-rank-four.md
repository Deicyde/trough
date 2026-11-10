---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lc_gl_preuniqueness_exclusion_rank_four
statement: formalized
proof: formalized
---

# LC_GL_preuniqueness_exclusion_rank_four

The milestone module `CFSG.Milestones.LC_GL_preuniqueness_exclusion_rank_four`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/LC_GL_preuniqueness_exclusion_rank_four.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_preuniqueness_exclusion_rank_four.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lc_gl_preuniqueness_exclusion_rank_four` (theorem, [line 3307](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_preuniqueness_exclusion_rank_four.lean#L3307)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lc_gl_preuniqueness_exclusion_rank_four
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hchar : IsCharTwoType G)
    (he : 4 ≤ evenRank G) :
    ∃ p ∈ LargeEvenBeta 4 G, ¬ LargeEvenWeakCoreLocal G p
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [LC_GL_theorem_C_rank_four](lc-gl-theorem-c-rank-four.md)
- [LC_GL_uniqueness_exclusion_rank_four](lc-gl-uniqueness-exclusion-rank-four.md)

## Sources

- [CFSG/Milestones/LC_GL_preuniqueness_exclusion_rank_four.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_preuniqueness_exclusion_rank_four.lean)
