---
declaration: theorem
origin: cited
lean: Plonk.Assembly.oracleVerifier_rbrKnowledgeSoundnessWith, Plonk.Assembly.error, Plonk.Assembly.sum_error, Plonk.Assembly.transcriptExtractor, Plonk.Assembly.oracleVerifier_knowledgeSoundnessWith
statement: formalized
---

# Plonk knowledge soundness

Under the hypotheses of Theorem [Plonk completeness](thm-plonk-completeness.md), the verifier is round-by-round knowledge sound from the input relation to the output relation. The errors at the three challenges are

$$
\frac{3n-1}{|\mathbb{F}|}\ \text{(grand product)},\qquad
\frac{2}{|\mathbb{F}|}\ \text{(power batch)},\qquad
\frac{4(n-1)}{|\mathbb{F}|}\ \text{(quotient)},
$$

and the reveal stage has no challenge. The errors sum to $(7n-3)/|\mathbb{F}|$. Consequently the verifier is knowledge sound with error $(7n-3)/|\mathbb{F}|$, and the extractor returns the wire table from the first prover message.

## Depends on

- [Plonk oracle reduction](def-plonk-assembly.md)

## Lean

Stated as [`Plonk.Assembly.oracleVerifier_rbrKnowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.oracleVerifier_rbrKnowledgeSoundnessWith), [`Plonk.Assembly.error`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.error), [`Plonk.Assembly.sum_error`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.sum_error), [`Plonk.Assembly.transcriptExtractor`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.transcriptExtractor), [`Plonk.Assembly.oracleVerifier_knowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.oracleVerifier_knowledgeSoundnessWith); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/plonk.tex, line 51](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/plonk.tex#L51)
