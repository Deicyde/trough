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

- [ArkLib blueprint: vcv/defs.tex, line 83](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/vcv/defs.tex#L83)
