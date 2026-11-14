---
declaration: theorem
origin: cited
lean: SendSingleWitness.oracleReduction_completeness, SendSingleWitness.oracleVerifier_coordinateWiseSpecialSoundWith
statement: formalized
---

# SendSingleWitness Security

The SendSingleWitness oracle reduction satisfies perfect completeness. Its oracle verifier is pure and has no challenges, so it is coordinate-wise special sound for every coordinate-wise structure, with the extractor that reads the witness off the unique transcript.

## Depends on

- [SendSingleWitness Oracle Reduction](def-sendsinglewitness-oracle-reduction.md)

## Lean

Stated as [`SendSingleWitness.oracleReduction_completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendSingleWitness.oracleReduction_completeness), [`SendSingleWitness.oracleVerifier_coordinateWiseSpecialSoundWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendSingleWitness.oracleVerifier_coordinateWiseSpecialSoundWith); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 93](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L93)
