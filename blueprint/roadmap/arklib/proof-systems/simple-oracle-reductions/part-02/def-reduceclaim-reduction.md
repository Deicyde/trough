---
declaration: definition
origin: cited
lean: ReduceClaim.reduction
statement: formalized
---

# ReduceClaim Reduction

The ReduceClaim reduction is a zero-round protocol that transforms claims via explicit mappings:

- **Protocol specification**: $\mathsf{pSpec} := []$ (no messages exchanged)
- **Statement mapping**: $\mathsf{mapStmt} : \mathsf{StmtIn} \to \mathsf{StmtOut}$
- **Witness mapping**: $\mathsf{mapWit} : \mathsf{StmtIn} \to \mathsf{WitIn} \to \mathsf{WitOut}$
- **Prover**: Applies both mappings to input statement and witness
- **Verifier**: Applies statement mapping to input statement
- **Input relation**: $R_{\mathsf{in}} : \mathsf{StmtIn} \to \mathsf{WitIn} \to \mathsf{Prop}$
- **Output relation**: $R_{\mathsf{out}} : \mathsf{StmtOut} \to \mathsf{WitOut} \to \mathsf{Prop}$

## Depends on

- [Interactive Reduction](../../../oracle-reductions/definitions/part-01/def-reduction.md)

## Lean

Formalized as [`ReduceClaim.reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReduceClaim.reduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 308](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L308)
