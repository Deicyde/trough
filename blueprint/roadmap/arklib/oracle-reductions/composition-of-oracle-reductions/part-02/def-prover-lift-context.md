---
declaration: definition
origin: cited
lean: Prover.liftContext
statement: formalized
---

# Prover Context Lifting

Given a prover $P$ for the inner context and a context lens, the lifted prover works by:

- Projecting the outer input to the inner context
- Running the inner prover
- Lifting the output back to the outer context

## Depends on

- [Type Signature of a Prover](../../definitions/part-01/def-prover.md)
- [Context Lens](def-context-lens.md)

## Lean

Formalized as [`Prover.liftContext`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Prover.liftContext).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 326](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L326)
