---
declaration: definition
origin: cited
lean: Prover.runToRoundFS
statement: formalized
---

# Fiat-Shamir Prover Execution

$\mathsf{runToRoundFS}\ i\ \mathsf{stmt}\ \mathsf{prover}\ \mathsf{state}$ starts from the empty message prefix, the statement and the prover state at round $0$, and applies $\mathsf{processRoundFS}$ to rounds $0, \ldots, i - 1$. It returns the messages up to round $i$, the statement and the prover state at round $i$.

## Depends on

- [Fiat-Shamir Round Processing](def-prover-process-round-fs.md)

## Lean

Formalized as [`Prover.runToRoundFS`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Prover.runToRoundFS).

## Sources

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 70](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/fiat_shamir.tex#L70)
