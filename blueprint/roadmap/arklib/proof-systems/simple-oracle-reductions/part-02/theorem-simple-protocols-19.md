---
declaration: theorem
origin: cited
lean: NoInteraction.reduction_completeness
statement: formalized
---

# No-interaction Completeness

If, for every input $(\mathsf{stmt}, \mathsf{wit}) \in R_{\mathsf{in}}$, running $\mathsf{mapWit}(\mathsf{stmt}, \mathsf{wit})$ yields $w'$ with $(\mathsf{mapStmt}(\mathsf{stmt}), w') \in R_{\mathsf{out}}$ with probability at least $1 - \varepsilon$, then the reduction is complete with error $\varepsilon$.

## Depends on

- [No-interaction Reduction](def-no-interaction-reduction.md)

## Lean

Stated as [`NoInteraction.reduction_completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/NoInteraction.reduction_completeness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 417](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L417)
