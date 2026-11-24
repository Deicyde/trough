---
declaration: definition
origin: cited
lean: NoInteraction.reduction
statement: formalized
---

# No-interaction Reduction

A zero-round reduction is determined by a pure statement map $\mathsf{mapStmt} : \mathsf{StmtIn} \to \mathsf{StmtOut}$ and a witness map $\mathsf{mapWit} : \mathsf{StmtIn} \to \mathsf{WitIn} \to \mathsf{OracleComp}\ \mathcal{O}\ \mathsf{WitOut}$ that may query the shared oracles. The verifier outputs $\mathsf{mapStmt}(\mathsf{stmt})$; the prover outputs it together with the result of $\mathsf{mapWit}$.

## Depends on

- [Interactive Reduction](../../../oracle-reductions/definitions/part-01/def-reduction.md)

## Lean

Formalized as [`NoInteraction.reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/NoInteraction.reduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 409](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/simple_protocols.tex#L409)
