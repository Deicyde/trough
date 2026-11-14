---
declaration: theorem
origin: cited
lean: ReduceClaim.reduction_completeness_of_imp, ReduceClaim.reduction_completeness
statement: formalized
---

# ReduceClaim Perfect Completeness

If $R_{\mathsf{in}}(\mathsf{stmt}, \mathsf{wit})$ implies $R_{\mathsf{out}}(\mathsf{mapStmt}(\mathsf{stmt}), \mathsf{mapWit}(\mathsf{stmt}, \mathsf{wit}))$, the ReduceClaim reduction is perfectly complete. The version stated with an equivalence is a corollary.

## Depends on

- [ReduceClaim Reduction](def-reduceclaim-reduction.md)

## Lean

Stated as [`ReduceClaim.reduction_completeness_of_imp`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReduceClaim.reduction_completeness_of_imp), [`ReduceClaim.reduction_completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReduceClaim.reduction_completeness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 325](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L325)
