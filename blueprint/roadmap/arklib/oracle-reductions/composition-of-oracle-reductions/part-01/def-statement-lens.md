---
declaration: definition
origin: cited
lean: Statement.Lens
statement: formalized
---

# Statement Lens

A statement lens between outer context types $(\mathsf{StmtIn}_{\mathsf{outer}}, \mathsf{StmtOut}_{\mathsf{outer}})$ and inner context types $(\mathsf{StmtIn}_{\mathsf{inner}}, \mathsf{StmtOut}_{\mathsf{inner}})$ consists of:

- $\mathsf{projStmt} : \mathsf{StmtIn}_{\mathsf{outer}} \to \mathsf{StmtIn}_{\mathsf{inner}}$ (projection to inner context)
- $\mathsf{liftStmt} : \mathsf{StmtIn}_{\mathsf{outer}} \to \mathsf{StmtOut}_{\mathsf{inner}} \to \mathsf{StmtOut}_{\mathsf{outer}}$ (lifting back to outer context)

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Statement.Lens`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Statement.Lens).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 264](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L264)
