---
declaration: definition
origin: cited
lean: Verifier.run
statement: formalized
---

# Verifier Execution

The execution of a verifier is simply the application of its verification function:

$$
\mathsf{Verifier}.\mathsf{run}(\mathsf{stmt}, \mathsf{transcript}) := \mathsf{verifier}.\mathsf{verify}(\mathsf{stmt}, \mathsf{transcript})
$$

This takes the input statement and full transcript, and returns the output statement, or rejects, via an optional oracle computation.

## Depends on

- [Type Signature of a Verifier](def-verifier.md)

## Lean

Formalized as [`Verifier.run`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.run).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 367](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L367)
