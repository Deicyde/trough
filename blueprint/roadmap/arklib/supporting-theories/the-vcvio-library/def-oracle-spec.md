---
declaration: definition
origin: cited
lean: OracleSpec
statement: formalized
---

# Specification of Oracles

An oracle specification on an index type $\iota$ is a map $\mathsf{spec} : \iota \to \mathsf{Type}$. Each $t : \iota$ is a possible query, and $\mathsf{spec}\ t$ is the type of answers to that query. The query type is therefore the index type itself (`spec.Domain` is $\iota$), and the answer type depends on the query (`spec.Range t` is $\mathsf{spec}\ t$). An oracle specification is the same data as a polynomial functor with positions $\iota$ and directions $\mathsf{spec}\ t$. The specification only describes interfaces, not how the oracles behave.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`OracleSpec`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleSpec).

## Sources

- [ArkLib blueprint: vcv/defs.tex, line 11](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/vcv/defs.tex#L11)
