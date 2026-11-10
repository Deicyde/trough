---
declaration: theorem
origin: cited
lean: CFSG.Milestones.alternating_automorphism_permutation
statement: formalized
proof: formalized
---

# AT_alternating_automorphism_permutation

The milestone module `CFSG.Milestones.AT_alternating_automorphism_permutation`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/AT_alternating_automorphism_permutation.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/AT_alternating_automorphism_permutation.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.alternating_automorphism_permutation` (theorem, [line 13](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/AT_alternating_automorphism_permutation.lean#L13)). Proved here.

```lean
theorem _root_.CFSG.Milestones.alternating_automorphism_permutation {n : ℕ} (hn : n = 5 ∨ 7 ≤ n)
    (f : MulAut (alternatingGroup (Fin n))) :
    ∃ σ : Perm (Fin n), ∀ g : alternatingGroup (Fin n),
      (f g : Perm (Fin n)) = σ * (g : Perm (Fin n)) * σ⁻¹
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/AT_alternating_automorphism_permutation.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/AT_alternating_automorphism_permutation.lean)
