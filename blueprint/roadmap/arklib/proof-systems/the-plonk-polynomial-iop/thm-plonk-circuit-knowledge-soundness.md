---
declaration: theorem
origin: cited
lean: Plonk.relation, Plonk.Assembly.Circuit.oracleReduction, Plonk.Assembly.Circuit.relIn, Plonk.Assembly.Circuit.oracleVerifier_rbrKnowledgeSoundnessWith, Plonk.Assembly.Circuit.oracleVerifier_knowledgeSoundnessWith
statement: formalized
---

# Plonk knowledge soundness for the circuit relation

With the prepared system above, the verifier is knowledge sound from the Plonk relation at public input $x$ to the accepting output relation, with error $(7(\ell+n)-3)/|\mathbb{F}|$. The extractor decodes the first prover message into the private witness $w$.

## Depends on

- [Plonk knowledge soundness](thm-plonk-knowledge-soundness.md)

## Lean

Stated as [`Plonk.relation`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.relation), [`Plonk.Assembly.Circuit.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.Circuit.oracleReduction), [`Plonk.Assembly.Circuit.relIn`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.Circuit.relIn), [`Plonk.Assembly.Circuit.oracleVerifier_rbrKnowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.Circuit.oracleVerifier_rbrKnowledgeSoundnessWith), [`Plonk.Assembly.Circuit.oracleVerifier_knowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.Circuit.oracleVerifier_knowledgeSoundnessWith); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/plonk.tex, line 79](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/plonk.tex#L79)
