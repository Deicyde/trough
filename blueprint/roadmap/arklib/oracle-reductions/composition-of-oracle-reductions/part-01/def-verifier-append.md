---
declaration: definition
origin: cited
lean: Verifier.append
statement: formalized
---

# Verifier Append

Given verifiers $V_1 : \mathsf{Verifier}\ \mathsf{pSpec}_1\ \mathsf{oSpec}\ \mathsf{StmtIn}_1\ \mathsf{StmtOut}_1$ and $V_2 : \mathsf{Verifier}\ \mathsf{pSpec}_2\ \mathsf{oSpec}\ \mathsf{StmtOut}_1\ \mathsf{StmtOut}_2$, their sequential composition is:

$$
V_1.\mathsf{append}\ V_2 : \mathsf{Verifier}\ (\mathsf{pSpec}_1 \mathrel{++_\mathsf{p}} \mathsf{pSpec}_2)\ \mathsf{oSpec}\ \mathsf{StmtIn}_1\ \mathsf{StmtOut}_2
$$

The composed verifier first runs $V_1$ on the first part of the transcript, then runs $V_2$ on the second part using the intermediate statement from $V_1$.

## Depends on

- [Type Signature of a Verifier](../../definitions/part-01/def-verifier.md)
- [Protocol Specification Append](def-protocol-spec-append.md)

## Lean

Formalized as [`Verifier.append`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.append).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 52](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L52)
