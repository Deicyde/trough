---
declaration: theorem
origin: cited
lean: CheckClaim.reduction_completeness, CheckClaim.verifier_rbrKnowledgeSoundness
statement: formalized
---

# CheckClaim Security

The CheckClaim reduction satisfies perfect completeness, and its verifier is round-by-round knowledge sound with error $0$.

## Depends on

- [CheckClaim Reduction](def-checkclaim-reduction.md)

## Lean

Stated as [`CheckClaim.reduction_completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CheckClaim.reduction_completeness), [`CheckClaim.verifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CheckClaim.verifier_rbrKnowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 379](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/simple_protocols.tex#L379)
