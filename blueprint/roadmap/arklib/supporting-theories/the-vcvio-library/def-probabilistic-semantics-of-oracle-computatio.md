---
declaration: definition
origin: cited
lean: evalDist
statement: formalized
---

# Probabilistic Semantics of Oracle Computations

A computation denotes a subprobability measure on its outputs, `evalDist mx`. The missing mass represents failure or nontermination; the output distribution does not add an `Option` outcome. For oracle computations, the semantics is fixed by choosing a probability measure on the answers to each query. The usual choice is the uniform measure, as for `ProbComp`. Probabilities of outputs and events are defined from this measure.

## Depends on

- [Oracle Computation](def-oracle-computation.md)

## Lean

Formalized as [`evalDist`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/evalDist).

## Sources

- [ArkLib blueprint: vcv/defs.tex, line 71](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/vcv/defs.tex#L71)
