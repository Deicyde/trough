---
declaration: definition
origin: cited
lean: OracleReduction.run, OracleReduction.runWithLog
statement: formalized
---

# Oracle Reduction Execution

The execution of an interactive oracle reduction runs the oracle prover on the statement together with the oracle statement data, and then the oracle verifier:

$$
\mathsf{OracleReduction}.\mathsf{run}(\mathsf{stmt}, \mathsf{oStmt}, \mathsf{wit}) := \mathsf{do} \; \{
$$

$$
\quad \langle \mathsf{transcript}, \mathsf{prvStmtOut}, \mathsf{witOut} \rangle \leftarrow \mathsf{reduction}.\mathsf{prover}.\mathsf{run}(\langle \mathsf{stmt}, \mathsf{oStmt} \rangle, \mathsf{wit})
$$

$$
\quad \mathsf{stmtOut} \leftarrow \mathsf{reduction}.\mathsf{verifier}.\mathsf{run}(\mathsf{stmt}, \mathsf{oStmt}, \mathsf{transcript})
$$

$$
\quad \mathsf{return} \; (\langle \mathsf{transcript}, \mathsf{prvStmtOut}, \mathsf{witOut} \rangle, \mathsf{stmtOut})
$$

$$
\}
$$

Here $\mathsf{prvStmtOut}$ and $\mathsf{stmtOut}$ each pair an output statement with output oracle data. The execution fails when the verifier rejects, and it returns no query logs.

The logged variant $\mathsf{OracleReduction}.\mathsf{runWithLog}$ runs the prover and the verifier under the logging oracle. On acceptance it returns the same two components, followed by the log of the prover's queries (to the shared oracle and the challenge oracle) and the log of the verifier's queries to the shared oracle. Extractors read these logs.

## Depends on

- [Interactive Oracle Reduction](def-oracle-reduction.md)
- [Complete Prover Execution](def-prover-run.md)
- [Oracle Verifier Execution](def-oracle-verifier-run.md)

## Lean

Formalized as [`OracleReduction.run`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleReduction.run), [`OracleReduction.runWithLog`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleReduction.runWithLog).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 413](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L413)
