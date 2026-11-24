---
declaration: definition
origin: cited
lean: simulateQ
statement: formalized
---

# Simulating Oracle Queries with Other Oracles

Given a query implementation of `spec` in a monad $m$, `simulateQ` runs an oracle computation by substituting the implementation for each query. Taking $m$ to be a computation with access to other oracles, possibly with state (for example a state monad over `OracleComp spec'`), simulates one specification by another.

## Depends on

- [Oracle Computation](def-oracle-computation.md)
- [Handling Oracle Queries](def-handling-oracle-queries.md)

## Lean

Formalized as [`simulateQ`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/simulateQ).

## Sources

- [ArkLib blueprint: vcv/defs.tex, line 83](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/vcv/defs.tex#L83)
