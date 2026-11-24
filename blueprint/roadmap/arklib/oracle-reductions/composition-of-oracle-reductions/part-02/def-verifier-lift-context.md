---
declaration: definition
origin: cited
lean: Verifier.liftContext
statement: formalized
---

# Verifier Context Lifting

The lifted verifier runs the inner verifier on the projected input statement and lifts its output statement with the statement lens.

## Depends on

- [Type Signature of a Verifier](../../definitions/part-01/def-verifier.md)
- [Statement Lens](../part-01/def-statement-lens.md)

## Lean

Formalized as [`Verifier.liftContext`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.liftContext).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 339](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L339)
