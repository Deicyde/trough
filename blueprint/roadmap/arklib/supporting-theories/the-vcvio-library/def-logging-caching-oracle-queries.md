---
declaration: definition
origin: cited
lean: OracleSpec.loggingOracle, OracleSpec.cachingOracle
statement: formalized
---

# Logging & Caching Oracle Queries

Using the simulation framework, we can add logging and caching behaviors to oracle queries:

- Logging records all queries made during a computation
- Caching remembers query responses and reuses them for repeated queries

Logging forwards every query and records it. Caching forwards only cache misses and answers repeated queries from the cache.

## Depends on

- [Oracle Computation](def-oracle-computation.md)
- [Simulating Oracle Queries with Other Oracles](def-sim-oracle.md)

## Lean

Formalized as [`OracleSpec.loggingOracle`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleSpec.loggingOracle), [`OracleSpec.cachingOracle`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleSpec.cachingOracle).

## Sources

- [ArkLib blueprint: vcv/defs.tex, line 94](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/vcv/defs.tex#L94)
