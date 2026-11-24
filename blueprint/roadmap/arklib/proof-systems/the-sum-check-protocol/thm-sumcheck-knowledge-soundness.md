---
declaration: theorem
origin: cited
lean: Sumcheck.Spec.oracleVerifier_knowledgeSoundness
statement: formalized
---

# Knowledge Soundness

Suppose $R$ is finite and an integral domain. Then the sum-check protocol satisfies knowledge soundness with error $n \cdot d / |R|$, the sum of the per-challenge errors over its $n$ challenges, where $d$ is the degree bound.

## Depends on

- [Round-by-Round Knowledge Soundness](thm-sumcheck-rbr-knowledge-soundness-standard.md)

## Lean

Stated as [`Sumcheck.Spec.oracleVerifier_knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.oracleVerifier_knowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 75](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/sumcheck.tex#L75)
