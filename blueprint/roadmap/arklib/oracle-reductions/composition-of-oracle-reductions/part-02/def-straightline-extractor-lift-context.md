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

- [ArkLib blueprint: oracle_reductions/composition.tex, line 463](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L463)
