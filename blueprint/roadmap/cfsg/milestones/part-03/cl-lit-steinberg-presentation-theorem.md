---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_steinberg_presentation_theorem
statement: formalized
proof: formalized
---

# CL_LIT_Steinberg_presentation_theorem

The milestone module `CFSG.Milestones.CL_LIT_Steinberg_presentation_theorem`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CL_LIT_Steinberg_presentation_theorem.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Steinberg_presentation_theorem.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_steinberg_presentation_theorem` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Steinberg_presentation_theorem.lean#L12)). Proved here.

```lean
theorem cl_lit_steinberg_presentation_theorem (t : CFSG.Assembly.LowTwoRank.StatedLieTag)
    (n p f : ℕ) [Fact p.Prime] (hadm : CFSG.Assembly.LowTwoRank.StatedLieAdmissible t n p f)
    (hrank : 3 ≤ bnRank t n) :
    PresentationA.{0, 0, w} (bnRootSystem (lieUniversal t n p f hadm.1))
        (lieUniversal t n p f hadm.1).D.rootGroup ∧
      (IsUntwistedTag t →
        IsParametrization (Φ := bnRootSystem (lieUniversal t n p f hadm.1))
            (lieUniversal t n p f hadm.1).D.rootGroup (untwistedParam t n p f hadm.1) ∧
          Nonempty (CommOrder (bnRootSystem (lieUniversal t n p f hadm.1))) ∧
          PresentationB (Φ := bnRootSystem (lieUniversal t n p f hadm.1))
            (untwistedParam t n p f hadm.1) ∧
          RedundantR2 (bnRootSystem (lieUniversal t n p f hadm.1))
            (lieUniversal t n p f hadm.1).D.rootGroup)
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)

## Sources

- [CFSG/Milestones/CL_LIT_Steinberg_presentation_theorem.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Steinberg_presentation_theorem.lean)
