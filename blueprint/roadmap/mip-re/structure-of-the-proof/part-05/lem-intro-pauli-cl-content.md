---
declaration: lemma
origin: cited
lean: MIPRE.QLD.PauliCL.presentation_exactlyOn, MIPRE.QLD.PauliCL.questionOfVector_presentation, MIPRE.QLD.PauliCL.presentation_pauli_eval, MIPRE.QLD.PauliCL.qldGame_mu_presentation, MIPRE.QLD.PauliCL.binaryPresentation_exactlyOn, MIPRE.QLD.PauliCL.binaryPresentation_pauli_eval, MIPRE.QLD.PauliCL.qldGame_mu_binaryPresentation, MIPRE.QLD.PauliCL.questionOfVector_canonical, MIPRE.QLD.PauliCL.encode_decode_eval, MIPRE.QLD.PauliCL.pullbackStrategy_value, MIPRE.QLD.PauliCL.pullbackStrategy_pauli_A, MIPRE.QLD.PauliCL.pullbackStrategy_pauli_B
statement: formalized
proof: formalized
---

# The actual three-level Pauli question sampler

All twenty-six actual Pauli question maps have explicit three-stage CL presentations: seed, truncated direction, and the remaining point and scale coordinates. The partition covers $3m+3$ field coordinates exactly. Both full-Pauli questions evaluate to zero. A supplied binary field basis gives three-stage binary presentations on $(3m+3)t$ bits with the exact Pauli-game question distribution. Canonical encoding is inverse on attained outputs, so arbitrary strategies for the binary game pull back to the actual Pauli game with the same state, dimensions, value, and full-Pauli measurements. This is mathematical sampler content; the uniform program and its runtime are additional obligations.

## Depends on

- [Conditionally linear function](../part-01/def-cl-function.md)
- [Pauli basis test](../../background-results/part-01/def-qld-game.md)
- [Finite-game detyping soundness](../part-02/lem-detype-game-soundness.md)
- [Downsizing](../part-01/lem-cl-downsize.md)
- [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)

## Proof

Construct each register map explicitly and decode its full evaluation into the original sampled question, including canonical line representatives. Use the content-to-coordinate equivalence to identify the uniform laws. Downsize through the given binary basis and number the coordinates. Encode each attained question canonically and pull back measurements along this encoding; the pointwise sample identity proves exact value preservation.

## Lean

Formalized as [`MIPRE.QLD.PauliCL.presentation_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.presentation_exactlyOn), [`MIPRE.QLD.PauliCL.questionOfVector_presentation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.questionOfVector_presentation), [`MIPRE.QLD.PauliCL.presentation_pauli_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.presentation_pauli_eval), [`MIPRE.QLD.PauliCL.qldGame_mu_presentation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.qldGame_mu_presentation), [`MIPRE.QLD.PauliCL.binaryPresentation_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.binaryPresentation_exactlyOn), [`MIPRE.QLD.PauliCL.binaryPresentation_pauli_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.binaryPresentation_pauli_eval), [`MIPRE.QLD.PauliCL.qldGame_mu_binaryPresentation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.qldGame_mu_binaryPresentation), [`MIPRE.QLD.PauliCL.questionOfVector_canonical`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.questionOfVector_canonical), [`MIPRE.QLD.PauliCL.encode_decode_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.encode_decode_eval), [`MIPRE.QLD.PauliCL.pullbackStrategy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.pullbackStrategy_value), [`MIPRE.QLD.PauliCL.pullbackStrategy_pauli_A`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.pullbackStrategy_pauli_A), [`MIPRE.QLD.PauliCL.pullbackStrategy_pauli_B`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.pullbackStrategy_pauli_B).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3280](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3280)
