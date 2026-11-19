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

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 363](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L363)
