---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lc_gl_theorem_a
statement: formalized
proof: formalized
---

# LC_GL_theorem_A

The milestone module `CFSG.Milestones.LC_GL_theorem_A`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/LC_GL_theorem_A.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_theorem_A.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lc_gl_theorem_a` (theorem, [line 1757](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_theorem_A.lean#L1757)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lc_gl_theorem_a
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : IsKProper G) (hchar : IsCharTwoType G) (he : 4 ≤ evenRank G)
    (m : ℕ) (hm : 4 ≤ m)
    (ha : ∀ q ∈ GLABeta (m + 1) G, GLAWeakCoreLocal G q)
    (hb : ∀ q ∈ GLABeta m G, GLAWeakCoreLocal G q ∨ GLADeltaZero G q)
    (hc : ∃ q ∈ GLABeta m G, GLATwoLocalRank q G = m ∧ GLADeltaZero G q) :
    ∃ p ∈ GLABeta m G, GLATwoLocalRank p G = m ∧ GLADeltaZero G p ∧
      ((p = 3 ∧ GLAGF2Type G) ∨
        ∃ (B : Subgroup G) (x : G) (L : Subgroup G),
          GLASStar p B x L ∧ GLAStandardType p B x L)
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CAT_native_realization](../part-01/cat-native-realization.md)
- [CL_LIT_Gorenstein_Walter_L_balance](../part-02/cl-lit-gorenstein-walter-l-balance.md)
- [CL_LIT_Timmesfeld_1978_large_extraspecial](../part-03/cl-lit-timmesfeld-1978-large-extraspecial.md)
- [FAM_sporadic_converse](../part-04/fam-sporadic-converse.md)

## Sources

- [CFSG/Milestones/LC_GL_theorem_A.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_theorem_A.lean)
