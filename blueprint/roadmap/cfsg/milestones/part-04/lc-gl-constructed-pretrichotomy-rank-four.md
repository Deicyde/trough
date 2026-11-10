---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lc_gl_constructed_pretrichotomy_rank_four
statement: formalized
proof: formalized
---

# LC_GL_constructed_pretrichotomy_rank_four

The milestone module `CFSG.Milestones.LC_GL_constructed_pretrichotomy_rank_four`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/LC_GL_constructed_pretrichotomy_rank_four.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_constructed_pretrichotomy_rank_four.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lc_gl_constructed_pretrichotomy_rank_four` (theorem, [line 1941](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_constructed_pretrichotomy_rank_four.lean#L1941)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lc_gl_constructed_pretrichotomy_rank_four
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hchar : IsCharTwoType G)
    (he : 4 ≤ evenRank G) :
    (∀ p ∈ LargeEvenBeta 4 G, LargeEvenWeakCoreLocal G p) ∨ LargeEvenGF2Type G ∨
      ∃ p ∈ LargeEvenBeta 4 G, ∃ (B : Subgroup G) (x : G) (L : Subgroup G),
        LargeEvenSStar p B x L ∧ LargeEvenStandardType p B x L
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [LC_GL_theorem_A](../part-05/lc-gl-theorem-a.md)

## Sources

- [CFSG/Milestones/LC_GL_constructed_pretrichotomy_rank_four.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_constructed_pretrichotomy_rank_four.lean)
