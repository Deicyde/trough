---
declaration: definition
origin: cited
lean: OracleSpec.randomOracle
statement: formalized
---

# Random Oracle

A random oracle is implemented as a caching oracle that uses lazy sampling:

- On first query: generates a uniform random response and caches it
- On repeated queries: returns the cached response

## Depends on

- [Oracle Computation](def-oracle-computation.md)
- [Handling Oracle Queries](def-handling-oracle-queries.md)

## Lean

Formalized as [`OracleSpec.randomOracle`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleSpec.randomOracle).

## Sources

- [ArkLib blueprint: vcv/defs.tex, line 108](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/vcv/defs.tex#L108)
