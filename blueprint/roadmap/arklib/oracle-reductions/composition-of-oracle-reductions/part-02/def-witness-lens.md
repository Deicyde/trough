---
declaration: definition
origin: cited
lean: Witness.Lens
statement: formalized
---

# Witness Lens

A witness lens, used by the prover, consists of:

- $\mathsf{projWit} : \mathsf{StmtIn}_{\mathsf{outer}} \times \mathsf{WitIn}_{\mathsf{outer}} \to \mathsf{WitIn}_{\mathsf{inner}}$ (projection to inner context)
- $\mathsf{liftWit} : \mathsf{StmtIn}_{\mathsf{outer}} \times \mathsf{WitIn}_{\mathsf{outer}} \to \mathsf{StmtOut}_{\mathsf{inner}} \times \mathsf{WitOut}_{\mathsf{inner}} \to \mathsf{WitOut}_{\mathsf{outer}}$ (lifting back to outer context)

The statements are part of both maps because the prover sees its full context.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Witness.Lens`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Witness.Lens).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 275](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L275)
