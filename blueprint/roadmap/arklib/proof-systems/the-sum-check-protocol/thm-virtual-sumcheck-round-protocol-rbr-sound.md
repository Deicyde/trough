---
declaration: theorem
origin: cited
lean: Sumcheck.Spec.SingleRound.Simple.verifier_rbrKnowledgeSoundness, Sumcheck.Spec.SingleRound.Simple.oracleVerifier_rbrKnowledgeSoundness
statement: formalized
---

# virtual_sumcheck_round_protocol_rbr_sound

Suppose $R$ is finite and an integral domain. The virtual sum-check round protocol is fixed-prefix round-by-round knowledge sound with error $d / |R|$.

## Depends on

- [Round-by-Round Knowledge Soundness](../../oracle-reductions/definitions/part-02/def-round-by-round-knowledge-soundness.md)
- [virtual_sumcheck_round_protocol](def-virtual-sumcheck-round-protocol.md)

## Lean

Stated as [`Sumcheck.Spec.SingleRound.Simple.verifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.Simple.verifier_rbrKnowledgeSoundness), [`Sumcheck.Spec.SingleRound.Simple.oracleVerifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.Simple.oracleVerifier_rbrKnowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 256](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/sumcheck.tex#L256)
