---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.AuxiliaryProgram.readingCheck_typed, MIPRE.Introspection.AuxiliaryProgram.rawCheck_haltsWithin, MIPRE.Introspection.AuxiliaryProgram.samplingProg_depthFamily, MIPRE.Introspection.AuxiliaryCanonical.canonicalProg_correct
statement: formalized
proof: formalized
---

# Full-register auxiliary programs

The full padded-register Read relation has an exact executable check, including the original answer cutoff. For a bounded source verifier and the explicit depth, dimension and answer-length hypotheses, a clocked source marginal call implements the padded Sample relation. Independently, a uniform polynomial-time elimination program computes the exact canonical quotient representative of a supplied binary row span.

## Depends on

- [Arbitrary binary source registers and exact padding](lem-intro-binary-source-padding.md)

## Proof

Parse canonical answer encodings while retaining unrestricted full-register dual labels. Restrict only the source sampling call to the original coordinates; exact zero extension proves its padded-game semantics. Use the source boundedness estimate to discharge the clock. For canonical reduction, identify the leading coordinates of the computed pivot basis with the canonical pivot set, and characterize the remainder by its coset and canonical complement. The dual-map specialization and the executable Hide checks are composed in Lemma [Executable quotient hiding and the finite decision kernel](lem-intro-quotient-kernel.md).

## Lean

Formalized as [`MIPRE.Introspection.AuxiliaryProgram.readingCheck_typed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AuxiliaryProgram.readingCheck_typed), [`MIPRE.Introspection.AuxiliaryProgram.rawCheck_haltsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AuxiliaryProgram.rawCheck_haltsWithin), [`MIPRE.Introspection.AuxiliaryProgram.samplingProg_depthFamily`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AuxiliaryProgram.samplingProg_depthFamily), [`MIPRE.Introspection.AuxiliaryCanonical.canonicalProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AuxiliaryCanonical.canonicalProg_correct).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3713](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3713)
