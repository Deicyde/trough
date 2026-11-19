---
declaration: definition
origin: cited
lean: Extractor.Straightline
statement: formalized
---

# Straightline Extractor

A **straightline extractor** takes in:

- the initial statement $x_{\text{in}}$,
- the output witness $w_{\text{out}}$,
- the IOR transcript $\tau$,
- the query logs from the prover and verifier

and returns a corresponding initial witness $w_{\text{in}}$. It runs once, after the execution, without rewinding the prover. It may query the shared oracle and may fail.

Note that the extractor does not need to take in the output statement, since it can be derived via re-running the verifier on the initial statement, the transcript, and the verifier's query log.

The type bounds neither the running time nor the computability of the extractor. This form of extractor suffices for proving knowledge soundness of most hash-based IOPs.

## Depends on

- [Protocol Transcript](def-transcript.md)

## Lean

Formalized as [`Extractor.Straightline`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Extractor.Straightline).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 480](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L480)
