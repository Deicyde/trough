---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lc_gl_local_rank_bounds
statement: formalized
proof: formalized
---

# LC_GL_local_rank_bounds

The milestone module `CFSG.Milestones.LC_GL_local_rank_bounds`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/LC_GL_local_rank_bounds.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_local_rank_bounds.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lc_gl_local_rank_bounds` (theorem, [line 14](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_local_rank_bounds.lean#L14)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lc_gl_local_rank_bounds (X : Type*) [Group X] [Finite X] :
    (∀ p : ℕ, p.Prime → p ≠ 2 →
      localRank p X ≤ pRank p (⊤ : Subgroup X) ∧ localRank p X ≤ evenRank X) ∧
    (∀ k : ℕ, 1 ≤ k → ((oddStrata k X).Nonempty ↔ k ≤ evenRank X)) ∧
    oddStrata (evenRank X + 1) X = ∅ ∧
    ∀ k : ℕ, 1 ≤ k → oddStrata (k + 1) X ⊆ oddStrata k X
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.low_two_rank`](../../case-division/case-hlow-lowtworankstatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/LC_GL_local_rank_bounds.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_local_rank_bounds.lean)
