---
declaration: definition
origin: cited
lean: Context.Lens
statement: formalized
---

# Context Lens

A context lens pairs a statement lens with a witness lens. It adapts a whole reduction: the verifier uses the statement lens and the prover uses both.

## Depends on

- [Statement Lens](../part-01/def-statement-lens.md)
- [Witness Lens](def-witness-lens.md)

## Lean

Formalized as [`Context.Lens`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Context.Lens).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 287](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L287)
