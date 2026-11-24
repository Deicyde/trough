---
declaration: theorem
origin: cited
lean: Plonk.Assembly.oracleReduction_completeness
statement: formalized
---

# Plonk completeness

Let $\mathbb{F}$ be finite and sampleable. For every initial distribution of the shared oracle state and every implementation of that oracle, the honest prover is complete from the input relation to the output relation with error $3n/|\mathbb{F}|$. The failure occurs only at the grand-product challenge.

## Depends on

- [Plonk oracle reduction](def-plonk-assembly.md)

## Lean

Stated as [`Plonk.Assembly.oracleReduction_completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.oracleReduction_completeness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/plonk.tex, line 41](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/plonk.tex#L41)
