---
declaration: theorem
origin: cited
lean: CFSG.Milestones.glauberman_replacement
statement: formalized
proof: formalized
---

# ZJ_glauberman_replacement

The milestone module `CFSG.Milestones.ZJ_glauberman_replacement`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/ZJ_glauberman_replacement.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/ZJ_glauberman_replacement.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.glauberman_replacement` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/ZJ_glauberman_replacement.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.glauberman_replacement {p : ℕ} (hp : Nat.Prime p) (hodd : Odd p)
    {S : Type*} [Group S] [Finite S] (hS : IsPGroup p S) (B : Subgroup S) (hB : B.Normal)
    (hclass : ⁅B, B⁆ ≤ (center B).map B.subtype) (hBZ : ⁅B, B⁆ ≤ thompsonCenter S) :
    (∀ A ∈ maxOrderAbelianSubgroups S, B ≤ A) ∨
      ∃ A ∈ maxOrderAbelianSubgroups S, ¬ B ≤ A ∧ B ≤ normalizer (A : Set S)
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/ZJ_glauberman_replacement.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/ZJ_glauberman_replacement.lean)
