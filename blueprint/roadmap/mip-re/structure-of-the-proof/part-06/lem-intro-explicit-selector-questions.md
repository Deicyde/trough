---
declaration: lemma
origin: cited
lean: MIPRE.QLD.PauliCL.ExplicitSeed.binaryOutputPermutation_presentation, MIPRE.QLD.PauliCL.ExplicitSeed.binaryQuestion_outputPermutation
statement: formalized
proof: formalized
---

# Output relabelling for the explicit selector

For a compatible seed permutation, explicit-selector and legacy Pauli outputs are related by an actual binary question equivalence. The decoded legacy questions agree under this equivalence.

## Depends on

- [Pauli basis test](../../background-results/part-01/def-qld-game.md)
- [Downsizing](../part-01/lem-cl-downsize.md)

## Proof

Conjugate the seed permutation through the binary basis and change only the line question seeds. Prove that this output map intertwines the two presentations with the common seed permutation, and that decoding agrees. The full strategy transport, including mixed edges and PCC completeness, is supplied by Lemma [Full question transport and actual QLD extraction](lem-intro-numbered-transport.md).

## Lean

Formalized as [`MIPRE.QLD.PauliCL.ExplicitSeed.binaryOutputPermutation_presentation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.ExplicitSeed.binaryOutputPermutation_presentation), [`MIPRE.QLD.PauliCL.ExplicitSeed.binaryQuestion_outputPermutation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.ExplicitSeed.binaryQuestion_outputPermutation).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3741](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3741)
