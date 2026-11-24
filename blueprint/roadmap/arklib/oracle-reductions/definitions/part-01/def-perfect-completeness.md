---
declaration: definition
origin: cited
lean: Reduction.perfectCompleteness
statement: formalized
---

# Perfect Completeness

A reduction satisfies **perfect completeness** if it satisfies completeness with error $0$. This means that the probability of the reduction outputting a valid statement-witness pair is *exactly* 1 (instead of at least $1 - 0$).

## Depends on

- [Completeness](def-completeness.md)

## Lean

Formalized as [`Reduction.perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.perfectCompleteness).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 463](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L463)
