---
declaration: theorem
origin: cited
lean: ReduceClaim.oracleReduction_completeness, ReduceClaim.oracleVerifier_rbrKnowledgeSoundness
statement: formalized
---

# ReduceClaim Oracle Security

The ReduceClaim oracle reduction is perfectly complete when the mapped honest inputs land in $R_{\mathsf{out}}$, with the oracle statements reindexed along $\mathsf{embedIdx}$. Given a backward witness map as in the non-oracle case, now taking the statement and oracle statements as input, its oracle verifier is round-by-round knowledge sound with error $0$.

## Depends on

- [ReduceClaim Oracle Reduction](def-reduceclaim-oracle-reduction.md)

## Lean

Stated as [`ReduceClaim.oracleReduction_completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReduceClaim.oracleReduction_completeness), [`ReduceClaim.oracleVerifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReduceClaim.oracleVerifier_rbrKnowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 352](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L352)
