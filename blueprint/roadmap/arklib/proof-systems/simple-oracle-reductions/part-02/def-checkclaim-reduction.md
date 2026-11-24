---
declaration: definition
origin: cited
lean: CheckClaim.reduction
statement: formalized
---

# CheckClaim Reduction

The CheckClaim reduction is a zero-round protocol that verifies predicates:

- **Protocol specification**: $\mathsf{pSpec} := []$ (no messages exchanged)
- **Predicate**: $\mathsf{pred} : \mathsf{StmtIn} \to \mathsf{Prop}$ (decidable)
- **Prover**: Simply stores and outputs the input statement with unit witness
- **Verifier**: Checks $\mathsf{pred}(\mathsf{stmt})$ and outputs statement if successful
- **Input relation**: $R_{\mathsf{in}}(\mathsf{stmt}, ()) := \mathsf{pred}(\mathsf{stmt})$
- **Output relation**: $R_{\mathsf{out}}(\mathsf{stmt}, ()) := \mathsf{True}$ (trivial after verification)

## Depends on

- [Interactive Reduction](../../../oracle-reductions/definitions/part-01/def-reduction.md)

## Lean

Formalized as [`CheckClaim.reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CheckClaim.reduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 363](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/simple_protocols.tex#L363)
