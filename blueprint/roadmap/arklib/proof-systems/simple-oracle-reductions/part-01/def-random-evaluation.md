---
declaration: definition
origin: cited
lean: RandomEvaluation.oracleReduction
statement: formalized
---

# RandomEvaluation Oracle Reduction

Given a map $P$ from statements and oracle statements to polynomials in $\mathbb{F}[X_1, \ldots, X_m]$:

- **Input relation**: $P(x, \mathsf{o}) = 0$ as a polynomial
- **Protocol specification**: Single challenge $\tau \in \mathbb{F}^m$ from verifier to prover
- **Output relation**: $P(x, \mathsf{o})(\tau) = 0$ for the sampled point $\tau$

## Depends on

- [RandomQuery Oracle Reduction](def-randomquery-oracle-reduction.md)

## Lean

Formalized as [`RandomEvaluation.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RandomEvaluation.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 181](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L181)
