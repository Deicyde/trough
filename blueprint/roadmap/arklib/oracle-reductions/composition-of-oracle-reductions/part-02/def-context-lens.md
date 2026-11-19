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

- [ArkLib blueprint: oracle_reductions/composition.tex, line 287](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L287)
