---
declaration: definition
origin: cited
lean: Reduction.Simulator
statement: formalized
---

# Simulator

A **simulator** consists of:

- Oracle simulation capabilities for the shared oracles
- A prover simulation function that takes an input statement and produces a transcript

The simulator should have programming access to the shared oracles and be able to generate transcripts that are indistinguishable from real protocol executions.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Reduction.Simulator`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.Simulator).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 838](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L838)
