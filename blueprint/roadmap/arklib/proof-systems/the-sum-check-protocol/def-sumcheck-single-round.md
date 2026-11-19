---
declaration: definition
origin: cited
lean: Sumcheck.Spec.SingleRound.reduction, Sumcheck.Spec.SingleRound.oracleReduction
statement: formalized
---

# Single Round Protocol

The $i$-th round of sum-check consists of:

1. **Input:** A statement containing target value and prior challenges, along with an oracle for the multivariate polynomial
2. **Prover's message:** A univariate polynomial $p_i \in R[X]_{\leq d}$
3. **Verifier's challenge:** A random element $r_i \gets R$
4. **Output:** An updated statement with new target $p_i(r_i)$ and extended challenges

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Sumcheck.Spec.SingleRound.reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.reduction), [`Sumcheck.Spec.SingleRound.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 162](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/sumcheck.tex#L162)
