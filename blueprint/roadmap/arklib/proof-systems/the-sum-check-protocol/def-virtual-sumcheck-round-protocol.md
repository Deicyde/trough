---
declaration: definition
origin: cited
lean: Sumcheck.Spec.SingleRound.Simple.reduction, Sumcheck.Spec.SingleRound.Simple.oracleReduction
statement: formalized
---

# virtual_sumcheck_round_protocol

1. In this protocol, the context is a pair $(p, c)$, where $p$ is now a *univariate* polynomial of degree at most $d$, given as an oracle, and $c \in R$ is public. The predicate / relation is that $\sum_{x \in \text{Image}(\mathcal{D})} p(x) = c$.
2. The prover first sends a univariate polynomial $s$ of degree at most $d$. In the honest case, it would just send $p$ itself.
3. The verifier samples and sends a random challenge $r \gets R$.
4. The verifier checks that $\sum_{x \in \text{Image}(\mathcal{D})} s(x) = c$ and outputs $(s(r), r)$. The predicate on the resulting output context is that $p(r) = s(r)$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Sumcheck.Spec.SingleRound.Simple.reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.Simple.reduction), [`Sumcheck.Spec.SingleRound.Simple.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Spec.SingleRound.Simple.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 199](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/sumcheck.tex#L199)
