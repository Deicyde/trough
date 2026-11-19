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

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 256](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/sumcheck.tex#L256)
