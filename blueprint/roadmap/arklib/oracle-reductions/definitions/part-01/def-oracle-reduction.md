---
declaration: definition
origin: cited
lean: OracleReduction
statement: formalized
---

# Interactive Oracle Reduction

An interactive oracle reduction for protocol specification $\mathsf{pSpec} : \mathsf{ProtocolSpec}(n)$ with oracle interfaces for all prover messages, and oracle specification $\mathsf{oSpec}$, consists of:

- An **oracle prover** $\mathcal{P} : \mathsf{OracleProver}(\mathsf{pSpec}, \mathsf{oSpec}, \mathsf{StmtIn}, \mathsf{WitIn}, \mathsf{StmtOut}, \mathsf{WitOut}, \mathsf{OStmtIn}, \mathsf{OStmtOut})$
- An **oracle verifier** $\mathcal{V} : \mathsf{OracleVerifier}(\mathsf{pSpec}, \mathsf{oSpec}, \mathsf{StmtIn}, \mathsf{StmtOut}, \mathsf{OStmtIn}, \mathsf{OStmtOut})$

where:

- $\mathsf{OStmtIn} : \iota_{\mathsf{si}} \to \mathsf{Type}$ are the input oracle statement types with oracle interfaces
- $\mathsf{OStmtOut} : \iota_{\mathsf{so}} \to \mathsf{Type}$ are the output oracle statement types

The oracle reduction allows the verifier to access prover messages and oracle statements only through specified oracle interfaces, enabling more flexible and composable protocol designs.

## Depends on

- [Type Signature of an Oracle Prover](def-oracle-prover.md)
- [Type Signature of an Oracle Verifier](def-oracle-verifier.md)

## Lean

Formalized as [`OracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleReduction).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 298](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L298)
