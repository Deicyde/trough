---
declaration: theorem
origin: cited
lean: SendClaim.oracleVerifier_coordinateWiseSpecialSoundWith
statement: formalized
---

# SendClaim Coordinate-wise Special Soundness

The SendClaim oracle verifier is coordinate-wise special sound for every coordinate-wise structure, with the trivial extractor: acceptance into the output relation forces the input into $R_{\mathsf{in}}$.

## Depends on

- [SendClaim Oracle Reduction](def-sendclaim-oracle-reduction.md)

## Lean

Stated as [`SendClaim.oracleVerifier_coordinateWiseSpecialSoundWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendClaim.oracleVerifier_coordinateWiseSpecialSoundWith); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 275](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/simple_protocols.tex#L275)
