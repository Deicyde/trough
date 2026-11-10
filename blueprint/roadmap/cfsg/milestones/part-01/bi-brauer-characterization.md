---
declaration: theorem
origin: cited
lean: CFSG.Milestones.bi_brauer_characterization
statement: formalized
proof: formalized
---

# BI_Brauer_characterization

The milestone module `CFSG.Milestones.BI_Brauer_characterization`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/BI_Brauer_characterization.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/BI_Brauer_characterization.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.bi_brauer_characterization` (theorem, [line 13](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/BI_Brauer_characterization.lean#L13)). Proved here.

```lean
theorem _root_.CFSG.Milestones.bi_brauer_characterization
    (G : Type) [Group G] [Finite G] (f : G → ℂ) (hf : BlocksIsClassFunction f) :
    f ∈ BlocksVChar G ↔
      ∀ E : Subgroup G, BlocksBrauerElementary E → (fun e : E => f e) ∈ BlocksVChar E
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/BI_Brauer_characterization.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/BI_Brauer_characterization.lean)
