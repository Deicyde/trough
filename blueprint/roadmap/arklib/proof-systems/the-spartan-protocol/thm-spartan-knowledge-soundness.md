---
declaration: theorem
origin: cited
lean: Spartan.totalError, Spartan.error_ledger, Spartan.sum_challengeError, Spartan.knowledgeSoundnessWith, Spartan.straightlineExtractor, Spartan.foldExtractor_eq_straightlineExtractor, Spartan.knowledgeSoundnessWith_straightlineExtractor, Spartan.knowledgeSoundness, Spartan.knowledgeSoundness_clipped
statement: formalized
---

# Knowledge soundness

The per-challenge errors sum to

$$
\frac{s}{q} + s \cdot \frac{3}{q} + \frac{1}{q} + t \cdot \frac{2}{q} = \frac{4s + 2t + 1}{q}.
$$

The Spartan verifier is knowledge sound for the original R1CS relation with error $(4s + 2t + 1)/q$, and also with error $\min(1, (4s + 2t + 1)/q)$. The extractor obtained by folding the round-by-round extractors equals an executable straight-line extractor, which restricts the first message (the padded witness table) to the original witness coordinates.

## Depends on

- [Round-by-round knowledge soundness](thm-spartan-rbr.md)
- [RBR Knowledge Soundness Implies Knowledge Soundness](../../oracle-reductions/definitions/part-02/thm-rbr-knowledge-soundness-implies-knowledge-so.md)

## Lean

Stated as [`Spartan.totalError`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.totalError), [`Spartan.error_ledger`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.error_ledger), [`Spartan.sum_challengeError`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.sum_challengeError), [`Spartan.knowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.knowledgeSoundnessWith), [`Spartan.straightlineExtractor`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.straightlineExtractor), [`Spartan.foldExtractor_eq_straightlineExtractor`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.foldExtractor_eq_straightlineExtractor), [`Spartan.knowledgeSoundnessWith_straightlineExtractor`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.knowledgeSoundnessWith_straightlineExtractor), [`Spartan.knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.knowledgeSoundness), [`Spartan.knowledgeSoundness_clipped`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.knowledgeSoundness_clipped); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/spartan.tex, line 113](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/spartan.tex#L113)
