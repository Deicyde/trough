---
declaration: definition
origin: cited
lean: QueryImpl
statement: formalized
---

# Handling Oracle Queries

To run oracle computations, we need a way to handle (or implement) the oracle queries. A query implementation `QueryImpl spec m` maps every query $t$ to a computation in a monad $m$ returning an answer in `spec.Range t`. Depending on the monad, this allows various interpretations of the queries.

## Depends on

- [Specification of Oracles](def-oracle-spec.md)

## Lean

Formalized as [`QueryImpl`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/QueryImpl).

## Sources

- [ArkLib blueprint: vcv/defs.tex, line 60](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/vcv/defs.tex#L60)
