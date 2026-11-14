---
declaration: definition
origin: cited
lean: Spartan.oracleReduction, Spartan.Assembly.stage, Spartan.PublicParams.forSize
statement: formalized
---

# Spartan PIOP

The Spartan oracle reduction is the composition of:

1. **Witness attachment** [$0$\]: the prover sends the padded witness table as an oracle message, an instance of the adapter of Definition [Single-message adapter](../simple-oracle-reductions/part-01/def-sendsinglewitness-adapter.md).
2. **Zero-check** [$s/q$\]: the verifier samples $\tau \in \mathbb{F}^{s}$, reducing the claim that every constraint holds (the multilinear extension of the residual $(Az) \circ (Bz) - Cz$ is zero) to the claim that this extension vanishes at $\tau$, equivalently $\sum_{x \in \{0,1\}^s} \tilde{\text{eq}}(\tau, x)\,((Az)_x (Bz)_x - (Cz)_x) = 0$.
3. **First sum-check** [$3/q$\]: sum-check of degree $3$ in $s$ rounds, ending at a point $r_x$.
4. **Send evaluations** [$0$\]: the prover sends $v_A, v_B, v_C$, and the verifier checks the first sum-check's final claim against them.
5. **Batching** [$1/q$\]: the verifier samples one challenge consisting of three independent coefficients $(r_A, r_B, r_C)$, forming the claim $T_2 = r_A v_A + r_B v_B + r_C v_C$.
6. **Second sum-check** [$2/q$\]: sum-check of degree $2$ in $t$ rounds, ending at a point $r_y$.
7. **Terminal check** [$0$\]: the verifier evaluates the second virtual polynomial at $r_y$ through the matrix and witness oracles and compares it with the final claim.

## Depends on

- [Interactive Oracle Reduction](../../oracle-reductions/definitions/part-01/def-oracle-reduction.md)
- [Single-message adapter](../simple-oracle-reductions/part-01/def-sendsinglewitness-adapter.md)
- [Single Round Protocol](../the-sum-check-protocol/def-sumcheck-single-round.md)

## Lean

Formalized as [`Spartan.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.oracleReduction), [`Spartan.Assembly.stage`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.Assembly.stage), [`Spartan.PublicParams.forSize`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.PublicParams.forSize).

## Sources

- [ArkLib blueprint: proof_systems/spartan.tex, line 64](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/spartan.tex#L64)
