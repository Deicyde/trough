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

- [ArkLib blueprint: vcv/defs.tex, line 60](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/vcv/defs.tex#L60)
