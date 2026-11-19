---
declaration: definition
origin: cited
lean: Reduction.run
statement: formalized
---

# Interactive Reduction Execution

The execution of an interactive reduction consists of running the prover followed by the verifier:

$$
\mathsf{Reduction}.\mathsf{run}(\mathsf{stmt}, \mathsf{wit}) := \mathsf{do} \; \{
$$

$$
\quad \langle \mathsf{transcript}, \mathsf{prvStmtOut}, \mathsf{witOut} \rangle \leftarrow \mathsf{reduction}.\mathsf{prover}.\mathsf{run}(\mathsf{stmt}, \mathsf{wit})
$$

$$
\quad \mathsf{stmtOut} \leftarrow \mathsf{reduction}.\mathsf{verifier}.\mathsf{run}(\mathsf{stmt}, \mathsf{transcript})
$$

$$
\quad \mathsf{return} \; (\langle \mathsf{transcript}, \mathsf{prvStmtOut}, \mathsf{witOut} \rangle, \mathsf{stmtOut})
$$

$$
\}
$$

Returns the prover's result (the complete transcript, output statement and output witness) and the verifier's output statement. The execution is an optional oracle computation: it fails when the verifier rejects.

## Depends on

- [Interactive Reduction](def-reduction.md)
- [Complete Prover Execution](def-prover-run.md)
- [Verifier Execution](def-verifier-run.md)

## Lean

Formalized as [`Reduction.run`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.run).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 395](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L395)
