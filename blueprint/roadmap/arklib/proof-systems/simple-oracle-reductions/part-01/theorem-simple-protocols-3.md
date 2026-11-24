---
declaration: theorem
origin: cited
lean: SendWitness.reduction_completeness, SendWitness.verifier_coordinateWiseSpecialSoundWith
statement: formalized
---

# SendWitness Security

The SendWitness reduction satisfies perfect completeness. Its verifier is pure and has no challenges, so it is coordinate-wise special sound for every coordinate-wise structure, with the extractor that reads the witness off the unique transcript.

## Depends on

- [SendWitness Reduction](def-sendwitness-reduction.md)

## Lean

Stated as [`SendWitness.reduction_completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendWitness.reduction_completeness), [`SendWitness.verifier_coordinateWiseSpecialSoundWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendWitness.verifier_coordinateWiseSpecialSoundWith); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 58](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/simple_protocols.tex#L58)
