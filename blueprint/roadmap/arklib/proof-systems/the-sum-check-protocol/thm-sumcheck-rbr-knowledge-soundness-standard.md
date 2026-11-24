---
declaration: theorem
origin: cited
lean: Sumcheck.Spec.oracleVerifier_rbrKnowledgeSoundness
statement: formalized
---

# Round-by-Round Knowledge Soundness

Suppose $R$ is finite and an integral domain. Then the sum-check verifier is fixed-prefix round-by-round knowledge sound with error $d / |R|$ at every challenge. The state function is the sequential composition of the single-round state functions of Section [Modular Description](README.md).

## Depends on

- [Single Round Knowledge Soundness](thm-sumcheck-single-round-soundness.md)

## Lean

Stated as [`Sumcheck.Spec.oracleVerifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.oracleVerifier_rbrKnowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 67](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/sumcheck.tex#L67)
