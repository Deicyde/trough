---
declaration: definition
origin: cited
lean: Extractor.Straightline.liftContext
statement: formalized
---

# Straightline Extractor Lifting

The lifted extractor runs the inner extractor on the projected statement and output witness and lifts the result with the inverse witness lens, using a default inner witness when the inner extractor fails.

## Depends on

- [Straightline Extractor](../../definitions/part-01/def-straightline-extractor.md)
- [Extractor Lens](def-extractor-lens.md)

## Lean

Formalized as [`Extractor.Straightline.liftContext`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Extractor.Straightline.liftContext).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 463](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L463)
