---
declaration: definition
origin: cited
lean: Reduction
statement: formalized
---

# Interactive Reduction

An interactive reduction for protocol specification $\mathsf{pSpec} : \mathsf{ProtocolSpec}(n)$ and oracle specification $\mathsf{oSpec}$ consists of:

- A **prover** $\mathcal{P} : \mathsf{Prover}(\mathsf{pSpec}, \mathsf{oSpec}, \mathsf{StmtIn}, \mathsf{WitIn}, \mathsf{StmtOut}, \mathsf{WitOut})$
- A **verifier** $\mathcal{V} : \mathsf{Verifier}(\mathsf{pSpec}, \mathsf{oSpec}, \mathsf{StmtIn}, \mathsf{StmtOut})$

The reduction establishes a relationship between input relations on $(\mathsf{StmtIn}, \mathsf{WitIn})$ and output relations on $(\mathsf{StmtOut}, \mathsf{WitOut})$ through the interactive protocol defined by $\mathsf{pSpec}$.

## Depends on

- [Type Signature of a Prover](def-prover.md)
- [Type Signature of a Verifier](def-verifier.md)

## Lean

Formalized as [`Reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 284](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L284)
