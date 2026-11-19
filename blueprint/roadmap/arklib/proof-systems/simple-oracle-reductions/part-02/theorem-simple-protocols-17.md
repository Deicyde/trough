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

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 379](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L379)
