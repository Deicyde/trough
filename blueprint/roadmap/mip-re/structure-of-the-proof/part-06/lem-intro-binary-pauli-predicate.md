---
declaration: lemma
origin: cited
lean: MIPRE.QLD.PauliBinaryProgram.program_ofBits_iff, MIPRE.QLD.PauliBinaryProgram.program_canonical, MIPRE.QLD.PauliAnswerProgram.answerBits_decodeBits, MIPRE.Introspection.DecisionKernel.Answer.pauliDecode_format, MIPRE.Introspection.DecisionKernel.Answer.rawProject_pauliDecode
statement: formalized
proof: formalized
---

# The complete binary Pauli predicate

A uniform polynomial-time program checks the actual QLD predicate on binary questions and answers, preserving all twenty-six question types. Canonical answer encoding and decoding agree on accepted payloads. The total decoder always produces a legal answer constructor for its Pauli question, and the executable full-Pauli projection agrees with the semantic qubit register.

## Depends on

- [Executable binary Pauli queries](lem-intro-executable-pauli-queries.md)
- [The introspective verifier](../part-02/def-intro-verifier.md)

## Proof

Parse the exact answer shape for each type, convert between effective field rows and the self-dual question basis, and compose the checked line, table, probe and phase programs. Prove each finite branch before combining the type dispatch. Full-table outcomes use the same explicit cube numbering as the register projection.

## Lean

Formalized as [`MIPRE.QLD.PauliBinaryProgram.program_ofBits_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliBinaryProgram.program_ofBits_iff), [`MIPRE.QLD.PauliBinaryProgram.program_canonical`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliBinaryProgram.program_canonical), [`MIPRE.QLD.PauliAnswerProgram.answerBits_decodeBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliAnswerProgram.answerBits_decodeBits), [`MIPRE.Introspection.DecisionKernel.Answer.pauliDecode_format`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionKernel.Answer.pauliDecode_format), [`MIPRE.Introspection.DecisionKernel.Answer.rawProject_pauliDecode`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionKernel.Answer.rawProject_pauliDecode).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3844](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3844)
