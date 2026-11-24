---
declaration: theorem
origin: cited
lean: CheckClaim.oracleReduction_completeness, CheckClaim.oracleVerifier_coordinateWiseSpecialSoundWith
statement: formalized
---

# CheckClaim Oracle Security

If every input in $R_{\mathsf{in}}$ satisfies $P$, the CheckClaim oracle reduction is perfectly complete. Its oracle verifier is coordinate-wise special sound for every coordinate-wise structure, with the trivial extractor.

## Depends on

- [CheckClaim Oracle Reduction](def-checkclaim-oracle-reduction.md)

## Lean

Stated as [`CheckClaim.oracleReduction_completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CheckClaim.oracleReduction_completeness), [`CheckClaim.oracleVerifier_coordinateWiseSpecialSoundWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CheckClaim.oracleVerifier_coordinateWiseSpecialSoundWith); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 399](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/simple_protocols.tex#L399)
