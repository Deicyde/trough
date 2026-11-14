---
declaration: theorem
origin: cited
lean: Sumcheck.Spec.SingleRound.verifier_rbrKnowledgeSoundness, Sumcheck.Spec.SingleRound.oracleVerifier_rbrKnowledgeSoundness
statement: formalized
---

# Single Round Knowledge Soundness

Suppose $R$ is finite and an integral domain. Each individual round of the sum-check protocol is fixed-prefix round-by-round knowledge sound with error $d / |R|$ at its challenge, where $d$ is the degree bound. The round is obtained by lifting the virtual round below along a context lens, which transfers both properties.

## Depends on

- [Single Round Protocol](def-sumcheck-single-round.md)
- [virtual_sumcheck_round_protocol_rbr_sound](thm-virtual-sumcheck-round-protocol-rbr-sound.md)

## Lean

Stated as [`Sumcheck.Spec.SingleRound.verifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.verifier_rbrKnowledgeSoundness), [`Sumcheck.Spec.SingleRound.oracleVerifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.oracleVerifier_rbrKnowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 184](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/sumcheck.tex#L184)
