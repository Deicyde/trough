---
declaration: definition
origin: cited
lean: Prover.append
statement: formalized
---

# Prover Append

Given provers $P_1 : \mathsf{Prover}\ \mathsf{pSpec}_1\ \mathsf{oSpec}\ \mathsf{StmtIn}_1\ \mathsf{WitIn}_1\ \mathsf{StmtOut}_1\ \mathsf{WitOut}_1$ and $P_2 : \mathsf{Prover}\ \mathsf{pSpec}_2\ \mathsf{oSpec}\ \mathsf{StmtOut}_1\ \mathsf{WitOut}_1\ \mathsf{StmtOut}_2\ \mathsf{WitOut}_2$, their sequential composition is:

$$
P_1.\mathsf{append}\ P_2 : \mathsf{Prover}\ (\mathsf{pSpec}_1 \mathrel{++_\mathsf{p}} \mathsf{pSpec}_2)\ \mathsf{oSpec}\ \mathsf{StmtIn}_1\ \mathsf{WitIn}_1\ \mathsf{StmtOut}_2\ \mathsf{WitOut}_2
$$

The composed prover works by:

- Running $P_1$ on the input context to produce an intermediate context
- Using this intermediate context as input to $P_2$
- Outputting the final context from $P_2$

Equality with two separate prover runs requires an execution condition such as the one in Theorem [Completeness Preservation under Append](thm-completeness-append.md); output queries can otherwise cross an opening challenge.

## Depends on

- [Type Signature of a Prover](../../definitions/part-01/def-prover.md)
- [Protocol Specification Append](def-protocol-spec-append.md)

## Lean

Formalized as [`Prover.append`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Prover.append).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 34](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L34)
