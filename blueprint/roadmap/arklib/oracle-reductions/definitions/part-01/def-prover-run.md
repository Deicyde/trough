---
declaration: definition
origin: cited
lean: Prover.run
statement: formalized
---

# Complete Prover Execution

The complete execution of a prover is defined as:

$$
\mathsf{Prover}.\mathsf{run}(\mathsf{stmt}, \mathsf{wit}) := \mathsf{do} \; \{
$$

$$
\quad \langle \mathsf{transcript}, \mathsf{state} \rangle \leftarrow \mathsf{prover}.\mathsf{runToRound}(\mathsf{Fin}.\mathsf{last}(n), \mathsf{stmt}, \mathsf{wit})
$$

$$
\quad \langle \mathsf{stmtOut}, \mathsf{witOut} \rangle \leftarrow \mathsf{prover}.\mathsf{output}(\mathsf{state})
$$

$$
\quad \mathsf{return} \; \langle \mathsf{transcript}, \mathsf{stmtOut}, \mathsf{witOut} \rangle
$$

$$
\}
$$

Returns the complete transcript, the output statement and the output witness, as an oracle computation that may also query the challenge oracle.

## Depends on

- [Type Signature of a Prover](def-prover.md)
- [Prover Execution to Round](def-prover-run-to-round.md)

## Lean

Formalized as [`Prover.run`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Prover.run).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 350](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L350)
