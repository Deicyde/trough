---
declaration: definition
origin: cited
lean: DoNothing.reduction, DoNothing.oracleReduction
statement: formalized
---

# DoNothing Reduction

The DoNothing reduction is a zero-round protocol with the following components:

- **Protocol specification**: $\mathsf{pSpec} := []$ (empty protocol, no messages exchanged)
- **Prover**: Simply stores the input statement and witness, and outputs them unchanged
- **Verifier**: Takes the input statement and outputs it directly
- **Input relation**: Any relation $R_{\mathsf{in}} : \mathsf{StmtIn} \to \mathsf{WitIn} \to \mathsf{Prop}$
- **Output relation**: The same relation $R_{\mathsf{out}} := R_{\mathsf{in}}$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`DoNothing.reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/DoNothing.reduction), [`DoNothing.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/DoNothing.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 9](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L9)
