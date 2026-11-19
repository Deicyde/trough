---
declaration: theorem
origin: cited
lean: Sumcheck.Spec.reduction_perfectCompleteness, Sumcheck.Spec.oracleReduction_perfectCompleteness
statement: formalized
---

# Perfect Completeness

The sum-check protocol satisfies perfect completeness. That is, for any valid input statement and oracle statement satisfying the input relation, the protocol accepts with probability 1.

## Depends on

- [Single Round Completeness](thm-sumcheck-single-round-completeness.md)

## Lean

Stated as [`Sumcheck.Spec.reduction_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.reduction_perfectCompleteness), [`Sumcheck.Spec.oracleReduction_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.oracleReduction_perfectCompleteness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 58](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/sumcheck.tex#L58)
