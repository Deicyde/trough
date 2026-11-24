---
declaration: definition
origin: cited
lean: OracleContext.Lens, OracleContext.ExecutableLens, OracleStatement.ExecutableLens
statement: formalized
---

# Oracle Context Lens

For oracle reductions, the statement lens acts on pairs of a statement and its oracle statements, and the witness lens sees these pairs. This form suffices for relations. To run an oracle verifier, an *executable* oracle context lens also implements the inner input oracles by queries to the outer ones, and the outer output oracles by queries to the outer input and inner output oracles, each agreeing with a materialized map.

## Depends on

- [Context Lens](def-context-lens.md)
- [Oracle Interface](../../definitions/part-01/def-oracle-interface.md)

## Lean

Formalized as [`OracleContext.Lens`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleContext.Lens), [`OracleContext.ExecutableLens`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleContext.ExecutableLens), [`OracleStatement.ExecutableLens`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleStatement.ExecutableLens).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 296](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L296)
