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

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 275](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L275)
