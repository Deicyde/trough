---
declaration: definition
origin: cited
lean: OracleProver
statement: formalized
---

# Type Signature of an Oracle Prover

An oracle prover is a prover whose input statement includes the underlying data for oracle statements, and whose output includes oracle statements. Formally, it is a prover with input statement type $\mathsf{StmtIn} \times (\forall i : \iota_{\mathsf{si}}, \mathsf{OStmtIn}(i))$ and output statement type $\mathsf{StmtOut} \times (\forall i : \iota_{\mathsf{so}}, \mathsf{OStmtOut}(i))$, where:

- $\mathsf{OStmtIn} : \iota_{\mathsf{si}} \to \mathsf{Type}$ are the input oracle statement types
- $\mathsf{OStmtOut} : \iota_{\mathsf{so}} \to \mathsf{Type}$ are the output oracle statement types

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`OracleProver`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleProver).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 196](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L196)
