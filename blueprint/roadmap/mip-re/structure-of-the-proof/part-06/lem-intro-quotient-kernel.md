---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.AuxiliaryDual.rowSpaceCheck_correct, MIPRE.Introspection.AuxiliaryDecision.guarded_complete, MIPRE.Introspection.AuxiliaryDecision.check_raw_sound, MIPRE.Introspection.DecisionKernel.program_sound_numbered, MIPRE.Introspection.DecisionKernel.program_complete_numbered
statement: formalized
proof: formalized
---

# Executable quotient hiding and the finite decision kernel

The actual binary decision kernel implements all auxiliary branches using one source-simulation clock and the supplied canonical parameters. Accepted raw answers decode into a finite quotient game: original answers retain their finite length bound and Pauli answers retain the actual QLD alphabet. Conversely, accepted finite answers with the honest prefix, source-output and Pauli-format support conditions have accepted canonical encodings.

## Depends on

- [Full-register auxiliary programs](lem-intro-executable-padded-auxiliary.md)
- [The complete binary Pauli predicate](lem-intro-binary-pauli-predicate.md)

## Proof depends on

- [Actual adaptive prefix law and residual registers](../part-04/lem-intro-adaptive-prefix.md)
- [Full Read rigidity](../part-04/lem-intro-read-rigidity.md)

## Proof

Use row-space membership to express the hiding relation independently of the local coordinate enumeration. Decode dual labels blockwise; prefix agreement makes the selected transforms agree in every tested block. Clocked source queries implement the guards and source decision call. Canonical format inversions and bounded source-answer decoding then give the raw soundness and honest encoding implications in both orientations.

## Lean

Formalized as [`MIPRE.Introspection.AuxiliaryDual.rowSpaceCheck_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AuxiliaryDual.rowSpaceCheck_correct), [`MIPRE.Introspection.AuxiliaryDecision.guarded_complete`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AuxiliaryDecision.guarded_complete), [`MIPRE.Introspection.AuxiliaryDecision.check_raw_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AuxiliaryDecision.check_raw_sound), [`MIPRE.Introspection.DecisionKernel.program_sound_numbered`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionKernel.program_sound_numbered), [`MIPRE.Introspection.DecisionKernel.program_complete_numbered`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionKernel.program_complete_numbered).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3868](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3868)
