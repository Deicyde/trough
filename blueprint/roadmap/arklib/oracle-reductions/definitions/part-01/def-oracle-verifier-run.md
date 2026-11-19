---
declaration: definition
origin: cited
lean: OracleVerifier.run
statement: formalized
---

# Oracle Verifier Execution

The execution of an oracle verifier is the execution of its converted verifier:

$$
\mathsf{OracleVerifier}.\mathsf{run}(\mathsf{stmt}, \mathsf{oStmtIn}, \mathsf{transcript}) := \mathsf{verifier}.\mathsf{toVerifier}.\mathsf{run}(\langle \mathsf{stmt}, \mathsf{oStmtIn} \rangle, \mathsf{transcript})
$$

It answers queries to the input oracle statements and prover messages from the actual data, runs the verification logic, and on acceptance returns the pair of the output statement and the materialized output oracle data. Its type is $\mathsf{OptionT}(\mathsf{OracleComp}(\mathsf{oSpec}), \mathsf{StmtOut} \times (\forall i, \mathsf{OStmtOut}(i)))$.

## Depends on

- [Type Signature of an Oracle Verifier](def-oracle-verifier.md)
- [Oracle Interface](def-oracle-interface.md)

## Lean

Formalized as [`OracleVerifier.run`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleVerifier.run).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 380](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L380)
