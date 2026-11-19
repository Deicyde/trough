---
declaration: definition
origin: cited
lean: Interaction.Oracle.Security.RoundExtractor, Interaction.Oracle.Security.RoundExtractor.IsProverPreserving, Interaction.Oracle.Security.RoundExtractor.IsLocallyBounded, Interaction.Oracle.Security.KnowledgeCertificate, Interaction.Oracle.Security.MeasuredKnowledgeCertificate
statement: formalized
---

# Round-by-Round Knowledge Certificate in the Interaction Layer

For an input $z$, an **interaction-layer round-by-round extractor** assigns to each node of the protocol tree a knowledge state (a witness type with a validity predicate) and a named map that transports a later witness one step backward. It is *prover preserving* if prover messages cannot make an invalid witness valid under these maps. It is *locally bounded* with error $\epsilon_j$ at round $j$ if, at every authored transcript prefix before a challenge of round $j$, including prefixes of probability zero in an honest run, the probability over the fresh uniform challenge that some later witness is valid while its backward image is invalid is at most $\epsilon_j$. A *knowledge certificate* bundles such an extractor with these two properties; a *measured* certificate adds a budgeted program for each extraction stage.

## Depends on

- [State-Restoration Experiment](def-sr-experiment.md)

## Lean

Formalized as [`Interaction.Oracle.Security.RoundExtractor`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.RoundExtractor), [`Interaction.Oracle.Security.RoundExtractor.IsProverPreserving`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.RoundExtractor.IsProverPreserving), [`Interaction.Oracle.Security.RoundExtractor.IsLocallyBounded`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.RoundExtractor.IsLocallyBounded), [`Interaction.Oracle.Security.KnowledgeCertificate`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.KnowledgeCertificate), [`Interaction.Oracle.Security.MeasuredKnowledgeCertificate`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.MeasuredKnowledgeCertificate).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 939](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L939)
