---
declaration: theorem
origin: cited
lean: ReduceClaim.verifier_rbrKnowledgeSoundness
statement: formalized
---

# ReduceClaim Round-by-Round Knowledge Soundness

Suppose $\mathsf{mapWitInv} : \mathsf{StmtIn} \to \mathsf{WitOut} \to \mathsf{WitIn}$ satisfies: if $R_{\mathsf{out}}(\mathsf{mapStmt}(\mathsf{stmt}), w')$, then $R_{\mathsf{in}}(\mathsf{stmt}, \mathsf{mapWitInv}(\mathsf{stmt}, w'))$. Then the ReduceClaim verifier is round-by-round knowledge sound with error $0$, with the extractor $\mathsf{mapWitInv}$.

## Depends on

- [ReduceClaim Reduction](def-reduceclaim-reduction.md)

## Lean

Stated as [`ReduceClaim.verifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReduceClaim.verifier_rbrKnowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 332](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L332)
