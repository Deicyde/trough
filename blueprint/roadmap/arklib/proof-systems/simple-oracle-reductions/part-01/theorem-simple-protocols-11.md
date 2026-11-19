---
declaration: theorem
origin: cited
lean: GeneratorBatch.oracleReduction_perfectCompleteness, GeneratorBatch.oracleVerifier_rbrKnowledgeSoundness
statement: formalized
---

# Generator Batching Security

Generator batching is perfectly complete. If $S$ is finite and nonempty and $G$ is $\varepsilon$-zero-evading, the verifier is fixed-prefix round-by-round knowledge sound with error $\varepsilon$ at its single challenge.

## Depends on

- [Generator Batching](def-generator-batch.md)

## Lean

Stated as [`GeneratorBatch.oracleReduction_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/GeneratorBatch.oracleReduction_perfectCompleteness), [`GeneratorBatch.oracleVerifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/GeneratorBatch.oracleVerifier_rbrKnowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 248](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L248)
