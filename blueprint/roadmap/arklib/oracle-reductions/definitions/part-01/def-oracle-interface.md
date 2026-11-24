---
declaration: definition
origin: cited
lean: OracleInterface
statement: formalized
---

# Oracle Interface

An oracle interface for an underlying data type $\mathsf{D}$ consists of the following:

- A type $\mathsf{Q}$ for queries to the oracle,
- A response family $\mathsf{R} : \mathsf{Q} \to \mathsf{Type}$, so that the type of the response may depend on the query,
- An answering function $\mathsf{answer} : \mathsf{D} \to (q : \mathsf{Q}) \to \mathsf{R}(q)$ that specifies the oracle's behavior given the underlying data and a query.

In Lean the response family and answering function are packaged as an oracle context whose implementation reads the underlying data. A constant response family $\mathsf{R}(q) = \mathsf{R}$ is the common special case.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`OracleInterface`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleInterface).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 72](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L72)
