---
declaration: theorem
origin: cited
lean: Sumcheck.Spec.SingleRound.reduction_perfectCompleteness, Sumcheck.Spec.SingleRound.oracleReduction_perfectCompleteness
statement: formalized
---

# Single Round Completeness

Each individual round of the sum-check protocol is perfectly complete, from the round-$i$ relation to the round-$(i+1)$ relation.

## Depends on

- [Single Round Protocol](def-sumcheck-single-round.md)
- [virtual_sumcheck_round_protocol_complete](thm-virtual-sumcheck-round-protocol-complete.md)

## Lean

Stated as [`Sumcheck.Spec.SingleRound.reduction_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.reduction_perfectCompleteness), [`Sumcheck.Spec.SingleRound.oracleReduction_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.oracleReduction_perfectCompleteness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 175](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/sumcheck.tex#L175)
